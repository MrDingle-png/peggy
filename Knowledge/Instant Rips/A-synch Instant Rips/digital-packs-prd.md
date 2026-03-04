# Digital Packs — PRD

> **Pack opening experience demos (Async Instant Rips):**
> - [Wax Pack](https://odyssey-experience-git-feature-asy-33ecf8-fanatics-collectibles.vercel.app/sandbox/async-wax-pack?hidepane=true)
> - [Repack](https://odyssey-experience-git-feature-asy-33ecf8-fanatics-collectibles.vercel.app/sandbox/async-repack?hidepane=true)

**Platform:** Fanatics Collect (Mobile App + Responsive Web)
**Technology:** Async Instant Rips
**Author:** Design (draft for PM team to own)
**Status:** Draft
**Dependencies:** Existing Instant Rips animation engine, Marketplace checkout infrastructure
**Target launch:** May 15, 2026 (target)

---

## 1. Problem statement

Instant Rips — the experience of purchasing a pack and watching cards reveal one by one — is currently only available through Fanatics Live streams. Collectors who want to rip a pack on their own time, without joining a live stream, have no way to do so. This creates three problems:

1. **Ripping is locked behind live schedules.** Collectors have to be watching a stream at the right time to participate in a rip. If they miss it, the moment is gone. There's no on-demand, "rip when I want" option.
2. **Commerce friction on the marketplace.** The Collect marketplace sells cards and sealed product, but there's no immersive purchasing experience. Buying a pack today is a standard ecommerce transaction — add to cart, checkout, wait for delivery. There's no excitement, no reveal, no dopamine.
3. **Missed engagement and revenue.** Every collector who would rip a pack but doesn't want to join a live stream is a missed sale. Async rips unlock impulse purchase behavior — browse, buy, rip, see what you got — on the collector's own schedule.

Digital Packs bring the instant rip experience into the Collect marketplace as a standalone, on-demand feature. No live stream required. No seller participation. Fanatics-sold packs, available 24/7, with an immediate rip animation after purchase.

### Strategic context

This connects directly to two broader initiatives:

- **Live-to-Collect unification:** As Fanatics Live is deprecated and consolidated into Collect, the rip experience needs a marketplace-native home. Digital Packs are how instant rips live on the platform without requiring a live stream.
- **Structural Model alignment:** The Structural Model positions Shop as the discovery and commerce pillar. Digital Packs are a new commerce vertical within Shop — alongside Cards, Drops, and (eventually) Live. The rip animation is classified as a "focused mode" experience with experiential checkout.

---

## 2. Goals

### Product goals

| Goal | How we measure it |
|---|---|
| Create an on-demand ripping experience on Collect | Digital Packs surface live with browse, purchase, and rip flow working end to end |
| Drive incremental pack revenue through impulse purchases | Revenue per user, conversion rate from pack view to purchase |
| Increase session depth and engagement | Time in app for Digital Packs users vs. non-users, repeat purchase rate |
| Establish the async rips platform for future expansion | Multi-pack, new pack types, and fast-follow features launch on the same infrastructure |

### Non-goals (V1)

- **Pack opening experience, gamification, and engagement loops.** This PRD covers the ecommerce experience only — discovery, merchandising, purchase, and the transition into the rip. The rip animation itself, card reveal mechanics, gamification, and any engagement loops designed to enhance the Instant Rips experience are addressed in subsequent work.
- Multi-pack purchase (planned for fast-follow, not MVP)
- Keep-sealed / open-later functionality
- Physical pack fulfillment
- Live stream integration
- Resume rip across devices
- Seller-listed packs (Fanatics-sold only)
- "Notify me" alerts for sold-out or restocking packs
- Back-office tooling beyond Retool configuration

---

## 3. How it works

Digital Packs use the existing Async Instant Rips technology to deliver a buy-and-rip experience entirely within Collect. The collector never leaves the app or website.

### Core flow

```
Collector opens Shop → Digital Packs tab
    → Browses pack grid (sorted, filtered)
    → Taps a pack → PDP with odds, price, "Buy Now"
    → Taps "Buy Now" → Experiential checkout (sheet/modal)
    → Payment completes → Immediate transition to rip animation
    → Cards reveal one by one (focused mode — nav suppressed)
    → All cards revealed → "View in Collection" CTA
    → Cards appear in Collection marked as "New"
```

### Structural Model alignment

| Concept | How Digital Packs fits |
|---|---|
| **Pillar** | Shop (Discovery & Commerce) |
| **Surface type** | Digital Packs tab within Shop → Discover |
| **Checkout pattern** | Experiential — sheet/modal preserves continuity, then transitions to immersive mode |
| **Focused mode** | Rip animation suppresses bottom nav (app) and takes over attention |
| **Exit behavior** | If launched from within app: close returns to origin. If launched via deep link: close returns to Home. Explicit CTA ("View in Collection") overrides. |
| **Collection behavior** | Cards appear in Collection upon reveal, marked as "New" |

---

## 4. User journeys

### 4.1 First-time collector discovers Digital Packs

```
Opens Collect → navigates to Shop
    → Sees Digital Packs tab
    → Taps into it → first-time tutorial triggers:
        "Buy a digital pack → open immediately → cards reveal one by one → cards go to your Collection → all purchases are final"
    → Dismisses tutorial → browses pack grid
    → Taps a pack → sees PDP with odds and price
    → Taps "Buy Now" → payment sheet
    → Completes purchase → pack rip animation begins
    → Cards reveal one by one → excitement builds
    → Final card revealed → "View in Collection" CTA
    → Taps CTA → sees new cards in Collection, marked as "New"
    → Hooked — returns to Digital Packs to buy another
```

### 4.2 Returning collector — repeat purchase

```
Opens Collect → goes directly to Digital Packs (knows the way)
    → Browses grid → notices "Selling Fast" badge on a limited pack
    → Taps pack → PDP → "Buy Now"
    → Payment completes → immediate rip animation
    → Cards revealed → "View in Collection"
    → Uses back navigation to return to PDP
    → Buys another pack of the same type
```

### 4.3 Collector exits mid-animation

```
Purchases a pack → rip animation begins
    → Receives a phone call / swipes away / closes browser tab
    → Cards from the pack are already assigned to the collector
    → Cards appear in Collection (no duplicate reveal)
    → No resume state — the reveal is lost but the cards are safe
    → Next time collector opens Collection, cards are there marked as "New"
```

### 4.4 Collector encounters a sold-out pack

```
Browses Digital Packs grid
    → Sees a pack with "Sold Out" overlay
    → Taps it → PDP loads (can still view odds, details)
    → "Buy Now" is disabled
    → Collector browses other available packs instead
```

### 4.5 Collector on web (responsive experience)

```
Visits Collect on desktop or mobile browser
    → Navigates to Shop → Digital Packs
    → Same grid, sorting, filtering as app
    → Taps pack → PDP → "Buy Now"
    → Experiential checkout in modal
    → Payment completes → rip animation plays in browser
    → Cards revealed → "View in Collection"
    → Cards appear in Collection across all devices (synced via FanID)
```

---

## 5. Feature areas (MVP scope)

### 5.1 Digital Packs index

The primary browse surface within the Shop pillar. The page combines an always-on pack catalog with CMS-driven merchandising zones that let the team promote, feature, and editorialize the pack offering.

**Page structure:**
- Title: "Digital Packs"
- Subheading: "Rip real cards instantly."
- Optional "How it works" link (reuses existing IR explainer)
- **Merchandising zone(s)** — CMS-driven promotional content (see 5.7 Merchandising)
- **Core category grid** — always-on pack catalog organized by category and tier
- **Short-run / limited packs** — featured prominently when live, removed when expired

**Pack grid:**
- Reuses existing pack merchandising components
- Each tile: pack image (dynamic — shows currently available cards, pulls latest grail), pack name, price
- "Selling Fast" badge (existing design system component, threshold defined separately)
- "Sold Out" overlay for short-run / limited packs (tile remains visible, clickable to PDP)
- "Out of Stock" or "Restocking" messaging for always-on tier packs that temporarily run out of inventory (wording TBD)

**Sorting and filtering:**
- Reuses existing marketplace sorting and filtering patterns
- No new interaction models

**Responsive behavior:**
- Grid adapts to viewport — 2 columns on mobile, 3–4 on tablet/desktop
- Same content and functionality across all breakpoints

### 5.2 Pack categories and tiers

The Digital Packs surface has two types of pack offerings: core (always-on) and short-run (time-limited).

**Core categories (always live):**
- Baseball
- Football
- Basketball
- Pokemon
- Mixed Sports
- Pop culture (Disney, Marvel, Star Wars) — potential addition; framework supports without structural changes

**Core tiers (available across categories):**
- Super
- Mega
- Ultra
- Infinity

Each category can have packs at multiple tier levels. The grid presents categories as the primary grouping, with tiers as a secondary dimension within each category.

**Short-run / limited packs:**
- Signature Series — premium, curated pack drops
- Event-based packs — GOAT Pack, Playoff Packs, and other seasonal or moment-driven series
- These appear prominently when active and are removed from the surface when the run ends

> **Decision (from Slack thread, Feb 24):** Pack grouping is manually configured, not derived from card metadata. This avoids mismatches (e.g., a baseball card in a basketball pack incorrectly setting the category).

**How grouping works:**
- Product groups are created manually in Retool
- Checklists (pack configurations) are assigned to a group
- All checklists in a group appear on the pack's PDP as the available tiers for that category (e.g., Super / Mega / Ultra)
- Tier ordering is controllable — so they always appear in the correct order
- Pack tier naming (Super, Mega, Ultra, Infinity) is metadata associated with the pack configuration, not derived from pack contents

**Reusability:** The grouping system supports evergreen packs (core categories × tiers) and short-run/limited packs. New pack types are added by creating new groups and assigning checklists — no engineering work required.

### 5.7 Merchandising

The Digital Packs surface requires merchandising capabilities to promote, feature, and editorialize the pack offering beyond a static product grid.

**Merchandising requirements:**
- **Hero / featured zone** — promotional banner or spotlight at the top of the Digital Packs page. Used to push new drops, highlight short-run packs (e.g., "Playoff Packs — available for 48 hours"), or run seasonal campaigns.
- **Featured pack callouts** — ability to elevate specific packs or categories within the grid (e.g., "New: Signature Series" or "Trending: Pokemon Ultra")
- **Category ordering and visibility** — control which categories appear first, and whether certain categories are temporarily boosted (e.g., Football during NFL season)
- **Editorial copy and imagery** — promotional text, banners, and imagery that give the surface editorial voice beyond a raw product grid
- **Scheduling** — ability to schedule merchandising content to go live and expire at specific times (e.g., Playoff Pack promotion goes live on a specific date)
- **No-code updates** — merchandising changes must not require code deploys

**What merchandising does not control:**
- What packs exist, their pricing, odds, inventory, or sold-out state — this is pack configuration (Retool)
- Pack tile content (image, name, price) — driven by pack data, not merchandising

> **Implementation decision pending:** The system that powers the merchandising layer has not been decided. Options include Contentstack (our CMS, used across Fanatics properties), an extension of the Retool configuration tooling, or another approach. This decision needs to be made with PM and Eng based on operational workflow, scheduling needs, and engineering cost. See Open Questions #11.

**Personalization (future — not MVP):**
The merchandising layer should be designed to support personalization in the future — e.g., surfacing categories or packs based on a collector's sport preferences, purchase history, or collection composition. This is explicitly out of scope for MVP but the architecture should not preclude it.

### 5.3 PDP (Product Detail Page)

PDP framework already exists. Changes for Digital Packs:

- CTA: **"Buy Now"** (not "Add to Cart")
- Odds displayed per existing legal standards
- "All sales final" clearly visible
- Quantity fixed at 1 (no selector in MVP)
- No per-user purchase limit — collectors can buy as many packs as they want
- If pack is sold out (short-run) or out of stock (always-on): CTA disabled, details still viewable. Messaging should distinguish between permanently sold out and temporarily out of stock.
- Tier selector: if the pack belongs to a group with multiple tiers, other tiers are shown as alternate options on the PDP

### 5.4 Purchase and open flow

**Purchase:**
- Experiential checkout — sheet/modal (per Structural Model)
- Supported payment methods: credit card, account funds (FanCash)
- Deferred payment methods (e.g., wire) are not supported
- No confirmation screen between payment and rip
- After payment completes → immediate transition to rip animation

**Transition to opening:**
- Direct launch into existing Instant Rips animation
- May include brief loading state (e.g., "Preparing your pack...")
- Must feel instant and uninterrupted

> **Scope boundary:** This PRD's scope ends at the handoff to the rip animation. The pack opening experience — animation design, card reveal mechanics, gamification, and engagement loops — is covered in subsequent work. The behaviors described below (focused mode, exit handling, post-reveal CTA) are included here only to define the ecommerce flow's end state and re-entry points.

**During opening (focused mode):**
- Bottom navigation suppressed (app)
- Cards reveal one by one
- If collector exits mid-animation: cards appear in Collection, no resume, no duplicate reveal

**Post-reveal:**
- Primary CTA: **"View in Collection"**
- Back navigation returns to PDP (can purchase again)
- Exit behavior follows Structural Model rules:
  - Launched from app → close returns to origin
  - Launched from deep link → close returns to Home
  - Explicit CTA overrides origin

### 5.5 First-time tutorial

**Triggered:**
- First visit to Digital Packs page, or
- First open attempt

**Content:**
- Buy a digital pack
- Open immediately
- Cards reveal one by one
- Cards go to Collection
- All purchases are final

Reuses existing Instant Rips copy.

**Open design decision:** Blocking modal vs. inline — design to explore and recommend.
Tutorial displays once per user.

### 5.6 Collection behavior

- Cards appear in Collection upon reveal
- Marked as "New"
- No sealed pack storage — there is no concept of an unopened digital pack in Collection
- No separate digital inventory section
- Cards sync across devices via FanID

---

## 6. Pack configuration, merchandising, and back-office

Digital Packs require two distinct back-office capabilities: pack configuration (what packs exist, their data and inventory) and merchandising (how packs are presented and promoted on the surface).

### 6.1 Pack configuration (Retool)

This section addresses the engineering implementation questions raised in the Slack thread (Feb 24).

**How packs are configured today:**
Packs are created and configured in Retool. The current system associates card categories with packs based on the types of cards added. This is fragile — if a baseball card is added to a basketball pack, the category metadata would be wrong.

**What changes for Digital Packs:**

| Configuration area | Current approach | Digital Packs approach |
|---|---|---|
| Pack grouping | Derived from card categories | Manually created "product groups" in Retool |
| Tier assignment | Pack naming convention | Metadata field on the pack configuration |
| Tier ordering | Uncontrolled | Explicit sort order per group |
| Checklist assignment | Individual packs | Checklists assigned to a product group; all appear as tiers on PDP |
| Category display | Hardcoded list | Configurable groups — new categories added without code changes |
| Pack imagery | Static per pack | Dynamic — shows currently available cards (latest grail) |

**What Retool needs to support:**

- Create and manage product groups
- Assign checklists to groups
- Set tier order within a group
- Set category metadata independently of card contents
- Control "Selling Fast" threshold per pack
- Mark packs as sold out

### 6.2 Merchandising (system TBD)

The merchandising layer controls how packs are presented and promoted on the Digital Packs surface — not what packs exist. The system that powers this layer has not been decided.

**What the merchandising system must support:**

- Create and manage hero/featured promotional zones (banners, spotlights)
- Feature specific packs or categories with callouts and editorial content
- Control category ordering and visibility on the Digital Packs index
- Manage promotional imagery and copy for short-run/limited packs
- Schedule merchandising content to go live and expire at specific times
- Update without code deploys

> **Implementation decision pending:** Options include Contentstack (our CMS), an extension of Retool, or another approach. The decision should be driven by: who needs to operate this day-to-day (ops team? marketing? PM?), whether scheduling and editorial workflows are needed, and engineering cost. See Open Questions #11.

### 6.3 Separation of concerns

Regardless of which system powers merchandising, the separation between pack configuration and merchandising should be clean:

| Concern | Responsibility | Example |
|---|---|---|
| "Does this pack exist?" | Pack configuration (Retool) | Create a new Playoff Pack with pricing and odds |
| "Where does this pack appear on the page?" | Merchandising (TBD) | Feature the Playoff Pack in the hero zone with a promotional banner |
| "What tier is this pack?" | Pack configuration (Retool) | Assign "Ultra" tier metadata |
| "Should Football be shown first this week?" | Merchandising (TBD) | Reorder categories to lead with Football |
| "Is this pack sold out?" | Pack configuration (Retool) | Mark pack as sold out; "Sold Out" overlay appears |
| "Should we promote Signature Series?" | Merchandising (TBD) | Add editorial callout and featured imagery |

> **Note:** Purpose-built back-office tooling is out of scope for MVP. Retool is the pack configuration layer; the merchandising system is TBD. If Digital Packs scale significantly, a dedicated tooling investment should be evaluated.

---

## 7. Web experience

Digital Packs must work on web from launch — this is not app-only. The experience should be responsive across mobile web, tablet, and desktop.

### What this means for MVP

- Pack grid, PDP, checkout, rip animation, and post-reveal all work in browser
- Responsive layout adapts across breakpoints
- Rip animation runs in browser (WebGL or equivalent — same technology as existing IR on web)
- FanID authentication works on web (consistent with the web auth patterns established for quest redemption and other flows)
- Cards sync to Collection across devices

### Current gap

> **No desktop or responsive web designs exist for Digital Packs.** The Slack thread (Feb 24) flagged this explicitly. Design work is needed to define the responsive behavior for the pack grid, PDP, checkout modal, and rip animation at desktop viewport sizes. This is blocking — designs must be produced before engineering can build the web experience. **Note:** Chad has begun designing web checkout patterns for live, which can inform the Digital Packs web purchase experience and should feel consistent.

### Design principles for web

- Mobile-first responsive design — the mobile app experience is the primary reference
- Desktop should not feel like a stretched mobile layout — take advantage of larger viewports (wider grid, larger rip animation canvas, side-by-side content where appropriate)
- Checkout remains a modal/sheet on all viewports (per Structural Model: experiential checkout)
- Rip animation is always focused mode — full viewport takeover regardless of screen size

---

## 8. Scope: MVP vs. fast-follow

| Area | MVP | Fast-Follow |
|---|---|---|
| Single pack purchase | Yes | — |
| Multi-pack purchase | No | Yes (confirmed by Marcos) |
| Auto-open after purchase | Yes | — |
| Keep sealed / open later | No | TBD |
| Responsive web (mobile/tablet/desktop) | Yes | — |
| Fanatics-sold packs only | Yes | — |
| Seller-listed packs | No | TBD |
| Merchandising capabilities | Yes | — |
| Personalization | No | Future (architecture should not preclude it) |
| Back-office tooling | Retool + merchandising system (TBD) | Purpose-built tooling |
| Resume across devices | No | TBD |
| Analytics specification | No | Yes |
| Debut pack async rip (onboarding) | No | Future — free debut pack could teach rip flow with no purchase required |
| Multi-pack transition UX | N/A | Needs design (how do you go from pack 1 reveal to pack 2?) |

### Multi-pack purchase (fast-follow)

Marcos confirmed (Slack, Feb 24) that multi-pack purchase is planned but not for launch. Key design question for fast-follow: after the first pack's reveal completes, how does the experience transition to the second pack? Options to explore:

- Sequential reveal: first pack finishes → brief interstitial → second pack begins
- Summary + continue: first pack results shown → "Open next pack" CTA
- Batch summary: all packs revealed in sequence → combined results screen

This needs design exploration before fast-follow engineering begins.

---

## 9. Error handling (UX level)

| Scenario | Behavior |
|---|---|
| Payment failure | Standard marketplace error handling — retry or update payment method |
| Animation load failure | Retry, or static fallback showing cards without animation (design to propose) |
| Exit mid-animation | Cards appear in Collection — no resume, no duplicate reveal |
| Card metadata visible before reveal | Must not happen — card data is hidden until the reveal moment |
| Pack sells out during purchase flow | Clear error message — "This pack just sold out" with link back to grid |
| Network loss during animation | Cards are already assigned server-side — when connectivity returns, cards appear in Collection |

---

## 10. Open questions

| # | Question | Owner | Status |
|---|---|---|---|
| 1 | Web/desktop responsive designs — who owns, what timeline? No designs exist yet. | Design | **Needs assignment** |
| 2 | Tutorial modality — blocking modal vs. inline? | Design | **Needs exploration** |
| 3 | Loading state design before rip animation | Design | **Needs exploration** |
| 4 | Static fallback if animation fails to load | Design | **Needs exploration** |
| 5 | Visual tone differentiation for the Digital Packs surface vs. rest of Shop | Design | **Needs exploration** |
| 6 | Multi-pack transition UX for fast-follow — how do you go from pack 1 to pack 2? | Design + PM | Open (fast-follow) |
| 7 | Keep-sealed functionality — is this ever on the roadmap? Does it change the Collection model? | PM | Open |
| 8 | Latest design file confirmation — are current Figma files still the source of truth? (Ana's question from Slack) | Design | **Needs confirmation** |
| 9 | "Selling Fast" badge threshold — what inventory level triggers it? Who configures it? | PM + Ops | Open |
| 10 | Analytics specification — what events do we track across the Digital Packs funnel? | PM + Data | Out of scope for MVP, needs scoping for fast-follow |
| 11 | What system powers the merchandising layer? Options: Contentstack (CMS), Retool extension, or other. Decision should consider who operates it day-to-day, scheduling needs, editorial workflows, and engineering cost. | PM + Eng | **Needs decision** |
| 12 | Merchandising zone design — what does the hero/featured zone look like across breakpoints? How does it interact with the pack grid? | Design | **Needs exploration** |

---

## 11. Dependencies

| Dependency | Status | Risk |
|---|---|---|
| Existing Instant Rips animation engine | Available (used in Live) | Low — proven technology |
| Marketplace checkout infrastructure | Available | Low — standard checkout flow |
| Retool pack configuration tooling | Exists but needs product group support | Medium — new configuration capabilities required |
| Merchandising tooling (system TBD) | Decision pending — options include Contentstack, Retool extension, or other | Medium — system choice affects content modeling, API integration, and operational workflow |
| Design system components (pack tiles, badges, grid) | Available | Low — reusing existing components |
| Web/responsive Instant Rips animation | Needs verification | Medium — must confirm IR animation runs well in browser across viewports |
| FanID web authentication | Available (shared with quest redemption, FanCash) | Low |

---

## 12. Acceptance criteria (MVP)

1. Digital Packs tab loads pack index on both app and web.
2. Pack grid is responsive — adapts from mobile to desktop viewports.
3. Sorting and filtering reuse marketplace components.
4. Pack tiles show pack image, name, and price.
5. "Selling Fast" badge displays when threshold is met.
6. Sold-out packs remain visible with overlay; PDP is still accessible.
7. PDP shows "Buy Now" CTA, odds, and "all sales final."
8. "Buy Now" triggers experiential checkout (sheet/modal).
9. Payment completion immediately launches rip animation (focused mode).
10. Cards reveal one by one; card metadata is not visible before reveal.
11. Cards appear in Collection upon reveal, marked as "New."
12. Exiting mid-animation results in cards appearing in Collection (no duplicate reveal).
13. First-time tutorial displays once per user.
14. Post-reveal CTA ("View in Collection") navigates to Collection.
15. Back navigation from post-reveal returns to PDP for repeat purchase.
16. Pack grouping and tier ordering are configurable in Retool.
17. Merchandising zones (hero, featured callouts) update without code deploys.
18. Category ordering on the Digital Packs index is controllable via the merchandising system.
19. Short-run/limited packs are prominently merchandised when live and removed when expired.

---

## Appendix A: Related documents

- **Digital Packs feature spec** (Notion) — `https://www.notion.so/fanaticscollect/Digital-Packs-309d7c400ecf80b5aa41cbdda98e910e`
- **Fanatics Collect Structural Model** (Notion) — `https://www.notion.so/fanaticscollect/Fanatics-Collect-Structural-Model-30bd7c400ecf805c8914e8c2150740df`
- **Fanatics Live → Collect Unification** — `Tasks/fanatics-live-to-collect-unification.md`
- **Digital Packs PRD Review (Mar 3, 2026)** — `Knowledge/Instant Rips/A-synch Instant Rips/digital-packs-review-mar3.md`
