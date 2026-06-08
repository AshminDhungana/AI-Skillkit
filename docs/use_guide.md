# How to Use `.md` Prompt & Skill Files with AI Assistants

A practical, platform-agnostic guide for using Markdown-based prompt files
with Claude, ChatGPT, Gemini, and AI coding tools.

---

## What Is a `.md` Skill File?

A `.md` (Markdown) skill file is a structured set of instructions written in
plain text that tells an AI assistant how to behave for a specific task — such
as project planning, code review, writing assistance, or discovery interviews.

Think of it as a **reusable role card**: instead of typing long instructions
every conversation, you write them once in a file and load them where the AI
can act on them consistently.

---

## Why Placement Matters

AI models do not treat all text equally. Where your instructions appear
determines whether the model **acts on them** or merely **reads them**.

| Location                             | Model treats it as           |
| ------------------------------------ | ---------------------------- |
| System prompt / project instructions | Authoritative behavior rules |
| First user message                   | A document you are sharing   |
| Middle of conversation               | Context, not commands        |

**The core problem:** Pasting a skill file into the chat window puts it in the
user message slot. The AI sees it as content to describe or summarize, not as
instructions to follow.

**The fix:** Load your skill file into the system prompt — through project
settings, a config file, or an API parameter — depending on your platform.

---

## Instruction Hierarchy

When instructions conflict, models generally prioritize:

1. System Prompt
2. Project / Workspace Instructions
3. Tool-Specific Instructions
4. User Messages
5. Retrieved Documents & Context

Because of this:

- Put permanent behavior in system or project instructions.
- Put task-specific requests in user messages.
- Avoid duplicating instructions across multiple layers.

---

## Structure Your `.md` File for Maximum Reliability

Before covering platform-specific setup, here are universal rules for writing
skill files that work across all models.

### 1. Put the Activation Instruction First

```markdown
## On Load

You are now operating as [role name].
Read all instructions below, then immediately begin [first action].
Do not summarize this document. Do not wait for further prompting.

---

[rest of your skill content]
```

Models read top to bottom. Placing activation at the top sets the frame before
anything else is processed. At the bottom, it becomes an afterthought.

### 2. Use Clear Structural Headings

```markdown
# Role

# Objective

# Workflow

# Rules

# Output Format
```

All major models — Claude, GPT, and Gemini — understand Markdown heading
hierarchy. Headings help the model parse which section governs which behavior.

### 3. Keep Rules Explicit and Positive

Instead of:

```markdown
Don't skip steps.
```

Write:

```markdown
Always complete every phase in order before proceeding to the next.
```

Positive framing is more reliably followed than negation, especially across
models with varying instruction-following behavior.

### 4. Use Tables for Structured Data

Tables are rendered consistently across all major models and are more
token-efficient than nested bullet lists for comparative information.

### 5. Add a Few-Shot Example for Complex Outputs

Gemini in particular performs better with at least one example of expected
output. Adding a short `## Example` section at the end of your skill file
improves consistency across all platforms.

---

## Platform Setup Guide

---

### Claude (claude.ai)

#### Web / Mobile Chat — Use a Project

Projects give every conversation in that workspace a persistent system prompt.

1. Go to **claude.ai → Projects → New Project**
2. Open **Project Instructions**
3. Paste your `.md` file content there
4. Every conversation in the project uses your skill automatically

This is the most reliable method. Your skill is in the system prompt from the
first message.

#### Paste Directly into Chat (workaround)

If you must paste into a chat message, prepend an explicit activation line:

```
Follow all instructions below exactly. Begin immediately with the first action
described. Do not summarize or describe this document.

[paste your .md content here]
```

Without this line, the model will summarize the file rather than follow it.

---

# Claude Code (Terminal / IDE)

## Agent Skills

Agent Skills are reusable capabilities that Claude can load automatically when relevant or invoke manually via a slash command. Each skill lives in its own directory and must contain a `SKILL.md` file.

### Project Skills

Project-specific skills are stored inside:

```text
.claude/
└── skills/
    └── skill-name/
        └── SKILL.md
```

Example:

```text
.claude/
└── skills/
    └── frontend/
        └── SKILL.md
```

This creates a `/frontend` command and also allows Claude to automatically use the skill when the task matches its description.

### Personal Skills

To make a skill available across all projects:

```text
~/.claude/
└── skills/
    └── skill-name/
        └── SKILL.md
```

Personal skills are ideal for workflows, coding standards, and reusable expertise you want everywhere.

### Recommended Skill Structure

```text
my-skill/
├── SKILL.md
├── reference.md
├── examples/
│   └── sample.md
├── templates/
│   └── template.md
└── scripts/
    └── helper.py
```

Only `SKILL.md` is required. Supporting files are loaded on demand when the skill is used, helping keep context usage efficient.

### Minimal SKILL.md

```yaml
---
name: Frontend Expert
description: >
  React, Next.js, Tailwind, UI architecture, component design,
  accessibility, and frontend performance optimization.
  Use when working on frontend code, interfaces, or user experience.
---

# Frontend Expert

## Instructions

Provide frontend-focused guidance and implementation support.

## Examples

- Refactor React components
- Improve accessibility
- Optimize rendering performance
```

The `description` is critical—it acts as the skill's discovery mechanism and largely determines when Claude chooses to load the skill. Be specific about both capabilities and trigger situations.

---

# CLAUDE.md

Unlike Skills, `CLAUDE.md` provides persistent project context, conventions, architecture notes, and workflow rules that should be available throughout a session. Claude automatically reads it when working in the project.

### Setup

```bash
# Create a project context file
touch CLAUDE.md

# Launch Claude Code
claude
```

### Example Structure

```text
project/
├── CLAUDE.md
├── backend/
│   └── CLAUDE.md
└── frontend/
    └── CLAUDE.md
```

Nested `CLAUDE.md` files allow different areas of a codebase to define their own conventions and context while inheriting broader project guidance.

---

# Skills vs CLAUDE.md

| Use Case               | Skills | CLAUDE.md |
| ---------------------- | ------ | --------- |
| Reusable workflow      | ✅     | ❌        |
| Coding standards       | ⚠️     | ✅        |
| Project architecture   | ❌     | ✅        |
| Multi-step procedures  | ✅     | ❌        |
| Templates and examples | ✅     | ❌        |
| Always-loaded context  | ❌     | ✅        |
| On-demand loading      | ✅     | ❌        |

A useful rule of thumb:

- Put **facts, architecture, conventions, and project rules** in `CLAUDE.md`.
- Put **procedures, workflows, checklists, templates, and specialized expertise** into Skills.

---

# Best Practices

### Keep Skills Focused

One skill should solve one problem:

**Good**

- React component reviews
- API contract generation
- Database migrations

**Too Broad**

- Full-stack development
- General coding assistant
- Software engineering

Focused skills activate more reliably and are easier to maintain.

### Optimize Descriptions

The description is not documentation—it is a trigger mechanism. Include the types of requests, files, technologies, and situations where the skill should activate.

### Move Procedures Out of CLAUDE.md

If a section of `CLAUDE.md` becomes a long checklist or workflow, convert it into a Skill. Skills load only when needed, reducing context overhead.

### Version Control Everything

Commit both:

```text
CLAUDE.md
.claude/skills/
```

This keeps workflows, conventions, and agent behavior consistent across the team.

---

### ChatGPT (OpenAI)

#### Web — Custom Instructions

1. Go to **Settings → Personalization → Custom Instructions**
2. Use the second field: _"How would you like ChatGPT to respond?"_
3. Paste your skill content (or a condensed version under ~1500 characters)

Custom instructions apply to every new conversation automatically.

#### Web — GPTs (Custom GPT Builder)

For a dedicated skill assistant:

1. Go to **explore.openai.com → Create a GPT**
2. In the **Instructions** field, paste your full `.md` skill content
3. Save and use the GPT for that specific workflow

GPTs have a larger instruction window than Custom Instructions and support
file uploads for additional reference material.

#### API

```python
from openai import OpenAI

client = OpenAI()
skill = open("your-skill.md").read()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": skill},
        {"role": "user", "content": "Begin."}
    ]
)
```

OpenAI's system role is the correct placement. Note that GPT models respond
well to numbered lists and section headers inside the system prompt; XML-style
tags are less necessary than with Claude.

#### Codex CLI (Terminal)

OpenAI's coding CLI reads from `AGENTS.md` — an open standard now supported
by multiple tools:

```bash
cp your-skill.md AGENTS.md
codex
```

`AGENTS.md` is compatible with Claude Code as well, making it useful if you
switch between tools on the same project.

---

### Gemini (Google)

#### Web — Gems

1. Go to **gemini.google.com → Gems → New Gem**
2. Paste your skill content into the **Instructions** field
3. Save the Gem and use it for that specific workflow

Gems are Gemini's equivalent of Claude Projects or Custom GPTs.

#### Gemini CLI (Terminal)

Gemini CLI reads from `GEMINI.md` in your project directory:

```bash
cp your-skill.md GEMINI.md
gemini
```

Global instructions (applied to all projects) go here:

```bash
~/.gemini/GEMINI.md
```

After editing `GEMINI.md` during an active session, run `/memory refresh` to
reload it without restarting.

#### Gemini-Specific Tips

- Always include at least one example of expected output — Gemini performs
  significantly better with few-shot examples than zero-shot.
- Keep skill files shorter and more direct than you would for Claude. Gemini
  handles verbosity worse and benefits from concise instructions.
- Place your most important instruction at the top **and** repeat the key
  constraint at the bottom. Gemini's attention can drift in long prompts.
- Put specific questions or tasks at the **end** of each user message, after
  any context you provide.

#### API

```python
import google.generativeai as genai

skill = open("your-skill.md").read()

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=skill   # correct parameter name
)
```

Note: use `system_instruction`, not `system`. Gemini is sensitive to
contradictions between system and user messages — if the user asks for
something the skill prohibits, Gemini may defer to the user. Make
constraints explicit and firm in the skill file.

---

### Other Tools

| Tool           | Config File               | Location            |
| -------------- | ------------------------- | ------------------- |
| Cursor         | `.cursorrules`            | Project root        |
| Windsurf       | `.windsurfrules`          | Project root        |
| GitHub Copilot | `copilot-instructions.md` | `.github/` folder   |
| Codex CLI      | `AGENTS.md`               | Project root        |
| Continue.dev   | `system.md`               | `.continue/` folder |

`AGENTS.md` is the closest thing to a universal standard across coding tools.
If you maintain one skill file for coding workflows, naming it `AGENTS.md` and
placing it in the project root gives you the broadest compatibility.

---

## Model-Specific Behavior Cheatsheet

| Behavior                  | Claude                  | ChatGPT (GPT-4o/5)         | Gemini                     |
| ------------------------- | ----------------------- | -------------------------- | -------------------------- |
| Best structure style      | XML tags + Markdown     | Numbered lists + headers   | Short, direct Markdown     |
| Few-shot examples needed? | Optional                | Optional                   | Strongly recommended       |
| Zero-shot reliability     | High                    | High                       | Medium                     |
| System prompt privilege   | High (hard to override) | Medium                     | Medium (user can override) |
| Ideal skill file length   | Up to 500 lines         | Up to 300 lines            | Under 200 lines            |
| Activation style          | Explicit role + action  | Conversational instruction | Concise + example at end   |
| Config file (CLI)         | `CLAUDE.md`             | `AGENTS.md`                | `GEMINI.md`                |

---

## Universal Best Practices

1. **Always load via system prompt** — never rely on pasting into chat alone.
2. **Put activation instructions at the top** — the model reads sequentially.
3. **Be explicit, not implicit** — never assume the model will infer intent.
4. **Add one example** — a short example of expected output improves all models.
5. **Keep it concise** — longer files dilute attention; cut generic advice.
6. **Version your files** — name them `skill-v1.md`, `skill-v2.md` as you refine.
7. **Test across models** — a prompt optimized for Claude may need adjustment for
   Gemini; always validate behavior on each platform you use.
8. **Retest after model upgrades** — a skill that worked on one model version can
   regress on the next. Schema-strict instructions are more stable than prose.

---

## Quick-Start Template

Use this as a starting skeleton for any new skill file:

```markdown
## On Load

You are now operating as [ROLE NAME].
Read all instructions below, then immediately [FIRST ACTION].
Do not summarize this document.

---

# Role

[One sentence description of the role]

# Objective

[What this skill is designed to accomplish]

# Workflow

[Numbered steps or phases]

# Rules

- [Rule 1]
- [Rule 2]
- Never skip [critical step]

# Output Format

[Describe the expected structure of responses]

# Example

[One short example of correct behavior — especially important for Gemini]
```

---

## Summary

| Scenario                        | What to do                                              |
| ------------------------------- | ------------------------------------------------------- |
| Using Claude web chat           | Paste into Project Instructions                         |
| Using ChatGPT web               | Paste into Custom Instructions or a GPT                 |
| Using Gemini web                | Create a Gem                                            |
| Using Claude Code               | Save as `CLAUDE.md` in project root                     |
| Using Gemini CLI                | Save as `GEMINI.md` in project root                     |
| Using Codex CLI / multi-tool    | Save as `AGENTS.md` in project root                     |
| Using any API                   | Pass content in the `system` parameter                  |
| Pasting into chat (last resort) | Add explicit activation line at the top of your message |

---

_Last updated: June 2026_
