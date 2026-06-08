# Documentation Standards

## Core Principles

### **1. Living Documentation**
- Documentation stays current with code
- Update docs in the same PR as code changes
- Living docs (README, CLAUDE, AGENTS) updated regularly
- Outdated information removed promptly

### **2. Clarity & Accessibility**
- Write for beginners, not experts
- Use simple, clear language
- Provide examples for all concepts
- Include troubleshooting sections

### **3. Structure & Consistency**
- Follow established templates
- Use consistent formatting
- Maintain clear hierarchy
- Keep related content together

## File Naming Conventions

### **General Rules**

```yaml
# Markdown files
README.md           # Repository root (UPPERCASE)
CLAUDE.md           # Repository root (UPPERCASE)
AGENTS.md           # Repository root (UPPERCASE)
CHANGELOG.md        # Repository root (UPPERCASE)
LICENSE             # Repository root (no extension)

# Other documentation (lowercase with hyphens)
installation-guide.md
user-guide.md
api-reference.md
troubleshooting.md
```

### **Directory-Specific Naming**

```yaml
# Agents (lowercase with hyphens)
agents/marketing/cs-content-creator.md
agents/c-level/cs-ceo-advisor.md

# Skills (lowercase, no hyphens in folder names)
marketing-skill/content-creator/SKILL.md

# Standards (lowercase with hyphens)
standards/communication/communication-standards.md

# Documentation (lowercase with hyphens)
documentation/implementation/implementation-plan-november-2025.md
documentation/delivery/sprint-11-05-2025/context.md
```

## Markdown Formatting Standards

### **1. Headings**

```markdown
# H1 - Document Title (only one per file)

## H2 - Major Sections

### H3 - Subsections

#### H4 - Details

**Don't skip heading levels!**
✅ H1 → H2 → H3
❌ H1 → H3 (skips H2)
```

### **2. Lists**

```markdown
# Unordered lists
- Item 1
- Item 2
  - Sub-item 2.1
  - Sub-item 2.2
- Item 3

# Ordered lists
1. First step
2. Second step
3. Third step

# Task lists
- [ ] Incomplete task
- [x] Completed task
```

### **3. Code Blocks**

```markdown
# Inline code
Use `code` for commands, filenames, and variables.

# Code blocks with syntax highlighting
\`\`\`bash
# Bash commands
git commit -m "feat(agents): implement cs-content-creator"
\`\`\`

\`\`\`python
# Python code
def analyze_content(text: str) -> Dict[str, Any]:
    return {"score": 0.85}
\`\`\`

\`\`\`yaml
# YAML configuration
name: cs-content-creator
domain: marketing
\`\`\`
```

### **4. Links**

```markdown
# External links
[Link text](https://example.com)

# Internal links (relative paths)
[Agent catalog](agents/README.md)
[Installation guide](INSTALL.md)

# Link to specific heading
[See quality standards](#quality-standards)

# Reference-style links (for repeated URLs)
[Claude Code][1]
[GitHub][2]

[1]: https://claude.com/code
[2]: https://github.com
```

### **5. Images**

```markdown
# Standard image
![Alt text describing image](path/to/image.png)

# Image with title
![Alt text](image.png "Image title")

# Linked image
[![Alt text](image.png)](https://link-destination.com)

**Always provide alt text for accessibility!**
```

### **6. Tables**

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
| Data 4   | Data 5   | Data 6   |

# Alignment
| Left | Center | Right |
|:-----|:------:|------:|
| L1   |   C1   |    R1 |
```

### **7. Emphasis**

```markdown
*Italic text* or _italic text_
**Bold text** or __bold text__
***Bold and italic*** or ___bold and italic___
~~Strikethrough~~

Use **bold** for emphasis, *italic* for definitions.
```

### **8. Blockquotes**

```markdown
> Single line quote

> Multi-line quote
> continues here
> and here

> **Note:** Important information
> highlighted in a quote block
```

### **9. Horizontal Rules**

```markdown
---

Use sparingly to separate major sections.
```

## Document Structure Templates

### **Agent Documentation (agents/*/cs-*.md)**

```markdown
---
name: cs-agent-name
description: One-line description
skills: skill-folder-name
domain: domain-name
model: sonnet
tools: [Read, Write, Bash, Grep, Glob]
---

# Agent Name

## Purpose
[1-2 paragraphs describing what this agent does]

## Skill Integration

**Skill Location:** `../../skill-folder/`

### Python Tools
[List with usage examples]

### Knowledge Bases
[List with relative paths]

### Templates
[List with relative paths]

## Workflows

### Workflow 1: [Name]
[Step-by-step process]

### Workflow 2: [Name]
[Step-by-step process]

## Integration Examples
[Concrete examples with code]

## Success Metrics
[How to measure effectiveness]

## Related Agents
[Links to related agents]

## References
[Links to documentation]
```

### **README.md Structure**

```markdown
# Project Title

[1-sentence project description]

## Quick Start

[Installation and first use - 30 seconds]

## Features

- Feature 1
- Feature 2
- Feature 3

## Installation

[Detailed installation steps]

## Usage

[Basic usage examples]

## Documentation

- [Installation Guide](INSTALL.md)
- [Usage Guide](USAGE.md)
- [Agent Catalog](agents/README.md)

## Contributing

[Contribution guidelines]

