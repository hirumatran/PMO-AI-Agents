# Baseline result, 2026-11-18

**Verdict: PASS. 15 / 15 correct, no wrong facts, trick question handled.**

| Check | Result |
|---|---|
| Auto-score | 14/15 first pass; Q14 was a scorer keyword gap (answer correct), fixed in `questions.json` → 15/15 |
| Trick question Q15 | Passed: said no clause exists, did not invent one |
| Sources section / output block | Present / present |
| "Not confirmed" used properly | Yes, 3 times, all on edition-currency questions |

## Details beyond the answer key (not verified by this test)
Chopper added detail the key does not cover: 89 FR 7496, §820.7, EN 556-1 clause 4.1, ISO 10993-7 clause 4.3, ISO 11137-2 Amd 1:2022 clause 9, ISO 11607 Amd 1:2023. Spot-check before quoting these in a deliverable.

## Limits of this run
- This session still gave Chopper all tools (the scoped `tools:` list loads in the next session). It said it did not open the answer key; that can't be proven from here.
- Run time 41 s, 3 tool calls, about 19k tokens.
