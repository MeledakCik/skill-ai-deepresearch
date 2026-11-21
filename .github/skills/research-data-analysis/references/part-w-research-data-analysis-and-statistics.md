# PART W — RESEARCH DATA ANALYSIS AND STATISTICS

Use when a research or decision question requires inspecting a dataset, reproducing quantitative claims, comparing estimates or assessing statistical evidence. This skill supports method selection and reproducible analysis. Use a spreadsheet skill for workbook formatting and ordinary spreadsheet editing. Use academic-writing for thesis structure and prose.

## W1. State the quantity before calculating

Record the research question, observational unit, target population, period, outcome, comparison and decision the estimate informs. Name the numerator, denominator, units and data origin. Distinguish a population quantity from a sample estimate and an observed association from a causal effect. Keep the raw file unchanged and work on a derived copy.

## W2. Audit and transform the data

Inspect the schema, row count, identifier uniqueness, duplicate records, data types, allowed values, date and timezone handling, units, missingness and coverage before summarizing. Preserve the difference between zero, missing, not reported, not applicable and a failed feed. Log each exclusion, recode, join, filter and derived field with its reason. Reconcile subtotals to the source and check a small sample against the original records.

## W3. Choose methods that fit the design

Start with distributions, denominators and subgroup coverage. For comparisons, state the estimand, effect measure and uncertainty interval in the units a decision-maker can interpret. Select an inferential method from the sampling and study design, not from a desired significance threshold. Report assumptions and meaningful sensitivity checks. Mark unplanned subgroup analysis as exploratory and account for multiple comparisons where they change interpretation.

For causal claims, identify assignment or comparison design, plausible confounders, selection, measurement and time trends. State which assumptions the estimate needs. Do not infer causation from an observational association alone. A p-value does not give the probability that a hypothesis is true or measure the practical size of an effect. [American Statistical Association statement on p-values](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf)

When combining studies, compare their population, intervention or exposure, comparator, outcome, measure and follow-up before pooling. Inspect risk of bias and clinical, methodological and statistical heterogeneity. A pooled number does not repair incompatible studies. For intervention meta-analysis, follow the current field-specific methods and consult the [Cochrane analysis handbook](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10). Do not generalize a clinical-review method to another field without checking its assumptions.

## W4. Make the result reproducible

Keep a runnable analysis script or notebook with the input identity, transformations, method, assumptions, software and relevant package versions, random seed when applicable, and a clear run command. Verify key totals with an independent calculation or invariant. Report sample size, missingness, exclusions, estimate, interval and limitations alongside charts. Do not write illustrative or synthetic values as if they came from the supplied data. Do not send private or identifying data to an external service without the user's authorization.

Primary methods: [ASA p-value statement](https://www.amstat.org/asa/files/pdfs/P-ValueStatement.pdf) · [Cochrane data analysis and meta-analysis](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-10) · [Cochrane risk of bias](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-08)
