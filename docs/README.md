# Taylor v1 — project docs

## Contracts

| File | Purpose |
|------|---------|
| [contracts/LaunchPad_Lab_-_Taylor_v1_Build_-_MSA___SOW_-_For_Signature.pdf](contracts/LaunchPad_Lab_-_Taylor_v1_Build_-_MSA___SOW_-_For_Signature.pdf) | Executed MSA, Data Privacy Addendum (Exhibit A), and SOW 1 (original filename). |
| [contracts/LaunchPad_Taylor_v1_MSA_SOW_signed.pdf](contracts/LaunchPad_Taylor_v1_MSA_SOW_signed.pdf) | Same document, short alias. |

## Product narrative (start here)

| Resource | Purpose |
|----------|---------|
| [prd/Taylor-v1-Open-Enrollment-Orchestration-PRD.md](prd/Taylor-v1-Open-Enrollment-Orchestration-PRD.md) | Full PRD; **Sources** table links Fathom recordings for April 2026 workshops (flow review, workbook, OMQ, executed workbook/docs, Prism import, benefit guide). |
| [prd/Renewal-End-to-End-Flow.md](prd/Renewal-End-to-End-Flow.md) | Numbered renewal flow, Taylor vs Questco responsibilities, ticket traceability, legacy February walkthrough reconciliation. |

## Meetings (transcripts)

Full **WebVTT** transcripts live in-repo for early discovery. **April 2026** Fathom paste-ups (`.md`) capture discovery sessions; cross-check the [PRD](prd/Taylor-v1-Open-Enrollment-Orchestration-PRD.md) for decisions. Older or empty **`.md` placeholders** may still exist—do not rely on them until populated.

| File | Purpose |
|------|---------|
| [meetings/GMT20260211-183202_Recording.transcript.vtt](meetings/GMT20260211-183202_Recording.transcript.vtt) | Proposal review — scope, commercials discussion, architecture direction. |
| [meetings/GMT20260223-170806_Recording.transcript.vtt](meetings/GMT20260223-170806_Recording.transcript.vtt) | Taylor workflow walkthrough (16-step flow, validation, documents, Prism import). |
| [meetings/BenefitGuideDiscovery-4.14.26.md](meetings/BenefitGuideDiscovery-4.14.26.md) | Benefit guide discovery — static vs dynamic pages, per-class guides, workbook/Prism validation, SharePoint library, DocuSign (April 14, 2026). |
| [meetings/DeepDiveDiscovery-executedworkbookanddocgeneration-4.9.26.md](meetings/DeepDiveDiscovery-executedworkbookanddocgeneration-4.9.26.md) | Executed workbook and CBE / cost sheet / benefit guide generation (April 9, 2026). |
| [meetings/DiscoveryPrismImport-4.10.26.md](meetings/DiscoveryPrismImport-4.10.26.md) | Prism import discovery — two CSV files, rules complexity, OE grid (April 10, 2026). |

## Integration systems (SOW)

- **PrismHR** — system of record (client, plan, census, enrollment APIs; import files).
- **ClientSpace** — workflows, DocuSign, task routing, status for reps.
- **SharePoint** — workbook storage, links into ClientSpace, completion triggers.

## Work items (Asana → local specs)

| Location | Purpose |
|----------|---------|
| [tickets/taylor-v1-open-enrollment/](tickets/taylor-v1-open-enrollment/) | Sprint 0–6 and Backlog tickets: Asana metadata, **preserved Notes**, and a **Description** scaffold for LaunchPad developers planning work in Cursor. |

## Kickoff

See [KICKOFF.md](KICKOFF.md) for agenda, access checklist, and open questions to resolve with LPL / Questco.
