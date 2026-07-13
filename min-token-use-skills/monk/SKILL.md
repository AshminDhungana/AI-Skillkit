---
name: monk
description: On-demand discipline to cut input/output tokens in a Claude Code
  session without harming correctness — read ranges, batch tools, delegate verbose
  reads to subagents, trim prose, reuse context, right-size the model. Use when the
  user wants to reduce the token cost of the current session.
---

# monk — Token Thrift

## When to use

Invoke `/monk` when you want the current session to cost fewer tokens without
sacrificing the quality or correctness of the work. Once invoked, these disciplines
apply to every turn for the rest of the session — no re-invocation needed. This is a
behavioral aid only: it changes no files, no configuration, and no repository state.

## Core principle

Every token in the context window is paid on **every** turn. Context is the fundamental
constraint, and model performance degrades as it fills.

Two layers of token cost have different owners:

- **Harness layer (not this skill's job):** Claude Code automatically caches the system
  prompt and stable prefixes — cache *reads* cost **0.1×** base input price — and
  auto-compacts the conversation near the context limit. `monk` does not touch caching
  or compaction.
- **Application layer (this skill's job):** Claude's own behavior — what it reads, how
  much it writes, which tools it calls, and whether it reuses prior work.

`monk` operates only on the application layer, which keeps it zero-risk and free of its
own token overhead.

## Operating rules

### Input / context (the biggest lever)

- **Read ranges, not whole files.** Use `offset`/`limit`; cap any single read at
  ~200 lines and expand only if needed. Never `Read` a 2000-line file to change
  one function.
- **Find with `Grep`/`Glob`, never `Read`-to-find.** `Grep` returns matches with line
  numbers; dumping a file just to locate text is the #1 input waste.
- **Do not re-read.** If a file's content is already in this session's context, reference
  it. Re-reading is pure waste.
- **Cap tool output.** Use `head_limit`, glob filters, and targeted queries rather than
  dumping full logs, directory listings, or command output.
- **Delegate verbose work to subagents.** Exploration and large log/file reads run in a
  *separate* context window; only a summary returns to the main thread. This is the
  single most powerful context lever. For scans that don't need Opus, prefer a cheap
  subagent model (`CLAUDE_CODE_SUBAGENT_MODEL=haiku`) so both the main context and the
  bill stay light. **Skip delegation when ≤4 already-located files cover the task** —
  a subagent round-trip would cost more than reading the ranges directly.
- **Right-size the model.** If currently on Opus for routine work, recommend `/model
  sonnet` (Opus output is far more expensive and unnecessary for most coding tasks). This
  is a *recommendation* the user accepts or declines — never switch the model silently.
- **Use built-in context controls:**
  - `/compact <instructions>` — preserve essentials during summarization.
  - `/clear` — reset between unrelated tasks so stale context stops costing tokens.
  - `/btw` — ask throwaway side-questions that should not enter conversation history.
  - `/context` — audit what is bloating turns; act on offenders.
- **Setup-once habits (documented, not enforced here):** keep `CLAUDE.md` under ~200
  lines; use `.claudeignore`; disable unused MCP servers (CLI tools are more
  context-efficient than MCP listings).

### Output (trim waste, keep insight)

- **Lead with the answer / code**; explanations follow.
- **Never restate code** just written in prose ("here is the function that…") — the block
  is self-explanatory.
- **Cut filler** ("Sure!", "Let me…", excessive qualifiers).
- **Keep the explanatory `★ Insight` blocks and the non-obvious *why*** — that is learning
  value, not waste. This is the line that respects the user's active Explanatory output
  style.
- **Prefer tables/lists over paragraphs** when denser conveys the same meaning.
- **Optionally lower `/effort` on genuinely simple tasks** — extended-thinking tokens are
  billed as output; reducing effort on trivial work cuts output cost with no quality loss.
- **Explicitly rejected as too aggressive:** "Caveman"-style silence (~65% output
  reduction) sacrifices the explanatory learning the Explanatory style exists to deliver.
  Out of scope, consistent with the conservative/zero-risk bar.

### Tool use & reuse

- **Batch** independent tool calls into one message (multiple tool-use blocks).
- **Parallelize** fan-out via subagents when it fits.
- **Do not re-derive** — reuse what was computed or discovered earlier this session.
- **Ask for a verification target up front** (test, build, screenshot). Self-verification
  prevents rework, and rework is the most expensive token waste of all. This sits *inside*
  the guardrail, not against it.
- **Pick the precise tool** for the job (e.g., `vault_get_document_map` before reading a
  whole vault file; structured sources like `21st` search before web-scrape).

## Never cut (zero-risk guardrail)

`monk` is **forbidden** from saving tokens by:

- Skipping verification (`verification-before-completion`, running tests).
- Omitting error messages / stack traces needed to debug.
- Dropping security-relevant or audit output.
- Summarizing away content a *correct decision* depends on.
- Guessing instead of a lookup when correctness depends on that lookup.
- Removing content the user explicitly asked to keep (including Explanatory insights).
- Disabling extended thinking on *complex* tasks.
- Downgrading the model on tasks that actually need Opus.

## Explanatory-style note

`monk` does **not** disable the user's active Explanatory output style. It trims
*redundancy* (restating code, filler, over-long prose), not *insight* (the `★ Insight`
blocks and the reasoning behind choices). If the user wants even terser output, they
switch off Explanatory separately — `monk` will not override the style setting.

## Optional hook (reference, not enabled)

A ready-made `PostToolUse` hook script can filter verbose test/log output (research shows
**80–99% reduction**) before it reaches context. It ships at
`reference/filter-verbose-output.sh` as a *reference only* and is **not** wired into
`settings.json` in v1. To enable later, add a `PostToolUse` hook in
`.claude/settings.json` that pipes Bash tool output through that script.

## Self-check before each response (while active)

1. Did I read only what's needed (ranges, not whole files)?
2. Did I reuse prior context instead of re-fetching?
3. Did I delegate verbose reads/exploration to a subagent?
4. Is context still lean (`/context`) — any offender to trim?
5. Is the model right-sized for this task?
6. Is my output free of restatement/filler but still insightful?
7. Did I avoid every item in the "never cut" list?
