# Fanatics Live → Collect Unification

## The Problem

We currently maintain and market two apps — Fanatics Collect and Fanatics Live — to the same collector audience. This doubles our acquisition cost, fragments the collector experience, and dilutes our brand. Both apps already share the same codebase, binary, and account system. There is no reason for two front doors.

## The Goal

Deprecate Fanatics Live as a standalone app. Make Fanatics Collect the single destination for everything — marketplace, live breaking, and collecting tools. One app, one install, one place to be a collector.

## Why This Matters

**For collectors:** No more juggling two apps for one hobby. Live breaks, purchases, and collection management all live together. The experience becomes coherent — a break leads to a card, a card lives in your collection, your collection drives your next break.

**For the business:** Cut duplicate marketing spend. Consolidate install-base metrics. Simplify feature development. Every dollar and every sprint goes further when you're building one product, not maintaining two storefronts.

## Timeline

| **Phase** | **When** | **Objective** |
| --- | --- | --- |
| **Phase 1: Parity & Polish** | Now → End of Q1 | Absolute feature parity between both apps — every feature available on Live must work equally well on Collect, and vice versa |
| **Phase 2: Redirect** | Q2 (GTM likely April start) | Stop all acquisition and marketing to Fanatics Live. Drive 100% to Fanatics Collect |
| **Phase 3: Migrate & Deprecate** | Q3 | Migrate remaining Live-only users. Submit app deprecation to app stores |

---

# Phase 1: Parity & Polish — Status Report

**Last updated:** March 5, 2026
**Linear project:** [Live and Collect App Parity](https://linear.app/fanaticscollect/project/live-and-collect-app-parity-5c267479933d/issues)
**Project lead:** Sameer Siddiqui
**Priority:** High

---

## Status Summary

| Metric | Value |
| --- | --- |
| Issues complete | 33 / 69 (48%) |
| Project target | March 6, 2026 |
| Status | **At risk** — 27 issues still in Todo, 4 milestones at 0% |
| Teams | Client Android (CAND), Client iOS (CIOS), Client App (CLI) |

Android is largely through its build phase (27/34 done). iOS has significant remaining work (20/30 in Todo), driven partly by 17 unresolved Design QA findings. Cross-platform (CLI) work has not started (0/5).

---

## Milestone Progress

| Milestone | Progress | Target Date | Status |
| --- | --- | --- | --- |
| Technical Design + Platform Plan | 0% | Jan 7 | Complete (planning milestone) |
| Purchase End to End | 82% | — | On track |
| Live Account UI Changes | 25% | — | In progress |
| Selling Flow | 0% | — | Not started |
| Deeplinking | 4% | Feb 27 | **OVERDUE** |
| Dogfooding start | 0% | Feb 27 | **OVERDUE** |
| Lifecycle / Comms / GTM | 0% | Mar 6 | **Due tomorrow — not started** |
| Launch + Post launch dashboards | 0% | Mar 6 | **Due tomorrow — not started** |

**Purchase End to End** is the furthest along — most of the Android marketplace integration is done and iOS buying flows are functional. **Selling Flow** and **Deeplinking** are the biggest gaps. Two milestones due tomorrow (Lifecycle/GTM and Launch dashboards) have zero progress.

---

## Issue Summary by Team

| Platform | Done | Ready for QA | In Review | In Progress | Todo | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Android (CAND) | 27 | 2 | 1 | 2 | 2 | 34 |
| iOS (CIOS) | 6 | 1 | 2 | 1 | 20 | 30 |
| Client App (CLI) | 0 | 0 | 0 | 0 | 5 | 5 |
| **Total** | **33** | **3** | **3** | **3** | **27** | **69** |

Android has completed 79% of its issues. iOS has completed 20%, with the majority of remaining work sitting in Todo. Client App (cross-platform items like watchlist, DMs, collection PDP) has not begun.

---

## Parity Areas

| Area | Live → Collect | Collect → Live | Key Issues | Status |
| --- | --- | --- | --- | --- |
| Marketplace (browse, search, PDP, purchase) | — | Marketplace tab + full buying flow on Live | CIOS-34, CIOS-35 (Done); CAND-5 (In Progress) | iOS done, Android in progress |
| Selling flows | — | Seller functionality on Live | CIOS-44 (In Progress); Selling Flow milestone at 0% | iOS in progress, Android not started |
| Account screens (orders, addresses, help, payments) | — | Match Collect version across both apps | CIOS-43 (In Review); CAND-22 (In Review); CIOS-40 (Ready for QA) | In progress on both platforms |
| Offers management | — | Offer management on Live | CIOS-130 (In Review); CAND-43, CAND-44 (Ready for QA) | iOS in review, Android in QA |
| DMs / Messaging | DMs on Collect | Messages on Collect | CIOS-138 (Done); CLI-82 (Todo) | Partially done — messages done, DMs not started |
| Watchlist | Combined watchlist | Combined watchlist | CLI-80 (Todo, High priority) | Not started |
| Collection PDP | — | Collection PDP + folders on Live | CLI-81 (Todo); CIOS-39 (Todo) | Not started |
| Deeplinking | — | Collect links route into Live if Collect not installed | CIOS-48, CIOS-49 (Todo); CAND-29 (In Progress), CAND-30 (Todo) | Android started, iOS not started |
| Shared storage | — | Live search shared across apps | CLI-16 (Todo) | Not started |

---

## Design QA Findings (iOS)

17 design QA issues were filed on February 24 by Sameer. As of March 5, **all 17 remain in Todo — zero resolved in 11 days**.

| Issue | Summary | Assignee |
| --- | --- | --- |
| CIOS-108 | Cart sheet not displayed when adding item from Marketplace tab | Ana Espuigperello |
| CIOS-109 | Header area on scroll uses wrong background colour | Ana Espuigperello |
| CIOS-110 | Heart icon in rest status not rendered correctly in tiles | Ana Espuigperello |
| CIOS-111 | 'For you' sort option not displayed | Ana Espuigperello |
| CIOS-112 | Inconsistent tile loading animation when filtering | Ana Espuigperello |
| CIOS-113 | Bid status badge missing on LDP | Ana Espuigperello |
| CIOS-114 | Sell sheet icons using wrong colour | Ana Espuigperello |
| CIOS-115 | Multiple filter panel display issues | Ana Espuigperello |
| CIOS-116 | Sell flow: radio buttons and allow offers minimum price issues | Ana Espuigperello |
| CIOS-117 | Heart icon not rendered on save item | Ana Espuigperello |
| CIOS-118 | Watch item heart icon not displayed or using wrong colour | Ana Espuigperello |
| CIOS-119 | Cart sheet checkout button floating in the middle | Ana Espuigperello |
| CIOS-120 | Sell on buy now: toggle appears stretched out | Ana Espuigperello |
| CIOS-121 | Cart sheet button dock not anchored to bottom on scroll | Ana Espuigperello |
| CIOS-122 | Product tile image background should use layer-2 | Ana Espuigperello |
| CIOS-123 | Select items: wrong tile outline and missing background colour | Ana Espuigperello |
| CIOS-124 | Cart qty selector buttons collapse on update — need spinner | Ana Espuigperello |

**Parent task:** CLI-23 "Design QA - iOS" — assigned to Will Rose, still in Todo.

These findings cover tiles, filters, cart behaviour, sell flow components, icon rendering, and colour tokens. Most are visual polish issues referencing the design system (DS1), but some are functional (cart not displaying, filter panel empty, bid status missing).

---

## Recent Activity (Since March 3)

| Date | Issue | Change |
| --- | --- | --- |
| Mar 4 | CIOS-138 "Bring messages to Collect" | Created and completed (Done) |
| Mar 4 | CIOS-137 "Bring Marketplace Orders to Live" | Created and completed (Done) |
| Mar 4 | CIOS-130 "Bring offer management over to Live" | Moved to In Review |
| Mar 4 | CIOS-44 "Bring seller functionality" | Updated (still In Progress) |
| Mar 4 | CAND-5 "Marketplace Feature preparation" | Updated (still In Progress) |
| Mar 4 | CAND-29 "Modify assetLinks.json" | Updated (still In Progress) |

Two new issues created and immediately closed — messages on Collect and marketplace orders on Live. Offer management for iOS moved into review. No movement on design QA findings.

---

## Key Concerns

1. **March 6 target is not achievable.** 27 issues remain in Todo. Four milestones are at 0%. The target date needs to be reassessed — this is a conversation for Sameer and stakeholders.

2. **Design QA is stuck.** 17 findings filed 11 days ago with zero movement. All assigned to Ana. CLI-23 (the parent task assigned to Will) is also untouched. This blocks the "polish" half of "Parity & Polish."

3. **Deeplinking and Dogfooding are overdue.** Both milestones had a Feb 27 target. Deeplinking is at 4% (one Android ticket done, rest in Todo/In Progress). Dogfooding has not started.

4. **iOS is significantly behind Android.** Android has 2 issues left in Todo. iOS has 20. The gap is partly explained by iOS foundation work predating the Linear project, but the design QA backlog and selling flow work represent real remaining effort.

5. **Cross-platform work (CLI) hasn't started.** Watchlist, DMs on Collect, Collection PDP, shared storage, and design QA — all 5 CLI tickets are in Todo with no assignee on most.

6. **Lifecycle/GTM and Launch dashboards are due tomorrow at 0%.** These milestones have no issues assigned and no progress. If Phase 2 redirect is targeting April, GTM planning needs to be underway now.

---

## Immediate Actions

| Action | Owner | Status |
| --- | --- | --- |
| Reassess March 6 target date — set a realistic Phase 1 completion date | Sameer Siddiqui | Needed |
| Unblock Design QA findings — confirm plan to resolve 17 iOS issues | Sameer / Ana / Will | Needed |
| Activate CLI tickets — assign owners for CLI-80 (watchlist), CLI-81 (collection PDP), CLI-82 (DMs) | Sameer Siddiqui | Needed |
| Confirm deeplinking plan — CIOS-48/49 and CAND-29/30 need a path to completion | Sameer Siddiqui | Needed |
| Start Lifecycle/GTM planning — milestone at 0% with Phase 2 targeting April | Sameer / GTM lead | Needed |
| Confirm dogfooding timeline — who is testing, on what builds, with what test plan | Sameer Siddiqui | Needed |
