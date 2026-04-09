#!/usr/bin/env python3
"""
Regenerate Taylor V1 ticket markdown files with a short PRD + success-criteria shape.
Run from repo root: python3 scripts/taylor_tickets_prds.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

TICKET_DIR = Path(__file__).resolve().parent.parent / "docs" / "tickets" / "taylor-v1-open-enrollment"
METADATA_FILE = TICKET_DIR / "asana_metadata.json"

# Optional richer content for exemplar / high-signal tickets (stem without .md)
OVERRIDES: dict[str, dict] = {
    "2.1.1-Review-and-Define-Technical-Architecture": {
        "intent": (
            "Establish a reviewed, agreed technical architecture for Taylor V1 open enrollment "
            "orchestration on Azure so implementation can proceed without rework from ambiguous "
            "infrastructure or integration choices."
        ),
        "requirements": [
            "Architecture covers Azure resources, integration patterns, data services, identity, "
            "logging/monitoring, and deployment environments relevant to Taylor V1.",
            "Written architecture documentation (or diagram set) exists and is approved by "
            "Questco / LaunchPad stakeholders responsible for sign-off.",
            "Decisions explicitly note implications for Prism HR, ClientSpace, SharePoint, and "
            "other named integrations in SOW scope.",
        ],
        "success": [
            "[ ] Architecture document or equivalent (diagrams + narrative) is stored in an "
            "agreed location and linked from this ticket or project docs.",
            "[ ] Stakeholder review is complete and recorded (meeting notes, email sign-off, or "
            "approval comment in Asana).",
            "[ ] No unresolved blocking questions remain for Sprint 1+ build work; follow-ups are "
            "tracked as separate tickets if needed.",
        ],
        "out_of_scope": None,
        "deps": [
            "[docs/README.md](../../README.md) (contracts, meeting assets)",
            "Downstream tickets: foundation work in 2.2.x–2.4.x assumes this architecture baseline.",
        ],
    },
    "2.1.2-Align-on-User-Stories-and-Acceptance-Criteria": {
        "intent": (
            "Produce a single agreed backlog of user stories and acceptance criteria with enough "
            "precision that development and QA can execute without repeated scope clarification."
        ),
        "requirements": [
            "User stories and technical requirements include implementation-relevant detail and "
            "testable acceptance criteria.",
            "Material is reviewed and approved by product/operations stakeholders for Taylor V1.",
            "Traceability exists from major backlog items to SOW or signed scope (reference links or "
            "mapping table).",
        ],
        "success": [
            "[ ] Approved story/criteria set is published in an agreed tracker (Asana) and/or docs.",
            "[ ] Each in-scope epic or feature area has at least one acceptance criterion that is "
            "objectively verifiable.",
            "[ ] Gaps or TBDs are explicitly listed—not left implicit in narrative only.",
        ],
        "out_of_scope": None,
        "deps": [
            "Depends on: [2.1.1 - Review and Define Technical Architecture](./2.1.1-Review-and-Define-Technical-Architecture.md) for technical constraints.",
            "[docs/README.md](../../README.md)",
        ],
    },
    "2.2.1-Prism-HR-API-Setup-authentication-connectivity-normalization": {
        "intent": (
            "Enable reliable, authenticated access to Prism HR APIs and normalize responses so "
            "downstream Taylor services consume a stable internal representation of client, plan, "
            "census, and enrollment data."
        ),
        "requirements": [
            "Application authenticates to Prism HR APIs using agreed credentials and token/credential "
            "rotation approach.",
            "Connectivity failures are distinguishable (auth vs network vs API error) in logs or "
            "structured errors.",
            "Normalized data model (or adapter output) is defined and used for ingestion paths that "
            "feed renewal processing.",
        ],
        "success": [
            "[ ] Successful authenticated call to Prism HR in non-production with logged request "
            "correlation id.",
            "[ ] Sample responses are normalized and persisted or logged in a redacted fixture for "
            "regression tests.",
            "[ ] *Success criteria: refine with product (API surface, PII handling, rate limits—"
            "source: Prism docs + SOW).*",
        ],
        "out_of_scope": None,
        "deps": [
            "[2.2.5 - Adapter/mapping layer](./2.2.5-Adapter-mapping-layer-to-manage-Prism-schema-dependencies.md)",
            "[2.4.1 - Automated ingestion](./2.4.1-Automated-ingestion-of-client-plan-census-enrollment-data-from-prism-and-rate-data-from-admin-console-upload.md)",
        ],
    },
    "2.6.1-Generate-renewal-workbooks-using-Questco-templates": {
        "intent": (
            "Automatically produce renewal workbooks from Questco-standard Excel templates so "
            "benefits analysts do not manually copy base structure each renewal."
        ),
        "requirements": [
            "System generates a workbook file from approved Questco renewal template(s) for a given "
            "client/renewal context.",
            "Generated file preserves required sheet names, structure, and protection expectations "
            "defined for the template version in use.",
            "Template version in use is identifiable (metadata, filename convention, or log) for audit.",
        ],
        "success": [
            "[ ] Generation runs without manual Excel steps for a representative renewal scenario.",
            "[ ] Output opens in Excel; structural checklist against template spec passes (TBD "
            "checklist owner).",
            "[ ] *Success criteria: refine with product (exact template inventory and versioning—"
            "source: Questco template owner).*",
        ],
        "out_of_scope": None,
        "deps": [
            "Follows: [2.4.x data ingestion](./2.4.1-Automated-ingestion-of-client-plan-census-enrollment-data-from-prism-and-rate-data-from-admin-console-upload.md); "
            "next: [2.6.2 Populate workbooks](./2.6.2-Populate-workbooks-with-Prism-and-rate-book-data.md).",
        ],
    },
    "Spike-Workbook-Generation-Tool": {
        "intent": (
            "Time-boxed investigation of libraries, tools, and approaches for programmatic Excel "
            "workbook generation and manipulation suitable for Taylor renewal templates."
        ),
        "requirements": [
            "Evaluate candidate tools against Taylor needs: template fidelity, performance, "
            "licensing, and operability in the chosen runtime.",
            "Produce a written recommendation with tradeoffs and risks.",
        ],
        "success": [
            "[ ] Recommendation document names chosen approach or short list with rationale.",
            "[ ] Spike does not block on production deployment; follow-up implementation tickets "
            "are identified.",
            "[ ] *Success criteria: refine with product (time-box duration and mandatory reviewers).*",
        ],
        "out_of_scope": "Full renewal workbook feature implementation (covered by 2.6.x stories).",
        "deps": [
            "Related: [2.6.3 Backend rewrite of workbook-setup macro logic](./2.6.3-Backend-rewrite-of-workbook-setup-macro-logic.md), "
            "[Spike - Document Generation](./Spike-Document-Generation.md).",
        ],
    },
}

CATEGORY_INTENT_SUFFIX: dict[str, str] = {
    "2.1": "Planning and alignment for Taylor V1.",
    "2.2": "Foundational integrations and platform configuration for Taylor V1.",
    "2.3": "Orchestration, reliability, and observability for renewal processing.",
    "2.4": "Data ingestion, validation, and normalization ahead of workbook and document generation.",
    "2.5": "Admin console capabilities for operators managing renewals and supporting data.",
    "2.6": "Renewal Excel workbook generation, completion, and parsing pipeline.",
    "2.7": "Benefits document package generation and e-signature workflow hooks.",
    "2.8": "Prism import file generation and submission workflow.",
    "2.9": "Billing, audit, and exception handling integrated with ClientSpace.",
    "2.10": "Off-Market Quote (OMQ) plan capture and inclusion in renewal and imports.",
    "2.11": "Release validation, performance, and production readiness.",
}


def read_title_line(path: Path) -> str:
    first = path.read_text(encoding="utf-8").splitlines()[:1]
    if first and first[0].startswith("# "):
        return first[0][2:].strip()
    return path.stem.replace("-", " ")


def load_metadata() -> dict[str, dict]:
    if not METADATA_FILE.is_file():
        raise SystemExit(
            f"Missing {METADATA_FILE}. Generate it from the Asana CSV export (see README in {TICKET_DIR})."
        )
    data = json.loads(METADATA_FILE.read_text(encoding="utf-8"))
    return data


def strip_title_number(title: str) -> str:
    m = re.match(r"^[\d.]+(?:\.[\d]+)*\s*-\s*(.+)$", title.strip())
    if m:
        return m.group(1).strip()
    m2 = re.match(r"^\[Spike\]\s*(.+)$", title.strip(), re.I)
    if m2:
        return m2.group(1).strip()
    return title.strip()


def category_key(stem: str) -> str | None:
    m = re.match(r"^(2\.\d+)", stem)
    if m:
        return m.group(1)
    return None


def is_spike(stem: str) -> bool:
    return stem.startswith("Spike-")


def substantive_notes(notes: str) -> bool:
    if not notes or not notes.strip():
        return False
    compact = " ".join(notes.split())
    if "No notes in Asana export" in compact:
        return False
    return True


def default_sections(
    stem: str, title: str, short: str, notes: str, has_notes: bool
) -> dict:
    ck = category_key(stem)
    suffix = f" {CATEGORY_INTENT_SUFFIX[ck]}" if ck and ck in CATEGORY_INTENT_SUFFIX else ""

    if has_notes:
        n = re.sub(r"\s+", " ", notes.strip())
        if n and not n.endswith((".", "!", "?")):
            n += "."
        intent = (
            f"{n} This supports Taylor V1 open enrollment orchestration.{suffix}"
        )
    else:
        intent = (
            f"Deliver the capability described in the ticket title: {short}. "
            f"This is part of Taylor V1 open enrollment orchestration.{suffix}"
        )

    if is_spike(stem):
        requirements = [
            f"Investigate and document how to satisfy: {short}, including options, risks, and recommendations.",
            "Produce artifacts (write-up, spike code, or prototype) sufficient for the team to estimate and split follow-on implementation work.",
        ]
        success = [
            "[ ] Written summary of findings, options, and a clear recommendation (or decision to defer).",
            "[ ] Follow-up tickets or tasks are identified where production implementation is required.",
            "[ ] *Success criteria: refine with product (spike time-box, reviewers, and mandatory decisions).*",
        ]
    else:
        requirements = [
            f"The implemented behavior satisfies: {short}.",
            "Completion can be verified without unstated assumptions: evidence aligns with the success criteria below.",
            "Errors, edge cases, and operator-visible states relevant to this scope are handled or explicitly deferred with tracking.",
        ]
        success = [
            f"[ ] The outcome for “{short}” is demonstrable in a non-production or staging environment.",
            "[ ] Verification evidence exists (automated tests, scripted manual test results, or signed QA checklist).",
            "[ ] Integration touchpoints (if any) are exercised at least once with logs or captured responses suitable for audit.",
            "[ ] *Success criteria: refine with product (SOW, Asana, or design review) for thresholds not inferable from the title alone.*",
        ]

    return {
        "intent": intent,
        "requirements": requirements,
        "success": success,
        "out_of_scope": None,
        "deps": [
            "Index: [README.md](./README.md). Project assets: [docs/README.md](../../README.md).",
        ],
    }


def format_traceability(meta: dict) -> list[str]:
    lines = ["## Traceability"]
    tid = meta.get("task_id") or "—"
    lines.append(f"- **Asana task ID:** `{tid}`" if tid != "—" else "- **Asana task ID:** —")
    if meta.get("section"):
        lines.append(f"- **Section:** {meta['section']}")
    if meta.get("sprint_field"):
        lines.append(f"- **Sprint (custom field):** {meta['sprint_field']}")
    if meta.get("assignee"):
        lines.append(f"- **Assignee:** {meta['assignee']}")
    if meta.get("start_due"):
        lines.append(f"- **Start / due:** {meta['start_due']}")
    if meta.get("est_dev_days"):
        lines.append(f"- **Est. dev days:** {meta['est_dev_days']}")
    return lines


def build_markdown(
    stem: str,
    title: str,
    meta: dict,
    notes: str,
    sections: dict,
) -> str:
    has_notes = substantive_notes(notes)

    out: list[str] = []
    out.append(f"# {title}")
    out.append("")
    out.extend(format_traceability(meta))
    out.append("")
    out.append("## Product intent")
    out.append("")
    out.append(sections["intent"])
    out.append("")
    out.append("## Product requirements (verifiable)")
    out.append("")
    for r in sections["requirements"]:
        out.append(f"- {r}")
    out.append("")
    out.append("## Success criteria")
    out.append("")
    for s in sections["success"]:
        line = s.strip()
        if not line.startswith("-"):
            line = "- " + line if line.startswith("[") else "- " + line
        out.append(line)
    out.append("")

    oos = sections.get("out_of_scope")
    if oos:
        out.append("## Out of scope")
        out.append("")
        out.append(f"- {oos}")
        out.append("")

    out.append("## Dependencies & references")
    out.append("")
    for d in sections["deps"]:
        out.append(f"- {d}")
    out.append("")

    out.append("## Historical notes (Asana export)")
    out.append("")
    if has_notes:
        out.append(notes)
    else:
        out.append("_No notes in Asana export._")
    out.append("")
    return "\n".join(out)


def main() -> None:
    if not TICKET_DIR.is_dir():
        raise SystemExit(f"Missing ticket dir: {TICKET_DIR}")

    metadata = load_metadata()

    for path in sorted(TICKET_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        stem = path.stem
        meta = metadata.get(stem)
        if not meta:
            raise SystemExit(f"No Asana metadata for {path.name}; update {METADATA_FILE.name}")

        title = read_title_line(path)
        notes = (meta.get("notes") or "").strip()

        if stem in OVERRIDES:
            sections = {**OVERRIDES[stem]}
            if isinstance(sections.get("deps"), str):
                sections["deps"] = [sections["deps"]]
        else:
            short = strip_title_number(title)
            sections = default_sections(
                stem, title, short, notes, has_notes=substantive_notes(notes)
            )

        body = build_markdown(stem, title, meta, notes, sections)
        path.write_text(body, encoding="utf-8")
        print(f"Wrote {path.relative_to(TICKET_DIR.parent.parent)}")


if __name__ == "__main__":
    main()
