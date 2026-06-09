---
name: watching-videos
description: >
  Analyze videos via URL or local path. Downloads with yt-dlp, extracts timestamped frames 
  with ffmpeg, pulls transcripts from captions or Whisper API fallback, and answers 
  questions about video content. Use when the user pastes a video link (YouTube, Vimeo, 
  X, TikTok, Twitch, etc.), points at a local video file (.mp4, .mov, .mkv, .webm), 
  types /watch, or asks "what happens in this video," "summarize this clip," "what is 
  said at [timestamp]," or any question about video content.
argument-hint: "<video-url-or-path> [question]"
allowed-tools: Bash, Read, AskUserQuestion
user-invocable: true
---

# /watching-videos — Video Analysis

## When to Use

- User pastes a video URL or local path and asks anything about it.
- User types `/watching-videos <source> [question]`.
- User asks about "this video," "the clip," "what happens at [time]," etc.

## When NOT to Use

- The user only wants to download a video without analysis → use yt-dlp directly.
- The user wants to edit or convert video formats → use ffmpeg directly.
- The user asks about audio-only files (podcasts, music) with no visual component.

---

## Step 0 — Setup Preflight (Silent)

Run before every `/watching-videos` invocation:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/setup.py" --check
```

**Exit codes:**
| Exit | Meaning | Action |
|------|---------|--------|
| 0 | Ready | Proceed silently |
| 2 | Missing binaries | Run `python3 "${CLAUDE_SKILL_DIR}/scripts/setup.py"` |
| 3 | No Whisper API key | Run installer, then ask user for Groq or OpenAI key |
| 4 | Both missing | Run installer, then ask for key |

**If API key needed:** Ask user via `AskUserQuestion` whether they have a Groq key (preferred) or OpenAI key. Write it to `~/.config/watching-videos/.env` as `GROQ_API_KEY=...` or `OPENAI_API_KEY=...`. If they decline, proceed with `--no-whisper` and warn that uncaptioned videos will be frames-only.

**Skip on follow-ups:** Within a session, skip Step 0 after the first successful `--check`.

---

## Step 1 — Parse Input

Separate the **source** (URL or path) from the **question** (if any).

Example: `/watching-videos https://youtu.be/abc what language is this?` → source=`https://youtu.be/abc`, question=`what language is this?`

---

## Step 2 — Run the Script

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/watching-videosing-videos.py" "<source>"
```

**Optional flags:**

| Flag                     | Purpose                                                | Example                   |
| ------------------------ | ------------------------------------------------------ | ------------------------- |
| `--start T` / `--end T`  | Focus on a section (SS, MM:SS, HH:MM:SS)               | `--start 2:15 --end 2:45` |
| `--max-frames N`         | Lower frame cap for token budget                       | `--max-frames 40`         |
| `--resolution W`         | Frame width in px (default 512, bump to 1024 for text) | `--resolution 1024`       |
| `--fps F`                | Override auto-fps (clamped to 2 max)                   | `--fps 1`                 |
| `--out-dir DIR`          | Custom working directory                               | `--out-dir /tmp/my-watch` |
| `--whisper groq\|openai` | Force backend                                          | `--whisper groq`          |
| `--no-whisper`           | Disable fallback entirely                              | `--no-whisper`            |

**Auto frame budgets (full video):**
| Duration | Frames | Notes |
|----------|--------|-------|
| ≤30s | ~1–2 fps (up to 30) | Dense coverage |
| 30s–1min | ~40 | |
| 1–3min | ~60 | |
| 3–10min | ~80 | |
| >10min | 100, sparse | Warn user; offer `--start`/`--end` |

**Focused mode budgets (when `--start`/`--end` set):**
| Duration | Frames | FPS |
|----------|--------|-----|
| ≤5s | up to 10 | 2 fps |
| 5–15s | up to 30 | 2 fps |
| 15–30s | up to 60 | ~2 fps |
| 30–60s | up to 80 | ~1.3 fps |
| 60–180s | 100 cap | ~0.6 fps |

**Transcript source priority:** native captions (free) → Whisper API fallback (Groq preferred, OpenAI fallback).

---

## Step 3 — Read All Frames

Read **every frame path** the script lists. Read all frames in a single parallel batch so you see them together. Frames are chronological with `t=MM:SS` timestamps for alignment with the transcript.

---

## Step 4 — Answer the User

You now have **Frames** (what's on screen) and **Transcript** (what's said). Use both.

### If the user asked a specific question:

Answer directly, citing timestamps. Example: "At 01:23, the presenter points to a chart showing..."

### If the user asked nothing:

Summarize the video using this template:

```markdown
## Video Summary

**Source:** [URL or filename]
**Duration:** [MM:SS]
**Transcript source:** [captions / whisper (groq) / whisper (openai) / none]

### Structure & Key Moments

- [00:00] [Brief description of opening scene + spoken content]
- [MM:SS] [Next key moment]
  ...

### Notable Visuals

- [Description of important on-screen text, graphics, people, actions]

### Spoken Content Overview

[Summary of main topics discussed]
```

**Accuracy rules:**

- Never invent visual details not present in frames.
- Never invent dialogue not present in transcript.
- If transcript is "none available," state this explicitly and answer from frames only.
- If the video is >10min and frames are sparse, acknowledge the sparse coverage.

---

## Step 5 — Cleanup

The script prints a working directory at the end.

- **If follow-ups likely:** Leave the directory in place.
- **If done:** `rm -rf <dir>`.

---

## Key Technical Details

**Audio extraction for Whisper (when needed):**

```bash
ffmpeg -vn -ac 1 -ar 16000 -b:a 64k
```

~0.5 MB/min mono 16kHz audio.

**Whisper backends:**

- **Groq** — `whisper-large-v3-turbo` (216× real-time, preferred). Key: `GROQ_API_KEY`.
- **OpenAI** — `whisper-1`. Key: `OPENAI_API_KEY`.
- Both in `~/watching-videos/.env` (mode `0600`).

**Failure modes:**

| Issue                                    | Handling                                       |
| ---------------------------------------- | ---------------------------------------------- |
| Download fails (login/region lock)       | Tell user plainly; do not retry                |
| No transcript + no Whisper key           | Proceed frames-only; warn user                 |
| Whisper API fails (rate limit, 25MB cap) | Retry with other backend or use `--no-whisper` |
| Long video warning                       | Acknowledge in answer; offer focused re-run    |

---

## Security & Permissions

**What this skill does:**

- Runs `yt-dlp` and `ffmpeg/ffprobe` locally.
- Sends audio clips (not video) to Groq/OpenAI Whisper APIs only when native captions are missing.
- Reads/creates `~/watching-videos/.env` for API keys.
- Writes working files to temp dir or `--out-dir`.

**What this skill does NOT do:**

- Uploads video to any API.
- Accesses platform accounts or posts content.
- Shares keys between providers.
- Persists working files beyond the session unless `--out-dir` is set.

**Bundled scripts:** `watch.py`, `download.py`, `frames.py`, `transcribe.py`, `whisper.py`, `setup.py`.

---
