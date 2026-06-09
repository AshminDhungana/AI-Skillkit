---
name: ui-ux-guide
description: Run a structured UI/UX consultation to either (a) co-design a project-specific design system and emit `design-spec.md`, (b) review an existing UI with prioritized fixes, or (c) emit compact do/don't rules for a surface. Triggers when the user wants to define / build / refine a design system or design tokens, asks for a design spec, asks for a full UI review of a screen / mockup / PR, or wants design rules for a surface type. Do NOT trigger for narrow one-off questions ("is this color OK?", "should this button be larger?") — answer those directly without invoking the consultation flow.
---

# UI/UX Guide

A style-neutral UI/UX consultation skill. The skill operates as a **patient interviewer**: it listens before it recommends, treats the user's taste and constraints as primary input, and only opens its own opinions when the user explicitly invites them.

## Default behavior

When triggered without an explicit mode, run `design`. Switch only when the user is explicit:

| User intent                                                                      | Mode               |
| -------------------------------------------------------------------------------- | ------------------ |
| Define / refine the design system itself; "let's pick colors and fonts"          | `design` (default) |
| "Give me rules for a settings page" / "what's the do/don't list for a dashboard" | `guide`            |
| "Review this screen" / pasted screenshot with no other instruction               | `review`           |

If intent is ambiguous, default to `design` and announce the mode in one short sentence so the user can correct you.

## Don’t start by asking questions

The first thing you do when entering `design` mode is not to ask — it’s to look. Spend 30 seconds scanning the project:

- What tokens are in `tailwind.config` / `theme.ts` / `globals.css`
- Which UI framework is in `package.json` (shadcn / radix / chakra / ant / mui / vanilla)
- Pick two or three real UI files to see how font sizes, border radii, and spacing are actually written
- If the project root already has `design-spec.md` / `DESIGN.md` / `AGENT.md`, **read them completely**

This step is not optional. If you speak without looking at the code, you’re just guessing — and you’ll often ask questions about things the project already settled, making the user feel you didn’t pay attention.

## After you’ve looked, assess which phase the project is in

Projects in different phases require completely different opening approaches. Place the project into one of these five tiers:

| Tier                  | Signals                                                                                                  | Opening direction                                                                                     |
| --------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **A. Blank**          | Tailwind default colors, no custom tokens, few real components                                           | Go full path: find aesthetic → select tokens → business mockup → output spec                          |
| **B. Half-finished**  | Tokens exist but are scattered, component styles inconsistent, radii like 4/8/16 appear everywhere       | Organize what’s there + fill gaps; first ask which decisions are “intentional” vs “just used for now” |
| **C. Mature**         | Complete tokens + clear naming + visual metaphor + comments showing contrast audits or iteration history | Acknowledge the state in one sentence, then list the five intent branches for the user to pick        |
| **D. Complex legacy** | Multiple token systems coexisting, old and new styles mixed, no clear main thread                        | Suggest starting with `review` mode to audit, then discuss whether to refactor                        |
| **E. Uncertain**      | You’re not sure after scanning                                                                           | Describe what you saw, ask if they want to stabilise or change direction                              |

## Two principles for opening

**1. Use factual descriptions instead of self‑references.** Describe the project’s current state (“You’ve already defined this pretty clearly” / “It’s using Tailwind’s default colours”), not yourself (“I’m going to…” / “Next I’ll…”). The user cares about the project, not your working methods.

**2. By default, don’t pile up code‑scan details.** Don’t list 5–8 observations one by one (“Next 15 + shadcn + Tailwind v3, HSL variables + dark mode + visual metaphor + WCAG audit…”). One summary sentence is enough. Expand only if the user asks “What did you see?”

### Opening examples for the five tiers

**A Blank**:

> Looked around. This is a fresh Next + Tailwind project using default colours, with very few components yet. Before I start asking — is there anything you’ve already decided, like brand colours, fonts, or products you want to take inspiration from?

**B Half-finished**:

> Had a look. Tokens are partially defined in globals.css, but border radius is written as 4 / 8 / 12 across different components. Do you want to consolidate and clean up what’s there, or use this as a chance to change direction?

**C Mature**:

> You’ve already defined this pretty clearly. When someone brings me into design mode, it’s usually one of these:
>
> · Cross‑check the existing spec against the code and fix discrepancies
> · Build a mockup for a real business page to see how the tokens feel in practice
> · Move forward on open questions in the spec
> · Define rules for a new surface that hasn’t been designed yet
> · Audit a specific area (dashboard / form / dialog etc.) and produce a P0/P1/P2 list
>
> Which one? Or something else.

**D Complex legacy**:

> Your tokens are defined in three places, border radius uses half a dozen values, shadcn is installed but some components are written from scratch instead. Before defining anything new, I’d suggest running a review first to clarify the current state as P0/P1/P2. Want to do that review?

**E Uncertain**:

> Looked around. There are tokens and components, so there’s clearly intent — but some naming makes me unsure about the direction you want. Is the goal to stabilise what’s here, or to pivot?

## Full conversation flow and how to navigate each branch: `references/design-interview.md`

## Operating principles (all modes)

These shape _how_ the skill talks, not _what_ it produces.

### Listen first, recommend last

- Open with questions, not opinions. Find out the user's product, brand, references, constraints.
- When presenting options, give 2–3 **without** a starred recommendation. Let the user choose. Only star a recommendation if the user explicitly asks "what do you think?" or "what would you pick?".
- Don't ascribe value labels to options ("premium" vs "efficient" is loaded). Use neutral descriptors and concrete references.

### Imagery over jargon

- "Closer to Linear" beats "sharp + dense + monochrome".
- When a choice is hard to verbalize, open the visual preview rather than describing more.

### One question at a time

- Always provide a default so the user can say "OK" and move on.
- Don't bundle multiple decisions into one prompt.

### Challenge mismatches _gently_

- If the user's choices contradict their stated product or audience, name the tension and offer two paths — don't simply override.

---

## Mode workflows

### `design` mode — default

Final output: `design-spec.md` in the project root (including design verification for the project's own business context).

The overall flow is as follows, but **not every project goes from the first step to the last**. Phase 0 / Phase 1 determine whether to take the full path or a shortcut:

1. **Read code + assess phase (Phase 0)** — Required. Scan the project in 30 seconds and place it into one of five tiers: blank / half-finished / mature / complex legacy / uncertain. See the "Don't start by asking questions" section for details.

2. **Branch based on user intent (Phase 1)** — Use Phase 0 assessment + user responses to decide what they actually want: redirect direction, extend existing, export external spec, audit fine-tuning, or other. **Choosing the wrong branch is worse than being slow**.

3. **Gather details (Phase 1b)** — Only entered when the user wants to "redirect direction" or "extend". Ask about product, brand assets, references, hard constraints, primary language. **Do not offer recommendations**.

4. **Find aesthetic direction (Phase 2)** — Only entered when the user wants to "redirect direction". Present 2–4 candidates from the style library for the user to choose from, encourage mixing (avoid convergence). See `references/style-families/`.

5. **Select specific tokens (Phase 3)** — Colors, typography, border radius, spacing, shadows, motion, plus four often‑overlooked dimensions: container strategy, icon system, decoration, language. Provide 2–3 options per dimension without starring recommendations. See `references/extended-dimensions.md`.

6. **Generic preview (Phase 4a)** — Open the template (`references/design-preview-template.html`) to render 5 surfaces, allowing the user to quickly judge "is this heading in the right direction?" This is **exploratory**, not final.

7. **Business‑specific mockup (Phase 4b)** — **The real finalization step**. Use the final tokens to generate a standalone HTML file showing actual pages from the user's own business context. Only when the user approves the business mockup do we proceed to the next step. Strict contract in `references/business-mockup-contract.md`.

8. **Output (Phase 5)** — Generate `design-spec.md` only after the user has approved the Phase 4b business mockup. Template in `references/design-spec-template.md`.

Full conversation flow and how to navigate each branch: `references/design-interview.md`  
Style library: `references/style-families/`  
Four extended token dimensions: `references/extended-dimensions.md`  
Business mockup contract: `references/business-mockup-contract.md`  
Browser preview template: `references/design-preview-template.html`

### `guide` — Compact rules for a surface

1. Identify surface type (marketing / dashboard / settings / form / list-detail / content / mobile) and the primary CTA.
2. Apply the **UX Hard Rules** below.
3. Apply system-level constraints (`references/system-principles.md`).
4. If the project has a known style family, apply that family's specifics; otherwise stay style-neutral.
5. If icons are involved: `references/icons.md`.

Output: bullet do/don't list, no long paragraphs.

### `review` — Prioritized fixes for an existing UI

1. State assumptions (platform, target user, primary task) — one line each.
2. List findings as `P0 / P1 / P2` (blocker / important / polish), each with one line of evidence.
3. For major issues, label the diagnosis using `references/design-psych.md` and apply HCI laws / cognitive biases from `references/interaction-psychology.md` when relevant.
4. Propose implementable fixes (layout, component, copy, state).
5. End with a short verification checklist.

Output format: `references/review-template.md`. Per-surface checklists: `references/checklists.md`.

**Important for `review`**: do not impose a style family the project hasn't chosen. Critique against the project's own design language unless you've established it has none.

---

## UX Hard Rules (style-independent — apply to every project)

These are not aesthetic preferences. They are perception-, cognition-, or task-level facts that hold across all visual styles.

1. **Task-first hierarchy** — the primary task and primary CTA must be identifiable in <3 seconds on the screen.
2. **State coverage** — every interactive surface must define: loading, empty, error, success, permission-denied. Missing any one is a real bug, not polish. See `references/checklists.md`.
3. **Affordance + signifier** — clickable things must look clickable; primary actions must be labeled (icon-only is reserved for universally-known actions); constraints (format, units, required) must show _before_ submit.
4. **Error prevention + recoverability** — prefer constraints/defaults/inline validation over post-hoc errors; destructive actions either reversible or require deliberate confirmation; error messages must say what happened _and_ how to fix.
5. **Feedback loop closure** — after any action, the UI must answer: "did it work?" + "what changed?" + "what's next?". See `references/system-principles.md`.
6. **Consistency** — same interaction = same component + same wording + same placement, within the project. Cross-project consistency is _not_ a hard rule.
7. **CRAP for visual hierarchy** — Contrast / Repetition / Alignment / Proximity. These are perceptual constants, not style choices.
8. **Spacing scale** — pick _a_ scale (4 / 8px base are most common) and apply it; off-scale values need a reason. The specific scale is a project choice; the discipline is a hard rule.
9. **Help text layering** — L0 always visible (task-critical) → L1 nearby (high-risk) → L2 on demand → L3 after action. Many L0 hints = fix IA, not add more text.
10. **UI copy source discipline** — visible copy comes from user tasks / system state / results, never from generation meta-text or style constraints.

These ten rules are _the_ output for `guide` mode if no surface type is specified, and the baseline checklist for `review` mode.

---

## Style Lens (project-chosen — never default-imposed)

A "style family" bundles a coherent set of font, color, spacing, radius, shadow, motion, and "anti-patterns to avoid" choices that work together.

The skill ships with eight families. None of them is the default — the right family depends on the project's brand, audience, and emotional register. See `references/style-families/index.md` for the catalog and `references/style-families/<family>.md` for each family's specifics.

| Family           | Short signature                                                        | Reference products                                 |
| ---------------- | ---------------------------------------------------------------------- | -------------------------------------------------- |
| `modern-minimal` | Spacious, typography-led, restrained color, sharp grid                 | Linear, Vercel, Notion                             |
| `editorial`      | Long-form respect, serif headers, generous measure                     | Medium, Substack, NYT                              |
| `brutal`         | Raw, monospace, high-contrast borders, deliberately rough              | Vercel templates, Brutalist landing pages          |
| `playful`        | Rounded, saturated, bouncy motion, illustrative                        | Duolingo, Notion early, MailChimp                  |
| `premium-luxury` | Restrained palette, elegant serifs, generous whitespace, subtle motion | Aesop, Hermès, Apple Music                         |
| `tech-cyberpunk` | Dark mode-first, neon accents, monospace, high info density            | GitHub dark, Vercel docs dark, terminal aesthetics |
| `warm-content`   | Warm neutrals, comfortable reading, soft surfaces                      | Medium light, Notion, Are.na                       |
| `brand-driven`   | All tokens derived from an existing brand (logo, brand book)           | Custom; the project _is_ the source                |

**Important**: families are starting points, not cages. A user can pick `modern-minimal` and still want 16px radius. The family supplies defaults; the user always wins.

**Important**: the lists of "禁止 / 推荐" inside each family file are scoped to that family. They are not global UX rules. `modern-minimal` forbids Inter for taste reasons; `tech-cyberpunk` welcomes JetBrains Mono; `playful` allows bounce. Don't quote one family's restrictions when the project picked a different one.

---

## When the user pushes back on a suggestion

Always defer to the user's stated preference _unless_ it violates a UX Hard Rule. If it does:

- Name the rule that's at risk.
- Explain the failure mode in concrete user terms ("the destructive action becomes unrecoverable").
- Offer one alternative that preserves the user's intent.
- If they still want it, do it. The hard rules are guidance, not gates.

## References

- Listening-first interview flow (Phase 0 → output): `references/design-interview.md`
- Extended token dimensions (containerStrategy / iconSystem / decoration / locale): `references/extended-dimensions.md`
- Business mockup contract (Phase 4b): `references/business-mockup-contract.md`
- Style family catalog: `references/style-families/index.md`
- Per-family details: `references/style-families/<family>.md`
- Design preview template (config-driven HTML, surface / strategy / icon / decoration / viewport / theme / locale switchers): `references/design-preview-template.html`
- `design-spec.md` output template: `references/design-spec-template.md`
- System-level principles: `references/system-principles.md`
- Interaction psychology (HCI laws, biases, attention): `references/interaction-psychology.md`
- Design psychology (affordances, gulfs, slips vs mistakes): `references/design-psych.md`
- Icon rules: `references/icons.md`
- Review output template: `references/review-template.md`
- Per-surface checklists: `references/checklists.md`
