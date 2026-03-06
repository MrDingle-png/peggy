# Collections Glossary

| Field | Value |
|-------|-------|
| **Category** | Reference |
| **Subdomain** | Collect / Vault |
| **Title** | Collections Glossary |
| **Version** | 1.0 |
| **Date** | 2025-11-03 |
| **Maintainer** | Product, Fanatics Collect |
| **Status** | Active |

---

## Purpose

This glossary defines key terms, system objects, and functional concepts used within the **Collections** framework. It serves as a reference for cross-disciplinary alignment between Product, Design, Engineering, and Data.

---

## Core Entities

- **CDP (Catalog Detail Page)** — The canonical, evergreen record of a card or collectible concept (e.g., 2018 Topps Chrome Shohei Ohtani #150). Anchors metadata shared by all instances of that card.
- **UIP (Unassigned Item Page)** — A unique certified item not yet claimed or owned (e.g., PSA 10 Jordan Rookie, cert #123456). Converts to OIP when ownership is established.
- **OIP (Owned Item Page)** — The system object representing an item owned by a collector. Serves as the control surface for listing, grading, transfer, and withdrawal.
- **LDP (Listing Detail Page)** — The buyer-facing representation of a listed OIP, used for auctions, Buy Now, offers, and breaks.
- **PDP (Product Detail Page)** — A standardized, platform-controlled listing for fungible or retail products (e.g., Topps Drops, Instant Rips).

---

## Collections Features

- **Collection View** — A dynamic page layout that displays subsets of a user's OIPs by selected criteria (e.g., graded cards only, Topps Chrome sets, total value).
- **Folder** — A user-defined grouping of OIPs, used for organization, curation, or public display. Folders can be private or shareable.
- **Sort & Filter** — Tools that let collectors reorder or narrow OIPs by attributes such as sport, grading company, grade, or estimated value.
- **Search Owned Items** — A universal search within a user's collection, indexed by cert number, title, or tag.
- **Valuation** — The estimated current market value of an owned item, based on recent public auction and marketplace data. Supports aggregate portfolio valuation.
- **Add Unvaulted Cards** — The ability for users to scan or manually search and add items not held in the Vault to their digital collection.

---

## Supporting Concepts

- **Vaulted Item** — A collectible held in the Fanatics Collect Vault, verified and authenticated. Eligible for instant listing and insured custody.
- **Unvaulted Item** — A collectible held by the user outside of the Vault. May be tracked digitally but is not eligible for instant sale until submitted.
- **Direct from [Manufacturer]** — An attribute indicating the item entered the ecosystem directly from a trusted manufacturer (e.g., Topps), granting elevated trust for raw items.
- **Graded Item** — A collectible certified and encapsulated by a grading partner (PSA, BGS, CGC, or SGC). Includes a cert number used to link to a CDP.
- **Raw Item** — A collectible not yet graded or encapsulated; may require verification before listing.
- **Portfolio Value** — The sum of valuations across all owned OIPs, displayed within the Collection View.
- **Single / Bulk Actions** — Batch operations (e.g., list, transfer, withdraw) performed across one or more OIPs.

---

## Cross-System Links

| Related Concept | Description |
|----------------|-------------|
| **Detail Page Taxonomy** | Defines classification logic and hierarchy (CDP → UIP → OIP → LDP → PDP). |
| **Vault Intake (Item Submission)** | Defines how items enter the Vault and become OIPs. |
| **Extended Bidding** | Defines auction closing logic and listing states for LDPs. |
| **Valuation Data Model** | Defines price estimation sources, recency weighting, and transparency principles. |
