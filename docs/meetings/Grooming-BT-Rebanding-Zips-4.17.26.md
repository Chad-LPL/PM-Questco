Taylor - Weekly Grooming/Office Hours - April 17
VIEW RECORDING: https://fathom.video/share/Stfm22KQe-CmU2xysGGoiUhVeWs1PzG9
Readiness gate removal from workbook @ 1:41

The team confirmed that the "ready for client call out" readiness gate can be removed from the workbook since Taylor will automatically handle macro running and formatting. Previously, this gate was needed to distinguish between pre-macro and post-macro versions, but with Taylor's automation, only one version of the workbook will exist. Jagger will delete this column as it's primarily for internal use and clients won't see it.

Baby Taylor end-to-end process flow @ 3:01

Chad outlined Baby Taylor's complete workflow: (1) batch and workbook generation in ClientSpace, (2) Baby Taylor validates rates against carrier rate books, confirms plan existence, checks mappings, and compares to previous year data, (3) flags whether regional plans are needed based on census zip codes, (4) runs Excel macros and adds Census data from Prism, (5) prefills class sheet columns and buy-down columns, (6) calculates renewal increase percentages with complex formulas, (7) runs validations including dental/vision carrier pairing and contributions, (8) after client execution, parses workbook data for Prism imports, and (9) generates CBE and Kashi files in ClientSpace. The team confirmed that Taylor will eliminate the need for macro execution steps since formatting will be pre-applied.

Regional plan validation using zip code files @ 10:29

The team discussed how to validate when regional plans are required. The existing zip code file is client-facing but can be repurposed for Taylor by: (1) renaming sheets to state codes (AZ, TX, NC), (2) keeping only the zip code column since other columns are irrelevant, and (3) creating a mapping sheet linking states to required plans. The logic is: check company headquarters zip code first—if in New York, New Jersey, or Connecticut, only offer tri-state plans; otherwise, check employee zip codes against state-specific zip code lists to determine if regional plans (Arizona, Texas, North Carolina) are needed. The team will confirm with Anna whether the plan mappings have changed from last year and whether MetLife Dental will also require this validation. Jagger will provide the state-to-plan mappings from last year.

Renewal increase percentage formula complexity @ 25:00

The renewal increase percentage formula on summary sheets calculates: (enrollment count × rate) summed by class and plan, then divided by the previous year's equivalent total, converted to a percentage. While complex due to multiple nested calculations, the logic is straightforward—comparing new total cost to prior year total cost. However, Excel has character limits for formulas, which becomes problematic for clients with 7+ classes. The team discussed potential solutions including breaking calculations into separate cells per class or using named variables. BabyTaylor currently adds this formula dynamically based on which classes and plans are populated. Some clients have unused classes marked "do not use" but these are still included in the workbook to prevent employee confusion in Prism elections.

Rebanding files and rate band validation @ 32:24

The team examined how different carriers structure rate bands in rebanding files: (1) BCBS uses simple tier numbers (e.g., "10"), (2) Aetna uses complex naming combining plan ID and band number (e.g., "QAET MC5000-70-1126"), and (3) Kaiser uses band numbers with associated factors. The rebanding file maps each client to their assigned rate band, which is critical because rates in Prism are organized by rate band and plan. In ClientSpace, BabyTaylor validated that correct rate bands were assigned; however, since Taylor will pull rates directly from Prism, this validation is no longer necessary—if rates are wrong, the issue is in Prism, not Taylor. Only BCBS, Aetna, and Kaiser assign rate bands; all other carriers (ancillary, dental, vision, OMQ) use global or static rates. The rebanding files include all clients who previously had the plan, even if their band didn't change, and are provided by carriers based on client lists Questco submits.

Workbook updates and admin console coordination @ 53:33

Chad indicated that the team needs to meet with Anna on Monday to finalize admin console configuration details. Jagger will meet with Anna to discuss workbook changes and will report back on feasibility for completing updates by end of next week. Chad plans to create a ticket to track the workbook modifications. This coordination is necessary before finalizing the change order discussion with Chris and Scott, which is scheduled for early next week.

GitHub repository with preliminary Taylor code @ 54:50

Jagger will upload preliminary Taylor code to a new GitHub repository that demonstrates how to pull all necessary data from Prism and build a workbook. The code includes examples of required Prism API calls, how to retrieve plans, rates, plan designs, benefit groups, and enrollment counts. This reference implementation will help the LaunchPad Lab team understand the data structure and API requirements when rebuilding the current plans and renewal plans sections. Jagger will share the repository link today.
