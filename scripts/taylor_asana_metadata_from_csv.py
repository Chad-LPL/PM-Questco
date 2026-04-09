#!/usr/bin/env python3
"""
Build docs/tickets/taylor-v1-open-enrollment/asana_metadata.json from an Asana CSV export.
Matches each local ticket filename stem to a CSV row by normalizing the task title.

Usage:
  python3 scripts/taylor_asana_metadata_from_csv.py /path/to/Taylor_V1_-_Open_Enrollment_Orchestration.csv
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TICKET_DIR = REPO / "docs" / "tickets" / "taylor-v1-open-enrollment"
OUT = TICKET_DIR / "asana_metadata.json"


def alnum_only(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def expand_parens(s: str) -> str:
    return re.sub(r"\(([^)]*)\)", r" \1 ", s)


def normalize_title_tail(name: str) -> str:
    name = name.strip().strip('"')
    m = re.match(r"^\[Spike\]\s*(.+)$", name, re.I)
    if m:
        rest = m.group(1)
    else:
        m = re.match(r"^[\d.]+\s*-\s*(.+)$", name)
        if m:
            rest = m.group(1)
        else:
            m = re.match(r"^([\d.]+)\s+(.+)$", name)
            rest = m.group(2) if m else name
    rest = expand_parens(rest)
    rest = re.sub(r"uploaded\s+on\s+demand", "", rest, flags=re.I)
    return alnum_only(rest)


def stem_tail_key(stem: str) -> str:
    m = re.match(r"^(?:\d+(?:\.\d+)*)-(.+)$", stem)
    if m:
        return alnum_only(m.group(1))
    if stem.lower().startswith("spike-"):
        return alnum_only(stem[6:])
    return alnum_only(stem)


def main() -> None:
    csv_path = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else Path.home() / "Downloads" / "Taylor_V1_-_Open_Enrollment_Orchestration.csv"
    )
    if not csv_path.is_file():
        raise SystemExit(f"CSV not found: {csv_path}")

    rows = []
    with open(csv_path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sec = (row.get("Section/Column") or "").strip()
            if sec not in ("Sprint 0", "Backlog"):
                continue
            rows.append(row)

    by_key: dict[str, dict] = {}
    for row in rows:
        name = (row.get("Name") or "").strip()
        tid = (row.get("Task ID") or "").strip().strip('"')
        if not name or not tid:
            continue
        k = normalize_title_tail(name)
        by_key[k] = row

    metadata: dict[str, dict] = {}
    missing: list[tuple[str, str]] = []
    for p in sorted(TICKET_DIR.glob("*.md")):
        if p.name == "README.md":
            continue
        stem = p.stem
        tk = stem_tail_key(stem)
        row = by_key.get(tk)
        if not row:
            missing.append((stem, tk))
            continue
        notes = (row.get("Notes") or "").strip()
        sd = (row.get("Start Date") or "").strip()
        dd = (row.get("Due Date") or "").strip()
        start_due = f"{sd} / {dd}".strip() if (sd or dd) else ""
        metadata[stem] = {
            "task_id": row.get("Task ID", "").strip().strip('"'),
            "section": (row.get("Section/Column") or "").strip(),
            "assignee": (row.get("Assignee") or "").strip(),
            "start_due": start_due,
            "sprint_field": (row.get("Sprint") or "").strip(),
            "est_dev_days": (row.get("Est Dev Days") or "").strip(),
            "notes": notes,
            "asana_name": (row.get("Name") or "").strip(),
        }

    if missing:
        raise SystemExit(f"Unmatched ticket files (update matching logic): {missing}")

    OUT.write_text(json.dumps(metadata, indent=2, sort_keys=True), encoding="utf-8")
    print(f"Wrote {len(metadata)} entries to {OUT}")


if __name__ == "__main__":
    main()
