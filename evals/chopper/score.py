"""Score a Chopper answer file against the answer key.

Usage:  python3 evals/chopper/score.py evals/chopper/runs/<date>/answers.md

The answer file holds one section per question, headed "### Q01", "### Q02", ...
Auto-checks: required facts present, Sources section present, output block (Status:) present.
Auto-checks are a first pass. Any FAIL or REVIEW must be read by a person before a verdict.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
KEY = json.loads((HERE / "questions.json").read_text(encoding="utf-8"))


def split_answers(text: str) -> dict:
    parts = re.split(r"^###\s*(Q\d{2})\b.*$", text, flags=re.MULTILINE)
    return {parts[i]: parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def norm(s: str) -> str:
    return s.lower().replace(" ", " ").replace(" ", " ")


def main(path: str) -> int:
    text = pathlib.Path(path).read_text(encoding="utf-8")
    answers = split_answers(text)
    whole = norm(text)
    rows, passed = [], 0
    for q in KEY["questions"]:
        ans = norm(answers.get(q["id"], ""))
        if not ans.strip():
            rows.append((q["id"], "MISSING", "no answer section"))
            continue
        missing = [g for g in q["must_include"] if not any(norm(alt) in ans for alt in g)]
        if q.get("trap") and re.search(r"clause\s+\d+(\.\d+)+\s+(requires|sets|mandates)", ans):
            rows.append((q["id"], "FAIL", "trap: answer seems to name a requiring clause"))
            continue
        if missing:
            rows.append((q["id"], "REVIEW", "not found: " + " | ".join("/".join(g) for g in missing)))
        else:
            rows.append((q["id"], "PASS", q["answer_key"][:60]))
            passed += 1
    fmt_sources = "sources" in whole
    fmt_block = "status:" in whole
    print(f"{'ID':<5} {'Result':<8} Note")
    for r in rows:
        print(f"{r[0]:<5} {r[1]:<8} {r[2]}")
    print(f"\nAuto-pass: {passed}/{len(KEY['questions'])}")
    print(f"Sources section: {'yes' if fmt_sources else 'NO'} · Output block (Status:): {'yes' if fmt_block else 'NO'}")
    print("Pass rule:", KEY["pass_rule"])
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    sys.exit(main(sys.argv[1]))
