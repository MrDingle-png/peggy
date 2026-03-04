# Programs vs. collecting quests — building blocks framework

## The key distinction

| | **Programs** (e.g., FanCash Trading Card) | **Collecting quests** (e.g., Chase the Grail) |
|---|---|---|
| **Goal** | Open-ended, no defined endpoint | Clear set of goals — collect these specific cards |
| **Outcome** | Defined by external performance (player stats) | Defined by completion — first to finish wins a prize |
| **Quantity** | Could own 1 or 30 | Specific set you're working toward |
| **End state** | Season ends, earnings stop | Quest is completed (or not) |
| **Motivation** | Earnings, status, social | Completionism, status, social, competition |

Programs are experiences with no real endpoint or defined outcome — you could hold one card or thirty, and the outcome depends on player performance. Collecting quests have a clear set of goals (collect these nine cards) and a defined outcome (first to complete gets a 1-of-1 collectible).

Both share the same fundamental building blocks, which means we can build a scalable system that serves both.

## The 8 building blocks

### 1. Discovery & education
A publicly accessible page that promotes and explains the quest or program. Evolves across three phases:
- **Pre-launch:** teaser, hype, "coming soon"
- **Active:** how to participate, current standings, results
- **Post:** recap, winners, archive

Applies to both: FanCash needs a landing page explaining the program and payout model. Quests need a page showing what to collect, who's in the lead, and what the prize is.

### 2. Redemption / entry
The mechanism to enter the experience through Collect. For FanCash, it's scratching a code and redeeming it. For quests, it might be pulling a qualifying card or opting in.

The building block is: a configurable entry point that connects a physical or digital action to participation in a program or quest.

### 3. Progress tracking
How collectors see where they stand. For FanCash, it's a portfolio view showing earnings by card, weekly breakdowns, and projections. For quests, it's "7 of 9 collected" with visual progress indicators.

The building block is: a dynamic progress view that surfaces participation status, what's been achieved, and what's remaining.

### 4. Notifications & lifecycle
Both programs and quests need to communicate with collectors at key moments:
- **Programs:** weekly payout notifications, season start/end, stat corrections
- **Quests:** "you're 2 cards away," "someone just completed this quest," milestone celebrations

The building block is: triggered communications at lifecycle moments (pre-launch, start, milestone, completion/end) that can be configured per program or quest.

### 5. Social & community
The layer that creates FOMO and connection around shared participation:
- **Programs:** who else owns this player's card, leaderboard of top earners
- **Quests:** who's closest to completing, community progress, competitive tension

The building block is: a social layer showing other participants, rankings, and shareable moments that works across any program or quest.

### 6. Rewards & outcomes engine
The mechanism that delivers the payoff:
- **Programs:** weekly FanCash payouts tied to real-world stats, end-of-season bonuses
- **Quests:** prizes for completion (1-of-1 cards, exclusive collectibles, status badges)

The building block is: a configurable reward system that can handle different reward types (currency, physical items, digital exclusives, status/badges) with different trigger conditions (time-based, completion-based, performance-based).

### 7. Collection integration
How quest/program items appear within the existing collection experience:
- **Programs:** FanCash cards in the portfolio with earnings data, displayable in public collections
- **Quests:** quest progress visible as a folder or stack, "Chase the Rainbow" as a collection organizer

The building block is: a way to surface program/quest participation within the collection, including grouping, progress indicators, and special display treatments.

### 8. Rules & eligibility engine
Every program and quest needs a rules framework:
- **Programs:** tier multipliers, redemption windows, FanID linkage, non-transferable earnings
- **Quests:** what cards qualify, time windows, first-to-complete vs. everyone-who-completes, tiebreakers

The building block is: a configurable rules engine that defines participation criteria, qualifying actions, time windows, reward distribution logic, and edge cases.

## Strategic implication

By building FanCash Trading Card well, we are simultaneously building the infrastructure for Collecting Quests. Each building block we create for FanCash should be designed with reusability in mind — the discovery page template, the progress tracking component, the notification system, and the rewards engine should all be configurable enough to power a quest like "Chase the Grail" without rebuilding from scratch.
