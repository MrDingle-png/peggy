# Competitive Quest Infrastructure — PRD

**Launch use case:** The Grail (Topps Soccer)
**Author:** Design (draft for PM team to own)
**Status:** Draft
**Dependencies:** FanCash Trading Card Redemption V1 (August 2026) — reuses shared infrastructure
**Target launch:** Post-FanCash V1 (TBD — aligned to next Grail season)

---

## 1. Problem statement

Topps currently runs competitive quests like The Grail on a standalone website (`ripped.topps.com/the-grail`), completely disconnected from Fanatics Collect. Collectors create a separate account, enter codes on a separate site, and track progress on a separate leaderboard. This creates three problems:

1. **Fragmented experience.** Collectors who use Collect for their vault, marketplace, and collection have no way to see their quest progress where they already spend time. The quest lives in a browser tab, not in their collecting app.
2. **No acquisition loop.** The Grail drives excitement and purchases, but none of that energy flows into Collect. We're missing a funnel from "I found a Grail card" to "I'm now an active Collect user."
3. **Not scalable.** Every new quest (Soccer Grail, F1 Grail, Topps Chrome Black) requires a new standalone build. There's no reusable infrastructure, no shared design system, and no operational consistency.

Fanatics Collect should be the home for competitive quests. By building configurable quest infrastructure, we can bring The Grail into Collect while simultaneously creating a system that scales to any future quest — same mechanic, different products, different sports.

---

## 2. Goals

### Product goals

| Goal | How we measure it |
|---|---|
| Make Collect the home for competitive quests | 100% of Grail participation happens through Collect (no standalone site) |
| Drive new user acquisition through quests | New Collect signups attributed to quest code redemption |
| Increase engagement and retention among quest participants | DAU/WAU of quest participants vs. non-participants |
| Build reusable infrastructure | Second quest (F1 or Chrome Black) launches with <30% of V1 effort |

### Non-goals (V1)

- Building quest creation tooling for non-technical users (V1 is eng-configured)
- Supporting non-competitive quest types (e.g., "collect at your own pace" set quests) — those are a separate initiative
- Social features beyond leaderboard (trading, matching, community feeds)

---

## 3. How The Grail works today — reference

Understanding the current experience is critical to designing the Collect-native version. This section documents the existing Grail mechanic as it runs on `ripped.topps.com`.

### Core mechanic

The Grail is a **9-card continuity set** spread across multiple Topps products released over a season. When collected, the 9 cards form a unique 3x3 card image. The first collector to find, redeem, and verify all 9 wins the Grand Prize.

### Current flow

```
Pull Grail card from pack
    → Scan QR code or visit ripped.topps.com
    → Create account (separate from Collect/FanID)
    → Enter unique redemption code from back of card
    → Card appears on your profile + live leaderboard
    → Repeat for all 9 unique Grail cards
    → When 9/9 redeemed, Topps contacts you for verification
    → Ship physical cards to Topps for authentication
    → Prize awarded based on finishing position
```

### Key parameters (2024/25 Soccer Grail)

| Parameter | Value |
|---|---|
| Cards to complete | 9 unique Grail cards (numbered 1–9) |
| Products spanning | 7 Topps soccer products across the 2024/25 season |
| Total Grail cards in circulation | ~450 across all products |
| Grand Prize (1st to complete) | 2 tickets to UEFA Champions League Final + travel/hotel + themed trading card + poster |
| Runner-up Prizes (2nd–6th) | Oversized themed trading card + poster |
| Total winners | 6 (1 Grand Prize + 5 Runner-up) |
| Entry mechanism | QR code scan or website visit → enter unique code |
| Verification | Physical cards shipped to Topps for authentication |
| Concurrent quests | Multiple (2024/25 Soccer, 2025/26 Soccer, F1 2025) |
| Redemption locks | Codes locked before new product releases, reopened on release day |

### What makes it compelling

- **Scarcity + competition.** ~450 total Grail cards across 7 products. Only 6 prizes. Race-to-complete creates urgency.
- **Serialized tension.** Cards drop across products over months. You can't complete on day one — everyone is waiting for the same final product.
- **Aspirational prize.** UCL Final tickets are a "money can't buy" experience that transcends card value.
- **Secondary market dynamics.** Grail cards trade on the secondary market with codes intact — adding a speculative layer.

### What's broken about the current experience

| Pain point | Impact |
|---|---|
| Separate account from Collect/FanID | Friction, no identity portability |
| No mobile-native experience | Standalone website, not optimized for mobile |
| No connection to vault or collection | Quest cards don't appear in the collector's Collect portfolio |
| No push notifications | Collectors have to manually check the site |
| No integration with marketplace | Can't buy/sell Grail cards with quest context on Collect |
| Manual verification by email | Slow, error-prone, no tracking for the collector |
| No reusability | Each new quest requires rebuilding |

---

## 4. Quest infrastructure — building blocks

This PRD scopes the generic infrastructure needed to power competitive quests on Collect. Each building block is designed to be configurable so that The Grail, a Chrome Black quest, an F1 quest, or any future competitive quest can be launched by configuring — not rebuilding.

The building blocks below align with the shared framework defined in `programs-vs-quests-building-blocks.md`, scoped specifically for competitive "race to complete" quests.

### 4.1 Quest definition engine

The data model that defines a quest instance. Each quest is a configuration, not code.

**A quest definition includes:**

| Field | Description | Example (Soccer Grail 2025/26) |
|---|---|---|
| Quest ID | Unique identifier | `grail-soccer-2025-26` |
| Quest name | Display name | "The Grail: 2025/26 Soccer" |
| Quest type | Mechanic classification | `competitive-completion` |
| Sport / category | Sport or product line | Soccer |
| Required cards | Number of unique cards to complete | 9 |
| Card definitions | List of quest card IDs, names, images, and associated products | Grail No. 1 → Topps UEFA Club Competitions 2025/26 |
| Product set | Products that contain quest cards | [list of 8 products] |
| Total cards in circulation | Approximate number of quest cards produced | ~450 |
| Prize tiers | Ranked prize definitions | 1st: Grand Prize, 2nd–6th: Runner-up |
| Entry period | Start/end dates or conditions | Starts at first product release, ends when all prizes claimed |
| Redemption windows | Periods when code entry is locked/unlocked per product | Locked before product release, unlocked on release day 9 AM ET |
| Status | Lifecycle state | `pre-launch` / `active` / `completing` / `completed` / `archived` |
| Rules | Terms, eligibility, verification requirements | Age 18+, physical card verification, one code per card |

**Reusability requirement:** The PM or ops team should be able to launch a new quest by creating a new quest definition with different values for the fields above — no engineering work beyond the initial infrastructure build.

### 4.2 Discovery & education hub

A publicly accessible quest landing experience within Collect that adapts across lifecycle phases.

**Three phases:**

| Phase | Content | Purpose |
|---|---|---|
| **Pre-launch** | Teaser imagery, countdown, product release calendar, "what is this quest" explainer | Build anticipation, drive pack purchases |
| **Active** | How to participate, which products to buy, current leaderboard standings, which cards are live | Drive participation and urgency |
| **Completed / Archived** | Winner spotlight, final leaderboard, recap content | Celebrate winners, build hype for next season |

**Key features:**
- Quest overview: name, description, imagery, prize details
- Product calendar: which products contain which quest cards, release dates, availability status
- Visual card grid: 3x3 layout showing all 9 cards, greyed out vs. collected (for logged-in users)
- Leaderboard: top collectors ranked by cards redeemed, sortable and filterable
- Rules / T&C: linked or inline
- Deep link support: shareable URLs for marketing, social, and QR codes on physical cards

**Reusability requirement:** The layout and content structure is templated. Each quest populates from the quest definition. Sport-specific branding (colors, imagery, logos) is configurable via theming.

### 4.3 Code redemption flow

The mechanism by which a collector enters a quest card code and registers progress.

**Flow:**

Code redemption works on both web and app. The QR code or URL on the card always lands on the public quest landing page (web), which routes collectors into the appropriate redemption path.

```
Collector pulls quest card from pack
    → Scans QR code or visits URL → public quest landing page (web)
    → Taps "Redeem Your Card"
    → Routing:
        - Has FanID + app installed → deep-linked into Collect app → code entry screen
        - Has FanID, no app → authenticates on web → code entry on web
        - No FanID → signs up on web → code entry on web
    → Enters unique alphanumeric code from back of card
    → System validates code (same logic on web and app):
        - Code exists and belongs to this quest
        - Code has not been previously redeemed
        - Redemption window for this product is currently open
        - User meets eligibility requirements (age, account status)
    → On success:
        - Digital image of the quest card is generated and added to quest progress
        - Progress tracker updates (e.g., "4 of 9 collected")
        - Leaderboard position updates
        - Confirmation screen with card reveal animation
        - If quest is now complete (9/9): trigger completion flow
        - Web-only users: prompt to download Collect for push notifications and full experience
    → On failure:
        - Clear error message (code already used, window closed, invalid code)
        - Guidance on what to do next
```

**Connecting to FanID:** Unlike the current standalone Grail site, code redemption is tied to the collector's FanID — no separate account creation. FanID authentication works on both web and app. This is a key acquisition moment: the web experience removes friction for first-time users (no app download required to redeem), while post-redemption prompts drive app adoption for ongoing engagement.

**Reusability requirement:** The code validation logic is quest-aware (checks which quest the code belongs to, whether the redemption window is open, etc.) but the redemption UX is shared across all quests. The web and app redemption experiences use the same validation API and quest rules engine.

### 4.4 Progress tracking

How collectors see where they stand in the quest.

**Individual progress:**
- Visual card grid (3x3 for Grail) showing collected vs. remaining
- Digital images of redeemed cards shown in full; uncollected slots show silhouette or placeholder
- Count indicator: "6 of 9 collected"
- Product hints for remaining cards: "Grail No. 7 can be found in Topps Chrome UEFA Club Competitions 2025/26"
- Estimated availability: "Available now" vs. "Releasing March 2026"

**Competitive context:**
- Your rank on the leaderboard
- How many other collectors are at the same progress level or ahead
- "X collectors have completed this quest" (if any)

**Where it lives:**
- Dedicated quest detail page (from quest hub)
- Summary card on collection home or profile
- Badge or indicator on quest-eligible cards in the marketplace

**Reusability requirement:** The progress component is driven by the quest definition (number of cards, card definitions, layout). A 9-card quest shows a 3x3 grid. Future quests with different card counts would render accordingly.

### 4.5 Notifications & lifecycle triggers

Automated communications at key quest moments.

| Trigger | Channel | Message type |
|---|---|---|
| New product releases containing quest cards | Push + in-app | "Grail No. 7 is now available in Topps Chrome UEFA. Start hunting." |
| Redemption window opens | Push + in-app | "Codes for [product] are now live. Redeem yours now." |
| Card successfully redeemed | In-app (confirmation) | "You've collected Grail No. 4! 5 of 9 complete." |
| Milestone reached (e.g., 6 of 9) | Push + in-app | "You're 3 cards away from completing The Grail." |
| Another collector completes the quest | Push + in-app | "[Collector] just completed The Grail! X prizes remaining." |
| Approaching final product release | Push + in-app | "The final Grail card releases on [date]. Get ready." |
| Quest completed (9/9) | Push + in-app + email | "You've completed The Grail! Verification instructions incoming." |
| Redemption window lock (pre-release) | In-app | "Code entry is locked until [date] at 9 AM ET." |

**Reusability requirement:** Notification templates are parameterized (quest name, card name, progress count, collector name). The lifecycle trigger system is shared with FanCash and other programs.

### 4.6 Leaderboard & social

The competitive layer that creates urgency and FOMO.

**Leaderboard features:**
- Ranked list of participants by number of unique cards redeemed
- Tie-breaking by timestamp of most recent redemption
- Display: username/avatar, cards collected (e.g., "7/9"), last card redeemed date
- Filterable by friends (future) or all participants
- Real-time or near-real-time updates after code redemption
- Highlight: "You" row always visible when scrolling

**Social sharing:**
- Share quest progress card (image showing your 3x3 grid with collected cards revealed)
- Share individual card redemption moment
- Share quest completion moment
- Deep link back to quest hub in Collect

**Reusability requirement:** The leaderboard component is generic — it ranks participants by a configurable metric (cards collected, completion time, etc.) and renders against the quest definition.

### 4.7 Completion & prize fulfillment

What happens when a collector redeems their final quest card.

**Completion flow:**

```
Collector redeems 9th unique card
    → Celebration moment (animation, confetti, full 3x3 reveal)
    → "You've completed The Grail!" confirmation
    → Leaderboard position shown: "You are the Xth collector to complete this quest"
    → If eligible for prize:
        → Prize details shown (Grand Prize vs. Runner-up based on position)
        → Verification flow initiated:
            - Instructions to send physical quest cards to the Fanatics Collect Vault
            - Free shipping label generated in-app (no cost to collector)
            - Collector ships 9 Grail cards to the vault
            - Tracking status visible in-app: "Label created" → "Cards shipped" → "Received at vault" → "Verified"
            - Vault ops team authenticates the cards
        → Upon verification:
            - Quest cards are now in the collector's vault as authenticated items
            - Prize card redeemed into collector's vault
            - Collector has full vault actions on their Grail cards: ship home / send for grading / list on marketplace / keep in vault
            - Physical prize items (poster, etc.) shipped separately
    → If not eligible for prize (finished after all prizes claimed):
        → Completion badge awarded
        → Digital completion card or certificate in vault
        → Recognition on leaderboard as a completer
```

> **⚠️ Needs ops validation:** The vault-based verification flow described above must be validated with Vault Operations before finalizing. Key questions: Can the vault team handle quest card authentication as part of their existing intake process? What is the SLA for verification turnaround? Are there any restrictions on card types the vault accepts that would affect quest cards? This is a process change from the current Grail flow (which ships directly to Topps) and needs alignment between Vault Ops, Topps product team, and the quest program owner.

**Why vault-based verification:** Routing verification through the Collect vault — rather than a separate Topps shipping address — keeps the experience within the Collect ecosystem and unlocks post-verification value. Once cards are authenticated and in the vault, collectors can sell them on the marketplace, send them for grading, or ship them home. This turns the verification step from a friction point into a value-add moment.

**Reusability requirement:** The completion flow is configurable per quest — number of prizes, prize types, whether physical verification is required, what digital/physical rewards are granted. The vault verification path can be toggled on/off per quest.

### 4.8 Rules & eligibility engine

The configurable rules that govern each quest.

| Rule type | Description | Example |
|---|---|---|
| Eligibility | Who can participate | Age 18+, valid Collect account with FanID |
| Card qualification | What cards count for the quest | Grail cards numbered 1–9 from specified product set |
| Redemption windows | When codes can be entered | Per-product windows, locked before release day |
| Completion criteria | What constitutes finishing | 1 of each unique card (1–9) redeemed |
| Winner determination | How prizes are allocated | First 6 to complete, ties broken by timestamp |
| Verification | How completion is confirmed | Physical cards shipped to Fanatics Collect Vault (free shipping), authenticated by vault ops team |
| Transferability | Can progress be moved between accounts | No — codes are one-time use, tied to FanID |
| Secondary market | Can quest cards be purchased secondhand | Yes, but Topps is not responsible for pre-redeemed codes |
| Concurrent quests | Can a user participate in multiple quests | Yes — each quest is independent |

**Reusability requirement:** Rules are stored as part of the quest definition. The rules engine evaluates eligibility and validates actions (code entry, completion) against these rules in real time.

---

## 5. User journeys

### 5.1 Entry point — QR code or URL (all collectors)

Every journey starts at the same place: the public quest landing page on web. This is true whether the collector scans the QR code on the back of the card, taps a link in marketing, or types in a URL.

```
Pulls a Grail card from a Topps soccer pack
    → Sees QR code on back of card (or a URL)
    → Scans QR code or visits URL
    → Lands on public quest landing page (web)
        - Quest overview: what The Grail is, prize details, how it works
        - Live leaderboard (view-only)
        - Product calendar: which packs contain Grail cards
        - "Redeem Your Card" CTA
    → Taps "Redeem Your Card" → routing logic:

        Path A — Has FanID + has the Collect app:
            → Deep-linked into Collect app → code entry screen
            → Enters code → card revealed, quest progress updates (see 5.3, 5.4)

        Path B — Has FanID, no app:
            → Authenticates with FanID on web
            → Enters code on web → card revealed, quest progress starts
            → Post-redemption prompt: "Get the app for push notifications, 
              leaderboard updates, and your full collection"
            → Can continue participating on web or download app later

        Path C — No FanID (new to Fanatics):
            → Signs up for FanID on web (lightweight registration)
            → Enters code on web → card revealed, quest progress starts (1/9)
            → Post-redemption prompt: "Download Collect to track your progress,
              see the leaderboard, and get notified when new Grail cards drop"
            → Now has FanID — can return via web or download app at any time
```

The web experience is a complete redemption path, not a fallback. The app is the preferred experience for ongoing engagement, but no collector should be blocked from redeeming because they don't have the app installed.

### 5.2 New collector — acquired through The Grail

```
Follows Path C above (no FanID, no app)
    → Creates FanID on web, redeems first code (1/9)
    → Sees quest hub on web: leaderboard, remaining cards, product calendar
    → Intrigued — downloads Collect from post-redemption prompt
    → Opens app → FanID already linked → quest progress visible immediately
    → Sees 1/9 progress, push notifications enabled
    → Hooked — now has a reason to keep opening Collect
```

### 5.3 Existing collector — casual participant

```
Already uses Collect for vault and marketplace
    → Pulls a Grail card, didn't know about the quest
    → Either:
        (a) Opens Collect → sees "Redeem a quest code" in quest hub or home feed
        (b) Scans QR code on card → lands on web → deep-linked into app (Path A)
    → Enters code → learns about The Grail, sees 1/9 progress
    → Browses marketplace for other Grail cards
    → Buys a Grail card on marketplace → enters that code too (2/9)
    → Follows quest passively, enters codes when cards appear
```

### 5.4 Competitive collector — racing to finish

```
Knows about The Grail, actively buying products to find cards
    → Checks quest hub daily for leaderboard updates
    → Gets push notification: "Grail No. 7 is now available in Topps Chrome UEFA"
    → Buys packs on release day, pulls Grail No. 7
    → Redeems code immediately → sees position on leaderboard (8/9, ranked 3rd)
    → Gets notification: "[Collector] just completed The Grail! 5 Runner-up prizes remain"
    → Urgency increases — hunts for final card
    → Finds Grail No. 9 → redeems → completes quest
    → Celebration moment → ranked 4th → Runner-up Prize
    → Ships cards for verification → prize card redeemed into vault
```

### 5.5 Collector who finishes after prizes are claimed

```
Completes The Grail after all 6 prizes are awarded
    → Still gets celebration moment and completion badge
    → Recognized on leaderboard as a completer
    → Digital completion card added to vault
    → Social sharing moment: "I completed The Grail"
```

---

## 6. Feature areas (V1 scope)

### Quest Hub

The central destination within Collect for discovering and managing quests.

- **Quest catalog:** List of active, upcoming, and completed quests
- **Quest detail page:** Full quest overview, progress, leaderboard, product calendar (see 4.2)
- **Entry point:** Accessible from Collect navigation (tab bar, profile, or home feed)

### Code Redemption

- **Public quest landing page (web):** QR codes and URLs route to a web-based quest landing page — not the app store. This page shows quest details, leaderboard, and a "Redeem Your Card" CTA. Accessible to anyone, no login required to browse.
- **Web redemption flow:** Collectors without the app can authenticate with FanID (or create one) and complete code redemption entirely on web. No app download required.
- **App deep linking:** Collectors who have FanID and the Collect app are deep-linked from the web landing page into the app's code entry screen.
- **Code entry screen:** Alphanumeric input with validation — same UX on web and app, backed by the same validation API.
- **New user onboarding:** No-FanID users sign up on web → redeem on web → post-redemption prompt to download app for notifications and full experience.
- **Validation engine:** Real-time checks against quest rules (see 4.3)

### Quest Progress & Card Grid

- **Visual grid:** 3x3 card layout showing collected vs. remaining
- **Digital card images:** Generated upon code redemption (not vault-ingested)
- **Progress indicator:** "X of 9 collected" with product hints for remaining cards
- **Collection integration:** Quest progress summary visible in user's collection/profile

### Leaderboard

- **Ranked participant list:** Sorted by cards collected, then by timestamp
- **Real-time updates:** Reflects new redemptions within minutes
- **Self-highlighting:** "Your position" always visible
- **Privacy:** Display name only (no personal info)

### Notifications

- **Push notifications:** Key quest moments (new product, milestone, competitor completion)
- **In-app messaging:** Code redemption confirmation, progress updates
- **Email:** Completion/verification instructions, prize confirmation

### Completion & Prize Flow

- **Completion celebration:** Full-screen moment when 9/9 redeemed
- **Prize assignment:** Based on finishing position against quest definition
- **Verification workflow:** In-app status tracking for physical card authentication
- **Prize card vault redemption:** Digital prize card added to vault with full vault actions (ship, grade, list, keep)

---

## 7. Configurable vs. fixed (V1)

To clarify what is built once vs. what changes per quest:

| Component | Fixed (built once) | Configurable (per quest) |
|---|---|---|
| Quest hub UI | Layout, navigation, component library | Quest branding, imagery, colors |
| Code redemption flow | Input screen, validation UX, error handling | Quest-specific validation rules, redemption windows |
| Progress grid | Grid component, animations, progress bar | Number of cards, card images, grid layout (3x3, etc.) |
| Leaderboard | Ranking logic, display component, real-time updates | Ranking metric, tie-break rules, display fields |
| Notifications | Delivery infrastructure, template engine | Message copy, trigger conditions, timing |
| Completion flow | Celebration UX, verification tracking | Prize definitions, verification requirements |
| Rules engine | Evaluation logic, eligibility checks | Rule parameters per quest |

---

## 8. Dependencies & sequencing

### Reuses from FanCash V1

| Capability | Built for FanCash | Extended for Quests |
|---|---|---|
| Code redemption flow | Scratch-off code entry in Collect | Same flow, quest-aware validation |
| FanID integration | Redemption tied to FanID | Quest participation tied to FanID |
| Collection integration | FanCash cards appear in collection | Quest progress appears in collection |
| Notification system | Weekly payout notifications | Quest lifecycle notifications |
| Landing page template | FanCash program hub | Quest discovery hub |

### New for Quests (not in FanCash scope)

| Capability | Why it's new |
|---|---|
| Quest definition engine | FanCash is a single program; quests need a configurable definition model |
| Leaderboard | FanCash has a leaderboard but it's earnings-based; quests need completion-race ranking |
| Multi-product card tracking | FanCash is single-product; quest cards span multiple products over time |
| Redemption window management | FanCash has a single long window; quests lock/unlock per product release |
| Completion & verification flow | FanCash has no "completion" state; quests have a race-to-finish with verification |
| Prize card vault redemption | FanCash rewards are FanCash currency; quest rewards are physical/digital collectibles |
| Digital card image generation | FanCash cards exist as physical items in vault; quest cards are digital-only representations |

### Sequencing recommendation

```
FanCash V1 ships (Aug 2026)
    → Shared infra proven: code redemption, FanID, notifications, collection integration
    → Quest infrastructure build begins
        → Quest definition engine + rules engine
        → Quest hub + discovery page (extends FanCash landing page template)
        → Leaderboard (extends FanCash leaderboard component)
        → Code redemption (extends FanCash flow with quest-aware validation)
        → Progress tracking + card grid (new)
        → Completion + verification + prize flow (new)
    → The Grail: Soccer 2026/27 launches as first quest on Collect
    → Fast follow: F1 or Chrome Black using same infrastructure
```

---

## 9. Success metrics

| Metric | Definition | Target |
|---|---|---|
| Quest participation rate | % of Grail card pullers who redeem at least 1 code on Collect | >80% |
| New user acquisition | New Collect accounts created via quest code redemption | TBD (benchmark against standalone site) |
| Engagement lift | DAU/WAU of quest participants vs. matched non-participants | Measurable lift |
| Time to second quest | Engineering effort to launch quest #2 (F1 or Chrome Black) | <30% of V1 build effort |
| Completion rate | % of participants who complete the quest | Benchmark (expected to be low given scarcity) |
| Marketplace integration | Quest card transactions on Collect marketplace | Track volume and whether quest context influences purchase |
| NPS / satisfaction | Post-quest survey of participants | Higher than standalone Grail experience |

---

## 10. Open questions

| # | Question | Owner | Status |
|---|---|---|---|
| 1 | What is the target launch window for the first Collect-native quest? Which Grail season do we aim for? | PM | Open |
| 2 | **⚠️ Vault-based verification — needs ops validation.** PRD now proposes that prize winners ship Grail cards to the Fanatics Collect Vault (free shipping) for authentication. This replaces the current flow of shipping directly to Topps. Needs validation: Can vault ops handle quest card authentication as part of existing intake? What is the verification SLA? Are there card type restrictions? How does this coordinate with the Topps product team who currently owns verification? | PM + Ops | **Needs validation** |
| 3 | Should quest cards be flagged or badged on the marketplace so buyers know a card has quest value? | PM + Design | Open |
| 4 | How do we handle the case where someone buys a quest card on the marketplace but the code was already redeemed? | PM + Legal | Open |
| 5 | Do we need to support concurrent quests in V1, or is one active quest sufficient? (Current Grail runs multiple concurrently) | PM + Eng | Open |
| 6 | What is the data contract with the Topps product team for quest card definitions and redemption codes? | PM + Eng | Open |
| 7 | Should non-prize completers receive a digital reward (badge, completion card)? How does this connect to the reward pyramid (L1–L4)? | PM + Design | Open |
| 8 | How do redemption locks work technically? Is there a content calendar system, or is this manual ops? | PM + Eng | Open |
| 9 | What analytics events do we need to track across the quest funnel (view hub → enter code → milestone → complete)? | PM + Data | Open |
| 10 | How does this integrate with the broader Collector Quests strategy (see `collector-quests-strategy-proposal.md`)? Is The Grail the first quest, or do simpler quests (L1/L2) launch first? | PM + Strategy | Open |

---

## Appendix A: The Grail V1 — quest definition

Example configuration for the first quest launched on this infrastructure:

```
quest_id: grail-soccer-2026-27
quest_name: "The Grail: 2026/27 Soccer"
quest_type: competitive-completion
sport: soccer
status: pre-launch

cards:
  total_unique: 9
  total_in_circulation: ~450
  layout: 3x3
  definitions:
    - id: grail-1
      name: "Grail No. 1"
      product: "Topps UEFA Club Competitions 2026/27"
      release_date: 2026-12-XX
    - id: grail-2
      name: "Grail No. 2"
      product: "Topps Chrome UEFA Club Competitions 2026/27"
      release_date: 2027-01-XX
    # ... (7 more cards)

product_set:
  - "Topps UEFA Club Competitions 2026/27"
  - "Topps Chrome UEFA Club Competitions 2026/27"
  - "Topps Museum UEFA Club Competitions 2026/27"
  - "Topps Finest UEFA Club Competitions 2026/27"
  - "Merlin Chrome UEFA Club Competitions 2026/27"
  - "Topps Stadium Club Chrome UEFA Champions League 2026/27"
  - "Topps Premier League Chrome 2026/27"
  - "Topps MLS Chrome 2026/27"

prizes:
  - position: 1
    name: "Grand Prize"
    description: "2 tickets to UEFA Champions League Final + travel + themed card + poster"
    type: experience + physical
    requires_verification: true
    vault_item: themed-trading-card
  - position: 2-6
    name: "Runner-up Prize"
    description: "Oversized themed card + poster"
    type: physical
    requires_verification: true
    vault_item: oversized-themed-card

rules:
  eligibility:
    min_age: 18
    account_required: true (FanID)
  completion:
    criteria: "1 of each unique card (1-9) redeemed"
    winner_determination: "First 6 to complete, ties broken by timestamp"
  verification:
    method: "Ship physical cards to Fanatics Collect Vault for authentication (free shipping)"
  transferability: "Codes are one-time use, tied to FanID, non-transferable"
  concurrent_participation: true
```

---

## Appendix B: Related documents

- `programs-vs-quests-building-blocks.md` — Shared building blocks framework for programs and quests
- `fancash-trading-card-redemption-v1.md` — FanCash Trading Card PRD (infrastructure dependency)
- `collector-quests-strategy-proposal.md` — Broader Collector Quests strategy and taxonomy
- `collector-quests-framework.md` — Task: defining the quest framework
- `building-blocks-for-topps-programmes.md` — Task: building shared infrastructure
