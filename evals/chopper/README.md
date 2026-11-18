# Chopper standards test

15 questions with known answers to check Chopper's accuracy on medical device standards and regulations. Based on ECC's `eval-harness` / `verification-loop` idea: re-run after any change to Chopper, CLAUDE.md or the model.

| Area | Questions |
|---|---|
| ISO 13485:2016 clauses | Q01–Q04 |
| FDA QMSR, EU MDR | Q05, Q07 |
| ISO 14971 risk management | Q06 |
| ISO 14644-1 cleanroom limits | Q08–Q09 |
| Sterility: SAL, EO residuals, radiation dose | Q10–Q12 |
| ISO 11607 packaging | Q13 |
| IEC 62304 / IEC 60601-1 | Q14 |
| Trick question (must not invent a clause) | Q15 |

## Pass rule
- **No wrong fact on any question.** One wrong clause or figure fails the run.
- At least **14 / 15** fully correct on the first try (pass@1).
- Q15: inventing a clause is an automatic fail.
- Every run ends with a Sources section and the CLAUDE.md 4.1 output block.

## How to run
1. In a Claude Code session on this repo, ask: *"Run the Chopper standards test."*
   The main session sends the 15 questions (not the answer key) to Chopper and saves the reply to `evals/chopper/runs/<date>/answers.md`, one `### Qnn` section per question.
2. Score it:
   ```bash
   python3 evals/chopper/score.py evals/chopper/runs/<date>/answers.md
   ```
3. Read every REVIEW or FAIL line by hand before giving a verdict. The script only looks for key facts.

## Keeping it honest
- The answer key is in `questions.json`. Never paste it into Chopper's prompt.
- Answer key last checked 2026-11-18. When a standard is revised (e.g. a new ISO 13485 edition), update the key first.
