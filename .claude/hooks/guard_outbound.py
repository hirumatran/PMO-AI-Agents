#!/usr/bin/env python3
"""PreToolUse guard for CLAUDE.md rule 3.4: never send without asking.

Any action that leaves the session (git push, publishing a page, sending
mail or messages, sharing files, PRs / comments) is turned into an explicit
approval prompt for the user, in every permission mode.
Everything else passes through untouched (no output, exit 0).
"""
import json
import re
import sys

BASH_PATTERNS = [
    (r"\bgit\s+push\b", "git push"),
    (r"\bgh\s+(pr|issue|release|repo|gist)\s+(create|comment|merge|close|edit|delete|review)\b", "GitHub write via gh"),
    (r"\bgh\s+api\b.*-X\s*(POST|PUT|PATCH|DELETE)", "GitHub API write"),
    (r"\b(sendmail|mailx?|mutt)\b", "sending email"),
    (r"\bcurl\b.*(-X\s*(POST|PUT|PATCH|DELETE)|--data|-d\s|-F\s|--upload-file)", "HTTP upload / post"),
]

# MCP tool names (mcp__<server>__<tool>) whose tool part means "send, share or publish"
MCP_OUTBOUND = re.compile(
    r"(send|share|post|publish|reply|forward|invite|create_pull_request|merge|push_files|"
    r"create_or_update_file|delete_file|add_issue_comment|add_reply|update_issue_comment|"
    r"issue_write|pull_request_review_write|create_branch|create_repository|trash|"
    r"create_event|update_event|create_draft_and_send)",
    re.IGNORECASE,
)

ARTIFACT_OUTBOUND = {"publish", "delete", "pin", "unpin"}


def reason_for(tool: str, tin: dict) -> str | None:
    if tool == "Bash":
        cmd = str(tin.get("command", ""))
        for pat, label in BASH_PATTERNS:
            if re.search(pat, cmd, re.IGNORECASE | re.DOTALL):
                return f"{label}: {cmd[:160]}"
        return None
    if tool == "Artifact":
        action = tin.get("action") or "publish"
        if action in ARTIFACT_OUTBOUND:
            return f"artifact {action}: {tin.get('url') or tin.get('file_path') or tin.get('type_url') or ''}"
        return None
    if tool.startswith("mcp__"):
        name = tool.split("__", 2)[-1]
        if MCP_OUTBOUND.search(name):
            return f"external tool {tool}"
    return None


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # never break the session on bad input
    tool = str(data.get("tool_name", ""))
    tin = data.get("tool_input") or {}
    why = reason_for(tool, tin if isinstance(tin, dict) else {})
    if not why:
        return 0
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "ask",
            "permissionDecisionReason": f"CLAUDE.md 3.4, outward action needs your approval: {why}",
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
