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
