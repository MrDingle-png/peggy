# Extended Bidding

| Field | Value |
|-------|-------|
| **Category** | Established Product Behaviour |
| **Subdomain** | Marketplace / Auctions |
| **Title** | Extended Bidding |
| **Version** | 1.0 |
| **Date** | 2025-10-06 |
| **Maintainer** | Product, Fanatics Collect |
| **Status** | Active |

---

Extended bidding is a feature often used in online auctions, to more closely represent a bricks and mortar auction experience, and to prevent last-second "sniping" by extending the auction's end time when a bid is placed within a final countdown window.

- **Weekly Auction**
  - Runs for 10 days, from Thursday evening to the following Sunday evening (PDT).
  - From the moment that a Weekly Auction opens, bids can be made by interested buyers. This phase is called "standard bidding".
  - During standard bidding a countdown timer is displayed, which counts down the days, hours, minutes, and seconds until the start of extended bidding.
  - All items in the Auction enter the first window of extended bidding, even if they haven't received a bid during standard bidding.
  - The first window of extended bidding lasts for 30 minutes (a countdown timer is displayed). The following 6 windows are 5 minutes each. All subsequent windows are 1 minute.
  - As long as an item receives a bid during an extended bidding window it is "extended" into the next window. The current window timer continues to countdown, and all items that are marked as extended are moved forward to the next window.
  - To make it clear to interested buyers we badge items with the following statuses:
    - `Bid needed` - Item will sell if no bids are made in the current window.
    - `Extended` - Item has received a bid in the current window and will extend to the following window.
  - Any item that does not receive a bid during an extended bidding window is closed and the item is sold to the highest bidder.
  - Any item that received no bids during standard or extended bidding closes as "unsold".
  - Extended bidding continues until all items are closed.

- **Premier Auction**
  - Runs for 14 days, from and until Thursday evening, normally in the middle two weeks of a given month.
  - From the moment that a Premier Auction opens, bids can be made by interested buyers. This phase is called "standard bidding".
  - During standard bidding a countdown timer is displayed, which counts down the days, hours, minutes, and seconds until the start of extended bidding.
  - All items in the Auction enter the first window of extended bidding, even if they haven't received a bid during standard bidding.
  - This is where the similarity between Weekly and Premier ends. Where Weekly has windows that run in their entirety before the countdown resets and the next window starts (for items that have received a bid in that window), Premier uses windows differently.
  - The first window of extended bidding lasts for 30 minutes. However, the countdown timer that the user sees, starts at 5 minutes. During this 30 minute window, anytime there is a bid on any of the items across the entire auction, this countdown is reset to 5 minutes.
  - Once 30 minutes has elapsed, we enter the second window which means that the countdown timer now resets to 2 minutes with every bid.
  - Once 30 minutes has elapsed (1 hour into extended bidding), we enter the third and final window which means that the countdown timer now resets to 1 minute with every bid. This continues until the timer gets to 0 seconds and the auction closes.
  - At close, all items that have received at least 1 bid are sold to the highest bidder.
  - Any items that received no bids during standard or extended bidding close as "unsold".
