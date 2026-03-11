# Agent-Driven UI — The Landscape

> AI agents are moving beyond text-only responses. The next frontier is agents that generate real, interactive interfaces at runtime. This document covers the concept, the major protocols and approaches, and what they mean for our roadmap.

---

## The Core Idea: Generative UI

Generative UI is the pattern where parts of a user interface are generated, selected, or controlled by an AI agent at runtime rather than being fully predefined by developers. Instead of an agent only returning text, it can render forms, tables, cards, dashboards, and task-specific UI based on context.

This matters because:

- Multi-step agent flows feel opaque when expressed only as chat messages
- User inputs are vague and hard to validate in free-text
- Tool execution and progress are hidden behind text responses
- The UI becomes a bottleneck when agents are capable of reasoning and acting

Generative UI turns the interface into an active part of agent execution — adapting as context changes, collecting structured input, and showing real progress.

---

## Three Patterns of Generative UI

The landscape has settled into three broad patterns, distinguished by how much control stays with the frontend versus how much freedom the agent has:

### 1. Static Generative UI (high control, low freedom)

Developers pre-build UI components. The agent only selects which component to show and fills it with data. Layout and interactions are fully owned by the application.

**Best for:** Product surfaces where brand consistency and design system compliance matter most. The agent is a smart router, not a designer.

### 2. Declarative Generative UI (shared control)

The agent returns a structured UI description (cards, lists, forms, widgets) as JSON. The frontend renders it using its own constraints, styling, and components. The agent has creative freedom within defined boundaries.

**Best for:** Dynamic experiences where the agent needs flexibility to compose UI, but the result must still render using your design system.

### 3. Open-ended Generative UI (low control, high freedom)

The agent returns a full UI surface (HTML, iframes, or free-form content). The frontend mainly acts as a container. Maximum flexibility, but you trade consistency and safety.

**Best for:** Complex tools, embedded third-party apps, and scenarios where the UI is too varied to pre-define.

---

## The Major Protocols and Approaches

### A2UI (Google)

**What it is:** An open protocol (Apache 2.0) that lets agents send declarative UI descriptions as streaming JSON. Clients render using their own native components. Falls into the "declarative" pattern.

**Key strengths:**
- Security-first: declarative JSON, not executable code. Agents can only reference pre-approved components from a trusted catalog
- LLM-friendly: flat, streaming JSON designed for incremental generation
- Framework-agnostic: same payload works across React, Angular, Flutter, Lit, native mobile
- Progressive rendering: UI streams in real-time

**Status:** v0.8 stable, v0.9 draft. 11,800+ GitHub stars. Created by Google with CopilotKit contributions. Public since December 2025.

**Core prerequisite:** Your design system must be in perfect parity with your code. a2ui references a component catalog — if that catalog doesn't match production, the output is meaningless.

- **Spec:** [a2ui.org](https://a2ui.org/)
- **Source:** [github.com/google/A2UI](https://github.com/google/A2UI)
- **Southleft's a2ui-bridge:** [github.com/southleft/a2ui-bridge](https://github.com/southleft/a2ui-bridge) — framework adapters connecting a2ui to real component libraries

---

### Vercel AI SDK — Generative UI

**What it is:** Vercel's approach to generative UI, built into their AI SDK. Rather than a standalone protocol, it's a toolkit integrated into the Next.js / React ecosystem. Supports both a "static" pattern (tool-based component rendering) and an experimental RSC streaming approach.

**Key strengths:**
- Deep React/Next.js integration — stream React Server Components directly from LLMs
- Tool-based architecture: each tool defines a Zod schema and a `generate` function that returns React components
- Production-tested AI SDK UI layer (hooks like `useChat`, `useCompletion`)
- Built from real experience shipping [v0.dev](https://v0.dev), Vercel's own generative UI product

**Status:** AI SDK 6 (December 2025). AI SDK UI is production-ready. AI SDK RSC (streaming React components) is still experimental. Vercel recommends AI SDK UI for production.

**Trade-offs:** React/Next.js-centric. Not framework-agnostic like a2ui. Best suited for teams already in the Vercel ecosystem. The `streamUI` approach ties you to React Server Components.

- **Docs:** [sdk.vercel.ai](https://sdk.vercel.ai/docs)
- **Generative UI intro:** [vercel.com/blog/ai-sdk-3-generative-ui](https://vercel.com/blog/ai-sdk-3-generative-ui)

---

### AG-UI Protocol (CopilotKit)

**What it is:** An open, lightweight protocol for real-time bi-directional communication between AI agent backends and user-facing applications. AG-UI is not a UI specification itself — it's the event/state layer that sits underneath UI specs like a2ui and Open-JSON-UI.

**Key strengths:**
- Bi-directional state sync between agent and application
- Supports all three generative UI patterns (static, declarative, open-ended)
- Human-in-the-loop workflows built in (approvals, input during agent execution)
- Adopted across major agent frameworks: LangGraph, CrewAI, Microsoft Agent Framework, Google ADK, PydanticAI
- Enterprise features: governance, analytics, guardrails against prompt injection

**Status:** Active, open-source. Oracle has adopted AG-UI for their Agent Spec.

- **Spec:** [copilotkit.ai/ag-ui](https://www.copilotkit.ai/ag-ui)
- **Source:** [github.com/ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)

---

### MCP Apps (Anthropic + OpenAI)

**What it is:** An extension to the Model Context Protocol (MCP) that enables interactive UI surfaces to render directly within AI chat applications. Jointly developed by Anthropic and OpenAI — a rare collaboration between competitors. Falls into the "open-ended" pattern.

**Key strengths:**
- Works across Claude, ChatGPT, Goose, VS Code, and other MCP-compatible clients
- External developers (Figma, Asana, Slack, etc.) build apps that agents can invoke
- Sandboxed HTML/JavaScript rendered in iframes for security
- Communication via JSON-RPC 2.0 over `postMessage`

**Status:** Released January 2026. Rapidly growing ecosystem.

**Trade-offs:** Web-only (iframe-based). Maximum flexibility but less design system control. The UI is authored by the MCP server, not constrained by your component catalog.

- **Spec:** [modelcontextprotocol.io/docs/extensions/apps](https://modelcontextprotocol.io/docs/extensions/apps)
- **OpenAI SDK:** [developers.openai.com/apps-sdk](https://developers.openai.com/apps-sdk/quickstart/)

---

### Open-JSON-UI (CopilotKit)

**What it is:** An open standardisation of OpenAI's internal declarative generative UI schema. Similar in concept to a2ui (declarative JSON describing UI), but with a different spec structure. Natively supported by CopilotKit's AG-UI protocol.

- **Docs:** [docs.copilotkit.ai/generative-ui/specs/open-json-ui](https://docs.copilotkit.ai/generative-ui/specs/open-json-ui)

---

## Comparison

| | A2UI | Vercel AI SDK | AG-UI | MCP Apps | Open-JSON-UI |
|---|---|---|---|---|---|
| **Pattern** | Declarative | Static + experimental RSC | Transport layer | Open-ended | Declarative |
| **By** | Google | Vercel | CopilotKit | Anthropic + OpenAI | CopilotKit |
| **Cross-platform** | Yes (React, Flutter, Angular, native) | React/Next.js only | Framework-agnostic | Web only (iframe) | Framework-agnostic |
| **Design system aware** | Yes (component catalog) | Yes (tool-defined components) | Depends on UI spec used | No (server-authored UI) | Yes (structured spec) |
| **Security model** | Pre-approved catalog, no code execution | Server-side rendering | Protocol-level guardrails | Sandboxed iframes | Spec-constrained |
| **Maturity** | Early (v0.8) | Production (AI SDK UI) / Experimental (RSC) | Active, adopted by Oracle | Released Jan 2026 | Early |
| **Best for** | Multi-platform, design-system-first products | React/Next.js apps in Vercel ecosystem | Underlying transport for any pattern | Embedding third-party tools in chat | Declarative alternative to a2ui |

---

## What This Means for Us

Regardless of which protocol we eventually adopt, the foundational work is the same. Every approach that generates UI from a design system requires:

1. **Semantic, structured design tokens** — machine-readable, not just human-readable
2. **Component catalog in parity with production code** — the system of record must match what ships
3. **Structured component metadata** — props, variants, states, documentation that agents can consume
4. **Token sync between Figma and code** — the source of truth can't drift

This is why our near-term priorities (AI-enabled semantic design system, token sync, component parity) are the critical path regardless of protocol choice. We are building the foundation that makes any of these approaches viable.

### Where we should pay attention

- **A2UI** is the most design-system-native option and aligns with Southleft's tooling (a2ui-bridge). Worth watching closely.
- **Vercel AI SDK** is relevant if our product engineering stack is React/Next.js. Production-ready today for the static pattern.
- **AG-UI** is a good bet as a transport layer — it doesn't lock you into a single UI spec.
- **MCP Apps** is relevant for embedding third-party experiences in agent interfaces, less so for generating UI from our own design system.

### The decision we don't need to make yet

We don't need to commit to a specific protocol now. The space is moving fast and will consolidate. What we do need to commit to is the foundational work that makes all of these approaches possible — and that work is already on our roadmap.

> By 2027, every design decision should be traceable, composable, and AI-augmentable. — Design × AI Roadmap
