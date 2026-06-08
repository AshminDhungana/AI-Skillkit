# Full-Stack Development Skills

This folder contains a collection of reusable skills (prompts, templates, or guidelines) for managing full-stack projects from initial planning to execution. Use them in a sequential or modular way depending on your team size and workflow.

## How to use these skills

| Skill File | Status | Purpose & Usage |
|------------|--------|------------------|
| `initial-project-planning-skill.md` | ✅ Created | **Planning phase of the project at the very beginning.** Start here to define scope, requirements, architecture, and milestones before any development. |
| `onedev-todo-creation-skill.md` | ✅ Created | **Creating `Todo.md` for a single‑developer workflow.** Generate a prioritized task list for one person handling both frontend and backend. |
| `twodev-todo-creation-skill.md` | ❌ Not created | **Two‑developer workflow** – one frontend, one backend. Will split responsibilities across two separate `Todo.md` files or sections. |
| `multidev-todo-creation-skill.md` | ❌ Not created | **Multi‑developer workflow** – one shared `Todo.md` + a `whatsuplog.md` to track who does what. <br><br>**Process:** Each agent (developer) reads `whatsuplog.md` → picks a task **not** listed there → updates `whatsuplog.md` claiming the task → works → after completion, updates `Todo.md` (mark done) and finally updates `whatsuplog.md` with status “done”. All agents repeat the same cycle. |
| `research-driven-planning-skill.md` | ✅ Created | **Use after selecting a task from `Todo.md`.** Before implementing the chosen task, apply this skill to research, evaluate alternatives, and plan the specific implementation details. Then proceed with coding. |
| `frontend-design-skill.md` | ✅ Created | **For frontend design.** Covers UI/UX, component structure, styling approach, and frontend framework conventions. |
| `backend-design-skill.md` | ❌ Not created | **For backend design** – API design, database schema, business logic, security, etc. |

## Typical workflow examples

### Single developer
1. `initial-project-planning-skill.md`
2. `onedev-todo-creation-skill.md` → creates `Todo.md`
3. For each task in `Todo.md`:
   - `research-driven-planning-skill.md`
   - `frontend-design-skill.md` and/or `backend-design-skill.md` (if available)
   - Implement the task

### Multi‑developer (future, when skills are created)
1. `initial-project-planning-skill.md`
2. `multidev-todo-creation-skill.md` → creates shared `Todo.md` and initial `whatsuplog.md`
3. Each agent loops:
   - Read `whatsuplog.md`
   - Claim an unclaimed task (update `whatsuplog.md`)
   - Run `research-driven-planning-skill.md` for that task
   - Apply `frontend-design-skill.md` / `backend-design-skill.md`
   - Implement, then update `Todo.md` and mark task as done in `whatsuplog.md`

## Notes
- Skills marked **Not created** are placeholders for future expansion.
- Adapt the order and selection of skills to match your actual project needs.