# Digital Packs PRD Review — Morning Check In

**Meeting:** `Morning Check In
**Date:** March 3, 2026
**Participants:** Jonny Ballard, Sam Sampson, Will Rose, Anthony De Sousa, Ana Espuigperello, Michael Dingle

---

## Context

Michael walked the team through the Digital Packs PRD he had drafted, covering the end-to-end ecommerce experience for async instant rips on Collect. The discussion below captures the Digital Packs portion of the meeting only.

---

## Key discussion points

### Scope confirmation

- **Pack opening experience, gamification, and engagement loops are out of scope.** This PRD covers discovery, merchandising, purchase, and the handoff to the rip animation only. The rip animation itself is already built (WebGL-powered) and doesn't need redesigning.
- **Multipack purchase is out of scope for MVP.** Stacking multiple packs requires shared design work with the WebGL experience team. Michael has an idea for how to handle the transition but it's a fast-follow.
- The experience hasn't fundamentally changed from what was originally planned — it's a matter of aligning the best-looking version and filling gaps (especially web).

### Payment methods

- Supported: **credit card** and **account funds (FanCash)**.
- Will flagged that deferred payment methods (e.g., wire) are not supported. Michael agreed this should be captured in the PRD.

### Categories and tiers

- **All categories at launch** — Baseball, Football, Basketball, Pokemon, Mixed Sports.
- Michael mentioned a potential **permanent "pop pack" category** covering Disney, Marvel, Star Wars. The framework supports this without structural changes.
- Core tiers (Super, Mega, Ultra, Infinity) apply across categories.
- Short-run / limited packs (Signature Series, event-based) will also be supported.

### Pack imagery should be dynamic

- Michael was clear: **pack imagery must be dynamic**, never showing a card that isn't available. The tile and PDP should pull "the latest grail available."
- This contradicts the PRD's current configuration table which says "Static per pack (no change)." Needs updating.

### Sold-out vs. out-of-stock messaging

- For **short-run / limited packs** that sell out: "Sold Out" (final).
- For **always-on tier packs** that temporarily run out of inventory: different messaging — "Out of Stock," "Restocking," or "Coming back soon" (wording TBD).
- **"Notify me" for sold-out packs:** Will suggested it. Michael pushed back — over-notification is a concern. Both agreed it's not for V1.

### No per-user purchase limit

- Will asked if there's a limit per person per day. Michael confirmed: **no limit** — a collector could buy as many as they want.

### Debut packs as a future onboarding mechanism

- Will raised the idea that **debut packs** (free packs for new users) could use the async rip experience. No money involved makes it the easiest way to teach people how ripping works.
- Michael agreed it's a good idea but **not in scope for this work**. Could be a future consideration for first-time tutorial flow.

### Web experience

- Digital Packs must work on web from launch.
- **Chad has started designing web checkout patterns for live** — Will suggested catching up with Chad to align the Digital Packs web experience, since both should feel similar.
- The PRD's current gap note ("No desktop or responsive web designs exist") should be softened to reflect this progress.

### Merchandising

- Michael walked through merchandising requirements: hero/featured zone, category ordering, editorial copy, scheduling, no-code updates.
- The system that powers merchandising is still TBD (Contentstack vs. Retool extension vs. other). This is a PM + Eng decision.

### Pack grouping

- Pack grouping is manually configured in Retool, not derived from card metadata. This prevents mismatches (e.g., a baseball card in a football pack incorrectly setting the category).

### OIP and replay

- Will asked about replay after opening. Michael confirmed **replays will exist** — the WebGL experience is replayable from Collection. The team is working on making replays better.
- Ideally, replay will support full orbit control (zoom, rotate) — built for Instant Wax but not yet in replay. Not in scope here.
- OIP (owned item page) will use standard vault imagery, not instant rips imagery. May note the origin as "Digital Pack."

### Timeline and design dependencies

- **Target launch: May 15, 2026.**
- Designs needed by ~mid-March for engineering to scope.
- Will flagged that next week will likely be heavily focused on FanCash Card work, so Digital Packs design may need to push to the following week. Michael is open to pushing back on the timeline if needed.
- **Existing design work is scattered.** Michael committed to bringing all prior design files together into one place (Q1 2026 folder).

### Approach

- Will suggested: bring together everything that exists, assemble the flow (even with missing screens), and then identify gaps. Michael agreed.
- Michael noted he wrote this PRD "in lieu of anyone actually gathering requirements" — positioned it as getting the product team aligned.

---

## Action items

- **Michael:** Make small PRD updates based on this discussion (payment methods, dynamic imagery, sold-out nuance, etc.)
- **Michael:** Consolidate all existing Digital Packs design work into one place
- **Will + Michael:** Catch up after this meeting to start on Digital Packs design work
- **Will:** Connect with Chad on web checkout patterns for alignment
- **Will + Ana:** Manage FanCash Card design load next week; Digital Packs design may shift to the following week
