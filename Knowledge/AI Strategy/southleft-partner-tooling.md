# Southleft — Partner & Tooling Ecosystem

> Boutique agency specialising in AI-powered design systems. Our partner for building an AI-enabled design system infrastructure.

---

## Who They Are

**Southleft** is a front-end engineering agency based in New Orleans, led by **TJ Pitre**. They focus exclusively on the intersection of AI and design systems — building tools, MCP integrations, and workflows that help product teams ship faster with systems that actually work.

- **Website:** [southleft.com](https://southleft.com)
- **GitHub:** [github.com/southleft](https://github.com/southleft)
- **Course:** Partnering with **Brad Frost** on an "AI & Design Systems" online course
- **Clients:** PetSmart (Sparky design system), Cura Freight, and other enterprise brands

---

## Their Philosophy: Context-Based Design Systems

Southleft's foundational model is **"Context-Based Design Systems"** — the idea that structured context should flow seamlessly between design and engineering, growing smarter and more capable at every step.

Their core position: **system parity is more important than code-to-design screen capture.** Tools like Claude Code to Figma are useful for exploration, but durable product work requires system awareness — tools that understand how components, tokens, and variables relate to each other across the entire ecosystem.

This aligns directly with our own approach: designers owning the design system, maintaining Figma-to-code parity, and building toward a fully agentic design workflow.

---

## Open-Source Tools Available to Us

### Figma Console MCP

**Your design system as an API.**

| | |
|---|---|
| **GitHub** | [southleft/figma-console-mcp](https://github.com/southleft/figma-console-mcp) (891 stars) |
| **Docs** | [docs.figma-console-mcp.southleft.com](https://docs.figma-console-mcp.southleft.com/) |
| **Latest** | v1.11.2 (Feb 2026) |

An MCP server that gives AI assistants full read and write access to Figma. Unlike the official Figma MCP (which focuses on component-level code generation from specific links), Console MCP provides complete project-wide context.

**Capabilities (56+ MCP tools):**
- Extract variables, styles, and components as structured data
- Export to CSS custom properties, Tailwind config, Sass variables, or JSON
- Create and update design tokens and variables across the entire system
- Set fills, strokes, and visual properties on any element
- Clone, rename, resize, and reorganise nodes
- Execute custom Figma Plugin API code through natural language
- Audit and document component libraries at scale
- Console log capture for plugin debugging

**Setup modes:**
- **Remote (SSE):** Zero setup, 18 read-only tools, OAuth authentication
- **Local (Desktop Bridge):** Full 56+ tools including write capabilities, requires Figma Desktop plugin

**How it complements the official Figma MCP:** Use the official MCP for quick code scaffolding from a component link. Use Console MCP when AI needs to understand the full design system or make changes to Figma itself.

---

### Story UI

**AI-powered layout generation inside Storybook.**

| | |
|---|---|
| **GitHub** | [southleft/story-ui](https://github.com/southleft/story-ui) (135 stars) |
| **npm** | `@tpitre/story-ui` |

Enables non-developers to generate production-ready layouts using natural language prompts directly within a Storybook environment.

**Capabilities:**
- Generate layouts from prompts (e.g. "a 3x3 grid of cards" or "an inventory dashboard")
- Chat-based interface within Storybook for iterative refinement
- Uses your real components, not mocks or approximations
- Vision support for attaching screenshots with requests
- Edit existing stories through conversation
- Orphan detection for unused stories

**Multi-framework:** React, Vue, Angular, Svelte, Web Components
**Multi-LLM:** Claude, OpenAI (GPT), Google Gemini

**Why it matters:** Story UI means designers, PMs, and non-developers can autonomously create and test page compositions using real system components — without engineering support. The starting point is already system-aligned.

---

### Design Systems MCP

**Trusted AI assistant for design system knowledge.**

| | |
|---|---|
| **GitHub** | [southleft/design-systems-mcp](https://github.com/southleft/design-systems-mcp) (126 stars) |

A dedicated MCP server that provides structured, reliable context about design systems. AI tools can query it to understand components, tokens, patterns, and best practices. Acts as a trusted source of truth for any AI-assisted design or development workflow.

---

### FigmaLint

**AI-powered design system compliance and accessibility auditing.**

| | |
|---|---|
| **GitHub** | [southleft/figmalint](https://github.com/southleft/figmalint) (41 stars) |
| **Install** | [Figma Community plugin](https://www.figma.com/community/plugin/1373339737439796370) |

A Figma plugin that audits components for compliance, structure, and accessibility gaps.

**What it checks:**
- Component metadata and structure
- Design token usage (flags hard-coded values)
- Naming conventions
- Accessibility standards
- Missing or unclear properties

**Why it matters:** Makes components "robust, structured, and self-describing" for both human developers and AI agents. Catches issues that typically only surface during development. Directly supports making our design system AI-compatible.

---

### Company Docs MCP

**Internal documentation as an AI-searchable knowledge base.**

| | |
|---|---|
| **GitHub** | [southleft/company-docs-mcp](https://github.com/southleft/company-docs-mcp) (31 stars) |

Transforms existing documentation (markdown, HTML, PDFs, web pages) into a searchable vector database that AI agents can query through MCP.

**Architecture:** Cloudflare Workers (hosting + vector conversion) + Supabase (PostgreSQL vector search) + npm CLI (content ingestion)

**Access channels:** Slack, Claude Desktop, Cursor, web chat, API endpoints

**Why it matters:** Directly relevant to our "knowledge platform + collector insights" priority. Could unify internal policies, research findings, and product documentation into a single queryable resource accessible across all our AI tools.

---

### a2ui-bridge

**Framework adapters for Google's a2ui protocol.**

| | |
|---|---|
| **GitHub** | [southleft/a2ui-bridge](https://github.com/southleft/a2ui-bridge) (18 stars) |

Connects Google's a2ui protocol to real component libraries. Provides the adapter layer needed to go from a2ui's declarative JSON to rendered UI using your actual design system components. See [a2ui-protocol.md](a2ui-protocol.md) for full protocol details.

---

## Additional Resources

### DSAudit
A codebase auditing tool for design systems — validates health, structure, and consistency of component libraries in code.

### Altitude
Southleft's internal design system, used as a testbed for AI integrations and workflow experiments. Powers demos for Story UI and FigmaLint.

---

## How Their Tools Map to Our Roadmap

Our presentation identified four things we need to productionise. Southleft's tooling maps directly:

| Our Priority | Southleft Tools |
|---|---|
| **Knowledge platform + collector insights** | Company Docs MCP, Design Systems MCP |
| **AI-enabled design system (semantic)** | Figma Console MCP, FigmaLint, Story UI, DSAudit |
| **Automated workflows** | Figma Console MCP (write mode), Story UI, a2ui-bridge |
| **AI-enabled brand system (semantic)** | Figma Console MCP (token/variable management), FigmaLint |

---

## Workshops and Learning

- **AI & Design Systems course** — New online course from Brad Frost and Southleft. Practical, grounded in real work with large-scale teams. [Get early access](https://aianddesign.systems/)
- **Maven workshop: Doing More With Your Design System in Figma** — Hosted with Joey Banks (Baseline Design). Covers component structuring, Figma MCP integration, and Figma Make.
- **Storybook webinar: When AI Meets Design Systems** — How design systems give AI the context and structure it needs.
- **SuperFriendly talk: AI-Enabled Design Systems and Product Design** — How design systems are becoming more essential in the age of AI, not less.

---

## Key Takeaway

Southleft is the leading practitioner in the AI-enabled design systems space. Their open-source tooling directly addresses every pillar of our productionisation roadmap. The partnership gives us access to proven infrastructure (Figma Console MCP, Story UI, FigmaLint) and a path toward protocol-level AI integration (a2ui-bridge) — without building everything from scratch.
