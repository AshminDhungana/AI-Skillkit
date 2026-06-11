<div align="center">

# 🧠 AI-Skillkit

**A modular library of battle-tested AI skills for solo developers and multi-agent teams.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![Works With](https://img.shields.io/badge/Works%20With-Claude%20%7C%20Cursor%20%7C%20Copilot%20%7C%20Gemini%20%7C%20Codex-blue)](https://github.com/AshminDhungana/AI-Skillkit)

</div>

---

> _AI agents are only as good as the instructions they follow._

AI-Skillkit is a curated collection of structured markdown prompts — called **skills** — that transform general-purpose AI coding agents into disciplined, domain-expert engineers. Each skill encodes a real workflow: phase-locked steps, verification gates, anti-pattern guards, and clear output contracts. Unlike throwaway prompts, skills are designed to compose — one skill's output becomes the next skill's input, enabling complex, production-grade workflows across both solo developers and coordinated multi-agent teams.

---

## Table of Contents

- [What Are Skills?](#-what-are-skills)
- [Why It Matters](#-why-it-matters)
- [Key Features](#-key-features)
- [Repository Structure](#️-repository-structure)
- [Quick Start](#-quick-start)
- [Anatomy of a Skill](#-anatomy-of-a-skill)
- [Usage Patterns](#-usage-patterns)
- [Sector Roadmap](#-sector-roadmap)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🧠 What Are Skills?

A **skill** is a self-contained capability package — a structured markdown file that gives an AI agent specialized knowledge, a step-by-step workflow, and a defined output contract for a specific type of task.

Think of each skill as an expert's onboarding guide for a narrow domain:

```
Without a skill → Generic agent → Inconsistent, token-heavy, directionless output
With a skill    → Expert agent  → Structured, verifiable, composable output
```

Skills follow a simple but powerful pattern: **read → reason → produce**. They tell the agent exactly what context to consume, how to think through the problem, and what to deliver — nothing more, nothing less.

Skills can be chained in sequence: the output of one skill becomes the structured input to the next, enabling sophisticated multi-step automation without complex orchestration frameworks.

---

## 💡 Why It Matters

Modern AI agents fail not because the models are weak, but because the instructions are vague. Research in prompt engineering consistently shows that <a href="https://www.techvoot.com/blog/prompt-engineering-best-practices">structured, detailed prompts dramatically reduce hallucinations, improve accuracy, and keep outputs aligned with real goals</a>. Production teams building agentic systems at scale have found that <a href="https://www.uipath.com/blog/ai/agent-builder-best-practices">single-responsibility agents with narrow, well-defined scopes outperform broad, general-purpose ones</a> in every measurable way.

AI-Skillkit operationalizes these findings. Instead of re-engineering prompts from scratch for every project, you get a growing library of skills that encode proven workflows, edge-case handling, and domain best practices — ready to drop into any AI-powered toolchain.

---

## ✨ Key Features

**🔗 Chainable workflows** — Skills are composable by design. Each skill defines what it consumes and what it produces, so they chain naturally without glue code.

**🔄 Multi-agent ready** — Skills support solo use, two-agent handoffs, and full multi-agent coordination patterns out of the box.

**📋 Phase-locked execution** — Every skill specifies discrete phases: what to read, how to reason, what to verify, and what to output. No ambiguity, no drift.

**🎯 Selective activation** — Load only the skills a task actually needs. This keeps agent context lean, focused, and accurate — avoiding the token bloat that degrades performance.

**📚 Battle-tested** — Each skill encodes real workflows from real projects, not theoretical best practices. Anti-patterns are documented; verification gates are included.

**🌍 Cross-platform compatible** — Works with Claude Code, Cursor, GitHub Copilot, Gemini CLI, OpenAI Codex, and any agent that can read a markdown file into its context.

**🧩 Progressive disclosure** — Lightweight metadata (name + description) surfaces first; full instructions load only when the skill is triggered. Agents stay efficient.

---

## 🏗️ Repository Structure

```
AI-Skillkit/
│
├── data-analysis-skills/        # Data cleaning, EDA, statistical modelling, visualization
├── development-skills/          # Code review, debugging, testing, refactoring
├── document-skills/             # PDF generation, Markdown conversion, document templating
├── full-stack-dev/              # Project planning, frontend/backend design, todo creation
├── health-and-lifesciences-skills/
├── learning-and-knowledge-skills/  # Spaced repetition, summarization, knowledge extraction
├── max-token-use-skills/        # High-detail, maximum-quality skills (token-intensive)
├── media-and-content-skills/    # Image generation, video scripting, social media content
├── min-token-use-skills/        # Fast, efficient skills optimized for low token usage
├── miscellaneous-collection/    # Experimental and uncategorized skills
├── preformance-improvement-skills/ # Performance Improvement Skills
├── refrence-for-ai-skills-designs/ # Design.md Files
├── scientific-skills/           # LaTeX documents, simulations, data-driven research
├── ui-ux-skills/                # Wireframing, accessibility, component design
├── utilities/                   # File ops, data conversion, system automation
├── writing-research-skills/     # Academic writing, peer review, grant proposals
│
├── docs/                        # Usage guides and examples
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

Each sector folder contains:

- A `README.md` explaining the skills in that sector and how to chain them
- Individual `*.md` skill files (active or planned)
- Skills can be used independently or composed across sector boundaries

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/AshminDhungana/AI-Skillkit.git
cd AI-Skillkit
```

### 2. Pick a skill

```bash
cat full-stack-dev/01-initial-project-planning-skill.md
```

### 3. Load it into your agent

**Claude Code / Cursor:**

```bash
cp full-stack-dev/frontend-design-skill.md ~/.claude/skills/
# or
cp full-stack-dev/frontend-design-skill.md .cursor/rules/
```

**Chat interface (Claude, ChatGPT, Gemini):**
Paste the skill content as the system prompt before your task.

**Custom agent / script:**

```python
skill = open("full-stack-dev/research-driven-planning-skill.md").read()
agent.set_context(skill)
agent.run(task)
```

### 4. Chain skills for complex workflows

```
01-initial-project-planning-skill.md
    ↓ outputs: requirements doc
02-research-driven-planning-skill.md
    ↓ outputs: technical design
03-frontend-design-skill.md
    ↓ outputs: component structure + styled UI
```

Each skill's output is structured to be the next skill's input — no manual bridging required.

---

## 📝 Anatomy of a Skill

Every skill is a markdown file with a YAML frontmatter block and a structured instruction body:

```markdown
---
name: frontend-design
description: >
  UI/UX design workflow covering component structure, styling conventions,
  and accessibility verification. Trigger when designing or implementing
  any frontend feature.
---

# Frontend Design Skill

## When to use this skill

Clear conditions that activate this skill — specific task types,
input signals, or prior skill outputs that indicate it's needed.

## Input format

What this skill expects: either user-provided context or the structured
output from a preceding skill.

## Workflow

### Phase 1 — Research & Understand

Step-by-step instructions for analyzing the input and gathering context.

### Phase 2 — Plan & Design

Checkpoints, decision criteria, and structured planning steps.

### Phase 3 — Execute & Verify

Build instructions with mandatory verification gates and quality checks.

## Anti-patterns to avoid

Documented failure modes and how to sidestep them.

## Output format

Exactly what this skill must produce — structured so the next skill
in the chain can consume it without transformation.

## Edge cases

How to handle ambiguous requirements, missing inputs, or conflicting signals.
```

The YAML frontmatter (name + description) is what surfaces in agent registries and IDE rule-loaders. Full instructions load only when the skill is activated.

---

## 🔧 Usage Patterns

For more detailed instructions, see the [Use Guide](docs/use_guide.md).

### With AI Code Editors

Reference a skill file in your prompt to anchor the agent's behavior:

```
"Build the new analytics dashboard.
Review full-stack-dev/frontend-design-skill.md before generating any code."
```

Or install skills as permanent rules in your IDE:

```bash
# Claude Code
cp writing-research-skills/*.md ~/.claude/skills/

# Cursor
cp development-skills/*.md .cursor/rules/
```

### With Autonomous Agents

Give your agent access to the skill registry. When a task matches a skill's trigger conditions, the agent reads the relevant file into context before executing:

```python
import os

def load_skill(name: str) -> str:
    path = f"skills/{name}/SKILL.md"
    return open(path).read() if os.path.exists(path) else ""

skill = load_skill("data-analysis")
agent.inject_context(skill)
agent.run(task)
```

### As Human SOPs

Every skill is written in clear, checklist-style markdown — which makes it equally useful as:

- **Onboarding documentation** for new team members joining a project
- **PR review checklists** for domain-specific code quality standards
- **Engineering runbooks** for recurring workflows that need consistent execution

---

## 🌍 Sector Roadmap

| Sector                | Status     | Description                                                                               |
| --------------------- | ---------- | ----------------------------------------------------------------------------------------- |
| 🖥️ **full-stack-dev** | ✅ Active  | Project planning, todo creation, research-driven design, frontend/backend workflows       |
| 📊 **data-analysis**  | ✅ Active  | Data cleaning, exploratory analysis, statistical modelling, visualization                 |
| 💻 **development**    | ✅ Active  | Code review, debugging, testing, refactoring, performance analysis                        |
| 📄 **document**       | ✅ Active  | PDF generation, Markdown conversion, Office document templating                           |
| 🧠 **learning**       | ✅ Active  | Spaced repetition, summarization, knowledge graph extraction                              |
| 🎨 **media**          | ✅ Active  | Image generation prompts, video scripts, social media content creation                    |
| 🔬 **scientific**     | ✅ Active  | LaTeX documents, simulation workflows, data-driven research                               |
| ✍️ **writing**        | ✅ Active  | Academic writing, peer review, grant proposals, technical documentation                   |
| 🎨 **frontend**       | 📅 Planned | UI component design, accessibility audits, responsive layout, framework-specific patterns |
| 🔧 **backend**        | 📅 Planned | API design, database schema, security hardening, performance optimization                 |
| 🐳 **devops**         | 📅 Planned | CI/CD pipelines, infrastructure as code, monitoring, container orchestration              |
| 🤖 **AI/ML**          | 📅 Planned | Model selection, training pipelines, evaluation frameworks, deployment                    |
| 🔒 **security**       | 📅 Planned | Threat modelling, secure code review, compliance checklists                               |
| 📦 **product**        | 📅 Planned | Requirements gathering, user story mapping, roadmap planning                              |
| 💼 **business**       | 📅 Planned | Financial modelling, market research, competitive analysis                                |

All sectors follow the same standardized skill structure — consistent experience regardless of domain.

---

## 🤝 Contributing

This is a personal library, but contributions are welcome.

1. **Fork** the repository
2. **Create** a new sector folder or add skill files to an existing sector
3. **Follow** the skill anatomy (YAML frontmatter + phased instruction body)
4. **Update** the sector's `README.md` with your new skill
5. **Submit** a pull request

For full contribution guidelines, see [`CONTRIBUTING.md`](./CONTRIBUTING.md).

**Good skill contributions:**

- Encode a real workflow you've actually used in production
- Include at least one documented anti-pattern or edge case
- Define a clear, structured output format that downstream skills can consume

---

## 📄 License

Licensed under the **[MIT License](./LICENSE)**.

---

<div align="center">

_Built by developers, for agents._

**AI-Skillkit — Skills that scale. From solo to swarm.**

</div>
