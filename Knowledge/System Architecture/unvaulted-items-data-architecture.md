# Unvaulted Items Data Architecture

| Field | Value |
|-------|-------|
| **Category** | System Architecture |
| **Subdomain** | Collect / Vault / Data |
| **Title** | Unvaulted Items Data Architecture |
| **Version** | 1.0 |
| **Date** | 2025-10-29 |
| **Maintainer** | Engineering, Fanatics Collect |
| **Status** | Proposed |

---

## Overview

The **Unvaulted Items Architecture** extends the Fanatics Collect ecosystem to support tracking, organizing, and valuing collectible cards **not stored in the Vault**. It enables a unified collection experience—allowing users to manage both **vaulted** and **unvaulted** items within the same interface.

This document defines the conceptual data architecture, integration model, and high-level design decisions behind this feature.

---

## Purpose

Unvaulted items bridge a major gap in the Collect experience: users can now manage the cards they physically hold (raw, graded, or authenticated) alongside those stored in the Vault. This unlocks:

- A complete view of a collector's portfolio
- Personalized valuation tracking
- Seamless transition paths to vault submission and listing
- Unified experiences across Folders, Collections, and valuation features

---

## Core Concepts

### Unvaulted Item

A record representing a collectible card owned by a user but not stored in the Vault.

- **Ownership:** Linked directly to user_id (not account_id)
- **Data Source:** May originate from Catalog search, manual entry, or scan
- **Integration:** Shares card and grade metadata with proto_items

### Proto Item

The canonical record that represents a unique card + grade pairing. Both Vaulted and Unvaulted items reference the same proto_item, ensuring data consistency.

### Vault Parity

Unvaulted items mirror Vault item behavior in structure and metadata, enabling mixed portfolios and consistent valuation across custody types.

---

## Data Architecture Summary

### Table Relationships

```
USER
 ├── ACCOUNTS (Vault)
 ├── VAULT_ITEMS (Vaulted)
 └── UNVAULTED_ITEMS (Personal)
        │
        ▼
     PROTO_ITEMS (Shared)
       ├── CARD_GRADES
       └── CARDS
```

- **Shared Metadata:** proto_items unify Vaulted and Unvaulted records.
- **Ownership Model:** Direct user_id ownership simplifies lifecycle and permissions.
- **Grouping Integration:** Both Vaulted and Unvaulted items can be organized under the same vault_item_groups (Folders, Collections).

---

## Key Behaviors

| Operation | Description | Outcome |
|-----------|-------------|---------|
| **Create** | User adds card manually or from Catalog | New Unvaulted Item created, linked to existing or new proto_item |
| **Update Grading** | User updates grading details after certification | Metadata updates; potential proto_item reassignment |
| **Update Valuation** | User enters purchase price or estimated value | Adjusts personal valuation and portfolio total |
| **Delete** | User removes card from personal collection | Record removed; associated links cleared |

---

## Schema Comparison

| Category | Vault Items | Unvaulted Items | Notes |
|----------|-------------|-----------------|-------|
| Ownership | account_id | user_id | Direct ownership (no Vault account required) |
| Workflow | Submission, Status, Location | — | No Vault workflow |
| Valuation | Market/Guide Values | Purchase + Estimated Value | User-entered values only |
| Marketplace | Listing flags, pricing fields | — | Not listable until vaulted |
| Storage | Archival & QR fields | — | No physical custody |

The Unvaulted table is roughly **70% smaller** than vault_items, optimized for simplicity and query performance.

---

## Integration: Mixed Collections and Folders

Both Vaulted and Unvaulted items can coexist within shared organizational structures:

- **Collections (Type 3)** — User-created, visual groupings
- **Folders (Type 2)** — Private organizational tools in the Vault UI

This is achieved by transitioning vault_item_groups from account-based to user-based ownership.

**Benefits:**
- Unified Collection and Folder logic
- Mixed Vault + Unvaulted items supported in one portfolio view
- Consistent actions (view, sort, filter, value)

---

## Data Integrity Considerations

### Serial Number Uniqueness

Serials must be unique **per user** across Vaulted and Unvaulted items to prevent duplication.

### ProtoItem Continuity

When items move from Unvaulted → Vaulted (via submission), proto_item_id should remain consistent to preserve historical continuity and valuation tracking.

### Deletion Behavior

All Unvaulted items use **hard deletes** to reduce storage overhead and complexity. Since they represent local user entries, no business workflows depend on soft-deletion recovery.

---

## Performance Overview

Unified queries leverage UNION ALL across Vaulted and Unvaulted tables, with index optimizations to maintain speed at scale.

| Metric | Target |
|--------|--------|
| Median Query Time | < 50ms |
| 95th Percentile | < 200ms |
| 99th Percentile | < 500ms (for 100k items) |

Caching is used for total counts (1-hour TTL) and recent collection snapshots (5-minute TTL).

---

## Future Enhancements

| Theme | Description |
|-------|-------------|
| **Event Store** | Persist domain events for audit/replay capabilities |
| **Tags / Labels** | Extend shared tagging model to Unvaulted items |
| **Valuation History** | Enable temporal queries ("value on X date") |
| **Mixed Collection Visibility** | Expand support for public Collections combining both item types |
