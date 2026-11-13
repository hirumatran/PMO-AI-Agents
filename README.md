# PMO AI Agents · OEPM

AI agent team for the **Operational Excellence PMO (OEPM)**, Olympus Vietnam.
Rulebook for every agent: [CLAUDE.md](CLAUDE.md). Visual rules: [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md).

## Dashboard

| Version | Where | Notes |
|---|---|---|
| **Private claude.ai page** | https://claude.ai/artifact/8X1u3fGjLgMGiGctT2FV8J | Owner-only until shared. No Olympus logo. Live weather is blocked on claude.ai, so it shows sample weather. |
| Local / internal file | [`dashboard/oepm-dashboard.html`](dashboard/oepm-dashboard.html) | Full version with the Olympus logo. Open in a browser; live weather loads from Open-Meteo. |

All figures, tasks, messages and risks on the dashboard are **sample data** until Microsoft 365 is connected.

## Requirements (owner's rules)

| # | Rule | Meaning |
|---|---|---|
| 1 | Premium look | Olympus-style design system: blue `#001C71`, yellow `#EAA100` thin rules only, Noto Sans JP / Noto Sans, 2px corners |
| 2 | Short, key points first | Answer in line one, one idea per bullet, risks and decisions visible at Board (BOD) level |
| 3 | Write like a person | Humanizer rules in CLAUDE.md 3.3: banned AI phrases, plain verbs, no filler |
| 4 | Never send without asking | No email, post, push, share or publish without approval of that specific action |
| 5 | Accuracy | Facts and exact figures only, sources cited (standard, edition, clause) |
| 6 | Languages | Deliverables trilingual: Japanese main, English and Vietnamese sub. Chat in English. |

Current project: **Single-use Endoscopic Camera line**, Olympus Vietnam. FAT at vendor Jan–Feb 2027, installation from Mar-2027, SAT Q3-2027, validation 2027–2029, then international release.

## Agent team

| Agent | Role | Handles | Definition |
|---|---|---|---|
| **Hiruma** | Lead Project Assistant, team orchestrator | Planning, WBS and schedule, BOD reports, Lean / OpEx, risk register. Routes work to the other two. | [`.claude/agents/hiruma.md`](.claude/agents/hiruma.md) |
| **Chopper** | Medical device and regulatory expert | Olympus / Omron / GE / Siemens product lines, ISO 13485, ISO 14971, IEC 60601, FDA QMSR, EU MDR, sterilization, IQ / OQ / PQ | [`.claude/agents/chopper.md`](.claude/agents/chopper.md) |
| **Jarvis** | Personal Assistant | Email review and drafts, to-do dashboard, reminders, daily communication; sales, HR, legal, logistics, supply chain | [`.claude/agents/jarvis.md`](.claude/agents/jarvis.md) |

Avatars: [`assets/avatars/`](assets/avatars/) (internal use only).

## Repository map

```
CLAUDE.md                     team rulebook (read automatically by Claude Code)
DESIGN_SYSTEM.md              Olympus-style tokens, type, layout rules
.claude/agents/               Hiruma, Chopper, Jarvis subagent definitions
assets/                       avatars, Olympus logo
dashboard/
  oepm-dashboard.template.html   source (edit this)
  build.py                       builds both versions below
  oepm-dashboard.html            local version with logo
  oepm-dashboard.publish.html    claude.ai version
docs/SESSION_NOTES.md         what was done, decisions, open items
```

## Rebuild and republish

```bash
python3 dashboard/build.py
```

Then ask Claude to republish `dashboard/oepm-dashboard.publish.html` to the link above, so the URL stays the same.
