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

**Last updated:** March 9, 2026
**Linear project:** [Live and Collect App Parity](https://linear.app/fanaticscollect/project/live-and-collect-app-parity-5c267479933d/issues)
**Project lead:** Sameer Siddiqui
**Priority:** High

---

## Status Summary

| Metric | Value |
| --- | --- |
| Issues effectively resolved | 55 / 67 active (82%) |
| Breakdown | 52 Done, 2 Duplicate, 1 Release Ready |
| Project target | March 6, 2026 (passed) |
| Status | **Past target date** — strong momentum continues but target has slipped. 6 issues in Todo. |
| Teams | Client Android (CAND), Client iOS (CIOS), Client App (CLI) |

Progress since last report (March 5 EOD): CIOS-130 (offer management) completed by Arnaud. CIOS-40 (payment methods) completed by George. CLI-81 (Collection PDP) moved to Ready for QA. CIOS-119 moved to Release Ready. One regression: CIOS-124 (cart qty selector) was reopened from Done back to In Progress. Live Account UI Changes milestone jumped from 50% to 75%.

---

## Milestone Progress

| Milestone | Progress | Target Date | Status |
| --- | --- | --- | --- |
| Technical Design + Platform Plan | 0% | Jan 7 | Complete (planning milestone) |
| Purchase End to End | 84% | — | On track |
| Live Account UI Changes | 75% | — | **Up from 50% — major jump** |
| Selling Flow | 0% | — | Not started |
| Deeplinking | 4% | Mar 6 | **Overdue — target passed** |
| Dogfooding start | 0% | Mar 9 | **Due today** |
| Lifecycle / Comms / GTM | 0% | — | Target date removed |
| Launch + Post launch dashboards | 0% | — | Target date removed |

Live Account UI Changes is the story — 50% to 75% driven by CIOS-130 (offer management) completing. Deeplinking target has now passed with only 4% progress. Dogfooding is due today (Mar 9) but at 0%.

---

## Issue Summary by Team

| Platform | Done | Duplicate | Release Ready | Ready for QA | In Progress | Todo | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Android (CAND) | 28 | 0 | 0 | 2 | 2 | 2 | 34 |
| iOS (CIOS) | 22 | 2 | 1 | 1 | 2 | 2 | 30 |
| Client App (CLI) | 2 | 0 | 0 | 1 | 0 | 2 | 5 |
| **Total** | **52** | **2** | **1** | **4** | **4** | **6** | **69** |

Android unchanged at 82% done. iOS at 73% done with offer management now complete and payment methods done. CLI progressing — Collection PDP now in QA.

---

## Parity Areas

| Area | Key Issues | Status |
| --- | --- | --- |
| Marketplace (browse, search, PDP, purchase) | CIOS-34, CIOS-35 (Done); CAND-5 (In Progress) | iOS done, Android in progress |
| Selling flows | CIOS-44 (In Progress); Selling Flow milestone at 0% | iOS in progress, Android not started |
| Account screens (orders, addresses, help, payments) | CAND-22 (Done); CIOS-40 (Done); CIOS-43 (Duplicate) | **Complete across both platforms** |
| Offers management | CIOS-130 (Done); CAND-43, CAND-44 (Ready for QA) | **iOS complete, Android in QA** |
| DMs / Messaging | CIOS-138 (Done); CLI-82 (Done) | **Complete** |
| Watchlist | CLI-80 (Todo, High priority) | Not started |
| Collection PDP + Collections | CLI-81 (Ready for QA, George) | **In QA — up from Todo** |
| Deeplinking | CIOS-48, CIOS-49 (Todo); CAND-29 (In Progress), CAND-30 (Todo) | Android started, iOS not started. Target passed. |
| Shared storage | CLI-16 (Todo) | Not started |

---

## Design QA Findings (iOS) — RESOLVED

All 17 design QA issues are resolved. One item (CIOS-124, cart qty selector) was reopened and is back In Progress. CIOS-119 (cart sheet checkout button) has moved to Release Ready.

| Status | Count |
| --- | --- |
| Done | 15 / 17 |
| Release Ready | 1 (CIOS-119) |
| Reopened / In Progress | 1 (CIOS-124) |

---

## Recent Activity (Since March 5 EOD)

| Date | Issue | Change |
| --- | --- | --- |
| Mar 9 | CIOS-130 (Offer management on Live) | **Done** — Arnaud Dorgans completed |
| Mar 7 | CIOS-119 (Cart sheet checkout button) | Moved to **Release Ready** |
| Mar 6 | CIOS-40 (Payment methods) | **Done** — George Tsifrikas completed |
| Mar 6 | CLI-81 (Collection PDP and Collections) | Moved to **Ready for QA** — George Tsifrikas |
| Mar 6 | CIOS-124 (Cart qty selector) | **Reopened** — moved from Done back to In Progress |
| — | Live Account UI Changes milestone | **50% → 75%** |

---

## Key Concerns

1. **Project target date has passed.** March 6 was the target. We're now 3 days past with 12 active issues remaining (4 Ready for QA, 4 In Progress, 6 Todo). Good momentum but the team needs a revised target.

2. **Deeplinking is overdue.** Target was March 6. Only CAND-29 is In Progress. Three tickets remain in Todo (CIOS-48, CIOS-49, CAND-30). This milestone will not hit its original target.

3. **Dogfooding is due today (Mar 9) at 0%.** No progress on dogfooding milestone. Design QA is largely clear so the blocker is gone, but the milestone hasn't formally started.

4. **CIOS-124 was reopened.** Cart qty selector buttons collapse issue was marked Done on March 5 but reopened to In Progress on March 6. Worth understanding what drove the regression.

5. **Selling Flow still at 0%.** CIOS-44 (seller functionality) remains In Progress with no completions.

6. **CLI-80 (watchlist) and CLI-16 (shared storage) still unassigned and in Todo.**

---

## Immediate Actions

| Action | Owner | Status |
| --- | --- | --- |
| Set revised project target date — Mar 6 has passed | Sameer Siddiqui | Needed |
| Confirm deeplinking plan — overdue, 3 tickets in Todo | Sameer Siddiqui | Needed |
| Start dogfooding — target is today (Mar 9) | Sameer Siddiqui | Needed |
| Investigate CIOS-124 regression — reopened from Done | George Tsifrikas | In progress |
| Complete seller functionality — CIOS-44 | Arnaud Dorgans | In progress |
| QA Collection PDP — CLI-81 Ready for QA | George Tsifrikas | In progress |
| Assign CLI-80 (watchlist) and CLI-16 (shared storage) | Sameer Siddiqui | Needed |
| Confirm Lifecycle/GTM timeline | Sameer Siddiqui | Needed |
