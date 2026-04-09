# [Spike] Workbook Generation Tool

## Traceability
- **Asana task ID:** `1213866893441645`
- **Section:** Backlog

## Product intent

Time-boxed investigation of libraries, tools, and approaches for programmatic Excel workbook generation and manipulation suitable for Taylor renewal templates.

## Product requirements (verifiable)

- Evaluate candidate tools against Taylor needs: template fidelity, performance, licensing, and operability in the chosen runtime.
- Evaluation must explicitly cover: **preservation of named ranges and `.xlsm` / VBA assets** (or agreed migration), **full workbook recalc** after cell writes, and **server-side licensing** constraints.
- Produce a written recommendation with tradeoffs and risks (including **pure library** vs **Excel COM/automation** for macros and calculation parity).

## Success criteria

- [ ] Recommendation document names chosen approach or short list with rationale.
- [ ] Spike does not block on production deployment; follow-up implementation tickets are identified.
- [ ] *Success criteria: refine with product (time-box duration and mandatory reviewers).*

## Out of scope

- Full renewal workbook feature implementation (covered by 2.6.x stories).

## Dependencies & references

- Related: [2.6.3 Backend rewrite of workbook-setup macro logic](./2.6.3-Backend-rewrite-of-workbook-setup-macro-logic.md), [Spike - Document Generation](./Spike-Document-Generation.md).
- Context: [Renewal-Workbook-Template-Sheet-Reference.md](../../Renewal-Workbook-Template-Sheet-Reference.md), [Renewal-Workbook-Questco-Discovery.md](../../prd/Renewal-Workbook-Questco-Discovery.md).

## Historical notes (Asana export)

_No notes in Asana export._
