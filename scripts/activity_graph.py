"""Generate a README graph from GitHub's public contribution calendar."""

import math
import re
import sys
from datetime import date, timedelta
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


class CalendarParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates = {}
        self.counts = {}
        self.tooltip = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("data-date") and attrs.get("id"):
            self.dates[attrs["id"]] = attrs["data-date"]
        if tag == "tool-tip" and attrs.get("for"):
            self.tooltip = (attrs["for"], [])

    def handle_data(self, data):
        if self.tooltip:
            self.tooltip[1].append(data)

    def handle_endtag(self, tag):
        if tag == "tool-tip" and self.tooltip:
            identifier, pieces = self.tooltip
            text = "".join(pieces).strip()
            match = re.match(r"([\d,]+) contributions?\b", text)
            if match:
                self.counts[identifier] = int(match[1].replace(",", ""))
            elif text.startswith("No contributions"):
                self.counts[identifier] = 0
            self.tooltip = None


def generate(username, destination):
    if not re.fullmatch(r"[A-Za-z0-9-]+", username):
        raise ValueError("Invalid GitHub username")
    request = Request(
        f"https://github.com/users/{username}/contributions",
        headers={"User-Agent": "GitHub-profile-activity-graph", "Accept-Language": "en"},
    )
    with urlopen(request, timeout=60) as response:
        parser = CalendarParser()
        parser.feed(response.read().decode("utf-8"))
    calendar = {day: parser.counts[key] for key, day in parser.dates.items() if key in parser.counts}
    if len(calendar) < 300:
        raise RuntimeError("GitHub contribution calendar was incomplete; keeping the previous graph")
    last = date.fromisoformat(max(calendar))
    days = [(last - timedelta(days=offset)).isoformat() for offset in range(30, -1, -1)]
    values = [calendar[day] for day in days]
    ceiling = max(4, math.ceil(max(values) / 4) * 4)
    points = [(62 + index * 26, 232 - count / ceiling * 156) for index, count in enumerate(values)]
    polyline = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="900" height="290" viewBox="0 0 900 290" role="img" aria-labelledby="title description">',
        '<title id="title">SYSTEM ACTIVITY</title>',
        f'<desc id="description">{escape(username)}: {sum(values)} contributions over the last 31 days, {days[0]} through {days[-1]}.</desc>',
        '<rect width="900" height="290" rx="12" fill="#0d1117"/>',
        '<g font-family="Arial,sans-serif" fill="#c9d1d9">',
        '<text x="34" y="34" font-size="20" fill="#00e5ff">SYSTEM ACTIVITY</text>',
        f'<text x="866" y="34" text-anchor="end" font-size="13">{sum(values)} contributions / 31 days</text>',
    ]
    for tick in range(5):
        y = 232 - tick * 39
        parts.append(f'<path d="M62 {y}H842" stroke="#30363d" stroke-width="1"/>')
        parts.append(f'<text x="48" y="{y + 4}" text-anchor="end" font-size="12">{ceiling * tick // 4}</text>')
    parts.append(f'<polygon points="62,232 {polyline} 842,232" fill="#00e5ff" opacity="0.12"/>')
    parts.append(f'<polyline points="{polyline}" fill="none" stroke="#00e5ff" stroke-width="2.5" stroke-linejoin="round"/>')
    for day, count, (x, y) in zip(days, values, points):
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="#ffffff"><title>{day}: {count} contributions</title></circle>')
    for index in (0, 5, 10, 15, 20, 25, 30):
        label = date.fromisoformat(days[index]).strftime("%b %d")
        parts.append(f'<text x="{62 + index * 26}" y="258" text-anchor="middle" font-size="12">{label}</text>')
    parts.append('</g></svg>')
    svg = "\n".join(parts)
    ET.fromstring(svg)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(svg, encoding="utf-8")
    print(f"Generated {destination}: {sum(values)} contributions across 31 days")


if __name__ == "__main__":
    generate(sys.argv[1], sys.argv[2])
