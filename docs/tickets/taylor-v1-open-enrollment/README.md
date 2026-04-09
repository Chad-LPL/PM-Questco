# Taylor V1 — Open Enrollment Orchestration tickets

Local copies of Asana work items **Sprint 0** through **Sprint 6** and **Backlog** (from board export). Each file is named after the ticket title.

Each ticket is a short **product requirement** with **success criteria** (checklists) so developers can plan and verify work in Cursor or other tools without wading through template scaffolding. **Product intent** and **Historical notes** come from the Asana **Notes** field when present; traceability (task id, section, dates) is sourced from the board export.

- **Success criteria** are the default definition of done for implementation planning; refine them with product when a line marks `*Success criteria: refine with product…*`.
- **[asana_metadata.json](asana_metadata.json)** holds task ids, section, dates, and notes keyed by filename stem. Regenerate it after a fresh Asana CSV export: `python3 scripts/taylor_asana_metadata_from_csv.py /path/to/export.csv`, then regenerate tickets: `python3 scripts/taylor_tickets_prds.py`.
- To deepen requirements (Phase C), pull from [docs/README.md](../../README.md) (contracts, meetings) and edit the ticket markdown or extend overrides in [scripts/taylor_tickets_prds.py](../../scripts/taylor_tickets_prds.py).

### Workbook contract (renewal `.xlsm`)

- **Sheet reference:** [Renewal-Workbook-Template-Sheet-Reference.md](../../Renewal-Workbook-Template-Sheet-Reference.md) — what each worksheet does and how data flows.
- **Questco discovery:** [Renewal-Workbook-Questco-Discovery.md](../../prd/Renewal-Workbook-Questco-Discovery.md) — open questions, owner table, and (when filled) answers that drive Prism→cell mapping and validation.
- **Related tickets:** [2.6.1](./2.6.1-Generate-renewal-workbooks-using-Questco-templates.md) (template generation), [2.6.2](./2.6.2-Populate-workbooks-with-Prism-and-rate-book-data.md) (population + recalc), [2.6.3](./2.6.3-Backend-rewrite-of-workbook-setup-macro-logic.md) (setup macro parity), [2.2.5](./2.2.5-Adapter-mapping-layer-to-manage-Prism-schema-dependencies.md) (adapter + workbook mapping), [2.4.1](./2.4.1-Automated-ingestion-of-client-plan-census-enrollment-data-from-prism-and-rate-data-from-admin-console-upload.md), [2.4.2](./2.4.2-Pre-generation-validation-of-plans-plan-groups-and-rate-band-designation.md), [[Spike] Workbook Generation Tool](./Spike-Workbook-Generation-Tool.md).

**Asana alignment:** Local markdown here can change before Asana. After discovery or ticket edits stabilize, either **paste key bullets** into the matching Asana tasks or run the next **CSV export** and `taylor_asana_metadata_from_csv.py` / `taylor_tickets_prds.py` workflow so product can sync descriptions in bulk.

#### April 8, 2026 transcript sync (complete)

Repo tickets and [Taylor v1 PRD v1.2](../../prd/Taylor-v1-Open-Enrollment-Orchestration-PRD.md) were updated from [DeepDiveDiscoveryonWorkbook-4.8.26](../../meetings/DeepDiveDiscoveryonWorkbook-4.8.26) and [WeeklyStatusCall-4.8.26.md](../../meetings/WeeklyStatusCall-4.8.26.md). **Paste into Asana (one block per relevant task):**

- **Rates:** Future rates path: Kelly/Kim rebanding → LaWanda Prism import (file/columns confirmed). Questco to publish OE cutoff dates (Chris).
- **Bands:** Band assignment not stored as automation-friendly field in Prism; Taylor ingests **SharePoint rebanding file** (all clients). Late band change → rerun that client; runs should be idempotent.
- **Apply plan groups:** If OBP skipped, Taylor owns carrier→plan catalog; eligibility driven by rebanding + config—not ClientSpace map.
- **Validation:** Zip file + state→plan map; deny list (test/GAP/removed); dental/vision pairing rules.
- **Reporting:** Q Insights evaluation in flight; if it cannot deliver, build admin console reporting. Triggers for generate/regenerate: not ClientSpace-only—manual procedure / M365 / Taylor UI.
- **OMQ:** BSR = tracking checkboxes only; Excel template + regenerate workbook; age-banded quotes may be partial in workbook; batch stays in consultation.

#### April 9, 2026 — OMQ deep dive ([transcript](../../meetings/DeepDiveonOMQ-4.9.26), [PRD v1.3](../../prd/Taylor-v1-Open-Enrollment-Orchestration-PRD.md))

- **Ops:** Agency owns shopping; kickoff = proactive strategy or client request (CS → shopping task). Quote timing often **5–10 BD** (longer for appointment gaps / large group). **Temps** key template; agency does strategy + client summary; Taylor needs **full Prism-level** template fields.
- **Rates:** OMQ **does not** use master **rate bands**; quote-specific carrier rates. Composite vs age-banded varies by **state and carrier**.
- **Materials:** Non-Questco-broker OMQ may be **excluded** from Questco-branded guides (liability); DocuSign = **human send**, **separate attachments** (no sloppy merge / no zip). Final OMQ rates timing vs enrollment **still open**.
- **Audits:** Pre-audit ≈ workbook/rates vs Prism; post-audit Taylor **flags** deltas—full underwriting stays external; possible follow-up session.

Then **export CSV from Asana** (when ready) and regenerate `asana_metadata.json` / tickets if you use the scripted pipeline.

## Index


### Sprint 0

- [2.1.1 - Review and Define Technical Architecture](./2.1.1-Review-and-Define-Technical-Architecture.md)
- [2.1.2 - Align on User Stories and Acceptance Criteria](./2.1.2-Align-on-User-Stories-and-Acceptance-Criteria.md)

### Backlog

- [[Spike] Architecture and Infrastructure Needs](./Spike-Architecture-and-Infrastructure-Needs.md)
- [[Spike] Workbook Generation Tool](./Spike-Workbook-Generation-Tool.md)
- [[Spike] Admin Panel Framework or Library](./Spike-Admin-Panel-Framework-or-Library.md)
- [[Spike] Node Application Boilerplate Setup](./Spike-Node-Application-Boilerplate-Setup.md)
- [[Spike] Document Generation](./Spike-Document-Generation.md)
- [2.2.1 - Prism HR API Setup (authentication, connectivity, normalization)](./2.2.1-Prism-HR-API-Setup-authentication-connectivity-normalization.md)
- [2.2.2 - ClientSpace API integration and workflow status updates](./2.2.2-ClientSpace-API-integration-and-workflow-status-updates.md)
- [2.2.3 - SharePoint file storage configuration](./2.2.3-SharePoint-file-storage-configuration.md)
- [2.2.4 - Azure hosting architecture and environment setup](./2.2.4-Azure-hosting-architecture-and-environment-setup.md)
- [2.2.5 - Adapter/mapping layer to manage Prism schema dependencies](./2.2.5-Adapter-mapping-layer-to-manage-Prism-schema-dependencies.md)
- [2.2.6 - Client list synchronization with ClientSpace](./2.2.6-Client-list-synchronization-with-ClientSpace.md)
- [2.3.1 - Renewal state machine with defined milestones and transitions](./2.3.1-Renewal-state-machine-with-defined-milestones-and-transitions.md)
- [2.3.2 - Structured logging and audit trail of system events](./2.3.2-Structured-logging-and-audit-trail-of-system-events.md)
- [2.3.3 - Error handling, retries, and exception management](./2.3.3-Error-handling-retries-and-exception-management.md)
- [2.3.4 - Submission process for completed workbook ingestion](./2.3.4-Submission-process-for-completed-workbook-ingestion.md)
- [2.3.5 - Automated state transitions tied to signature, import, and audit events](./2.3.5-Automated-state-transitions-tied-to-signature-import-and-audit-events.md)
- [2.3.6 - Admin console providing renewal status visibility and light reporting](./2.3.6-Admin-console-providing-renewal-status-visibility-and-light-reporting.md)
- [2.4.1 - Automated ingestion of client, plan, census, enrollment data from prism, and rate data from admin console upload (uploaded on demand)](./2.4.1-Automated-ingestion-of-client-plan-census-enrollment-data-from-prism-and-rate-data-from-admin-console-upload.md)
- [2.4.2 - Pre-generation validation of plans, plan groups, and rate band designation](./2.4.2-Pre-generation-validation-of-plans-plan-groups-and-rate-band-designation.md)
- [2.4.3 - Data normalization prior to workbook population](./2.4.3-Data-normalization-prior-to-workbook-population.md)
- [2.4.4 - Server-side validation of submitted workbook data](./2.4.4-Server-side-validation-of-submitted-workbook-data.md)
- [2.5.1 - Role-based access control](./2.5.1-Role-based-access-control.md)
- [2.5.2 - Renewal status dashboard](./2.5.2-Renewal-status-dashboard.md)
- [2.5.3 - Rate book management](./2.5.3-Rate-book-management.md)
- [2.5.4 - OMQ plan data entry and management](./2.5.4-OMQ-plan-data-entry-and-management.md)
- [2.5.5 - Audit result review and exception monitoring](./2.5.5-Audit-result-review-and-exception-monitoring.md)
- [2.5.6 - Renewal pipeline reporting and workbook generation activity summaries](./2.5.6-Renewal-pipeline-reporting-and-workbook-generation-activity-summaries.md)
- [2.6.1 - Generate renewal workbooks using Questco templates](./2.6.1-Generate-renewal-workbooks-using-Questco-templates.md)
- [2.6.2 Populate workbooks with Prism and rate book data](./2.6.2-Populate-workbooks-with-Prism-and-rate-book-data.md)
- [2.6.3 - Backend rewrite of workbook-setup macro logic](./2.6.3-Backend-rewrite-of-workbook-setup-macro-logic.md)
- [2.6.4 - Programmatic sheet and workbook protection](./2.6.4-Programmatic-sheet-and-workbook-protection.md)
- [2.6.5 - SharePoint storage and posting URL to ClientSpace](./2.6.5-SharePoint-storage-and-posting-URL-to-ClientSpace.md)
- [2.6.6 - Workbook completion trigger automation](./2.6.6-Workbook-completion-trigger-automation.md)
- [2.6.7 - Retrieval, parsing, normalization, and validation of executed workbooks](./2.6.7-Retrieval-parsing-normalization-and-validation-of-executed-workbooks.md)
- [2.6.8.1 - Scheduled batch generation (including overnight runs)](./2.6.8.1-Scheduled-batch-generation-including-overnight-runs.md)
- [2.6.8.2 - Parallel generation of one, some, or all client workboos](./2.6.8.2-Parallel-generation-of-one-some-or-all-client-workboos.md)
- [2.7.1.1 - Automated generation of the Client Benefit Elections (CBE)](./2.7.1.1-Automated-generation-of-the-Client-Benefit-Elections-CBE.md)
- [2.7.1.2 - Automated generation of the Cost Sheets](./2.7.1.2-Automated-generation-of-the-Cost-Sheets.md)
- [2.7.1.3 - Automated generation of the Benefit Guide](./2.7.1.3-Automated-generation-of-the-Benefit-Guide.md)
- [2.7.1.4 - Automated generation of the combined packed](./2.7.1.4-Automated-generation-of-the-combined-packed.md)
- [2.7.2 - DocuSign Workflow via ClientSpace](./2.7.2-DocuSign-Workflow-via-ClientSpace.md)
- [2.7.3 - Signature tracking and automated workflow transitions](./2.7.3-Signature-tracking-and-automated-workflow-transitions.md)
- [2.8.1 - Generate plan setup and contribution import files](./2.8.1-Generate-plan-setup-and-contribution-import-files.md)
- [2.8.2 - Generate Open Enrollment workflow to invoke import](./2.8.2-Generate-Open-Enrollment-workflow-to-invoke-import.md)
- [2.8.3 - Manual review checkpoint prior to Prism submission](./2.8.3-Manual-review-checkpoint-prior-to-Prism-submission.md)
- [2.9.1.1 - Billing and contribution reconciliation](./2.9.1.1-Billing-and-contribution-reconciliation.md)
- [2.9.1.2 - Audit Reporting](./2.9.1.2-Audit-Reporting.md)
- [2.9.1.3 - ClientSpace task creation for exceptions](./2.9.1.3-ClientSpace-task-creation-for-exceptions.md)
- [2.9.2.1 - HSA Audit](./2.9.2.1-HSA-Audit.md)
- [2.9.2.2 - Orphan audits](./2.9.2.2-Orphan-audits.md)
- [2.9.2.3 - Enrollment mismatch detection](./2.9.2.3-Enrollment-mismatch-detection.md)
- [2.9.2.4 - Data discrepancy validation](./2.9.2.4-Data-discrepancy-validation.md)
- [2.9.2.5 - Exception routing through ClientSpace workflows](./2.9.2.5-Exception-routing-through-ClientSpace-workflows.md)
- [2.10.1.1 - Admin console form for manual entry of OMQ plan data](./2.10.1.1-Admin-console-form-for-manual-entry-of-OMQ-plan-data.md)
- [2.10.1.2 - Fields aligned to Prism plan schema](./2.10.1.2-Fields-aligned-to-Prism-plan-schema.md)
- [2.10.1.3 - Plan attributes, carrier, rate structure and core design elements](./2.10.1.3-Plan-attributes-carrier-rate-structure-and-core-design-elements.md)
- [2.10.1.4 - Server-side validation of entered data](./2.10.1.4-Server-side-validation-of-entered-data.md)
- [2.10.2.1 - Injection of OMQ plans into renewal workbook alongside Prism-sourced plans](./2.10.2.1-Injection-of-OMQ-plans-into-renewal-workbook-alongside-Prism-sourced-plans.md)
- [2.10.2.2 - Side-by-side comparison within standard workbook format](./2.10.2.2-Side-by-side-comparison-within-standard-workbook-format.md)
- [2.10.3.1 - Inclusion of selected OMQ plans in generated Prism import files](./2.10.3.1-Inclusion-of-selected-OMQ-plans-in-generated-Prism-import-files.md)
- [2.10.3.2 - OMQ plans follow standard Taylor validation and orchestration flow](./2.10.3.2-OMQ-plans-follow-standard-Taylor-validation-and-orchestration-flow.md)
- [2.11.1 - Production deployment in agreed environment](./2.11.1-Production-deployment-in-agreed-environment.md)
- [2.11.2 - End-to-end QA and validation](./2.11.2-End-to-end-QA-and-validation.md)
- [2.11.3 - Performance testing aligned to renewal season volume](./2.11.3-Performance-testing-aligned-to-renewal-season-volume.md)
