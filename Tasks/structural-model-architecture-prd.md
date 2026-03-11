# Fanatics Collect Structural Model — Architecture PRD

> **Interactive wireframe:** [structural-model-wireframe.html](../Artifacts/structural-model-wireframe.html)
> **Source model:** [Notion — Structural Model](https://www.notion.so/fanaticscollect/Fanatics-Collect-Structural-Model-30bd7c400ecf805c8914e8c2150740df)

**Platform:** Fanatics Collect (Mobile App + Responsive Web)
**Author:** Design (draft for PM team to own)
**Status:** Draft
**Dependencies:** Existing marketplace, vault, and live infrastructure; Fanatics One identity layer
**Target:** Rolling adoption — no single launch date; individual initiatives align to this model as they ship

---

## 1. Problem statement

Fanatics Collect has grown organically around commerce. The current information architecture reflects that history: the product is structured like a marketplace with ownership features attached, rather than a collecting platform with commerce embedded. This creates four specific problems:

1. **Account is a dumping ground.** Offers, Bids, Orders, Vault Activity, Wallet, and settings all share the same space. Active engagement behaviors (bidding on an auction, negotiating an offer) sit alongside system machinery (order history, payout settings). Collectors have to context-switch between "things I'm actively doing" and "things I need to manage."

2. **Communication is fragmented.** Notifications (system-to-user) and Messaging (user-to-user) are separate surfaces with separate entry points. Offers — which are inherently conversational — live in Account rather than in either communication channel. Collectors check three places to understand "what needs my attention."

3. **Shop lacks vertical structure.** The current Shop toggles between Discover and Saved as primary modes. Content verticals (Cards, Packs, Drops, Live) are secondary browse filters within Discover. This inverts the natural browsing model: collectors think in verticals first ("I want to browse cards") and then apply filters, not the other way around.

4. **Ownership and commerce are structurally entangled.** Collection, which should be a portfolio and display space, risks absorbing workflow logs. Account, which should be operational machinery, absorbs discovery behaviors. The boundaries between pillars are not clearly defined, leading to feature placement that feels convenient rather than intentional.

These problems will compound as the platform scales. More features, more content types, more community interaction — without clear structural boundaries, every new addition becomes a negotiation about "where does this go?"

---

## 2. Goals

### Product goals

| Goal | How we measure it |
|---|---|
| Reduce cognitive load in Account | Task completion time for common Account actions (manage listing, check order status) decreases; heatmap dead zones in current Account reduce |
| Unify communication into a single destination | Percentage of users who check a single surface (Inbox) vs. multiple surfaces for alerts and messages; notification discovery rate |
| Increase Shop engagement through vertical-first browsing | Browse depth per session increases; conversion rate from Shop entry to listing view improves |
| Establish clear IA boundaries that scale | New features can be placed using the model's guardrails without requiring IA redesign; feature placement disputes decrease |
| Prepare for community and social expansion | Messaging, offers, and future trade negotiation share a unified container that scales with collector relationships |

### Non-goals

- Redesigning individual screens or UI components — this document defines structure, not visual design
- Defining the Live-to-Collect unification timeline — that is a separate initiative that aligns to this model
- Specifying API or data architecture changes — those follow from IA decisions but are out of scope here
- Defining the Want List public/social mechanics — Want List is positioned structurally but its feature spec is separate

---

## 3. North Star and principles

### North Star

Fanatics Collect is evolving from:

> **A commerce app with ownership attached**

to:

> **An ownership-first collecting platform with industry-best commerce embedded.**

The product should increasingly answer: *"What's happening in my collecting world?"*

Ownership is the center of gravity. Commerce, operations, and social activity orbit around it.

### Governing principles

1. **Ownership is the center; operations orbit it.** Collection is where meaning lives. Account is where machinery lives. They must not blur.
2. **Account is machinery; Collection is meaning.** Account handles ledgers, settings, and servicing. It should never become a discovery surface, a social feed, or a place to manage active engagement.
3. **Watchlist is private discovery memory; Want List is public intent.** Watchlist (in Shop) is a personal, private filter for saved items and bid activity. Want List (in Collection) is an opt-in public signal of what a collector is looking for.
4. **Inbox is a unified communication hub.** Messages, Offers, and Alerts converge in a single filterable feed. One place to check "what needs my attention."
5. **Cart is a commerce utility.** Persistent across sessions and devices. Always accessible. Never a navigation pillar.
6. **Hide navigation only for true focused modes.** Depth alone does not justify suppressing the tab bar. Only immersive, attention-capturing experiences suppress navigation.
7. **Immersive modes remember origin.** Close returns to where you came from. Deep-linked entry returns to Home. Explicit CTAs override both.
8. **Canonical product catalogue records are foundational.** Search, Hubs, and Collection growth all depend on canonical card records that exist independent of active marketplace supply.
9. **Programs are ownership-adjacent features that live in Collection.** Performance Cards, Red Rookie, and similar programs reinforce ownership gravity. Currency balances live in Wallet, not Programs.
10. **Shop has a curated home and dedicated verticals.** Shop Home surfaces cross-vertical recommendations and entry points. Cards, Packs, Drops, and Live are dedicated browsing surfaces with their own filter bars. Filters (including Watchlist) are inline tools within each vertical.

---

## 4. Information architecture

Five primary pillars, each with a clear job. No pillar absorbs responsibilities from another for convenience.

### 4.1 Home — Orchestration

**Purpose:** Curate what matters right now across the ecosystem.

Home is not a utility dump. It is a narrative and prioritization layer that references underlying surfaces without replacing them.

**Home surfaces:**

- Priority tasks requiring action (e.g., payment due, offer awaiting response)
- Portfolio highlights (e.g., collection value changes)
- Contextual summaries (e.g., "Since your last visit...")
- Entry points into focused modes (e.g., auction closing soon, live stream starting)

**Guardrail:** Home orchestrates. It summarizes, highlights, and deep-links. It must not absorb core functionality from other pillars.

---

### 4.2 Shop — Discovery & Commerce

**Purpose:** Browse and purchase inventory and experiences.

Shop has a two-level structure: a **curated home page** for cross-vertical discovery, and **dedicated vertical surfaces** for focused browsing.

#### Shop Home (default landing)

When a collector taps Shop, they land on a curated home page — not directly inside a vertical. The home page serves two roles:

**1. Entry point grid.** A 2x2 grid of entry points into the four dedicated verticals:

| Entry point | Navigates to |
|---|---|
| **Cards** | Dedicated Cards surface with full filter bar |
| **Packs** | Dedicated Packs surface |
| **Drops** | Dedicated Drops surface |
| **Live** | Dedicated Live surface |

**2. Recommendation carousels.** Horizontally scrollable content rows, each with a "View All" link that navigates to the relevant dedicated vertical:

| Carousel | View All destination |
|---|---|
| **Recommended Cards** | Cards vertical |
| **Recommended Packs** | Packs vertical |
| **Latest Topps Release** | Drops vertical |
| **Live Now** | Live vertical |

Carousels surface personalized and editorial content across all verticals. The collector can browse casually from Shop Home or drill into a vertical for focused shopping.

#### Dedicated vertical surfaces

Each vertical is a full browsing context accessed from Shop Home (via entry grid, "View All" link, or back navigation). The four verticals:

| Vertical | What it contains |
|---|---|
| **Cards** | Individual card marketplace listings — Buy Now, Weekly Auction, Premier Auction |
| **Packs** | Sealed product, hobby boxes, retail packs |
| **Drops** | Time-limited releases, digital pack drops, exclusive releases |
| **Live** | Live streaming commerce — active streams, scheduled events |

Navigating into a vertical updates the header title (e.g., "Cards") and shows a back arrow that returns to Shop Home.

#### Category tabs (within each vertical)

Each vertical opens with a horizontally scrollable row of icon+label category tabs, styled after the Fanatics Live pattern. Each tab has a sport icon in a rounded square with the label below, and an underline on the active tab:

| Tab | Purpose |
|---|---|
| **For You** | Personalized recommendations within this vertical (default active) |
| **Basketball** | Sport category filter |
| **Football** | Sport category filter |
| **Baseball** | Sport category filter |
| **Soccer** | Sport category filter |
| **Hockey** | Sport category filter |
| **UFC** | Sport category filter |

Tapping a category tab filters the listing feed to that sport. "For You" shows a personalized cross-sport feed within the vertical.

#### Pill filters (below category tabs)

Below the category tabs, a horizontally scrollable row of pill filters provides additional scoping:

| Filter | Behavior |
|---|---|
| **Filter** (icon button) | Opens a full-screen advanced filter panel |
| **Watchlist** | Toggle pill — when active, scopes the view to items the collector has saved or is bidding on within this vertical. Absorbs the previous "Saved" concept and surfaces bid activity (Watching, Bidding, Won, Lost) |
| **Format** | Dropdown pill — select purchase format: Buy Now, Weekly Auction, Premier Auction, or All Formats |
| **Grade** | Dropdown pill — select grade: PSA 10, PSA 9, BGS 9.5, SGC 10, Raw, or All Grades |
| **Price** | Dropdown pill — select price range: Under $25, $25–$100, $100–$500, $500+, or Any Price |

Category tabs and pill filters are consistent across all four verticals (Cards, Packs, Drops, Live).

**Guardrails:**

- Shop Home orchestrates discovery across verticals. It uses carousels to surface content, not to replace the dedicated surfaces.
- Shop is where commerce happens. It should not feel like account machinery.
- Discovery memory (Watchlist) lives within each vertical as an inline filter, not as a separate mode or pillar.

---

### 4.3 Search — Utility, Hubs & Canonical Records

**Purpose:** Find anything across the ecosystem — whether it is currently for sale or simply exists in the collecting world.

Search surfaces a blended set of result types:

| Result type | What it includes |
|---|---|
| **Marketplace listings** | Active Buy Now and Auction items |
| **Entity hubs** | Players, teams, sets, IP — rich context pages |
| **Catalogue records** | Canonical card pages, even when no active listings exist |

Search prioritizes actionable listings when relevant, but must also support complete collecting context by surfacing canonical records for ownership tracking and want-list creation.

**Search is distinct from Shop:**

- **Shop** = organic discovery, merchandising, vertical browsing
- **Search** = intent-driven finding and canonical exploration

**Guardrail:** Search exists to find. It is not a browse surface and should not duplicate Shop's merchandising role.

---

### 4.4 Collection — Ownership Space

**Purpose:** Organize, display, and manage what I own.

Collection should feel like how collectors behave in real life — binders, displays, curated sets, piles on a desk. It is portfolio-first, not a workflow log.

| Surface | Purpose |
|---|---|
| **All Items** | Complete ownership inventory |
| **Stacks** | Multi-membership groupings — private by default, optionally public. Tag-powered organization that avoids deep folder hierarchies |
| **Quests** | Finite, task-driven initiatives that encourage collecting behavior or feature adoption |
| **Programs** | Ongoing or season-based systems (Performance Cards, Red Rookie) that may generate rewards. Currency balances remain in Wallet |
| **Want List** | Public intent signal — initially implemented as a system-supported Stack. Opt-in public visibility. Want List is identity and community signal, not private shopping memory |
| **OIP** | Owned Item Page — canonical place for item state, context, and history |

Collection integrates directly with the product catalogue. Collectors can add canonical cards to their collection even when no marketplace listing exists, enabling complete portfolio tracking and want-list creation independent of active supply.

**Guardrails:**

- Collection must not contain submission logs, grading job history, service fee ledgers, or operational timelines. Those live in Account → Vault Activity.
- Collection must scale 5–10x. Design for large collections, power users (especially on Web), bulk management, filtering, and dynamic views.
- Items can belong to multiple Stacks. Avoid deep folder-tree hierarchies as a scaling solution.

---

### 4.5 Account — Operations & Identity

**Purpose:** System machinery, ledgers, settings, and servicing.

Account becomes clean when it focuses exclusively on:

| Section | Purpose |
|---|---|
| **Orders** | Commerce ledger — completed or in-progress transactions. If ownership is not transferring through a purchase, it does not belong here |
| **Selling** | Active and past listing management — a surface with separate intent from buying |
| **Vault Activity** | Ownership operations log — custody, grading workflows, redemption tracking |
| **Wallet** | Balances, payouts, stored value, FanCash |
| **Preferences** | Notification settings, privacy, display preferences |
| **Help** | Support, FAQs, contact |
| **Fanatics One Identity** | Profile, linked accounts, cross-platform identity |

**What migrated out of Account:**

| Item | Previous location | New location | Rationale |
|---|---|---|---|
| **Bids** | Account (primary section) | Shop → Watchlist (inline filter) | Bids are active commerce engagement, not account machinery. They belong near discovery |
| **Offers** | Account (primary section) | Inbox → Offers (negotiation threads) | Offers are conversational and relationship-driven. They belong in the communication hub |

**Guardrails:**

- Account must not become a discovery surface, a social feed, or a saved-items destination.
- Orders record commercial transactions only. Vault operations, messaging, saved items, and redemption tracking do not belong in Orders.

---

## 5. Global utility layers

Two cross-cutting experiences that are always accessible and should not be forced into a pillar.

### 5.1 Inbox — Unified Communication Hub

**Purpose:** One place for everything that needs the collector's attention — messages, offers, and system alerts.

Inbox is accessible from a global header icon. It presents a unified chronological feed with filter chips at the top:

| Filter | What it shows |
|---|---|
| **All** | Interleaved feed of all item types, ordered by recency |
| **Messages** | User-to-user conversations, collector relationships |
| **Offers** | Negotiation threads — buy/sell offers, counter-offers, future trades. Each offer is a conversation, not a ledger entry |
| **Alerts** | System-to-user events — payment due, grading complete, vault status change, shipping updates |

**Behavioral rules:**

- **Messages** clear when read (standard unread indicator).
- **Alerts** clear when resolved, not when read. An alert for "payment due" persists until the payment is made, even if the collector has seen it.
- **Offers** show negotiation state (active, awaiting response, accepted, declined) and surface the latest message in the thread.
- Tapping a message or offer thread enters focused mode (navigation suppressed).

**What converged into Inbox:**

| Previous surface | Now lives in |
|---|---|
| Notifications (standalone bell icon) | Inbox → Alerts filter |
| Messaging (standalone chat icon) | Inbox → Messages filter |
| Offers (Account section) | Inbox → Offers filter |

**Guardrails:**

- Inbox must not contain marketing or low-signal content. If an event does not require action or represent a meaningful state change, it does not enter Inbox.
- Message events must not be duplicated in Alerts. Each item type has its own unread/attention signal.
- As community grows, Inbox remains globally accessible. It does not retreat into Account.

---

### 5.2 Cart — Commerce Utility

**Purpose:** Persistent, cross-device commerce container.

- Remembers items across sessions and devices
- If items are no longer available, Cart reconciles with clear messaging
- Visible in commerce-intent surfaces (Home, Shop, Search)
- From non-commerce surfaces (Collection, Account), "Add to cart" uses a toast with "View cart" action
- "View cart" opens a consistent overlay/modal experience

**Guardrail:** Cart is transactional. It must not become a sixth pillar or disappear based on session state.

---

## 6. Migration map

This section documents every structural change from the current product to the proposed model.

### 6.1 Bids: Account → Shop Watchlist

| Aspect | Before | After |
|---|---|---|
| **Location** | Account → Bids (primary section) | Shop → any vertical → Watchlist (inline filter toggle) |
| **Mental model** | "Go to Account to check my bids" | "Toggle Watchlist in Cards to see what I'm bidding on" |
| **States surfaced** | Bid list | Watching, Bidding, Won, Lost as states within Watchlist |
| **Home integration** | Limited | Home can surface closing-soon moments and deep-link into the relevant vertical's Watchlist view |

**Why:** Bids are active commerce engagement, not account settings. They belong near the discovery context where the collector encountered the item.

---

### 6.2 Offers: Account → Inbox

| Aspect | Before | After |
|---|---|---|
| **Location** | Account → Offers (primary section) | Inbox → Offers filter (negotiation threads) |
| **Mental model** | "Go to Account to manage my offers" | "Check Inbox to see and respond to offers" |
| **Interaction** | Offer as ledger entry with accept/decline buttons | Offer as conversation thread — message, counter, negotiate |
| **Outcome** | Accepted offers create order entries | Accepted offers still create entries in Account → Orders |

**Why:** Offers are relationship-driven negotiation. They are conversations with another collector that happen to have commerce attached. The outcome (a completed transaction) lives in Account → Orders; the activity itself lives where relationships live.

---

### 6.3 Notifications + Messaging → Unified Inbox

| Aspect | Before | After |
|---|---|---|
| **Entry points** | Two header icons (bell + chat) | One header icon (Inbox) |
| **System alerts** | Standalone Notifications surface | Inbox → Alerts filter |
| **User messages** | Standalone Messaging surface | Inbox → Messages filter |
| **Offers** | Account section | Inbox → Offers filter |
| **Attention model** | Check three places | Check one place, filter as needed |

**Why:** Collectors should have a single answer to "what needs my attention?" The unified Inbox reduces cognitive overhead while preserving the behavioral distinction between message types through filtering and different clearing behaviors.

---

### 6.4 Shop: Discover/Saved toggle → Shop Home + Dedicated Verticals

| Aspect | Before | After |
|---|---|---|
| **Landing experience** | Discover mode with vertical pills | Shop Home with entry grid + recommendation carousels |
| **Content verticals** | Secondary pills within Discover | Dedicated surfaces accessed from Shop Home |
| **Cross-vertical browsing** | Single flat feed | Carousels on Shop Home (Recommended Cards, Recommended Packs, Latest Release, Live Now) with "View All" links |
| **Vertical deep-dive** | Same screen with filter change | Dedicated surface with back-to-Shop navigation, full filter bar |
| **Saved items** | Separate Saved mode with categories (Listings, Events, People, Searches) | Watchlist toggle within each vertical's filter bar |
| **Browse filters** | Category pills below mode content | Inline horizontal scrollable bar: Filter, Watchlist, Format dropdown, then category pills |

**Why:** Shop Home gives collectors a curated, cross-vertical landing that surfaces personalized recommendations across all content types. "View All" bridges to dedicated vertical surfaces where focused browsing with filters happens. This replaces both the Discover/Saved mode toggle and the flat vertical pills — casual browsing happens on Shop Home, intentional browsing happens in verticals.

---

## 7. Focused modes

Focused modes suppress bottom navigation and take over the collector's attention. They are reserved for immersive, attention-capturing experiences — not for every deep screen.

| Focused mode | Entry trigger |
|---|---|
| **Inbox thread view** | Tapping a message, offer, or alert thread in Inbox |
| **Checkout (traditional)** | Full-screen checkout flow from Cart |
| **Checkout (experiential)** | Sheet/modal checkout that transitions into immersive experience (e.g., instant rip) |
| **Live stream** | Entering a live broadcast |
| **Scanner capture** | Camera-based card scanning flow |
| **Instant rip / break replay** | Pack opening animation, break replay |
| **Auction finale (future)** | End-of-auction immersive bidding experience |

**Exit behavior:**

- **Launched from within the app:** Close returns to origin (preserves tab and scroll state)
- **Launched from deep link / external entry:** Close returns to Home
- **Explicit CTA exists** (e.g., "View in Collection"): CTA defines destination and overrides origin

**Guardrail:** New immersive experiences must enter focused mode. They must not require new primary navigation pillars.

---

## 8. Surface behavior rules

To keep navigation predictable, every surface in the product falls into one of three categories.

### 8.1 Browsing surfaces (navigation remains visible)

Primary tabs and standard detail pages: Home, Shop, Search, Collection, Account, OIP, listing detail, player hubs, Watchlist views.

Rule: depth alone does not justify suppressing navigation.

### 8.2 Utility overlays (lightweight)

Cart and Inbox are accessible without re-rooting navigation. They open as overlays, modals, or sheets that sit on top of the current context.

### 8.3 Focused mode surfaces (navigation suppressed)

See Section 7. These are the only surfaces where the tab bar is hidden.

---

## 9. Guardrails

These guardrails exist to prevent drift, duplication, and accidental scope creep as the platform evolves. They are condensed from the original Structural Model and updated to reflect the evolved architecture.

### Pillar integrity

- **Orders = commerce ledger only.** If ownership is not transferring through a purchase, it does not belong in Orders.
- **Collection is not a workflow log.** Collection shows ownership, organization, display, and portfolio context. It may show item state badges (listed, grading, redemption pending), but submission logs, grading job histories, and service fee ledgers live in Account → Vault Activity.
- **Account is machinery.** It must not become a discovery surface, a social feed, or a saved-items destination.

### Communication integrity

- **Inbox is the single communication surface.** Messages, Offers, and Alerts are filters within Inbox, not separate destinations.
- **No duplication across filters.** A message event must not appear in both Messages and Alerts. Each item belongs to exactly one filter.
- **Inbox eligibility rule.** If an event does not require action or represent a meaningful state change, it must not appear in Inbox.

### Discovery integrity

- **Watchlist is discovery memory.** It lives within Shop as an inline filter. It is not part of Account or Collection.
- **Want List is ownership-side.** It lives in Collection as a Stack. It is public (opt-in). It is not the same as Watchlist. Watchlist ≠ Want List.
- **Shop Home orchestrates, verticals go deep.** Shop Home surfaces recommendations and entry points across all content types. Dedicated verticals are focused browsing surfaces. Shop Home must not absorb full vertical functionality, and verticals must not lose their dedicated contexts.

### Scaling integrity

- **Stacks are multi-membership.** Items can belong to multiple Stacks. Avoid deep folder-tree hierarchies.
- **Collection must scale 5–10x.** Design for large collections, power users on Web, bulk management, filtering, and dynamic views.

### Evolution integrity

- **Inbox must not retreat into Account** as community grows.
- **Home orchestrates, it does not replace.** Home may summarize, highlight, and deep-link, but it must not absorb core functionality from other pillars.
- **Mode-based experiences are additive.** New immersive experiences enter focused mode. They do not require new navigation pillars.

---

## 10. Open questions for collector validation

These questions are framed as testable hypotheses suitable for evaluation against collector research, behavioral data, or LLM-assisted insight analysis.

### Unified Inbox

1. **Hypothesis:** Collectors prefer a single communication hub with filters over separate Notifications and Messaging surfaces.
   - **Test:** Does reducing entry points from three to one increase the rate at which collectors discover and act on system alerts, messages, and offers?
   - **Risk:** Power users who treat messaging as a relationship space may not want system alerts in the same feed. Does filtering adequately address this?

2. **Hypothesis:** Offers are better understood as conversations than as ledger entries.
   - **Test:** Does moving offers into a messaging-style thread increase offer response rates and negotiation engagement?
   - **Risk:** Some collectors may expect offers to live closer to the listing or the item, not in a communication surface.

### Shop Home + Dedicated Verticals

3. **Hypothesis:** A curated Shop Home with recommendation carousels and entry points is a better default landing than immediately dropping collectors into a single vertical.
   - **Test:** Does Shop Home increase cross-vertical engagement (e.g., a Cards buyer also browsing Packs or Drops) compared to the old Discover mode?
   - **Risk:** Adding a landing page creates one more tap to reach listings. Power users who always go to Cards may want to skip Shop Home. Consider a "recently visited" shortcut or configurable default.

4. **Hypothesis:** "View All" links on carousels are an effective bridge from casual browsing (Shop Home) to intentional browsing (dedicated vertical).
   - **Test:** What percentage of carousel interactions result in "View All" taps vs. individual item taps? Does carousel → View All → purchase conversion exceed direct vertical entry?
   - **Risk:** If carousels feel too generic or are poorly personalized, collectors may bypass Shop Home entirely.

5. **Hypothesis:** An inline Watchlist toggle within each vertical is a sufficient replacement for a dedicated Saved section.
   - **Test:** Do collectors who previously used Saved find their watched items and bid activity equally discoverable through the inline filter?
   - **Risk:** Watchlist scoped to one vertical at a time may frustrate collectors who want a cross-vertical "everything I'm watching" view.

### Account simplification

6. **Hypothesis:** Removing Bids and Offers from Account reduces cognitive load without creating disorientation.
   - **Test:** Do collectors who currently use Account → Bids successfully find their bids through Shop → Watchlist within the first session after migration?
   - **Risk:** Habitual navigation patterns take time to unlearn. Transition requires clear wayfinding and possible redirect bridges.

### Communication behavior

7. **Hypothesis:** The behavioral distinction "messages clear when read, alerts clear when resolved" is intuitive within a unified feed.
   - **Test:** Do collectors understand why an alert persists after being viewed, or does it create confusion about "why won't this go away?"
   - **Risk:** Mixed clearing behaviors in a single feed may feel inconsistent if not clearly communicated through visual treatment.
