# Valuation & Pricing Questions

| Field | Value |
|-------|-------|
| **Category** | Behaviour Clarifications |
| **Subdomain** | Collect / Valuation |
| **Title** | Valuation & Pricing Questions |
| **Version** | 1.0 |
| **Date** | 2025-11-03 |
| **Maintainer** | Product, Fanatics Collect |
| **Status** | Draft |

---

## Overview

This document captures open questions and clarification topics related to **valuation logic, pricing display, and chart representation** within the Collect ecosystem.

It provides context for product, engineering, and data teams as they finalize how estimated item values ("guide prices") are surfaced and interpreted across Collection, Folder, and Marketplace experiences.

---

## Open Topics & Clarifications

### 1. Rounding of Guide Prices

**Question:** Should pricing services return decimal precision, and if so, should Collect round displayed prices to reinforce that they are estimates?

**Considerations:**
- Pricing data from external partners or internal valuation models may include decimal places.
- Rounding (to nearest whole dollar) can emphasize *estimate* rather than *absolute* value.
- Impacts UI consistency across Listing Detail Pages (LDPs), Owned Item Pages (OIPs), and Collection Views.

**Pending Decision:** Adopt a single rounding convention across valuation surfaces (likely to nearest dollar). Document display precision separately for internal reporting.

---

### 2. Terminology: "Guide Price" → "Collect Market Value"

**Background:** The term "Collect Market Value (CMV)" has been proposed to replace "Guide Price (GP)" in user-facing contexts.

**Implications:**
- "Guide Price" is currently embedded in multiple surfaces (valuation UI, portfolio view, and listing flows).
- "Collect Market Value" may offer clearer, brand-consistent language and emphasize proprietary methodology.

**Open Questions:**
- Should the transition be purely naming (GP → CMV) or reflect a refined calculation method?
- How will this affect existing API and data model references?
- What downstream systems rely on "guide_price" as a field name?

**Pending Decision:** Confirm nomenclature with Data Science and Product Marketing. Define migration timeline for schema and UI.

---

### 3. Indexing Status Visibility

**Question:** When valuation data is re-indexing, should the UI indicate this to users?

**Context:**
- Indexing affects aggregated charts (e.g., collection or folder valuation history).
- Re-indexing may be intermittent or background-only.

**Considerations:**
- If re-indexing typically completes within seconds, temporary loading states may suffice.
- If longer, explicit messaging ("Re-indexing in progress") could manage expectations.

**Pending Decision:** Define threshold for display (e.g., >10s triggers a visible indicator). Confirm whether indexing affects individual OIP valuations or only aggregate visuals.

---

### 4. Chart Aggregation (3M / 6M / 1Y / All)

**Question:** For time-based valuation charts, what value should represent each aggregated period (e.g., week)?

**Options:**
1. **Average value across the period** – smooths volatility; better for trend interpretation.
2. **Last known value** – maintains temporal fidelity; aligns with auction data.

**Considerations:**
- Aggregation method affects both trend shape and total perceived portfolio value.
- Consistency needed across time ranges (3M, 6M, 1Y, All) and surfaces (Folder vs. Collection).

**Pending Decision:** Data Science to define preferred aggregation logic. Product to validate UX expectations for consistency across dashboards and charts.

---

### 5. Folder Valuation Behaviour

**Question:** How should folder valuation charts handle item additions or removals over time?

**Options:**
1. **Keep Item Count:** Estimated value changes dynamically as items are added or removed, representing current contents.
2. **Remove Item Count:** Chart reflects only the value of items present at each historical point, without reflecting movement history.

**Considerations:**
- Folders differ from Collections in meaning: Folders are organizational, not transactional.
- Tracking additions/removals adds historical noise but offers realism for portfolio monitoring.
- Simpler models (current items only) may align better with user mental models.

**Pending Decision:** Define whether Folder valuation should behave like Collection valuation (static snapshot) or track item count changes historically.

---

## Summary of Pending Decisions

| Topic | Owner | Status |
|-------|-------|--------|
| Rounding of Guide Prices | Product / Data | Pending convention |
| Terminology (GP → CMV) | Product / Marketing | Pending naming alignment |
| Indexing Visibility | Engineering / Design | Pending UX threshold |
| Chart Aggregation Logic | Data Science | Pending method definition |
| Folder Valuation Model | Product / Design | Pending behavioural decision |
