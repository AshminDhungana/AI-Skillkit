# 🧠 AI-Skillkit

> **A personal library of reusable AI skills for any task.**
> Each skill is a structured, phase-locked prompt that tells the AI exactly what to do, what to read, and what to produce—chaining together for solo or multi-agent workflows.

AI agents are only as good as the instructions they follow. **AI-Skillkit** is a curated, battle-tested library of structured markdown prompts (skills) that transform AI coding agents into disciplined, production-ready engineers. Unlike generic prompts, these skills encode **actual workflows** with steps, checkpoints, verification gates, and anti-pattern guards.

Skills act as "onboarding guides" for specific domains or tasks, transforming a general-purpose AI agent into an expert with specialized procedural knowledge.

---

## 📖 Table of Contents

- [🧠 What Are Skills?](#-what-are-skills)
- [✨ Key Features](#-key-features)
- [🏗️ Repository Structure](#️-repository-structure)
- [⚡ Quick Start](#-quick-start)
- [📝 Anatomy of a Skill](#-anatomy-of-a-skill)
- [🔧 Using This Repository](#-using-this-repository)
  - [With AI Code Editors (Cursor, Claude Code, etc.)](#with-ai-code-editors-cursor-claude-code-etc)
  - [With Autonomous Agents / Custom GPTs](#with-autonomous-agents--custom-gpts)
  - [As Human SOPs](#as-human-sops)
- [🌍 Sector Roadmap](#-sector-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🧠 What Are Skills?

A **skill** is a modular, self-contained capability package that extends an AI agent's capabilities by providing specialized knowledge, workflows, and tools. At its core, a skill is a folder containing a `SKILL.md` file with metadata (`name` and `description`) and instructions that tell an agent how to perform a specific task.

Skills can be chained together—one skill's output becomes the next skill's input—enabling complex, multi-step workflows across both **solo developers** and **multi-agent teams**.

---

## ✨ Key Features

- **🔗 Chainable workflows** — Use skills sequentially; each skill's output feeds directly into the next skill as input.
- **🔄 Multi-agent ready** — Built-in support for single, two-developer, and multi-agent coordination.
- **📋 Phase-locked** — Each skill specifies exactly what it does, what to read, and what to produce.
- **🎯 Task‑specific** — Activate only the skills you need, avoiding token bloat and maintaining AI focus.
- **📚 Battle‑tested** — Every skill encodes proven workflows, best practices, and domain expertise.
- **🌍 Cross‑product compatible** — Works across Claude Code, Cursor, GitHub Copilot, Gemini CLI, OpenAI Codex, and more.
- **🧩 Progressive disclosure** — Lightweight metadata first, full instructions only when triggered.

---

## 🏗️ Repository Structure

```
AI-Skillkit/
├── README.md                     # This file
├── full-stack-dev/               # 🖥️ FULL‑STACK DEVELOPMENT SECTOR
│   ├── README.md                 # Sector‑specific usage guide
│   ├── 01-initial-project-planning-skill.md
│   ├── 2.1-onedev-todo-creation-skill.md
│   ├── 2.2-twodev-todo-creation-skill.md
│   ├── 2.3-multidev-todo-creation-skill.md
│   ├── 3-research-driven-planning-skill.md
│   ├── 4.1-onedev-workflow-skill.md
│   ├── 4.2-twodev-workflow-skill.md
│   ├── 4.3-multidev-workflow-skill.md
│   ├── 5-frontend-design-skill.md
│   └── 6-backend-design-skill.md
│
├── max-token-use-skills         # Will Use more token best result
├── reduce-token-use-skills      # Will Use less token good result
├── ui-ux-skills                 # ui/ux design skill
├── utilities                    # Utilities skills
├── miscellaneous-collection     # A whole world inside, massive collection
│
├── [future-sectors]/             # 🚧 Coming soon: frontend, backend, DevOps, AI/ML, security, product management, etc.
│   └── ...
├── CONTRIBUTING.md               # Guidelines for adding new skills
└── LICENSE                       # MIT License
```

Each **sector** folder contains:

- A sector‑specific `README.md` explaining how to use its skills.
- Individual `*.md` skill files (created / planned).
- Skills can be used alone or chained together within and across sectors.

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/AshminDhungana/AI-Skillkit.git
cd AI-Skillkit
```

### 2. Pick a skill

```bash
cat full-stack-dev/initial-project-planning-skill.md
```

### 3. Load it into your AI agent

- **Claude Code / Cursor** → Copy the content into `CLAUDE.md` or `.cursor/rules/`.
- **Custom agent** → Read the `SKILL.md` (or sector skill file) into the agent's context before task execution.
- **Chat interface** → Paste the skill content as a system prompt.

### 4. Chain multiple skills

Use the output of one skill as the input for the next. Example workflow:

```
initial-project-planning-skill.md → research-driven-planning-skill.md → frontend-design-skill.md
```

---

## 📝 Anatomy of a Skill

Every skill is a markdown file (e.g., `frontend-design-skill.md`) that follows the Agent Skills specification:

```markdown
---
name: frontend-design
description: UI/UX design workflow with component structure, styling approach, and accessibility checks. Use when designing or implementing frontend features.
---

# Frontend Design Skill

## When to use this skill

[Clear conditions that trigger this skill]

## Input format

[What this skill expects to receive from a previous skill or user]

## Workflow

1. Step‑by‑step instructions
2. Checkpoints and verification gates
3. **Mandatory sections** (e.g., research, planning, execution)
4. **Output format** (what to produce)

## Best Practices

- Do's and don'ts
- Anti‑pattern examples to avoid

## Output format

[Exactly what this skill must produce, often linked to the next skill's expected input]

## Common edge cases

- How to handle ambiguous requirements
```

---

## 🔧 Using This Repository

For more detailed instructions, see the [Use Guide](docs/use_guide.md).

### With AI Code Editors (Cursor, Claude Code, etc.)

When asking your IDE to perform a task, reference the relevant skill file to strictly guide the AI's output:

> _"I need to build a new dashboard page. Please review `full-stack-dev/frontend-design-skill.md` before generating the code."_

Or install the skill into your IDE's rules directory:

```bash
# For Claude Code
cp full-stack-dev/frontend-design-skill.md ~/.claude/skills/

# For Cursor
cp full-stack-dev/frontend-design-skill.md .cursor/rules/
```

### With Autonomous Agents / Custom GPTs

Provide the repository structure or a `registry.json` to your agent. When a task matches a skill, the agent can read the relevant file into its context **before** executing.

```python
skill_content = read_file("full-stack-dev/research-driven-planning-skill.md")
execute_workflow(skill_content)
```

### As Human SOPs

Because each skill is written in clear, checklist‑style markdown, it doubles perfectly as:

- Onboarding documentation for new team members
- PR review checklists
- Team engineering standards

---

## 🌍 Sector Roadmap

Skills will be added progressively across multiple domains. Each sector will contain specialized skills for its domain, all following the same standardized format.

| Sector                | Status     | Description                                                                        |
| --------------------- | ---------- | ---------------------------------------------------------------------------------- |
| 🖥️ **full-stack-dev** | ✅ Started | Initial planning, todo creation, research, and frontend/backend design.            |
| 🎨 **frontend**       | 📅 Planned | UI component design, accessibility, responsive layouts, framework‑specific skills. |
| 🔧 **backend**        | 📅 Planned | API design, database schema, security hardening, performance optimization.         |
| 🐳 **devops**         | 📅 Planned | CI/CD pipelines, infrastructure as code, monitoring, container orchestration.      |
| 🤖 **AI/ML**          | 📅 Planned | Model selection, training pipelines, evaluation, deployment.                       |
| 🔒 **security**       | 📅 Planned | Threat modeling, secure code review, compliance checks.                            |
| 📦 **product**        | 📅 Planned | Requirement gathering, user story mapping, roadmap planning.                       |
| 💼 **business**       | 📅 Planned | Financial modeling, market research, sales strategies.                             |

Each sector will mirror the same skill structure, ensuring a consistent experience across all domains.

---

## 🤝 Contributing

This repository is a **personal library**, but contributions are welcome!

### Quick guidelines:

1. **Fork** the repository.
2. **Create** a new folder for a new sector, or add skill files to an existing sector.
3. **Follow** the skill anatomy (YAML frontmatter + markdown instructions).
4. **Update** the sector's `README.md` with your new skill.
5. **Submit** a pull request.

For full guidelines, see [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## 📄 License

Licensed under the **MIT License**.

---

_Built by developers, for agents._  
**AI-Skillkit — Skills that scale. From solo to swarm.**
