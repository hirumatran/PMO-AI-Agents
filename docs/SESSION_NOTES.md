# Session notes

## 2026-11-13 · Set-up of rulebook, agent team and OEPM dashboard

### Done
- **CLAUDE.md**: profile (PMO, OpEx team, Olympus), accuracy rules, output rules (premium look, short, humanizer, never send without asking), team defaults, agent team. Icon rule relaxed: clean line icons allowed, no emoji or clip-art.
- **DESIGN_SYSTEM.md**: added as supplied (Olympus-style tokens).
- **Agents**: Hiruma, Chopper, Jarvis in `.claude/agents/`, avatars in `assets/avatars/`.
- **OEPM Dashboard** (`dashboard/`), sample data throughout:
  - Blue header: Olympus logo (local version only), title, welcome widget with Japanese date, Vietnamese lunar date, JST / ICT clocks, weather for Tokyo, Ho Chi Minh City, Dong Nai.
  - Overview tiles, project selector (PRJ-01 camera line + 2 sample projects), summary (plan %, actual %, variance, SPI, next milestone).
  - Detailed WBS Gantt: planned vs actual bars, hover for progress % and progress date, collapsible phases, near-term / full view.
  - Agent performance cards, task board with owner filter.
  - Microsoft 365 section with Outlook / Teams tabs (not connected yet).
  - Board risks: priority filter, red only for urgent (action due ≤ 7 days), "Report in Outlook" opens a draft only.
- **Private claude.ai page**: https://claude.ai/artifact/8X1u3fGjLgMGiGctT2FV8J (version without the logo).

### Decisions
| Topic | Decision |
|---|---|
| Vietnamese font | Noto Sans (design system), not Helvetica |
| FAT timing | Before installation (Jan–Feb 2027); SAT Q3-2027 |
| Chat language | English; deliverables JA main, EN / VI sub |
| Red colour | Status only: overdue tasks, behind-plan bars (>10 pt), urgent risks |
| Logo | White plate on blue header; omitted on the claude.ai version |
| Progress % | Duration-weighted (validation phase dominates PRJ-01 totals) |

### Open items
1. **Microsoft 365 link**: owner to provide; then replace sample Outlook / Teams boxes with live data.
2. **Display name** for the greeting (`USER_NAME` in the template).
3. **Real WBS dates and actuals** for PRJ-01; confirm the FAT date (still TBC).
4. **Progress weighting**: switch to budget or effort weights if figures are provided.
5. **Outlook web domain**: confirm Olympus uses `outlook.office.com`.
6. **Official reversed (white) Olympus logo**, if available, to drop the white plate.
7. Live weather verified only by design: the session network blocked Open-Meteo, so check it once in your own browser.

### How to resume
- Open a new Claude Code session on this repo. CLAUDE.md loads automatically, and `/agents` lists the team.
- Edit `dashboard/oepm-dashboard.template.html`, run `python3 dashboard/build.py`, ask Claude to republish to the same link.

## 2026-11-18 · Harness hardening, step 1 (from ECC `agent-harness-construction`)
- Each agent limited to the tools it needs (`tools:` in `.claude/agents/*.md`). No agent has shell, git or send tools.
- CLAUDE.md section 4: output block (4.1), hand-off brief (4.2), failure rule (4.3), tool-scope table (4.4).
- Next: step 2, a hook that blocks push / send / publish without approval; then a 15-question standards test for Chopper.
