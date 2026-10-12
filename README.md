
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,50:111827,100:00e5ff&height=230&section=header&text=RAFAEL%20SARMENTO&fontSize=44&fontColor=ffffff&fontAlignY=38&desc=DEVELOPER%20%2F%2F%20SYSTEM%20INITIALIZATION&descAlignY=59&descSize=15&animation=fadeIn" width="100%"/>

<br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=21&duration=2800&pause=900&color=00E5FF&center=true&vCenter=true&width=850&lines=Initializing+system...;Full-Stack+Developer;Lua+%7C+Java+%7C+Python+%7C+JavaScript;Frontend+%2B+Backend+%2B+Architecture;Building+systems%2C+not+just+code.;Portfolio+still+under+construction..." alt="Typing Animation"/>

<br><br>

<a href="https://github.com/sarmento777">
<img src="https://img.shields.io/badge/GITHUB-000000?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://portfoliosarment.netlify.app/">
<img src="https://img.shields.io/badge/PORTFOLIO-00E5FF?style=for-the-badge&logo=googlechrome&logoColor=black"/>
</a>

<img src="https://komarev.com/ghpvc/?username=sarmento777&style=for-the-badge&color=00e5ff&label=PROFILE+VIEWS"/>

</div>

---

# `> SYSTEM_PROFILE`

```text
┌──────────────────────────────────────────────────────────────┐
│                    SYSTEM PROFILE                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  USER        : Rafael Sarmento                               │
│  HANDLE      : @sarmento777                                  │
│  AGE         : 16                                             │
│  LOCATION    : Brazil 🇧🇷                                     │
│  ROLE        : Developer                                      │
│  EXPERIENCE  : 4+ years scripting                            │
│  STATUS      : ONLINE                                         │
│                                                              │
│  FOCUS       : Frontend / Backend / Architecture             │
│  LANGUAGES   : Lua / Java / Python / HTML / CSS / JS         │
│                                                              │
│  OBJECTIVE   : Build better systems                           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

I'm a developer focused on building **organized, scalable and functional systems**.

I've been scripting with **Lua/Luau for 3+ years**, while expanding my experience through Java, Python, HTML, CSS and JavaScript.

My main focus is the intersection between **frontend, backend, server-client architecture, modular systems and clean code**.

I don't just want to make something work.

I want to understand **why it works, how it can scale and how it can be improved.**

```text

```

---

# `> TECH_STACK`

<div align="center">

### LANGUAGES

<img src="https://skillicons.dev/icons?i=lua,java,python,html,css,js&theme=dark" />

<br><br>

### TOOLS

<img src="https://skillicons.dev/icons?i=robloxstudio,vscode,git,github,netlify&theme=dark" />

</div>

---

# `> CORE_SKILLS`

<table>
<tr>
<td width="50%">

### ⚡ Frontend

* Responsive interfaces
* Modern UI
* Interactive components
* PC + Mobile layouts
* Frontend architecture
* Performance optimization

</td>

<td width="50%">

### 🧠 Backend

* APIs
* Databases
* Caching
* Data processing
* Fallback systems
* Server architecture

</td>
</tr>

<tr>
<td width="50%">

### 🏗️ Architecture

* Client / Server
* OOP
* Modular systems
* Separation of responsibilities
* Reusable components
* Clean code

</td>

<td width="50%">

### 🤖 AI

* AI API integration
* Structured outputs
* Prompt engineering
* Prompt caching
* AI recommendation systems
* Local fallback engines

</td>
</tr>
</table>

---

# `> FEATURED_PROJECT`

<div align="center">

# 🎬 CineVerse

### `AI-POWERED MOVIE & SERIES PLATFORM`

<img src="https://img.shields.io/badge/STATUS-ACTIVE-00E5FF?style=for-the-badge"/>
<img src="https://img.shields.io/badge/AI-CLAUDE-FF6B35?style=for-the-badge"/>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JAVASCRIPT-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>

</div>

## `SYSTEM_OVERVIEW`

**CineVerse** is a movie and series platform built around a database-first architecture and an AI recommendation assistant.

The main feature is **CineBot**, an AI assistant capable of understanding natural-language requests and recommending movies directly from the platform's catalog.

Example:

```text
USER
> "quero um filme com plot twist muito bom,
> drama + terror"

CINEBOT
> analyzing request...
> checking catalog...
> matching genres...
> ranking results...
> generating structured response...

RESULT
> Recommended titles → [Movie Cards]
```

---

## `> CINEBOT`

CineBot uses the **Anthropic Claude API** and sends the platform's catalog as context so the assistant can recommend titles that actually exist in the CineVerse database.

### Main architecture

```text
USER
 │
 ▼
CINEBOT
 │
 ├── User Intent
 │
 ├── Catalog Context
 │
 ├── Claude API
 │
 └── Structured Output
        │
        ▼
   Movie Cards
```

### AI features

* Claude API integration
* Catalog-aware recommendations
* Structured outputs
* Prompt caching
* Local search fallback
* Natural-language queries
* Database-driven results

Prompt caching is used to significantly reduce repeated processing and can cut the intended AI cost by approximately **90% per message**.

If the AI API becomes unavailable, CineBot can fall back to a **local search engine** instead of leaving the feature completely unavailable.

---

# `> DATA_PIPELINE`

CineVerse uses the database as the main source of truth.

Instead of depending on external APIs every time the user navigates through the website, movie information is stored locally in the database.

```text
             MOVIE API
                 │
                 ▼
        ┌─────────────────┐
        │ NEW MOVIE CHECK  │
        └────────┬────────┘
                 │
                 ▼
            DATABASE
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
     Name      Poster      ID
       │         │         │
       └─────────┼─────────┘
                 │
                 ▼
          TRANSLATION API
                 │
                 ▼
        TRANSLATED DATABASE
                 │
                 ▼
              FRONTEND
```

Movies are added through an API that searches for titles that are not already present in the database.

The system stores information such as:

* Movie name
* Poster
* ID
* Player information
* Metadata
* Translated content
* Additional movie information

---

# `> SEARCH_ENGINE`

The search page operates over the platform's own database.

```text
USER SEARCH
     │
     ▼
DATABASE QUERY
     │
     ▼
SIMILARITY / MATCHING
     │
     ▼
RELEVANT RESULTS
     │
     ▼
MOVIE CARDS
```

This means the user searches against the catalog already available inside CineVerse.

---

# `> MY_LIST`

The **My List** system allows users to save movies directly into their personal collection.

Features:

```text
✓ Database persistence
✓ 24 items per page
✓ Pagination
✓ Two-layer caching
✓ Reduced duplicated work
✓ Efficient database retrieval
```

---

# `> WHAT_I_CAN_BUILD`

## 🎮 Game Systems

```text
COMBAT SYSTEM
├── Combo
├── Knockback
├── Hit Detection
├── Damage Processing
└── Combat State

ABILITY SYSTEM
├── Q / E Abilities
├── Ability Framework
├── Cooldowns
└── Modular Architecture

PLAYER SYSTEM
├── Health
├── Status Effects
├── Buffs
├── Debuffs
└── Kill Feed

GAMEPLAY
├── Quests
├── Missions
├── Puzzle Systems
├── Inventory
└── Class Systems
```

## 🖥️ UI Systems

* Responsive interfaces
* PC + Mobile support
* HUDs
* Menus
* Inventory interfaces
* Leaderboards
* Damage numbers
* Kill feeds
* Interactive systems

---

# `> CURRENT_MISSION`

```text
┌──────────────────────────────────────────────────────────────┐
│                      CURRENT OBJECTIVES                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  [██████████████████░░] 90%  Portfolio                       │
│  [████████████████░░░░] 80%  Full-Stack Development          │
│  [██████████████░░░░░░] 70%  Software Architecture           │
│  [████████████░░░░░░░░] 60%  AI Engineering                  │
│  [██████████░░░░░░░░░░] 50%  Larger Projects                 │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  STATUS  : IN_PROGRESS                                       │
│  TARGET  : KEEP BUILDING                                     │
│  MODE    : CONTINUOUS IMPROVEMENT                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

# `> GITHUB_ANALYTICS`

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=sarmento777&show_icons=true&theme=transparent&hide_border=true&title_color=00e5ff&icon_color=00e5ff&text_color=c9d1d9&bg_color=00000000" height="180"/>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=sarmento777&layout=compact&theme=transparent&hide_border=true&title_color=00e5ff&text_color=c9d1d9&bg_color=00000000" height="180"/>

<br><br>

<img src="https://streak-stats.demolab.com?user=sarmento777&theme=transparent&hide_border=true&ring=00e5ff&fire=00e5ff&currStreakLabel=00e5ff&sideLabels=c9d1d9&dates=777777"/>

</div>

---

# `> ACTIVITY_GRAPH`

<div align="center">

<img src="https://raw.githubusercontent.com/sarmento777/sarmento777/output/activity-graph.svg" alt="GitHub activity over the last 31 days" width="100%"/>

</div>

---

# `> TROPHY_ROOM`

<div align="center">

<img src="https://raw.githubusercontent.com/sarmento777/sarmento777/output/trophies.svg" alt="GitHub profile trophies" width="100%"/>

</div>

---

# `> CONTRIBUTION_MATRIX`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sarmento777/sarmento777/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sarmento777/sarmento777/output/github-contribution-grid-snake.svg"/>
  <img src="https://raw.githubusercontent.com/sarmento777/sarmento777/output/github-contribution-grid-snake-dark.svg" alt="GitHub Contribution Snake" width="100%"/>
</picture>

</div>

---

# `> SOCIAL_LINKS`

<div align="center">

<a href="https://github.com/sarmento777">
<img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://portfoliosarment.netlify.app/">
<img src="https://img.shields.io/badge/Portfolio-00E5FF?style=for-the-badge&logo=googlechrome&logoColor=black"/>
</a>

</div>

---

<div align="center">

```text
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          "DON'T JUST WRITE CODE. BUILD SYSTEMS."             ║
║                                                              ║
║                  ── RAFAEL SARMENTO ──                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

<br>

`SYSTEM STATUS: ONLINE`

`PROFILE STATUS: UNDER CONSTRUCTION`

`NEXT UPDATE: UNKNOWN`

<br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00e5ff,50:111827,100:050505&height=120&section=footer" width="100%"/>

</div>
