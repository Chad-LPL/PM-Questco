# Renewal Workbook (.xlsm) — Sheet Reference

This document describes how the **Questco Renewal Workbook** is structured: what each worksheet is for, how data flows, and how the **blank template** differs from a **filled client workbook** (example: *107 Claymore University Renewal Workbook Client Version.xlsm*).

The file is macro-enabled (`.xlsm`) and contains a VBA project (`vbaProject.bin`). Sheet logic relies heavily on **Excel defined names** (for example `BEGIN_CURRENT_HEALTH`, `Class1_Name`, `Benefit_Year_Display`) and on modern functions such as **`XLOOKUP`** and **`IFNA`/`IFERROR`** alongside **`VLOOKUP`**.

---

## Big picture

1. **Identity and readiness** live on **`CSExport`** (client name, number, contacts, benefit year, and a “ready for client” gate).
2. **Plan definitions** are normalized on **`CurrentPlans`** (current-year attributes) and **`RenewalPlans`** (renewal-year attributes, including “renewed from” keys and contribution metadata).
3. **Cross-class configuration** is on **`ClassesPlans`**: up to seven benefit classes, enrollment counts, and which unique plan codes apply—this drives how many rows “stack” on each class tab and how summary tabs know how many plans to show.
4. **Per-class presentation and math** happen on **`Class 1` … `Class 7`** (or equivalently renamed sheets such as **`PRIMARY`**, **`OWNERS`** in a client deliverable). Each class tab compares **current vs renewal vs alternate** premiums and pulls benefit detail via lookups into the plan tables.
5. **Rollups** appear on **`Total Cost`** (employer cost and enrollment by class) and on the **`* Summary`** sheets (side-by-side renewal options for medical, dental, vision, STD, LTD, life).
6. **Voluntary / ancillary marketing rates** appear on **`Ancillary Plans`** and **`Questco Voluntary`** (largely parallel content with minor labeling differences).
7. A **census** list may be included on a **`Census`** sheet in client-specific builds (not present in the blank template inventory analyzed here).

---

## Worksheet-by-worksheet

### `CSExport`

**Purpose:** Client-facing header data and export-oriented metadata.

- **Counts as of** (`B4`): As-of date for enrollment/census counts (also referenced from `ClassesPlans!B1`).
- **Client identity:** Name, DBA, client number (`B5`–`B7`).
- **Readiness:** Cell **`B8`** drives `A1`: if `B8` is not `"Yes"`, the workbook shows **“NOT READY FOR CLIENT”**; otherwise **“READY FOR CLIENT”**.
- **Contacts:** Benefit contact name/email/phone; optional benefit rep fields (`B9`–`B14`).
- **Benefit year** (`B15`): Feeds named values such as `Benefit_Year_Display` used in class tabs and titles.

Many workbook-wide names point here (for example `BenefitContactEmail`, `Benefit_Year_Display`).

---

### `ClassesPlans`

**Purpose:** Master mapping for **all benefit classes** and **unique plan codes** used in dropdowns and row-offset calculations.

- **Class grid (columns B–H):** For each of **Class1 … Class7**, holds **display name**, **code**, **current** counts (health/dental/vision), **renewal** counts (health/dental/vision/STD/LTD/life), and computed **start row** values for where each class’s blocks begin in the renewal/current sections (rows 18–23). Empty class names short-circuit formulas so unused classes do not contribute.
- **Unique plan lists:** Sections for **Health, Dental, Vision, STD, LTD, Life** with **PlanCode** and **SELECT PLAN** style inputs—aligned with named ranges like `BEGIN_UniqueHealthPlans`, `BEGIN_UniqueDentalPlans`, etc.

This sheet is the hub that ties **which plans exist** to **how class tabs and summaries scale**.

---

### `CurrentPlans`

**Purpose:** Wide, normalized **current plan year** attribute table.

- Organized in **blocks** by product: **Health**, **Dental**, **Vision**, **Other** (with headers around rows 2–3, 7–8, 12–13, 17–18).
- Typical columns include **PrimaryKey**, **PlanClass**, **PlanID**, **UniquePlanCode**, **Carrier**, **RiskTier**, **BenefitGroup**, tier counts (EO/ES/EC/FAM, etc.), and many **benefit design** columns (deductibles, copays, OOP max, pharmacy, services, etc.).
- Row 1 uses **column-index formulas** (`COLUMN(A3)` style) to support dynamic named columns such as `CURRENT_COL_*` (for example `CURRENT_COL_PlanClass`, `CURRENT_COL_OOP_MAX_INDIV`).

Class tabs use **`XLOOKUP`** on **`CurrentPlans!B:B`** (PlanClass key) to pull the correct column for **current** benefit text and numbers in the side-by-side comparison blocks.

---

### `RenewalPlans`

**Purpose:** Wide, normalized **renewal plan year** table—parallel in spirit to `CurrentPlans`.

- Blocks for **Health, Dental, Vision, STD, LTD, Life, Other**.
- Includes **Renewed From Primary Key**, **Renewed From Plan**, **Unique Plan Code**, **Effective Date**, **Contribution Method**, and the same style of benefit columns as the renewal year (referenced by `RENEW_COL_*` style names and `BEGIN_RENEW_*` anchors).

Named ranges (for example `BEGIN_RENEW_HEALTH`, `BEGIN_RENEWEDFROM_HEALTH`) anchor the renewal blocks for **VLOOKUP/IFNA** chains on class tabs and summaries.

---

### `Welcome`

**Purpose:** Cover / introduction (typical client workbook pattern).

- The used range may span **`A1:P58`**, but **cell content can be empty** if the page is built from **shapes, text boxes, or images**. Open in Excel to view the full layout.

---

### `Total Cost`

**Purpose:** Executive **roll-up by benefit class**.

- For each class (`Class1_Name` … `Class7_Name`), pulls **medical / dental / vision employee counts** and **current vs estimated renewal total employer cost** from fixed rows on each corresponding class sheet (for example references like `'Class 1'!R$870`–`R$872` and sums around **`J$867:J$869`** vs **`R$867:R$869`**—exact row anchors are part of the template contract).
- **Totals** row sums classes **5–11** in the template layout.

If class sheets are **renamed** (e.g. `PRIMARY` instead of `Class 1`), formulas must still resolve to the same internal sheet names or be updated accordingly.

---

### `Class 1` through `Class 7` (client variants may rename, e.g. `PRIMARY`, `OWNERS`)

**Purpose:** The main **per–benefit class** worksheet: premiums, contributions, and **benefit comparison** for **current vs renewal** (and **alternate** plan option).

Typical structure (repeated per class with `ClassN_*` names):

- **Title area:** Client name, client number, benefit year display.
- **Summary strip:** “All Plans Combined” / **Medical Renewal Summary** with current vs renewal **total annual premium**, enrollment, **annual difference**, **% change** (medical, dental, vision, life/disability).
- **Three-column layout:** **CURRENT PLANS** | **PLAN RENEWAL** | **ALTERNATE PLAN** with rates, contributions, EE counts, and **SELECT PLAN** dropdowns.
- **Health (and other lines):** Repeating blocks for each plan “slot”; rows beyond enrolled plan count may show **DELETE** to hide unused slots (`IF(A14>ClassN_CurrentHealthCount,"DELETE",...)` pattern).
- **Benefit Plan Summary:** For a constructed plan key (e.g. plan name + class), uses **`XLOOKUP`** against `CurrentPlans` and `RenewalPlans` to fill **in-network** and **out-of-network** rows (deductibles, OOP, office visits, pharmacy, common services, etc.).

Each class sheet is large (on the order of **900+ rows** in the template) because it repeats structured blocks for multiple plans and tiers.

---

### `Health Summary`, `Dental Summary`, `Vision Summary`

**Purpose:** **Side-by-side comparison** of up to many **renewal** medical/dental/vision plans.

- **Row 1–3:** Plan slot indices, **PlanCount**, and logic to mark extra columns **`DELETE`** when unused or when the plan code indicates **voluntary** (`"-VOL"` suffix pattern).
- **Row 5+:** **SELECT PLAN** row then **Premium** by tier (Employee Only, +Spouse, +Child(ren), Family).
- **Benefit rows** use **`VLOOKUP`** against named renewal ranges (for example `BEGIN_RENEW_HEALTH_PLANID:END_RENEW_HEALTH` for medical) keyed by **row codes** in column A (e.g. 25 = deductible individual, 29 = PCP, etc.—health rows mirror carrier file coding).

These sheets are **renewal-focused** comparison matrices, not a full duplicate of the class tab narrative.

---

### `STD Summary`, `LTD Summary`, `Life Summary`

**Purpose:** Same pattern as the medical/dental/vision summaries, for **disability and life**.

- **STD:** e.g. rate per **$10** of weekly benefit, elimination periods, benefit duration, **Teleguard**, etc.
- **LTD:** rate per **$100** of monthly benefit, min/max monthly benefit, elimination, definition of disability, Social Security integration, etc.
- **Life:** splits **employer** vs **voluntary** columns where plan text contains `"Vol"`; premium and benefit rows (coverage amount, GI max, AD&D, ADB, waiver of premium, etc.).

---

### `Ancillary Plans` and `Questco Voluntary`

**Purpose:** Reference / marketing-style **voluntary ancillary** rate tables (MetLife/Chubb-style layouts in the template), including voluntary STD/LTD, accident, critical illness, and age-banded rates.

- Content is **largely parallel** between the two sheets; differences are mainly **presentation** (for example **Bi-Weekly** vs **Monthly** rate labeling on comparable rows in the template).
- Not the primary driver of employer renewal cost math on `Total Cost`; they support **voluntary** product education and quoting context.

---

### `Census` (present in some client workbooks, e.g. Claymore)

**Purpose:** Employee-level listing for the engagement.

Example columns observed: **Employee ID**, **Name**, **Zipcode**, **State**, **Is Eligible for Regionalized Plans**, **Employment Type**, **PPO Required**.

This sheet is **not** part of the blank template’s tab list we inspected; it is **added or populated** for specific clients.

---

## Template vs filled “Claymore” workbook

| Aspect | Blank template | Claymore client workbook |
|--------|----------------|---------------------------|
| Benefit class tabs | Named **`Class 1` … `Class 7`** | First classes renamed (e.g. **`PRIMARY`**, **`OWNERS`**) while **`Class 3`–`Class 7`** may remain |
| `Census` | Absent | **Present** with employee rows |
| Core data sheets | `CSExport`, `ClassesPlans`, `CurrentPlans`, `RenewalPlans` | Same pattern |

Renaming class sheets changes **display names** only; **defined names** and formulas that still reference `'Class 1'!...` must remain consistent with Excel’s actual sheet names or be updated.

---

## Technical notes

- **Defined names:** Hundreds of names map logical roles to cells (for example `BEGIN_CURRENT_HEALTH` → `CurrentPlans!$A$4`, `BEGIN_RENEW_HEALTH` → `RenewalPlans!$B$4`). They are the backbone of **`VLOOKUP`** ranges and **dynamic** plan counts.
- **Array formulas:** Some cells use legacy **array formulas**; open-source parsers may show `ArrayFormula` objects rather than evaluated values until opened in Excel.
- **Macros:** Enable macros only from trusted sources; behavior was not audited here.
- **External links:** The package may include **externalLinks** (connections to other workbooks); refresh behavior depends on Excel’s trust and path settings.

---

## Questco discovery

Open questions for Questco (template ownership, Prism-to-cell coverage, macros, rates, census, OMQ injection) that affect Taylor implementation are tracked in **[Renewal-Workbook-Questco-Discovery.md](prd/Renewal-Workbook-Questco-Discovery.md)**. Fill the owner table and answers there as workshops complete.

---

## Sources

- Automated inspection of **Workbook Template.xlsm** and **107 Claymore University Renewal Workbook Client Version.xlsm** (sheet names, dimensions, formulas, and defined names) using `openpyxl` (April 2026).
