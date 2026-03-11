# Artifacts

Interactive prototypes and visual artifacts supporting product design work.

## Structural Model Wireframe

**File:** `structural-model-wireframe.html`

An interactive HTML wireframe demonstrating the proposed Fanatics Collect information architecture. Open the file in a browser to explore.

### What it shows

The wireframe models the ownership-first platform structure with five primary pillars, global utility layers, and detailed Shop browsing.

**Primary pillars (tab bar):**
- **Home** — orchestration layer with priority tasks, portfolio highlights, and entry points
- **Shop** — curated home page with entry point grid and recommendation carousels, plus dedicated vertical surfaces (Cards, Packs, Drops, Live)
- **Search** — intent-driven finding across marketplace listings, entity hubs, and canonical catalogue records
- **Collection** — ownership space with All Items, Stacks, Quests, Programs, and Want List
- **Account** — operations and identity (Orders, Selling, Vault Activity, Wallet, Preferences)

**Global layers (header icons):**
- **Cart** — persistent cross-device commerce utility
- **Inbox** — unified communication hub with filterable feed (Messages, Offers, Alerts)

**Shop detail:**
- Shop Home lands on a curated page with a 2x2 entry grid and recommendation carousels (Recommended Cards, Recommended Packs, Latest Release, Live Now)
- Each vertical (Cards, Packs, Drops, Live) is a dedicated browsing surface with icon+label category tabs (For You, Basketball, Football, Baseball, Soccer, Hockey, UFC) and pill filters (Filter, Watchlist, Format, Grade, Price)
- Header updates with back navigation when inside a vertical

### Key architectural decisions demonstrated

- Bids migrated from Account to Shop Watchlist (inline filter within each vertical)
- Offers migrated from Account to Inbox (as negotiation threads)
- Notifications and Messaging unified into a single Inbox with filter chips
- Shop restructured from Discover/Saved mode toggle to curated home + dedicated verticals with icon category tabs

### How to use

Open `structural-model-wireframe.html` in any browser. Tap the tab bar to switch pillars, tap header icons for Cart and Inbox overlays, and navigate through Shop Home into dedicated verticals.

---

## Related Knowledge Base context

When working on or extending this wireframe, load these Knowledge documents for domain context:

### Essential — Architecture & IA

| Document | Path | Why it matters |
|---|---|---|
| **Structural Model (Notion)** | `Knowledge/notion-hubs.md` → Structural Model URL | The canonical Notion doc this wireframe is based on. Fetch live via the Notion MCP for the latest version. |
| **App Architecture Schematic** | `Knowledge/Games & Interactive/collect-app-architecture-schematic.md` | Mermaid diagrams of the three-layer architecture (pillars, global utilities, focused modes) — the same model the wireframe implements. |
| **Structural Model Proposed Changes** | `Knowledge/Games & Interactive/structural-model-proposed-changes.md` | Pending additions (Activities, Rewards Hub) that will affect future wireframe iterations. |

### Important — Collection & Ownership

| Document | Path | Why it matters |
|---|---|---|
| **Collections Framework** | `Knowledge/Experience Framework/collections.md` | Defines how ownership, organization, and value tracking work — the Collection pillar's foundation. |
| **Folders, Tags & Collection Lists** | `Knowledge/System Architecture/folders-tags-and-collection-lists.md` | Data architecture behind Stacks, folders, and how items are organized — critical for the Collection pillar. |
| **Unvaulted Items Data Architecture** | `Knowledge/System Architecture/unvaulted-items-data-architecture.md` | How unvaulted items are modelled — affects what shows up in Collection. |

### Important — Commerce & Marketplace

| Document | Path | Why it matters |
|---|---|---|
| **Detail Page Taxonomy** | `Knowledge/Reference Taxonomy/detail-page-taxonomy.md` | Defines the types of detail pages (listing, OIP, catalogue) that Shop verticals link to. |
| **Extended Bidding** | `Knowledge/Established Product Behaviour/extended-bidding.md` | How auctions work — relevant to the Weekly/Premier Auction formats in Shop filters. |
| **Item Submission** | `Knowledge/Established Product Behaviour/item-submission.md` | How items enter the vault — connects to the Account pillar's selling flow. |
| **Collections Glossary** | `Knowledge/Reference Taxonomy/collections-glossary.md` | Shared vocabulary across product, design, and engineering. |

### Useful — Programs & Engagement

| Document | Path | Why it matters |
|---|---|---|
| **Collector Quests Strategy** | `Knowledge/Quests/collector-quests-strategy-v5.md` | Quest framework and collector archetypes — Quests live in the Collection pillar. |
| **Games & Quests Strategy Brief** | `Knowledge/Games & Interactive/games-quests-programmes-strategy-brief.md` | How games, quests, and programmes fit into the structural model. |
| **Programs vs Quests Building Blocks** | `Knowledge/Programs & Quests/programs-vs-quests-building-blocks.md` | Distinction between programs and quests — both are Collection sub-sections. |
