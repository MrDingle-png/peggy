# Collections

| Field | Value |
|-------|-------|
| **Category** | Experience Framework |
| **Subdomain** | Collect / Vault |
| **Title** | Collections |
| **Version** | 1.0 |
| **Date** | 2025-11-03 |
| **Maintainer** | Product, Fanatics Collect |
| **Status** | Active |

---

## Overview

The **Collections** framework defines how collectors experience ownership, organization, and value tracking across all Fanatics Collect surfaces.

It represents the digital expression of a collector's personal portfolio — bridging **Vaulted**, **Unvaulted**, and **Live-purchased** items into one unified view.

Historically, **Collect** operated primarily as a marketplace, and **Live** focused on livestream commerce. The *Collections* initiative completes the ecosystem by digitizing the **core collecting experience** itself — turning fragmented ownership data into a coherent, interactive home for collectors.

---

## Purpose

Collections serves as the connective layer that:

1. **Unifies ownership records** from every entry point (Vault submissions, Live purchases, manufacturer integrations, etc.).
2. **Enables organizing and showcasing** a collector's assets through views, filters, and folders.
3. **Connects value, liquidity, and provenance** through real-time valuation and listing integration.
4. **Drives engagement** by making Collect the central destination for hobby activity — not just transactions.

This experience aims to make Collect **the true home of the hobby**: where every item a collector owns — graded, raw, or digital — lives within a single, interactive interface.

---

## Core Concepts

- **OIP (Owned Item Page)** — Each owned collectible in a user's vault or portfolio.
- **Collection Views** — User-configurable layouts showing subsets of OIPs by type, value, or theme.
- **Folders** — Organizational groupings for owned items (e.g., "Top 10 Cards," "Graded PSA 10s").
- **Sort & Filter** — Attribute-driven controls to reorder or isolate OIPs by grading, value, or origin.
- **Search Owned Items** — Fast retrieval of individual collectibles across the user's portfolio.
- **Valuation** — Aggregates real-time market and auction data to surface estimated portfolio worth.
- **Add Unvaulted Cards** — Scanning or searching to manually add items held outside the Vault.

---

## Experience Mapping

Collections is not a single page or feature — it's a framework that integrates with all major surfaces:

| Surface | Role in Collections |
|---------|-------------------|
| **Marketplace** | Enables listing and value realization from OIPs |
| **Vault** | Custodial record and authentication source |
| **Live** | Entry point for instant ownership of break or rip outcomes |
| **Profile / My Collection** | Unified view across all items owned or previously sold |
| **Taxonomy Layers (CDP / UIP / OIP / LDP)** | Provide consistent data structure for ownership, listing, and display |

---

## Cross-Cutting Principles

1. **Unified Ownership** — All collectibles—whether vaulted, unvaulted, or purchased live—must resolve to an OIP to ensure consistent display, valuation, and listing eligibility.
2. **Data Integrity** — Every OIP references its canonical CDP (Catalog Detail Page), ensuring provenance and shared metadata.
3. **Action Consistency** — Single and bulk actions (list, transfer, grade, withdraw) share UI and logic patterns.
4. **Valuation Transparency** — Estimated values derive from public sale and auction data sources, clearly labeled and traceable.
5. **Future-Proof Extensibility** — Folders, filters, and valuation logic are designed to scale across future asset types (e.g., memorabilia, tickets, or digital collectibles).

---

## Lifecycle Alignment

Collections sits alongside the **Detail Page Taxonomy** as the user-facing manifestation of ownership:

**CDP** (concept) → **UIP** (cert instance) → **OIP** (owned item) → **LDP** (listed item)

Collections visualizes and manages this lifecycle — serving as the collector's "hub" for viewing, valuing, and acting on OIPs.
