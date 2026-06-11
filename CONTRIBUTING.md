# Contributing to AI-Skillkit

First off, thank you for considering contributing to AI-Skillkit.

AI-Skillkit exists to build a high-quality, community-driven library of reusable AI skills that improve the reliability, consistency, and effectiveness of AI agents. Every contribution helps expand the collection of proven workflows available to developers, researchers, and agent builders worldwide.

Whether you're fixing documentation, improving an existing skill, or contributing a completely new workflow, your contributions are welcome.

---

# Table of Contents

- Code of Conduct
- Ways to Contribute
- Before You Start
- Skill Design Standards
- Creating a New Skill
- Updating an Existing Skill
- Repository Structure
- Pull Request Process
- Quality Checklist
- Style Guidelines
- Reporting Issues
- License

---

# Code of Conduct

Please be respectful and constructive in all interactions.

We welcome contributors from all backgrounds and experience levels. Discussions should remain professional, technical, and focused on improving the project.

Unacceptable behavior includes:

- Harassment or discrimination
- Personal attacks
- Spam or promotional content
- Intentionally misleading information
- Low-effort AI-generated submissions without review

---

# Ways to Contribute

You can contribute by:

### Adding New Skills

Create new skills that encode proven workflows for AI agents.

Examples:

- Software development workflows
- Research workflows
- Scientific analysis workflows
- Writing and documentation workflows
- Data analysis workflows
- Productivity and automation workflows

### Improving Existing Skills

Help improve:

- Accuracy
- Structure
- Verification steps
- Edge-case handling
- Anti-pattern documentation
- Output contracts

### Documentation

Improve:

- README files
- Examples
- Usage guides
- Skill explanations
- Installation instructions

### Bug Reports

Report:

- Broken references
- Incorrect instructions
- Missing dependencies
- Ambiguous workflow definitions

---

# Before You Start

Before opening a pull request:

1. Search existing issues and pull requests.
2. Verify that your contribution does not duplicate existing work.
3. Read the repository README.
4. Follow the skill structure used throughout the project.
5. Ensure your contribution represents a workflow you understand well.

The best skills come from real-world experience, not theoretical prompting techniques.

---

# Skill Design Philosophy

A skill should do one thing well.

Skills should be:

- Focused
- Reusable
- Verifiable
- Composable
- Platform-agnostic

A skill is not:

- A generic prompt
- A personality preset
- A roleplay instruction
- A collection of unrelated tasks

The goal is to encode repeatable expertise.

---

# Creating a New Skill

## Step 1: Choose the Correct Sector

Place your skill inside the most relevant sector folder.

Examples:

| Domain               | Folder                  |
| -------------------- | ----------------------- |
| Debugging            | development-skills      |
| Statistical Analysis | data-analysis-skills    |
| Academic Writing     | writing-research-skills |
| UI Design            | ui-ux-skills            |
| Scientific Research  | scientific-skills       |

If no suitable sector exists, open an issue before creating a new category.

---

## Step 2: Follow the Standard Skill Structure

Every skill must contain YAML frontmatter.

Example:

```yaml
---
name: api-design-review
description: >
  Reviews API architecture, validates contracts,
  identifies design flaws, and produces actionable recommendations.
---
```

Then use a structured workflow format.

Recommended sections:

```markdown
# Skill Name

## When to Use

## Input Requirements

## Workflow

### Phase 1 — Understand

### Phase 2 — Analyze

### Phase 3 — Verify

### Phase 4 — Produce

## Anti-Patterns

## Edge Cases

## Output Format
```

---

## Step 3: Define Clear Inputs

The skill should clearly state:

- What information it expects
- Required context
- Optional context
- Expected format

Agents should not have to guess.

---

## Step 4: Define a Repeatable Workflow

Workflows should be phase-based.

Good example:

```text
Read
↓
Analyze
↓
Verify
↓
Produce
```

Avoid vague instructions such as:

```text
Think deeply.
Do your best.
Use judgment.
```

Instead, provide explicit steps.

---

## Step 5: Add Verification Gates

Strong skills verify their own output.

Examples:

- Requirements coverage checks
- Security validation
- Edge-case review
- Consistency checks
- Reference verification

Verification should happen before output generation whenever possible.

---

## Step 6: Document Anti-Patterns

Every skill should describe common failure modes.

Example:

```markdown
## Anti-Patterns

- Skipping stakeholder requirements
- Optimizing before measuring
- Generating implementation details before planning
```

This significantly improves agent reliability.

---

## Step 7: Define an Output Contract

Specify exactly what the skill should produce.

Example:

```markdown
## Output Format

1. Findings Summary
2. Risk Assessment
3. Recommendations
4. Action Items
```

Structured outputs make skills chainable.

---

# Updating Existing Skills

When modifying an existing skill:

- Preserve backward compatibility when possible
- Avoid changing established output contracts unnecessarily
- Explain major workflow changes in the pull request
- Ensure new instructions do not conflict with existing phases

Large redesigns should be discussed in an issue first.

---

# Repository Structure

Example:

```text
sector/
├── README.md
├── skill-a.md
├── skill-b.md
└── skill-c.md
```

Sector README files should be updated whenever:

- New skills are added
- Skills are removed
- Skill names change

---

# Pull Request Process

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-skill
```

3. Commit your changes.

```bash
git commit -m "Add API design review skill"
```

4. Push your branch.

```bash
git push origin feature/new-skill
```

5. Open a Pull Request.

Please include:

- Purpose of the contribution
- Problem being solved
- Sector affected
- Example use case
- Any breaking changes

---

# Quality Checklist

Before submitting, verify:

- [ ] Skill has valid YAML frontmatter
- [ ] Name is unique and descriptive
- [ ] Description clearly explains purpose
- [ ] Workflow is phase-based
- [ ] Inputs are documented
- [ ] Outputs are documented
- [ ] Anti-patterns are included
- [ ] Edge cases are considered
- [ ] Formatting is consistent
- [ ] Markdown renders correctly
- [ ] Sector README has been updated if needed

---

# Style Guidelines

## Writing Style

Use:

- Clear language
- Action-oriented instructions
- Explicit requirements
- Consistent terminology

Avoid:

- Ambiguous wording
- Excessive verbosity
- Marketing language
- Model-specific assumptions

---

## Platform Compatibility

Skills should work across:

- Claude Code
- Cursor
- GitHub Copilot
- Gemini
- OpenAI Codex
- Other markdown-capable AI agents

Avoid instructions that depend on a single vendor unless the skill explicitly targets that platform.

---

# Reporting Issues

When reporting an issue, include:

### Bug Reports

- Skill name
- Expected behavior
- Actual behavior
- Reproduction steps

### Improvement Suggestions

- Current limitation
- Proposed improvement
- Example workflow

Clear reports help maintain quality across the skill library.

---

# License

By contributing to AI-Skillkit, you agree that your contributions will be licensed under the same MIT License that governs this repository.

---

Thank you for helping build a better ecosystem of reusable AI skills.

**Build workflows. Encode expertise. Scale intelligence.**
