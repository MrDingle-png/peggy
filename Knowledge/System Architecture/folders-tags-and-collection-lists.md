# Folders, Tags, and Collection Lists

| Field | Value |
|-------|-------|
| **Category** | System Architecture |
| **Subdomain** | Collect / Vault / Backoffice |
| **Title** | Folders, Tags, and Collection Lists |
| **Version** | 1.0 |
| **Date** | 2025-11-03 |
| **Maintainer** | Engineering, Fanatics Collect |
| **Status** | Active |

---

## Overview

Fanatics Collect uses three related but distinct organizational systems — **Folders**, **Tags**, and **Collection Lists** — to manage how vault items and listings are grouped, organized, and displayed across multiple platforms.

Each system reflects a different context:

| Concept | System | Primary Use | Data Type | Sync Behaviour |
|---------|--------|-------------|-----------|---------------|
| **Folders** | PWCC (PHP Monolith) | User vault organization | VaultItemGroup (Type 2) | Syncs to Backoffice as Tags |
| **Tags** | Backoffice (Go) | Commerce and internal labeling | item_tags (Spanner) | Receives syncs from Folders |
| **Collection Lists** | Live API (Elixir) | User-facing collections with UI metadata | VaultItemGroup (Type 3) | Independent; no sync to Backoffice |

Together, these systems support both internal operations (Backoffice tagging, commerce organization) and user-facing experiences (Vault folders, public Collections).

---

## Shared Foundation: vault_item_groups Table

All organizational objects are stored in the vault_item_groups table within the Marketplace MySQL database.

**Key Fields:**
- id — Primary key.
- title — Folder or collection name.
- type — Type discriminator: 1 = Shares, 2 = Folders, 3 = Collections.
- notes — JSON metadata (used for Collections UI).
- account_id — Owner's account.
- url_uuid — Public shareable identifier.
- is_published — Public/private flag.
- inserted_at, updated_at — Audit timestamps.

**Type Definitions:**
- Type 1 — Shares (legacy).
- Type 2 — Folders (PWCC, synced to Backoffice).
- Type 3 — Collections (Live API, user-facing).

All types use the same join table: vault_item_vault_item_group (many-to-many between vault_items and groups).

---

## System Roles

### Folders (Type 2)

- **System:** PWCC (PHP Monolith)
- **Purpose:** Organize vault items within a collector's vault UI.
- **Sync:** Folder titles sync to Backoffice as tags (for commerce alignment).
- **Visibility:** Private to user; internal organization only.
- **Data Behaviour:**
  - Stored as VaultItemGroup (type=2).
  - Membership changes trigger Backoffice tag updates via gRPC (BatchSyncTags).

**Key Principles:**
- Each Folder can contain multiple vault items.
- Folders are not shareable or public.
- Sync applies only to items with a back_office_listing_id.

---

### Tags (Backoffice)

- **System:** Backoffice (Go)
- **Purpose:** Internal labeling system for listings, variants, and products.
- **Storage:** item_tags table (Spanner).
- **Scope:** Scoped per user (fan_id) and entity type.
- **Operations:** Supports add, remove, and full-sync states.
- **Data Source:** Receives automated updates from PWCC Folder syncs.

**Key Principles:**
- Tags are normalized (lowercase, trimmed) and idempotent.
- Used primarily for search, reporting, and operational segmentation.
- Tags are not exposed directly to collectors.

---

### Collection Lists (Type 3)

- **System:** Live API (Elixir)
- **Purpose:** User-created, customizable groupings of owned items, typically with icon/background UI metadata.
- **Sync:** Independent; does **not** sync to Backoffice.
- **Visibility:** Currently private; future versions may enable public sharing.
- **Data Behaviour:**
  - Stored as VaultItemGroup (type=3).
  - Supports icon, background, and share URL metadata.
  - Managed through GraphQL endpoints.

**Key Principles:**
- Collections represent personalized, UI-driven lists.
- Distinct from Folders (which are organizational) and Tags (which are operational).
- Serve as the foundation for user curation and portfolio storytelling.

---

## Integration & Synchronization

### PWCC → Backoffice Tag Sync Flow

1. User adds or removes vault items from a Folder.
2. PWCC triggers async job SyncVariantTags.
3. Job constructs gRPC BatchSyncTagsRequest for each affected listing.
4. Backoffice processes request, overwriting tag state to match Folder membership.

**Result:** Backoffice tag state mirrors PWCC Folder membership for listings.

**Important Constraints:**
- Only Folders (type=2) sync.
- Only VaultListings with back_office_listing_id are included.
- Collections (type=3) remain independent.

**Error Handling:**
- 3 retry attempts per job (60s timeout).
- Failures logged; do not block user operations.
- Sync operations are idempotent.

---

## Product Context & UX Alignment

| System | User-Facing | Primary Role | Integration |
|--------|-------------|-------------|-------------|
| **Folders (PWCC)** | Yes (Vault UI) | Private organization of Vault items | Syncs to Backoffice Tags |
| **Tags (Backoffice)** | No (internal) | Operational categorization | Receives sync from Folders |
| **Collections (Live API)** | Yes (App / GraphQL) | Public or private showcases | Independent |

**User Mental Models:**
- *Folders* behave like file-system folders (organization).
- *Collections* behave like albums or showcases (presentation).
- *Tags* behave like labels used for internal sorting.

---

## Known Risks & Mitigations

| Risk | Description | Mitigation |
|------|-------------|-----------|
| **Type Overlap** | All systems use same table (vault_item_groups). | Strict type filtering; explicit type enums. |
| **Eventual Consistency** | Folder-tag sync occurs asynchronously. | Retry logic and idempotent sync. |
| **Data Drift** | Failed jobs can leave orphaned tags. | Monitoring + retry queue. |
| **User Confusion** | "Folders" vs. "Collections" overlap conceptually. | Clear UX copy and contextual help. |

---

## Future Considerations

1. **Potential Merge:** Explore unifying Folder and Collection List logic once Collections adoption stabilizes.
2. **Cross-System Visibility:** Enable Folders and Collections to reference shared group metadata.
3. **Expanded Tagging:** Optionally sync Collections to Backoffice for analytics alignment.
4. **Public Collections:** Introduce shareable URLs and discoverability for Collection Lists.
