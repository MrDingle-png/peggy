# Games, Quests & Programmes — Strategy Brief

**Status:** Draft — for leadership alignment
**Last updated:** Feb 27, 2026
**Related docs:**
- [Games & Interactive Strategy (Notion)](https://www.notion.so/fanaticscollect/Fanatics-Collect-Games-Interactive-304d7c400ecf8025a58bcc4606add021)
- [Structural Model (Notion)](https://www.notion.so/fanaticscollect/Fanatics-Collect-Structural-Model-30bd7c400ecf805c8914e8c2150740df)
- `Knowledge/Programs & Quests/programs-vs-quests-building-blocks.md`
- `Knowledge/Quests/collector-quests-strategy-proposal.md`

---

## The opportunity

Fanatics Collect is shifting from a commerce-first marketplace to an ownership-first collecting platform. Games, quests, and programmes are how we make ownership active — giving collectors reasons to open the app daily, engage with the hobby, and deepen their relationship with what they own.

Today, interactive experiences are shipped in pockets with inconsistent cadence and no shared structure. Engagement lift is inconsistent, work doesn't compound, and each new feature has to re-earn attention from scratch.

**Core thesis:** Shipping interactive features drives engagement lift. Connecting those features to shared progress is what turns isolated wins into an ecosystem flywheel.

---

## What we're building and why it matters

Three categories of interactive experience, each serving a distinct engagement goal:

### 1. Daily activities (drives DAU, trains ecosystem behavior)

Lightweight, repeatable actions that give collectors a reason to open the app every day. Two sub-types:

**Daily games** — collector-themed content. 60–90 seconds. One session, one result, share it.
- Trivia, stat-or-bluff, headline puzzles, card face-offs
- Collection-aware: what I own shapes what I play
- AI-generated content pipeline for sustainable daily cadence

**Collector challenges** — cross-surface actions that train ecosystem behavior.
- "Watch a break," "rip a pack," "scan a card," "list a card for sale"
- Each challenge is a single action tied to a real product surface
- Trains collectors to use the full ecosystem, not just one feature

Both sub-types earn progress toward quests, programmes, and rewards.

**Why this matters:** Daily games give collectors a reason to open the app that isn't "am I buying something today?" Collector challenges turn that daily habit into ecosystem adoption — training the behaviors (watching, ripping, scanning, listing) that drive GMV. Together they attack DAU while building the behavioral data to prove engagement → sessions → spend.

### 2. Quests (drives D7/D30 retention, collecting behavior)

Finite, task-driven initiatives that reward collectors for collecting. Time-boxed, multi-day goals tied to what you own and what you're building toward.

- Set quests, player quests, attribute quests, chase quests (see collector-quests-strategy-proposal.md for full taxonomy)
- Collection-aware: quests reference what you already own and guide what to collect next
- Four-tier reward pyramid from digital badges (L1) to 1/1 cards and VIP experiences (L4)

**Why this matters:** D7/D30 retention requires anticipation — a reason to come back tomorrow, not just today. Quests reward collectors for deepening the hobby — completing sets, chasing players, building thematic collections. Daily activities train the behaviors; quests give those behaviors a collecting purpose.

### 3. Programmes (drives long-term retention, ecosystem value)

Ongoing or season-based systems that reference ownership or participation and generate rewards. No defined endpoint.

- FanCash Trading Card, Performance Cards, Red Rookie, seasonal programmes
- Streak programmes and collector tier progression
- Fanatics One integration for cross-ecosystem loyalty

**Why this matters:** Programmes create persistent identity and progress. A quest might bring someone back for a week. A programme gives them a reason to care for a season.

---

## Where this lives in the product architecture

The structural model defines five pillars (Home, Shop, Search, Collection, Account) and three global utility layers (Cart, Notifications, Messaging). Games, quests, and programmes map cleanly onto this architecture without requiring a new pillar.

### Collection is the home for doing

Quests and programmes already live in Collection per the structural model — "they reinforce ownership gravity." Daily activities are the same category: lightweight, daily ownership-gravity reinforcement. When activities are collection-aware (what I own shapes what I play), they're a collecting experience, not standalone entertainment.

Collection houses:
- **Quests** — finite, task-driven collecting initiatives
- **Programmes** — ongoing, season-based systems
- **Activities** — daily games (entertainment) and collector challenges (ecosystem actions)

Activities launch in focused mode (nav suppressed during gameplay), consistent with how instant rips and live streams already work.

### Home orchestrates

Home's job is to "curate what matters right now." It surfaces:
- Today's daily challenge → deep links to Collection > Activities
- Quest progress → deep links to Collection > Quests
- Programme milestones → deep links to Collection > Programmes
- Rewards milestones → deep links to Rewards Hub

Home references these surfaces. It doesn't replace them.

### Rewards Hub is a new global utility layer

Rewards earned across the ecosystem (watching streams, buying, collecting, selling, following) don't belong in any single pillar. A Rewards Hub follows the same pattern as Cart — a cross-cutting utility layer accessible from a persistent header icon.

Two access patterns:
1. **Quick check (header icon)** — overlay/sheet showing points, tier progress, earning opportunities, streak status
2. **Full view (Account > Fanatics One)** — complete history, tier details, earning breakdown, redemption options

The Rewards Hub is distinct from Wallet:
- **Wallet** = balance ledger ("what do I have?") — FanCash, payouts, stored value
- **Rewards Hub** = progress and motivation ("how am I doing?") — points, tiers, earning opportunities, streaks

The separation:
- **Collection shows what you did** — "Quest: Rip 3 Series 1 packs — 2/3 complete"
- **Rewards Hub shows what you earned** — "150 points this week, 50 to next tier"
- **Wallet shows what you hold** — "FanCash balance: $12.50"

---

## Layered delivery approach

Rather than picking one feature, build in layers where each creates the conditions for the next:

### Layer 1 — Daily habit (ship first)

Ship a lightweight daily activity. Start on web (low friction, reusable across surfaces), measure DAU lift and return rates.

- Lowest engineering cost, fastest to ship, clearest signal
- Generates the behavioral data needed to build the business case
- Completion writes to a shared progress system from day one — even before the quest UI exists

### Layer 2 — Quests and programmes (ship second)

Activate the quest taxonomy and programme infrastructure. Collecting quests give D7/D30 retention a purpose beyond streaks — complete the set, chase the player, build the collection.

- Requires integration with transactional systems (rips, marketplace, collection data)
- Internal ownership matters here — a partner can't build collection-aware quests without deep stack access
- Builds on the 8 building blocks already defined (see programs-vs-quests-building-blocks.md)

### Layer 3 — Rewards Hub and connected progress (ship third)

Stand up the global Rewards Hub and connect all earning surfaces. This is when the flywheel compounds — daily activities, quests, programmes, and ecosystem actions all feed into a unified progress and motivation system.

- Requires the content from Layers 1 and 2 to populate it — shipping an empty hub is worse than no hub
- Design the data model for the hub now, even while building Layers 1 and 2. Streaks, quest completions, and rewards should write to shared progress infrastructure from day one.
- Connects naturally to Fanatics One loyalty infrastructure

---

## How this maps to goals

| Goal | Layer 1 (Daily Activities) | Layer 2 (Quests & Programmes) | Layer 3 (Rewards Hub) |
|---|---|---|---|
| **DAU** | Primary driver — daily reason to open | Reinforces — "check quest progress" | Compounds — "see everything, earn everywhere" |
| **D7 retention** | Streak mechanics create 7-day hooks | Multi-day quests are the main D7 lever | Visualizes streak/progress, triggers loss aversion |
| **D30 retention** | Streaks alone fade past ~14 days | Rotating programmes and seasonal events sustain | Long-term identity and tier progression |
| **Collecting behavior** | Indirect — builds habit and affinity | Direct — quests require rips, purchases, scans | Connecting layer — "here's what to do next" |
| **GMV** | Builds the session frequency that correlates to spend | Quests drive purchasing as a gameplay mechanic | Rewards redemption creates reinvestment loops |

---

## Build vs. partner

| Layer | Recommendation | Rationale |
|---|---|---|
| **Daily activities** | Internal (1 engineer + content pipeline) or lightweight partner | AI-assisted content generation makes this fast. Prototypes already exist. Low complexity. |
| **Quests & programmes** | Internal | Requires deep integration with transactional systems, collection data, and product catalogue. A partner can't build collection-aware quests without full stack access. |
| **Rewards Hub** | Internal | This is the connective tissue of the ecosystem. Competitive moat. Must own. |
| **In-stream interactivity** | Partner or internal depending on priority | Architecturally solved (focused mode), but lower priority than ownership-gravity features. Could test with a partner like Little Snacks for directional signal. |

---

## What we need for alignment

1. **Engagement → GMV data** from analytics (Dwight) — even directional data ("users with 5+ sessions/week have 2x GMV") frames the investment case
2. **Agreement on layer ordering** — daily activities first, quests second, rewards hub third
3. **Agreement on the Rewards Hub as a global utility layer** — this is a structural model change that needs design and product alignment
4. **Internal team commitment** — at minimum, 1 engineer with WebGL/interactive experience working alongside design to ship Layer 1 and build toward Layer 2
5. **Definition of quests for Q2 launch** — which quest types from the taxonomy ship first (recommendation: Set Quest L1 + Chase the Rainbow L2 as MVP)

---

## Success metrics

**North star:**
- Engaged time: minutes/session, sessions/day, % sessions with an interactive action
- Retention: D1/D7/D30, streak continuation, return after first reward
- Collecting behavior lift: scan rate, rip rate, marketplace activity among engaged vs. non-engaged cohorts

**Supporting:**
- Ecosystem conversion: play/engage → watch/rip/collect conversion rate
- Quest participation: start rate, completion rate, time to complete
- Rewards engagement: hub open rate, points earning rate, redemption rate
- Incremental GMV per engaged user
