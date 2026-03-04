# Structural Model — Proposed Changes

**Status:** Draft — for review before updating the canonical Notion doc
**Context:** These changes add games, quests, programmes, and a Rewards Hub to the Fanatics Collect Structural Model. They follow the existing architectural principles and guardrails rather than introducing new structural patterns.

---

## Change 1: Expand Collection (Section 2.4) to include Activities

**Current text:**

> Collection includes:
> - All items
> - Stacks (multi-membership groupings; behaves like tag-powered organization)
> - Quests (task-based collecting initiatives)
> - Programs (ownership-adjacent initiatives such as Performance Cards and Red Rookie)
> - OIP (Owned Item Page) as the canonical place for item state and context

**Proposed text:**

> Collection includes:
> - All items
> - Stacks (multi-membership groupings; behaves like tag-powered organization)
> - Quests (task-based collecting initiatives)
> - Programs (ownership-adjacent initiatives such as Performance Cards, Red Rookie, and streak/tier programmes)
> - Activities (daily games and collector challenges that reinforce hobby engagement)
> - OIP (Owned Item Page) as the canonical place for item state and context

**Rationale:** Activities (daily trivia, stat-or-bluff, card-based challenges) reinforce ownership gravity the same way quests and programmes do — they're collection-aware, completion feeds into shared progress, and they deepen hobby engagement. They follow the same principle: live in Collection because they make ownership more active.

---

## Change 2: Expand the Quests/Programs distinction (Section 2.4) to include Activities

**Current text:**

> Programs and Quests are distinct but related:
> - **Programs** are ongoing or season-based systems that may reference ownership or participation and may generate rewards such as FanCash.
> - **Quests** are finite, task-driven initiatives that encourage collecting behavior or feature adoption.
> Both live in Collection because they reinforce ownership gravity.

**Proposed text:**

> Programs, Quests, and Activities are distinct but related:
> - **Programs** are ongoing or season-based systems that may reference ownership or participation and may generate rewards such as FanCash.
> - **Quests** are finite, task-driven initiatives that encourage collecting behavior or feature adoption.
> - **Activities** are lightweight, repeatable daily or weekly interactions (trivia, challenges, card-based games) that reinforce hobby engagement and collecting habits. Activities are collection-aware — a collector's owned items may shape the content they see. Completion feeds into quest and programme progress.
> All three live in Collection because they reinforce ownership gravity.

---

## Change 3: Add Activities to Focused Mode Surfaces (Section 6.3)

**Current text:**

> Examples:
> - Messaging thread view
> - Checkout (traditional)
> - Live stream
> - Scanner capture flow
> - Instant rip / break replay
> - End-of-auction "finale mode" (future)

**Proposed text:**

> Examples:
> - Messaging thread view
> - Checkout (traditional)
> - Live stream
> - Scanner capture flow
> - Instant rip / break replay
> - End-of-auction "finale mode" (future)
> - Daily activity / game (future)

**Rationale:** When a collector launches a daily game from Collection or Home, gameplay takes over the screen in focused mode. On exit, close returns to origin — identical behavior to instant rips and live streams. This is consistent with guardrail A4.1 (hide navigation only for mode changes) and A6.3 (mode-based experiences are additive).

---

## Change 4: Add Rewards Hub as a Global Utility Layer (new Section 3.4)

**Proposed new section after Section 3.3 (Messaging):**

> ## 3.4 Rewards Hub (Ecosystem Progress)
>
> The Rewards Hub is a **cross-ecosystem progress and motivation surface**, not a pillar.
>
> Collectors earn rewards across many surfaces — watching streams, ripping packs, completing quests, scanning cards, following sellers, bidding in auctions. No single pillar owns all earning behavior, so the Rewards Hub is a global utility layer accessible from a persistent header icon.
>
> Two access patterns:
> - **Quick check (header icon):** overlay or sheet showing points, tier progress, active earning opportunities, and streak status. Accessible from any surface.
> - **Full view (Account > Fanatics One):** complete rewards history, tier details, earning breakdown, and redemption options.
>
> The Rewards Hub is distinct from Wallet:
> - **Wallet** stores balances and handles payouts (FanCash, stored value). It answers "what do I have?"
> - **Rewards Hub** shows progress and earning opportunities. It answers "how am I doing and what should I do next?"
>
> Design principles:
> - Collection shows what you did (quest progress, programme status)
> - Rewards Hub shows what you earned (points, tier, streaks)
> - Wallet holds what you can spend (FanCash, balances)
>
> The Rewards Hub is the primary product surface for Fanatics One within Collect. As the loyalty programme evolves, this layer scales with it.

---

## Change 5: Add Rewards Hub to Cart Behavior Guardrail (Appendix A4.3) as a parallel pattern

**Proposed new section A4.4:**

> ### A4.4 Rewards Hub Behavior
>
> Rewards Hub:
> - Persistent header icon, accessible from any surface
> - Opens as overlay/sheet showing progress summary
> - Full destination view available from Account > Fanatics One
> - Does not duplicate quest/programme progress already shown in Collection; instead links to it
> - Currency balances (FanCash) remain in Wallet; Rewards Hub references but does not replicate them
>
> Rewards Hub must not become:
> - A discovery surface (that's Shop)
> - A quest management tool (that's Collection)
> - A currency ledger (that's Wallet)

---

## Change 6: Add Activities to Guardrail A4.1 (Section A4)

**Current text:**

> Primary navigation remains visible unless the user enters:
> - Messaging thread
> - Checkout
> - Live stream
> - Instant rip animation
> - Break replay
> - Auction finale mode
> - Scanner capture flow

**Proposed text:**

> Primary navigation remains visible unless the user enters:
> - Messaging thread
> - Checkout
> - Live stream
> - Instant rip animation
> - Break replay
> - Auction finale mode
> - Scanner capture flow
> - Daily activity / game

---

## Change 7: Add Rewards guardrail to Appendix A1 (Pillar Integrity)

**Proposed new section A1.4:**

> ### A1.4 Rewards Are Not a Pillar
>
> Rewards and loyalty progress are cross-cutting ecosystem concerns.
>
> Rewards must not:
> - Become a primary navigation tab
> - Live exclusively in Collection (earning happens outside of ownership)
> - Live exclusively in Account (it's a motivation surface, not machinery)
>
> The Rewards Hub is a global utility layer. Earned rewards surface contextually:
> - Quest/programme completion in Collection
> - Earning opportunities in Home
> - Currency balances in Wallet
> - Full progress and history in Rewards Hub

---

## Summary of additions

| Area | What changes | Type |
|---|---|---|
| Section 2.4 (Collection) | Add Activities as a Collection surface | Expansion |
| Section 2.4 (Collection) | Add Activities to the Programs/Quests distinction | Expansion |
| Section 3 (Global Utility Layers) | Add Rewards Hub (3.4) | New section |
| Section 6.3 (Focused Modes) | Add daily activity / game | Expansion |
| Appendix A1 (Pillar Integrity) | Add "Rewards Are Not a Pillar" guardrail (A1.4) | New guardrail |
| Appendix A4.1 (Nav Behavior) | Add daily activity / game to focused mode list | Expansion |
| Appendix A4 (Surface Behavior) | Add Rewards Hub behavior guardrail (A4.4) | New guardrail |

All changes follow existing structural patterns. No new pillars. No navigation changes. Two new concepts (Activities, Rewards Hub) integrated using patterns the model already defines (Collection surfaces, global utility layers, focused modes).
