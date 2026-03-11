# Tasks

Active and completed product design tasks tied to current goals.

## Structural Model Architecture PRD

**File:** `structural-model-architecture-prd.md`

A hybrid architecture PRD documenting the evolved Fanatics Collect information architecture. Written as a PRD (problem statement, goals, principles) with an architecture-focused body, structured for evaluation against collector expectations via Marvin.

### What it covers

- **Problem statement** — why the current commerce-first IA creates structural confusion as the platform scales
- **North Star** — shift from commerce-first marketplace to ownership-first collecting platform with embedded commerce
- **Full IA specification** — all five pillars (Home, Shop, Search, Collection, Account), global utility layers (Inbox, Cart), and how they relate
- **Shop architecture** — curated Shop Home with recommendation carousels, plus dedicated vertical surfaces (Cards, Packs, Drops, Live) with icon category tabs and pill filters (Format, Grade, Price, Watchlist)
- **Migration map** — what moved and why (Bids → Shop Watchlist, Offers → Inbox, Notifications + Messaging → unified Inbox, Discover/Saved → Shop Home + verticals)
- **Focused modes and surface behavior rules** — when navigation is suppressed, exit behavior, and surface categories
- **Guardrails** — rules to prevent IA drift as the platform evolves
- **Open questions** — testable hypotheses for collector validation

### Companion wireframe

The interactive wireframe at `../Artifacts/structural-model-wireframe.html` demonstrates the architecture described in this PRD.

## Other tasks

- `fanatics-live-to-collect-unification.md` — Live-to-Collect platform unification planning
- `live-to-collect-unification/` — Phase plans and segmentation brief for the unification initiative

---

## Related Knowledge Base context

When working on or extending the PRD and related tasks, load these Knowledge documents for domain context:

### Essential — Architecture & IA

| Document | Path | Why it matters |
|---|---|---|
| **Structural Model (Notion)** | `Knowledge/notion-hubs.md` → Structural Model URL | The canonical Notion doc the PRD is based on. Fetch live via the Notion MCP for the latest version. |
| **App Architecture Schematic** | `Knowledge/Games & Interactive/collect-app-architecture-schematic.md` | Mermaid diagrams of the three-layer architecture — the same model the PRD describes. |
| **Structural Model Proposed Changes** | `Knowledge/Games & Interactive/structural-model-proposed-changes.md` | Pending additions (Activities, Rewards Hub) that may need PRD coverage in future iterations. |

### Important — Collection & Ownership

| Document | Path | Why it matters |
|---|---|---|
| **Collections Framework** | `Knowledge/Experience Framework/collections.md` | Defines the ownership model the PRD's Collection pillar is built on. |
| **Folders, Tags & Collection Lists** | `Knowledge/System Architecture/folders-tags-and-collection-lists.md` | Data architecture for Stacks and item organization — directly referenced in PRD Section 4.4. |
| **Unvaulted Items Data Architecture** | `Knowledge/System Architecture/unvaulted-items-data-architecture.md` | How unvaulted items are modelled — affects Collection pillar scope. |

### Important — Commerce & Marketplace

| Document | Path | Why it matters |
|---|---|---|
| **Detail Page Taxonomy** | `Knowledge/Reference Taxonomy/detail-page-taxonomy.md` | Defines detail page types linked from Shop vertical listings. |
| **Extended Bidding** | `Knowledge/Established Product Behaviour/extended-bidding.md` | Auction mechanics relevant to PRD Section 4.2 (Format filter: Weekly/Premier Auction). |
| **Item Submission** | `Knowledge/Established Product Behaviour/item-submission.md` | Vault intake flows — relevant to Account pillar and the selling experience. |
| **Valuation & Pricing** | `Knowledge/Established Product Behaviour/valuation-and-pricing-questions.md` | Open questions about pricing that affect marketplace behavior in Shop. |
| **Collections Glossary** | `Knowledge/Reference Taxonomy/collections-glossary.md` | Shared vocabulary for cross-team alignment on PRD terminology. |
| **Cross-Reference Index** | `Knowledge/Reference Taxonomy/collections-cross-reference-index.md` | Maps concepts across Collect, Vault, and Live — useful for migration map accuracy. |

### Useful — Programs, Quests & Engagement

| Document | Path | Why it matters |
|---|---|---|
| **Collector Quests Strategy (v5)** | `Knowledge/Quests/collector-quests-strategy-v5.md` | Quest framework and collector archetypes — Quests are a Collection sub-section in the PRD. |
| **Quest Infrastructure PRD (The Grail)** | `Knowledge/Quests/quest-infrastructure-prd-the-grail.md` | Technical infrastructure for quests — relevant if extending Collection pillar. |
| **Games & Quests Strategy Brief** | `Knowledge/Games & Interactive/games-quests-programmes-strategy-brief.md` | How games, quests, and programmes map to the structural model. |
| **Programs vs Quests Building Blocks** | `Knowledge/Programs & Quests/programs-vs-quests-building-blocks.md` | Distinguishes programs from quests — both live under Collection. |

### Useful — Platform Unification

| Document | Path | Why it matters |
|---|---|---|
| **Live-to-Collect Unification** | `Tasks/fanatics-live-to-collect-unification.md` | Platform unification strategy — the "Live" vertical in Shop depends on this initiative. |
| **Unification Phase Plans** | `Tasks/live-to-collect-unification/` | Phased execution plans and segmentation for the Live-to-Collect merge. |
