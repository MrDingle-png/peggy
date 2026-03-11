# Design × AI — Operations Strategy

> What we need to build to move from individual AI-augmented work to scalable, agentic design and development.

---

## The Premise

The team has proven the value of AI in daily work — design QA in code, feature building in Cursor, research synthesis through Marvin, creative asset generation. What we've demonstrated is real and impressive, but it's individual. Each workflow depends on a person assembling the right context, choosing the right tools, and directing the agent.

To scale this, we need to make context available by default — not assembled per session. That means building infrastructure that lets agents access the right knowledge, speak the right design language, and execute within brand and system constraints without human orchestration.

The strategy is three layers. Each layer depends on the one below it.

---

## The Stack

```
                    ┌─────────────────────────────────────────────┐
                    │           LAYER 3: EXECUTION                │
                    │                                             │
                    │   Agentic Product        Agentic Creative   │
                    │   Design & Dev           & Content           │
                    │                                             │
                    │   Linear → PRD →         Brief → Creative   │
                    │   Design → Code →        → Assets →         │
                    │   PR → Ship              Content → Publish  │
                    ├─────────────────────────────────────────────┤
                    │           LAYER 2: SYSTEMS                  │
                    │                                             │
                    │   AI-Enabled             AI-Enabled          │
                    │   Design System          Brand System        │
                    │                                             │
                    │   Semantic tokens,       Visual identity,    │
                    │   component catalog,     tone & voice,       │
                    │   Figma ↔ code parity    content patterns    │
                    ├─────────────────────────────────────────────┤
                    │           LAYER 1: KNOWLEDGE                │
                    │                                             │
                    │   Product Knowledge      User Knowledge      │
                    │                                             │
                    │   PRDs, decisions,       Research, insights,  │
                    │   architecture,          behaviours,          │
                    │   business rules         collector context    │
                    │                                             │
                    └─────────────────────────────────────────────┘
```

---

## Layer 1: Knowledge Foundation

**The problem it solves:** Agents make bad decisions when they lack context. Today, product context lives in Notion pages, Slack threads, Linear tickets, and people's heads. An agent can write code, but it can't know why a decision was made, what the business constraints are, or what collectors actually care about — unless someone manually feeds it.

**The goal:** A shared, AI-readable knowledge layer that any agent in any workflow can query for product and user context.

### Product Knowledge

Everything an agent needs to make good product decisions:

- **Strategy and roadmap:** What we're building, why, and in what order
- **Decision history:** Why we chose X over Y — the reasoning, not just the outcome
- **PRDs and specs:** Current and past product requirements
- **Architecture and business rules:** How the product actually works — data models, system constraints, integration dependencies
- **Domain knowledge:** Collecting, marketplace mechanics, live commerce — the things a new team member would need months to learn

**What needs to happen:**
- Consolidate and structure product documentation so it's queryable (not buried in Notion page hierarchies or Slack threads)
- Stand up an MCP-accessible knowledge base (Company Docs MCP or similar) that agents across Cursor, Claude, and Slack can query
- Define what stays as living documents vs. what gets ingested into vector search
- Establish ownership and update cadence — knowledge that drifts is worse than no knowledge

### User Knowledge

Everything an agent needs to understand collectors:

- Research findings and synthesis
- Behavioural patterns and mental models
- Pain points, motivations, and unmet needs
- Segment-specific context

**Current state:** Largely solved. HeyMarvin is our research-enabled LLM with MCP connectors. Research synthesis already pipes into Claude directly. The infrastructure exists — the work is ensuring coverage and freshness of the research corpus.

**What needs to happen:**
- Continue building the research corpus in Marvin
- Ensure MCP integration is active and reliable across team workflows
- Define patterns for how agents should cite and weight research findings

---

## Layer 2: Systems

**The problem it solves:** Even with perfect knowledge, an agent that generates UI or creative output needs to do so within our design language and brand voice. Without a semantic, machine-readable system layer, agents produce generic output that requires heavy human rework — defeating the purpose.

**The goal:** Design system and brand system that are structured for AI consumption — not just human reference docs, but queryable, enforceable, and generative.

### AI-Enabled Design System

The design system is the interface contract between design intent and production code. For agents to generate real UI (via a2ui or similar protocols), the system must be:

- **Semantic:** Tokens named by purpose, not appearance (`surface-primary`, not `gray-100`). Components described by behaviour, not implementation
- **In parity:** What exists in Figma must match what exists in code. No drift. No "design version" vs. "dev version"
- **Metadata-rich:** Every component needs structured props, variants, states, usage guidelines, and accessibility requirements that agents can read
- **Queryable:** Exposed via MCP so agents can look up components, validate token usage, and understand relationships

**What needs to happen:**
- Complete token sync between Figma and code (bidirectional)
- Audit and restructure component library for semantic naming and full metadata
- Deploy Figma Console MCP for AI read/write access to the design system
- Implement FigmaLint to enforce compliance and catch drift
- Build toward component catalog exposure for generative UI protocols

**Why this matters for the business:** This is the single biggest unlock. Without design system parity, none of the generative UI protocols work. With it, we unlock the entire execution layer for product.

### AI-Enabled Brand System

The brand system is the creative equivalent of the design system. It governs how we look, sound, and communicate across every touchpoint. For agents to produce on-brand creative and content, this system must be equally machine-readable.

**Visual identity:**
- Logo usage rules, clear space, sizing constraints
- Colour palette with semantic meaning (not just hex codes)
- Typography scales, pairing rules, hierarchy
- Photography and imagery guidelines — what we use, what we don't
- Layout patterns and grid systems for marketing surfaces

**Tone and content:**
- Voice and tone principles — how we sound as a brand
- Content patterns by channel (email, push, social, in-app)
- Copy guidelines — terminology, naming conventions, things we say and don't say
- Writing structures for common formats (product descriptions, announcements, marketing copy)

**What needs to happen:**
- Audit existing brand guidelines and convert from static documents (PDFs, Figma pages) into structured, queryable formats
- Define semantic brand tokens (similar to design tokens but for brand attributes)
- Build or configure an MCP-accessible brand knowledge base
- Create validation rules that agents can check against (like FigmaLint, but for brand)

**Why this matters for the business:** Marketing and creative output is high-volume and repetitive. An AI-enabled brand system means agents can produce first-draft creative, content, and campaign assets that are on-brand by default — not by review.

---

## Layer 3: Execution

**The problem it solves:** Even with knowledge and systems in place, someone still has to orchestrate the workflow — trigger the agent, load the right context, point it at the right system, review the output, and ship it. The execution layer is about closing those loops.

**The goal:** End-to-end agentic workflows where humans curate, direct, and approve — but don't manually assemble context or do the mechanical work.

### Agentic Product Design and Development

The pipeline from the presentation, fully closed:

```
Trigger → Knowledge → Planning → Build → Ship → Done
Linear     Product      Design      Code     PR      Slack
Ticket     Context      Automated   Drafted  Opened  Notify
```

**What this looks like when it works:**
- A Linear ticket arrives with a product requirement
- The agent pulls product context (Layer 1) — what does this feature relate to? What decisions have been made? What do collectors need?
- The agent pulls design system context (Layer 2) — what components exist? What tokens apply? What patterns should this follow?
- A PRD is drafted, design is composed using system components, code is written against the design system
- A PR is opened, scoped to one surface, with design and code shipping together
- Team is notified for review

**Current state:** Steps 01-04 are already running in Chad's workflow. The gap is automation of context assembly and design system integration.

**What needs to happen:**
- Layer 1 and Layer 2 must be operational first
- Define the trigger-to-ship pipeline as a repeatable agent workflow
- Build approval checkpoints (human-in-the-loop at planning and ship stages)
- Evaluate generative UI protocols for the design composition step (see [Agent-Driven UI landscape](a2ui-protocol.md))
- Instrument for quality — automated visual regression, design system compliance checks

### Agentic Creative and Content Development

The parallel pipeline for marketing and brand:

```
Trigger → Knowledge → Creative → Production → Review → Publish
Campaign   Brand &      Concept     Assets       Brand     Channel
Brief      Collector    Direction   Generated    Check     Deploy
           Context
```

**What this looks like when it works:**
- A campaign brief or content request arrives
- The agent pulls brand context (Layer 2) — tone, visual guidelines, content patterns
- The agent pulls collector context (Layer 1) — who is this for? What resonates?
- Creative direction is proposed, assets are generated (imagery, motion, copy)
- Output is validated against brand system rules
- Content is formatted for channel and published

**What needs to happen:**
- Layer 2 (brand system) must be operational first
- Define repeatable creative workflows by output type (social, email, in-app, campaign)
- Integrate generative creative tools (Krea, Dream Machine, Remotion) into the pipeline
- Build brand validation checkpoints
- Establish human approval patterns for creative output

---

## Dependencies and Sequencing

The layers create a natural build order. You cannot skip ahead.

| Phase | Focus | Unlocks |
|---|---|---|
| **Now** | Individual AI-augmented work (current state) | Team productivity, proof of concept |
| **Next** | Layer 1: Knowledge foundation | Agents that understand our product and our collectors |
| **Then** | Layer 2: Design system + Brand system | Agents that produce on-system, on-brand output |
| **Future** | Layer 3: Agentic execution pipelines | End-to-end workflows where humans curate, not construct |

Within this sequence:

- **User knowledge (Marvin)** is largely operational — continue investing in coverage
- **Product knowledge** is the most immediate gap — context is scattered and not AI-accessible
- **Design system** is the highest-leverage systems work — it unlocks the entire product execution layer
- **Brand system** can develop in parallel with the design system but serves a different audience (marketing/creative vs. product/engineering)
- **Execution layer** is the outcome, not a thing you build directly — it emerges when Layers 1 and 2 are solid

---

## Who This Matters To

| Stakeholder | What they care about | Which layer |
|---|---|---|
| **Product** | Faster feature delivery, better decisions, less handoff friction | Layer 1 + Layer 3 (product) |
| **Engineering** | Less rework, clearer specs, design-system-compliant code from the start | Layer 2 (design system) + Layer 3 (product) |
| **Design** | Own the system, QA in code, ship design and code together | Layer 2 (design system) + Layer 3 (product) |
| **Marketing / Creative** | On-brand output at speed, less production bottleneck | Layer 2 (brand system) + Layer 3 (creative) |
| **Leadership** | Scalable output without proportional headcount growth | All layers |

---

## The Positioning

**What we tell the organisation:**

We've proven AI works at the individual level. Now we're building the infrastructure that makes it work at the organisational level. The investment is in three layers:

1. **Knowledge** — so agents understand our product and our collectors, not just generic patterns
2. **Systems** — so agents speak our design language and brand voice, not generic output
3. **Execution** — so entire workflows run end-to-end, with humans directing and approving rather than assembling

Each layer depends on the one below it. We're not skipping to the exciting part — we're building the foundation that makes the exciting part actually work.

> By 2027, every design decision should be traceable, composable, and AI-augmentable. — Design × AI Roadmap
