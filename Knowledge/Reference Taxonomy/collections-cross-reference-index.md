# Collections Knowledge Base — Cross-Reference Index

| Field | Value |
|-------|-------|
| **Category** | Reference / Taxonomy |
| **Subdomain** | Collect / Vault |
| **Title** | Collections Knowledge Base — Cross-Reference Index |
| **Version** | 1.0 |
| **Date** | 2025-11-03 |
| **Maintainer** | Product, Fanatics Collect |
| **Status** | Active |

---

## Purpose

This index provides an overview of all active documentation related to **Collections**, **Vault**, and **Valuation** in Fanatics Collect.

It helps Product, Design, Engineering, and QA navigate how user experiences, data models, and behaviours connect across the ecosystem.

---

## 1. Experience Framework

### Collections

**Version:** 1.0 — *2025-11-03*

Defines how collectors experience ownership, organisation, and value tracking across Vaulted, Unvaulted, and Live-purchased items.

**Dependencies:** Detail Page Taxonomy, Collections Glossary, Unvaulted Items Data Architecture.

---

## 2. System Architecture

### Folders, Tags, and Collection Lists

**Version:** 1.0 — *2025-11-03*

Describes how organisational concepts (Folders, Tags, and Collections) are implemented across PWCC Monolith, Backoffice, and Live API systems. Explains shared tables (`vault_item_groups`) and data flow between Vault and Backoffice.

**Dependencies:** Collections, Unvaulted Items Data Architecture.

### Unvaulted Items Data Architecture

**Version:** 1.0 — *2025-10-29*

Defines the system architecture for Unvaulted Items, enabling collectors to manage both Vaulted and personal cards. Covers data ownership (`user_id`), proto-item reuse, and unified queries for mixed portfolios.

**Dependencies:** Collections, Folders / Tags / Collection Lists.

---

## 3. Established Product Behaviour

### Valuation & Pricing Questions

**Version:** 1.0 — *2025-11-03*

Documents open clarifications and product decisions around valuation, rounding, and chart aggregation. Captures alignment points for Product, Design, and Data on "Collect Market Value" terminology.

**Dependencies:** Collections, Unvaulted Items Data Architecture.

*(See also: Item Submission, Extended Bidding — both defined under Established Product Behaviour.)*

---

## 4. Reference / Taxonomy

### Collections Glossary

**Version:** 1.0 — *2025-11-03*

Defines key terms and system objects (OIP, LDP, PDP, Folders, Valuation) used throughout the Collections experience.

**Dependencies:** Collections, Detail Page Taxonomy.

### Detail Page Taxonomy

**Version:** 1.0 — *2025-10-06*

Defines the taxonomy of all detail page types (CDP, UIP, OIP, LDP, PDP) and their relationships. Serves as a foundational reference for Collections, Vault Intake, and Live features.

**Dependencies:** Collections, Folders / Tags / Collection Lists.

---

## How to Use This Index

- **Product Managers** → Identify behavioural logic and dependencies across systems.
- **Designers** → Reference shared terminology and data model implications.
- **Engineers** → Locate upstream/downstream relationships between TDDs.
- **QA & Support** → Understand how Vaulted and Unvaulted experiences interact.
