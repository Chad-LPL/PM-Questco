# Kickoff checklist — Taylor v1

Use this in the kickoff call with LaunchPad Lab and Questco. Full framing and transcript notes live in your Cursor plan (`sow_intake_and_setup_86896453`); this file is the short operational view.

## Goals

- Confirm timeline and **milestone dates** (SOW payment schedule vs actual sprint start).
- Align on **definition of done** per sprint and for the **final milestone / payment**.
- Surface **blockers**: API access, templates, samples.

## Agenda (60–90 min)

- **Roles** — Questco PO / ops SMEs (Karen, Anna, Jagger); engineering (Chris or delegate); LPL PM, architect, devs (confirm names).
- **Workflow** — Optional 5 min; otherwise team reads `docs/meetings/GMT20260223-170806_Recording.transcript.vtt` summary / plan.
- **Open questions** (prioritize ~15 min on items 1–3):
  1. **Post-build support** — ~$8k/mo stabilization / OE hypercare discussed on proposal call: signed elsewhere, verbal only, or TBD? Who owns an amendment if needed?
  2. **Sprint 6 vs go-live** — Hardening → live with implementation clients → tweaks before OE: inside **$220k** through final milestone or **support / T&M**? What is “done” for last invoice?
  3. **Demo cadence** — End-of-sprint demos + test environments: explicit commitment and owners?
  4. **FinOps / Azure TCO** — Who produces first monthly burn model and by when?
  5. **Staffing** — Any open items on nearshore/offshore, same team into support, named architect?
  6. **V2 / bundle** — Exec need for written V2 range; timing vs V1 delivery.
  7. **Spikes (assign owners/dates)** — Headless Excel/macros; ClientSpace ↔ DocuSign multi-doc envelopes; live SharePoint rate file vs admin re-upload; control-group / “no missed client” admin design.

## Access checklist

- [ ] Prism API — credentials, documentation, sandbox
- [ ] ClientSpace API — and DocuSign flow behavior
- [ ] SharePoint — site/library for workbooks, permissions for LPL
- [ ] Azure — subscription, RBAC for LPL, any IP allowlists

## Artifacts from Questco (target dates)

- Workbook template(s)
- Sample rate books (standard + client-specific)
- CBE, cost sheet, benefit guide templates
- Prism import templates
- Jagger’s post-enrollment audit checklist

## Follow-ups

- Architecture review — target date
- Daily / Slack rhythm
- Risk register owner

## Open follow-ups (from Anna workflow review — 2026-04-07)

Source: [meetings/AnnaSync-WorkflowReview-4.7.26.md](meetings/AnnaSync-WorkflowReview-4.7.26.md). Track until closed; related ticket context is in [tickets/taylor-v1-open-enrollment/](tickets/taylor-v1-open-enrollment/).

| Item | Owner |
|------|--------|
| Workspace / data form ID report for ClientSpace API work | Dimple |
| Assess Prism import of carrier rate grid into **future rate band** (lift vs Taylor-assisted path) | Anna / Dimple + **LaWanda** |
| DocuSign **48h** envelope expiry — confirm configuration vs accidental default | Dimple |
| ClientSpace **Reset DocuSign** / extended **Send DocuSign** in failure states — feasibility | Dimple (with Jagger) |
| Prism import design sessions — include **analyst** stakeholder from the start | Questco + LPL scheduling |
| **Q Insights** status vs executive renewal reporting (overlap with Taylor / ClientSpace) | Dimple / Chris check-in |
