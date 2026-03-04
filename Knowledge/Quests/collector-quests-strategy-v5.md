# Collector Quests — Initial Strategy Proposal (v5)

**Source:** Feb2026_CollectorQuests_Sendv5.pdf (Feb 2026)
**Author:** Brianne Mahoney
**Status:** Draft — subject to Exec feedback
**Classification:** Privileged & Confidential

---

## Overview

Collector Quests is a strategic framework for inspiring new collecting journeys through structured quest types, naming conventions, tiered rewards, and incentive programs on the Fanatics Collect app. This v5 proposal covers collector segmentation, quest taxonomy, quest schematics, naming conventions, a phased GTM strategy, MVP priorities, reward tiering, and the product infrastructure needed to power quests at scale.

---

## 1. Collector types

Six collector archetypes, each with distinct motivations:

| Type | Motivation | Implication |
|---|---|---|
| **Novice** | New to the hobby — learning, experimentation, first hits | Needs onboarding-friendly quests |
| **Hobbyist** | Fun, nostalgia, sentimental value — value appreciation is secondary | Responds to community and sharing |
| **Investor** | Long-term value, portfolio growth — graded cards, rarity, appreciation potential | Cares about scarcity and grade |
| **Set Builder** | Completion and organization — finishing full sets, acquiring missing cards | Natural quest participant |
| **Player/Team** | Dedicated to a favorite player, team, or character — fandom and personal connection | Depth over breadth |
| **Flipper** | Opportunistic, transaction-driven — buy/sell for profit, less emotional attachment | Profit-motivated engagement |

**Key insight:** Collectors are not one-size-fits-all. Their motivations drive how they spend, engage, and evolve across different collecting journeys.

---

## 2. Quest taxonomy (6 categories)

**Goal:** Build a structured ecosystem of collector quests that increases appetite, depth, and lifetime engagement across the hobby.

### A. Set Quests (collector facing — MVP recommended)
Complete a defined checklist or card group:
- Complete set (e.g., 25 Topps BK base set)
- Master set (e.g., 25 Heritage master set)
- Insert set (e.g., Future Stars, Youthquake)
- Autograph set (e.g., Real One Autos)
- PSA set registry (e.g., complete set in PSA 10)
- Sticker set (e.g., sticker albums)

### B. Player/Team Quests (collector facing — MVP recommended)
Build depth around a single player or character:
- Team sets (e.g., 1952 Topps base set NYY)
- Rainbow (1/1 and up)
- Player stack (same subject across card types)
- Player runs (same card across years)
- Jersey # match (serial # matches player)
- Prospects/Rookies chase (prospecting)
- PSA set registry (graded set — player or team)

### C. Attribute Quests (collector facing)
Collect across a shared theme, story, or rule:
- Milestone chase (MVPs, ROY, 500 HR Club)
- Nationality set/run (from their country)
- Unique relic chase (bat knobs)
- Parallel set/run (e.g., Gold /50, color match)
- Serial-number run (e.g., 07/99 parallels)
- Era-based chase (Pre-War, Vintage, Modern)
- Attribute chase (e.g., portraits, tape patterns)

### D. Rarity Quests (product/campaign driven)
Chase specific releases driven by key hits or product innovations:
- Case chase (collect a season of case hits)
- Nameplate (complete name/jersey)
- Jigsaw (complete the patch)
- Autograph chase (e.g., only 1/1 autos)
- Relic chase (e.g., Gold Logoman)

### E. Program Quests (product/campaign driven)
Chase specific releases driven by product innovation:
- Three Kings (collect RDPA, Bowman 1st Super Auto, Chrome Rookie Super Auto)
- The Grail (find all 9 grail cards for a prize)
- MVP Buyback program (Chrome)
- Red Rookie Redemption (Bowman)
- FanCash card (redemption)

### F. Action Quests (product/campaign driven — future state)
Challenge-oriented quests that reward participation, engagement, and collecting behaviors — not purchase driven:
- Check-in/Events (check in at Hobby Shops, Rip Night, Fanatics Fest, National, etc.)
- Collect streaks (check-in cards every week)
- And more…

---

## 3. Quest schematics of a card

A single card can sit inside dozens of quest types simultaneously, driving engagement across the ecosystem. Example using a Cooper Flagg card:

- Rookie Chase / Rookie Set
- Color Match Parallel
- Chase the Rainbow
- C. Flagg Base Collection
- Mavericks Team Set
- C. Flagg Player Run
- Build a Master Set
- Insert Set
- Parallel Set of Blues
- Serial Number Chase (#10)
- Duke Chase
- Rookie Inserts
- Chase the Rainbow (Insert)

---

## 4. Naming conventions (glossary)

| Term | Definition | Example (by level) |
|---|---|---|
| **Stack** | Same subject across different types/attributes | L1: Flagg Base Stack — all Cooper Flagg base rookies across products · L2: Ohtani Auto Stack — Ohtani auto from all Chrome cards in 2025 (Chrome, Finest, Chrome Black, etc.) · L3/4: Ohtani SSP Stack — all Ohtani mega hit inserts in 2025 (Anime, Helix, Alter Egos, Headliners, Aura, etc.) |
| **Set** | Same attribute across different subjects | L1: Insert Set — all Future Stars base inserts in 2025 Chrome BK · L2: Golden Mirror Set — full Golden Mirror set from 2025 Series 1 / Parallel Set — Blue /150 of every subject · L3/4: Anime Set — all 2025 Anime cards from Bowman BB releases |
| **Pursuit** | Same card type across card subjects | L1: Rookie Pursuit — every NBA RC base card from 2025 season · L2: Award Winner Pursuit — all MLB MVPs, Cy Young, & ROY in Gold /50 · L3/4: RDPA Pursuit — 1/1 auto relics of top rookie debuts |
| **Rainbow** | Collection based on parallels of a subject from a single release | L1: Flagg 2025 Chrome Rainbow (partial) — Gold /50 and up · L2: Flagg Chrome Rainbow — Super 1/1 through Refractor · L3/4: Flagg Topps Rainbow — Flagship, Chrome, & Finest combined |
| **Run** *(future state)* | Same card type and subject across multiple years (career run) | L1: Gold Ohtani Run — gold /50 Topps Chrome every year · L2: Ohtani Golden Mirror Run — Golden Mirror from every Series 1 release · L3/4: Ohtani Anime Run — Anime card from every calendar year |

Additional naming options considered: Straight, Flush, Journey.

**Note:** Quests are not mutually exclusive or collectively exhaustive — a single card can participate in multiple quests simultaneously.

---

## 5. GTM strategy — phased expansion

Phased rollout designed to validate collector behavior, de-risk system architecture, and scale quests across the portfolio.

### Phase 1: Pilot
**Objective:** Prove collector demand/behaviors and validate underlying system design within controlled scope.

| Focus Area | Details |
|---|---|
| **Define the Quests** | Prioritize foundational quests (Complete Set, Insert Set, Simple Player Stack). Introduce one curated depth quest. |
| **Establish Design & Data Architecture** | Stand up Data Lake (checklists, scanned HD card imagery, etc.). Define quest framework (onboarding, enrollment, milestones). Implement guardrails to protect brand. |
| **Align on Reward Philosophy** | Anchor MVP on intrinsic progression (status, badges, recognition). |

### Phase 2: Expand
**Objective:** Introduce higher-difficulty quests and validate collector progression mechanics.

| Focus Area | Details |
|---|---|
| **Build the Quest Portfolio** | Introduce rarity-driven and progression-based quests (SSP Stack). Test multi-level quest ladders and milestone structures. |
| **Strengthen System & Data** | Enhance quest tracking/integration. Validate scalability of quest logic across multiple brands. Refine UX based on pilot engagement. |
| **Refine Incentive Strategy** | Introduce milestone-based rewards to reinforce progression. Test limited FanCash/physical rewards. |

### Phase 3: Scale
**Objective:** Scale collector quests across all brands and optimize the experience.

| Focus Area | Details |
|---|---|
| **Standardize & Scale Quests** | Deploy standardized quest architecture across remaining brands. Enable brand-specific customization and cross-brand quests. |
| **Optimize Infrastructure** | Ensure infrastructure scales to allow product or non-technical users to create & launch quests seamlessly. |
| **Elevate Rewards & Recognition** | Introduce tiered recognition systems (leaderboards, showcases, status tiers). Unlock experiential rewards for top-tier achievements. |

---

## 6. MVP priorities — introducing new ways to collect

### Foundational collector quests

| Priority | Quest Name | Level | Description | Example Reward |
|---|---|---|---|---|
| Basic | Complete Set(s) | 1 | Collect a copy of the entire base or parallel set of a product | Digital badge upon full set completion |
| Basic | Insert Set | 1 | Complete a copy of the entire insert set of a product (e.g., Instinct from Topps Chrome Basketball) | Digital badge upon full set completion |
| MVP | Chase the Rainbow | 2 | Collect as many parallels of a star player/rookie from a flagship Topps product | FanCash distributed at milestones · Physical badge at completion (shipped) |
| MVP | All-Star Pursuit | 2 | Collect the all-star team in different ways (e.g., inserts, parallels, etc.) | Digital badge at each set completion · Special team set (shipped) |
| MVP | SSP Stack | 3 | Collect "quest-eligible" SSP cards of a player across multiple Flagship & Chrome brands (e.g., Ohtani SSP Stack — Helix, All Aces, Hidden Gems, etc.) | FanCash distributed at milestones · Limited exclusive card at completion |

### Future quests to add
1. **Nine-up** — A pre-defined 9-card collecting journey designed to fill one digital binder page, with each pocket representing a specific card to chase and complete (e.g., 9 on-card Autos of Ohtani in 2025 season)
2. **Award Winner Pursuit** — Collect all MLB MVPs, Cy Young, & ROY in Gold /50
3. **Nationality Run** — Collect all base cards from a specific nationality for a product (e.g., all Japan players from Series 1)
4. **Program Quests** — Bring all ongoing and future program quests (e.g., Three Kings, The Grail) onto Fanatics Collect

---

## 7. Reward pyramid (4 tiers)

| Tier | % of Quests | Reward Type | Objective |
|---|---|---|---|
| **Level 1** | 80% | Digital badge & participation milestones | Drive digital onboarding, participation, and appetite for collecting |
| **Level 2** | 15% | Tangible reward or access | Encourage sustained engagement and reinvestment without becoming transactional |
| **Level 3** | 4% | Recognition & scarcity asset | Reward complex achievements with tangible scarce assets and status |
| **Level 4** | 1% | Prestige & VIP experience | Create hobby-defining moments for the rarest accomplishments |

### Incentive structure by level

| Level | Incentive Components |
|---|---|
| **Level 1** | Digital badge, progress trackers, profile markers |
| **Level 2** | Level 1 + modest FanCash or early access |
| **Level 3** | Level 2 + app recognition / collector leaderboard, exclusive quest card |
| **Level 4** | Level 3 + 1/1 quest-stamped card, VIP event access or physical display case/trophy |

---

## 8. Reward strategy by level

Collector quests should balance extrinsic motivation to spark participation with intrinsic achievement to deepen commitment — growing long-term collectors through purity of pursuit, not just purchase.

### Level 1 — Digital badges on Collect App
**Objective:** Drive digital onboarding, collector engagement, and support collecting behaviors.

- **Quest types:** Sticker Set, Base Set, Rookie/Prospect Chase, Bronze Nine-Up
- **Why:** High-volume, repeatable, and accessible quests. Inclusive of lifelong quests. Rewards reinforce collector identity ("Set Builder," "Prospector").

### Level 2 — FanCash at milestones & digital badge
**Objective:** Incentivize sustained engagement and reinvestment.

- **Quest types:** Rainbow, Master Set, PSA Set Registry, Silver Nine-Up
- **Why:** Requires meaningful time and spend. Cash rewards encourage reinvestment without diluting card scarcity. Physical badge sent for higher-end quests.

### Level 3 — Exclusive low-numbered auto
**Objective:** Reward complex achievements with tangible scarcity.

- **Quest types:** Nameplate, Anime Set, Double Rainbow (multi-product)
- **Why:** Premier collector tier for Topps. Exclusive cards must be clearly limited and equal to quest difficulty to preserve value.

### Level 4 — VIP experience & physical display
**Objective:** Create aspirational VIP moments for the rarest accomplishments.

- **Quest types:** The Grail, Three Kings, 1-of-1 Super Set (all subjects of a set)
- **Why:** These feats should be rare. Experiential rewards reinforce status and deepen long-term brand loyalty.

---

## 9. Product infrastructure needed

Building the operating system for collector quests.

### Foundational features

| Category | Feature | Description |
|---|---|---|
| **Collection Engine** | Unified Digital Collection | Scan/import cards into Collection in Collect App (supported by data lake of cards) |
| **Guided Onboarding** | Onboarding Experience | Introduce quests and encourage collector participation |
| **Quest Hub** | Quest Hub & Checklists | Menu page to see available quests, associated checklists, and track progress |
| **Marketplace Integration** | Missing Card Alerts | Collectors can see/be notified when cards missing from their active quests are listed on Collect |
| **Reward System** | Tiered Badge Reward System | Milestone badges awarded to collectors for scanning cards as part of their quest |
| **Reward System** | FanCash Integration | FanCash distributed to collectors who hit quest milestones with cards in the Vault |
| **Reward System** | Physical Reward Distribution | Back-end system to distribute exclusive cards/experiences for L3/L4 quest completion |
| **Community** | Trade Layer | Opt-in matching of collectors with duplicates of each other's missing cards |
| **Community** | Quest Leaderboard | Leaderboard of collectors who completed quests / are leading the chase |
| **Community** | Personalization | Quest recommendations based on current cards in vault and friends' active quests |
