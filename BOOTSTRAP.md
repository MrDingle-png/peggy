# Bootstrap — Fanatics Collect Product Brain

Read this file to load full context for working with me. It tells you who I am, what I'm working on, and where to find everything you need.

## Who I am

VP of Product Design at Fanatics Collect. I work across marketplace, live streaming commerce, and collecting services. I lead product design teams and work closely with product, engineering, and business stakeholders to build the best experience for collectors.

## How I work

- **Collector-first**: every decision starts from the collector's perspective
- **Stakeholder framing**: always consider why something matters to the business and to customers — help me frame things for buy-in
- **Execution-oriented**: if a task involves others, help me structure it — who to involve, what the path looks like, how to bring it to market

## Current goals

Read [GOALS.md](GOALS.md) for full detail. Summary:

1. **Collector quests** — quest and challenge engine for collecting habits (strategic bet)
2. **Team development** — clear goals, progression, check-ins for the design team
3. **Topps programme building blocks** — FanCash Trading Cards for 2026 Flagship Football
4. **Design system adoption** — Figma-to-code pipeline with MCP tooling
5. **Collector innovation** — next bets beyond this quarter

## Knowledge map

Everything below lives in the `Knowledge/` folder. Read the specific files when you need depth — do not load everything upfront.

### Strategy and frameworks

| Folder | What it covers | Key files |
|--------|---------------|-----------|
| **Quests/** | Collector quest strategy, frameworks, infrastructure PRD | `collector-quests-strategy-v5.md`, `quest-infrastructure-prd-the-grail.md` |
| **Programs & Quests/** | Shared building blocks for Topps programmes and quests | `programs-vs-quests-building-blocks.md`, `building-blocks-for-topps-programmes.md` |
| **Games & Interactive/** | Games strategy, app architecture, structural model | `games-quests-programmes-strategy-brief.md`, `collect-app-architecture-schematic.md` |
| **Experience Framework/** | UX frameworks connecting Collect, Vault, and Live | `collections.md` |
| **AI Strategy/** | AI ops strategy, tooling, partner evaluations | `design-ai-operations-strategy.md`, `a2ui-protocol.md` |

### Product knowledge

| Folder | What it covers | Key files |
|--------|---------------|-----------|
| **FanCash Trading Card/** | FanCash proposal, redemption flows, Figma board refs | `fancash-trading-card-proposal.md`, `fancash-trading-card-redemption-v1.md` |
| **Instant Rips/** | Digital packs PRD and async instant rips | `digital-packs-prd.md` |
| **Established Product Behaviour/** | How systems work today — bidding, submission, valuation | `extended-bidding.md`, `item-submission.md`, `valuation-and-pricing-questions.md` |

### System and taxonomy

| Folder | What it covers | Key files |
|--------|---------------|-----------|
| **System Architecture/** | Data models, services, integration patterns | `folders-tags-and-collection-lists.md`, `unvaulted-items-data-architecture.md` |
| **Reference Taxonomy/** | Shared terminology and classification | `detail-page-taxonomy.md`, `collections-glossary.md`, `collections-cross-reference-index.md` |

### External context (Notion)

Some product context still lives on Notion and can be fetched via the Notion MCP integration. See [Knowledge/notion-hubs.md](Knowledge/notion-hubs.md) for links.

## Active tasks

Check `Tasks/` for current work items. Tasks are tied to the goals above.

## Specialist skills

I have specialist skills available. Use the right one based on what I ask for:

| Skill | When to use |
|-------|------------|
| **product-design** | Design reviews, product critiques, experience strategy, competitor analysis |
| **backend-engineering** | System architecture, API design, data modelling, backend code |
| **ios-engineering** | iOS development, SwiftUI, mobile UX, app architecture |
| **ux-copy** | Microcopy, UI strings, error messages, onboarding flows, tone of voice |
| **safe-coding** | Any time code is being generated — enforces process-first workflow and branch safety |

## Code generation rules

When generating any code:

1. **Explain the approach first** — what you plan to build, why, and what the trade-offs are
2. **Wait for confirmation** before writing code
3. **Always create a new branch** — never commit to main or an existing feature branch without asking
4. **Name branches clearly** — use the pattern `{skill}/{short-description}` (e.g., `backend/quest-api-scaffold`)
5. **Keep changes isolated** — do not modify files outside the scope of the task

## Integrations

MCP integrations are configured in `.cursor/mcp.json`:

- **Linear** — issue tracking and project management
- **Figma** — design files and components
- **Granola** — meeting notes and context
- **Slack** — team communication
- **Design Systems** — component documentation

## How this repo works

This repo (Peggy) is the source of truth for product knowledge. Changes here are published to Notion via a sync pipeline so the wider team can read them. Do not edit docs in Notion — those edits will be overwritten.

```
Contributors (GitHub) → Peggy repo (source of truth) → Notion (read-only mirror)
```
