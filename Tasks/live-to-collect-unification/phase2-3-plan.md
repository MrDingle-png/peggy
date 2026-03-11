# Live → Collect Unification: Phase 2 & 3 Plan

**Status:** Planning
**Last updated:** March 11, 2026
**Owner:** Michael Dingle
**Audience:** Product leadership, exec alignment

---

## Context

Phase 1 (Parity & Polish) is nearing completion — 82% of issues resolved as of March 9. This document covers the non-technical planning for Phases 2 and 3: the user migration, GTM wind-down, and app deprecation.

Both apps already share the same codebase, binary, and account system. The migration challenge is not technical — it is operational, communicative, and commercial. Done well, this is a seamless upgrade for collectors. Done poorly, it is churn.

---

## Phase 2: Redirect (Q3)

**Objective:** Stop all acquisition to Fanatics Live. Drive 100% of new installs and re-engagement to Fanatics Collect.

### Gate criteria (go/no-go)

Before the redirect begins, the following must be confirmed:

- [ ] Phase 1 feature parity signed off — all critical issues resolved
- [ ] Deeplinking complete — all Live deeplinks resolve correctly in Collect
- [ ] Dogfooding complete — internal team has validated the Collect experience
- [ ] Segmentation analysis complete — at-risk cohorts identified and sized
- [ ] Lifecycle migration flows built and tested
- [ ] Creator and community briefing complete
- [ ] Paid marketing attribution infrastructure migrated

---

### Product Management

**Migration sequencing**
A phased rollout reduces blast radius. Recommended sequence:
1. Internal dogfooding (gate already passed before redirect)
2. Power users and creators — briefed directly, given early access
3. General rollout — full redirect live

**User segmentation**
Four cohorts require distinct handling:
- **Live-only active users** — highest risk, need dedicated migration experience
- **Cross-app users** — lowest risk, already familiar with Collect
- **High-value sellers** — require direct outreach, selling parity must be confirmed before this group migrates
- **Dormant Live users** — lower priority but worth a re-engagement attempt

**Rollback posture**
Define a named decision-maker and a threshold (e.g. DAU drop > X%, support ticket volume > Y) that triggers a pause on the redirect. This should be agreed before go-live, not after.

**Success metrics**
- % of Live-only users who open Collect within 30 days of redirect
- Collect DAU growth from migrated users
- Churn rate among migrated cohort vs. baseline
- Support ticket volume during migration window

---

### Paid Marketing

**Attribution infrastructure**
Live and Collect have separate app store listings and separate MMP tracking. Before stopping acquisition to Live:
- Audit all active campaigns pointing to Live store links — update or retire
- Migrate MMP attribution to Collect for all channels
- Preserve historical Live attribution data for reporting continuity
- Confirm SKAdNetwork / attribution window implications with growth team

**Deep link ecosystem audit**
Every Live deeplink in the wild — paid ads, social posts, influencer content, push notifications, emails — must either be updated to Collect or redirect automatically before the switch is flipped. This is a dependency on the deeplinking work in Phase 1 (currently at 4% — critical path item).

**Live app store listing strategy**
Three options, each with different trade-offs:

| Option | Description | Trade-off |
|--------|-------------|-----------|
| Update listing | Change copy to "now on Fanatics Collect — download here" | Keeps existing installs as a funnel to Collect |
| Leave as-is | No changes until app is submitted for deprecation | Risk of organic installs with broken experience |
| Remove from store | Pull listing before full deprecation | Eliminates confusion but loses funnel value |

Recommended: update listing with a redirect message in Q3, remove in Q4 as part of Phase 3.

**Cost efficiency**
Consolidating acquisition to one app should improve blended CAC. Prepare a before/after model for exec reporting.

---

### Growth & Lifecycle

**Push notification migration**
Live users have opted into Live push tokens. When they migrate to Collect:
- If accounts are linked (confirmed in Phase 1), push token migration may be possible without re-opt-in — confirm with engineering
- If re-opt-in is required, expect opt-in rates lower than Live baseline — model this downside
- Build a dedicated push re-permission flow for migrated Live users

**CRM and email segment merging**
- Audit whether Live and Collect are separate segments in the ESP
- Define merge logic — avoid duplicate sends, suppression gaps, or conflicting journeys
- Update lifecycle triggers that currently reference "Live install" as an event

**Migration moment as onboarding**
The redirect event is a high-churn moment, but also a high-engagement opportunity. Design a dedicated "welcome to your new home" flow for migrated Live users — not a generic Collect onboarding. This flow should:
- Acknowledge that this is their new home for breaking and collecting
- Surface their history (purchases, watchlist, collection)
- Drive the first key action in Collect (browse a live break, check their collection)

**Re-engagement of dormant Live users**
Decide whether to attempt re-engagement before or after the redirect:
- Before: higher intent, gives them context for the change
- After: uses Collect as a fresh start signal

Recommendation: run a pre-redirect re-engagement campaign for users dormant 31–90 days, targeting the 90%+ dormant group with a post-redirect winback.

---

### Product Marketing

**The narrative**
The story to collectors is not "we're shutting down Live." It is: *one home where everything you do as a collector lives together — your breaks, your purchases, your collection.*

Frame this as an upgrade, not a migration. The collector experience gets better. Nothing is lost.

**Community and creator briefing**
The live breaking community follows creators, not the app. A small number of top breakers will shape how the community receives this change. Plan:
1. Identify the 10–20 most influential creators on Fanatics Live
2. Brief them directly, ahead of any public announcement
3. Give them early access to Collect's breaking experience
4. Provide talking points — let them tell the story in their own voice

**Announcement sequencing**
| Audience | Channel | Timing |
|----------|---------|--------|
| Internal team | All-hands / Slack | 2 weeks before public |
| Power users and sellers | Direct email | 1 week before public |
| Creators | 1:1 briefing | 1 week before public |
| General users | In-app + email | At redirect go-live |
| App store listing | Updated copy | At redirect go-live |
| Public / press | No proactive outreach recommended | Reactive only |

**Tone**
Warm, collector-first, forward-looking. Avoid language that implies loss, closure, or inconvenience.

---

## Phase 3: Migrate & Deprecate (Q3/Q4)

**Objective:** Complete migration of remaining Live-only users. Submit app deprecation to app stores.

### Product Management

**Final parity check**
Before deprecation, run a final audit against the parity checklist — particularly selling flows and any edge cases surfaced during Phase 2.

**Deprecation gate criteria**
- [ ] Live-only active user count below agreed threshold (to be defined)
- [ ] Collect DAU has absorbed migrated users without churn spike
- [ ] No critical support issues outstanding from migration
- [ ] Selling flow complete and validated
- [ ] App store submissions prepared and reviewed

**Timeline**
App store deprecation submissions require lead time (Apple typically 1–2 weeks review). Build this into the Q4 plan.

---

### Growth & Lifecycle

**Remaining Live-only users**
By Phase 3, the goal is to move the last cohort of holdouts. Tactics:
- Final push notification to Live users: "Fanatics Live is retiring on [date] — your account is ready in Fanatics Collect"
- Email sequence: 30 days out, 14 days out, 7 days out, final day
- In-app banner in Live: persistent from 30 days before deprecation

**Support readiness**
- Update all CS documentation to reflect Collect as the single app
- Prepare FAQ for common migration questions (where are my purchases? where is my collection? do I need a new account?)
- Brief CS team ahead of Phase 2 redirect — they will see a volume spike

---

### Product Marketing

**End-of-life communications**
Once a deprecation date is set, all Live-facing communications shift to a clear, deadline-driven message. Avoid ambiguity — users need to know the date and what to do.

**App store end state**
Submit the Live app for deprecation once the active user threshold is met. Coordinate the submission with the lifecycle final comms sequence so users are not left with a broken app.

---

## Open Questions and Decisions Needed

| Question | Owner | Priority |
|----------|-------|----------|
| What is the go/no-go threshold for deeplinking completeness? | Sameer Siddiqui | High |
| Can push tokens be migrated without re-opt-in? | Engineering | High |
| Are Live and Collect separate segments in the ESP today? | Lifecycle team | High |
| What GMV threshold defines a "high-value seller" for direct outreach? | Product / Commercial | High |
| What DAU drop % triggers a rollback? | Michael Dingle | High |
| Who are the top 10–20 creators to brief? | Product Marketing | Medium |
| What is the target deprecation date for Q4 submission? | Sameer Siddiqui | Medium |
| Do we want any press coverage of the unification? | Marketing | Medium |

---

## Dependencies on Phase 1

Two Phase 1 items are direct blockers for Phase 2:

| Issue | Current Status | Risk |
|-------|---------------|------|
| Deeplinking (CIOS-48, CIOS-49, CAND-29, CAND-30) | 4% complete | **Critical** — redirect cannot go live without this |
| Selling Flow (CIOS-44) | 0% complete | **High** — sellers must not migrate before selling parity is confirmed |
