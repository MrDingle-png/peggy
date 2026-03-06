# Item Submission

| Field | Value |
|-------|-------|
| **Category** | Established Product Behaviour |
| **Subdomain** | Vault / Intake |
| **Title** | Item Submission |
| **Version** | 1.0 |
| **Date** | 2025-10-08 |
| **Maintainer** | Product, Fanatics Collect |
| **Status** | Active |

---

Item Submission refers to the **ways in which collectors, sellers, and trusted partners introduce physical collectibles into the Fanatics Collect Vault**.

Each submission pathway defines the item's *origin*, *authentication state*, and *permitted downstream actions* (listing, storage, grading, redemption).

---

## Submission Types

### 1. Standard Vault Submission (Graded)

- **Who:** Collectors or sellers
- **Input state:** Already graded and authenticated
- **Process:**
  - The submission form collects minimal details (item count, total declared value, item type, and intent — list vs. store).
  - Users may indicate their intention to list at submission.
- **Outcome:**
  - Items are shipped to the Collect Vault, ingested, and added to the user's collection as Owned Item Pages (OIPs).
- **Sellability:**
  - Can be listed to **Weekly** or **Premier** auctions at submission.
  - **Buy Now** listings are unavailable at submission because the intake form does not collect item-level details such as asking price, minimum offer, or offer eligibility.
  - Once items are ingested and itemized, users can manually list them to Buy Now.

---

### 2. Standard Vault Submission (Raw)

- **Who:** Collectors or sellers
- **Input state:** Raw (ungraded)
- **Process:**
  - The submitter selects a grading partner (e.g., PSA, BGS, CGC, SGC) during submission.
  - Collect itemizes the items, prepares them for grading, ships to the selected partner, and re-ingests once graded.
- **Outcome:**
  - Graded items return to the vault, are added to the user's collection as OIPs.
- **Sellability:**
  - Not sellable until graded.
- **Future Behaviour:**
  - In future, raw items may be submitted without selecting a grading partner at submission, aligning with partner-integrated intake flows.

---

### 3. Red Rookie Redemption Submission

- **Who:** Collectors participating in the Topps Red Rookie campaign
- **Input state:** Raw, uncertified card linked to player achievements
- **Process:**
  - Collector submits the Red Rookie card to the Collect Vault for storage and potential redemption.
- **Outcome:**
  - The raw card is added to the user's collection.
- **Sellability:**
  - Not sellable until graded.
- **Redemption Values:**
  - $100 — Player wins Rookie of the Year
  - $300 — Player also wins first MVP or Cy Young
  - $500 — Player wins a second MVP or Cy Young
  - $700 — Player wins three MVPs or Cy Youngs (any combination)
  - $1,000 — Player inducted into Hall of Fame within 10 years of retirement

---

### 4. Topps General Redemption Submission

- **Who:** Collectors redeeming Topps redemption cards
- **Input state:** Raw, manufacturer-origin guaranteed
- **Process:**
  - Collector redeems the code at Topps.
  - Chooses to have the redeemed card shipped to their personal address or directly to the **Collect Vault**.
- **Outcome:**
  - The manufacturer (e.g. Topps) ships the redeemed card directly to the Collect Vault.
  - Upon ingestion, the item receives the **Direct from [Manufacturer]** attribute.
- **Sellability:**
  - May be sold raw on Collect while in the Vault *if it retains the Direct from [Manufacturer] attribute.*
  - Once withdrawn from the Vault, the item permanently loses this attribute and can no longer be listed raw.

---

### 5. Topps on Collect

- **Who:** Collectors purchasing sealed products sold by manufacturers (e.g. Topps) via Fanatics Collect
- **Input state:** Sealed product (not opened or graded)
- **Process:**
  - User purchases the sealed product from the manufacturer's storefront integrated into Fanatics Collect.
  - User chooses shipping destination: personal address or the **Collect Vault**.
- **Outcome:**
  - If shipped to the Vault, the item is ingested and marked with the **Direct from [Manufacturer]** attribute.
  - Added to the buyer's collection as an OIP.
- **Sellability:**
  - Sealed items with the Direct from [Manufacturer] attribute may be listed raw on Collect while in the Vault.
  - Once withdrawn from the Vault, the attribute and raw sellability are permanently lost.
- **Lifecycle:**
  - Appears as an OIP in the buyer's collection and becomes an LDP when listed.

---

### 6. Dropshipper Submission

- **Who:** Third-party certified sellers (integrated via Shopify or similar)
- **Input state:** Mostly graded; some raw
- **Process:**
  - Inventory is listed directly on Collect via the seller's integration.
  - Buyers can choose to ship purchased items to their personal address or directly to the **Collect Vault**.
  - Shipping to the Vault incurs standard domestic shipping and intake fees, as the item physically moves from seller custody to the Vault.
- **Outcome:**
  - Upon arrival, items are ingested and added to the buyer's collection as OIPs.
  - Raw items are not sellable until graded; users receive follow-up prompts to select a grading partner.
- **Sellability:**
  - Graded items: immediately sellable.
  - Raw items: must be graded first.

---

### 7. Live Platform Submission

- **Who:** Collectors purchasing via Fanatics Live
- **Input state:** Graded or raw
- **Process:**
  - Buyers can choose to ship purchased items directly to the **Collect Vault**.
  - Items are ingested and added to the buyer's collection.
  - Raw items are held until graded; users are notified post-ingestion and offered grading options.
- **Sellability:**
  - Graded items: immediately sellable.
  - Raw items: must be graded first.

---

## Cross-Cutting Principles

1. **Custody defines trust** — Items originating **Direct from [Manufacturer]** or other trusted partners may be treated as authenticated even if raw.
2. **Vault entry ≠ automatic sellability** — Only items that are graded or carry the *Direct from [Manufacturer]* attribute can be listed raw.
3. **Listing path determined post-ingestion** — Standard submissions collect minimal metadata; item-level curation happens after intake.
4. **Lifecycle alignment** — All submissions ultimately create or update an **Owned Item Page (OIP)**. Listing eligibility determines whether a **Listing Detail Page (LDP)** may be spawned.
5. **Withdrawal resets trust** — Once an item leaves the Vault, it permanently loses its *Direct from [Manufacturer]* (or equivalent) attribute and raw sellability.
