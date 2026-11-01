import re
from collections import Counter
from pathlib import Path

LOG_FILE = "auth.log"

# Common failure patterns, tried in order:
# - user=alice / user: alice
# - Failed password for alice from ...
# - Failed password for invalid user alice from ...
_PATTERNS = [
    re.compile(r"user\s*[=:]\s*([A-Za-z0-9_.-]+)", re.IGNORECASE),
    re.compile(r"for\s+(?:invalid\s+user\s+|illegal\s+user\s+)?([A-Za-z0-9_.-]+)\s+from", re.IGNORECASE),
]


def parse_failed_user(line: str) -> str | None:
    """Return the username if this line is a failed login, else None."""
    if "fail" not in line.lower():
        return None
    for pattern in _PATTERNS:
        match = pattern.search(line)
        if match:
            return match.group(1)
    return None


def count_failures(path: str | Path = LOG_FILE) -> Counter:
    """Count failed login attempts per username from a log file."""
    counts: Counter = Counter()
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            user = parse_failed_user(line)
            if user:
                counts[user] += 1
    return counts


def main():
    try:
        counts = count_failures(LOG_FILE)
    except FileNotFoundError:
        print(f"Error: {LOG_FILE} not found.")
        return

    if not counts:
        print("No failed login attempts found.")
        return

    print("Top 5 failed login attempts by username:")
    for user, count in counts.most_common(5):
        print(f"{user}: {count}")


if __name__ == "__main__":
    main()
