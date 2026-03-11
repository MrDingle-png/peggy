# Setting up Claude Co-work with your knowledge and skills

This guide explains how to bring your Fanatics Collect knowledge base and specialist skills into a Claude Co-work project.

## Create a new project

1. Open Claude and create a new Project
2. Name it something descriptive: "Fanatics Collect — Product Brain"

## Set custom instructions

Paste the contents of `AGENTS.md` into the project's Custom Instructions field. This gives the agent your identity, rules, and code generation process.

For deeper context, also paste the contents of `BOOTSTRAP.md` below the AGENTS.md content. This gives the agent your full knowledge map and specialist skill descriptions.

## Upload knowledge files

Upload the most relevant files from the `Knowledge/` folder as Project Knowledge. You do not need to upload everything — start with the files most relevant to your current work.

### Recommended starting set

| File | Why |
|------|-----|
| `GOALS.md` | Current priorities |
| `Knowledge/Quests/collector-quests-strategy-v5.md` | Active strategic bet |
| `Knowledge/Quests/quest-infrastructure-prd-the-grail.md` | Quest infrastructure PRD |
| `Knowledge/Programs & Quests/programs-vs-quests-building-blocks.md` | Building blocks framework |
| `Knowledge/Reference Taxonomy/collections-glossary.md` | Shared terminology |
| `Knowledge/Experience Framework/collections.md` | UX framework |

### Adding more context over time

As conversations shift to other topics, upload the relevant knowledge files. The knowledge map in BOOTSTRAP.md tells you which files cover which topics.

## Using specialist skills

Claude Co-work does not have a skills system like Cursor or Claude Code. Instead, paste the relevant `SKILL.md` content into the conversation or custom instructions when you need a specialist perspective.

### Quick method

Tell Claude which specialist mode you want:

- "Think like a backend engineer about this problem" — then paste `~/.ai-skills/backend-engineering/SKILL.md`
- "Help me write UX copy for this screen" — then paste `~/.ai-skills/ux-copy/SKILL.md`
- "Review this from a product design perspective" — then paste `~/.ai-skills/product-design/SKILL.md`

### Alternative: add skills to custom instructions

If you are working in a specific mode for an extended period (e.g., a week of backend architecture work), paste the relevant SKILL.md into the project's Custom Instructions alongside AGENTS.md. Remove it when you shift focus to keep context lean.

## Code generation safety

If using Claude Co-work to generate code, include the safe-coding rules from `AGENTS.md` in your custom instructions. Claude Co-work cannot create branches or run git commands, so you will need to handle branch management yourself. The key rules:

1. Ask the agent to explain the approach before generating code
2. Create a new branch locally before applying any generated code
3. Review the code before committing

## Keeping knowledge fresh

When you update files in the Peggy repo, re-upload the changed files to your Claude Co-work project. The repo is the source of truth — Claude Co-work project knowledge is a snapshot.
