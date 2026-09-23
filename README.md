# econ5200-lab02-deflation
Daqian Chen
# Index Integrity — Deflation, Substitution Bias & Goodhart

## Objective

This project evaluates the reliability of economic indexes and performance metrics by debugging a deflation pipeline, measuring CPI substitution bias, detecting Goodhart’s Law, and building reusable monitoring tools.

## Methodology

- Diagnosed and corrected four bugs in a nominal-to-real deflation pipeline, including an output-unit error that produced values in 1982–84 dollars while labeling them as 2020 dollars.
- Aligned wage and CPI series by shared dates, removed missing observations, and used the average CPI for the selected base year.
- Compared CPI-U with Chained CPI-U to measure upper-level substitution bias using compounded annual inflation rates.
- Distinguished an index-point difference from a percentage-point difference in annual inflation rates.
- Evaluated KPI integrity using DAU/MAU as the primary metric and time per session as a counter-metric.
- Detected Goodhart’s Law through a correlation sign flip between the organic-growth and gaming phases.
- Created and tested a reusable `deflation_utils.py` module containing `deflate_series()`.
- Built an interactive index-integrity monitor using pandas, Plotly, and ipywidgets to examine CPI comparisons and rolling KPI correlations.

## Key Findings

The CPI comparison produced an average annual inflation rate of **2.61% for CPI-U** and **2.35% for C-CPI-U**, implying an estimated **upper-level substitution bias of 0.27 percentage points per year**.

The cumulative difference between the indexes corresponded to approximately **0.50 index points per year**. This is not the same as the 0.27 percentage-point inflation gap because index points measure differences in index levels, while inflation rates reflect compounded percentage growth.

The KPI analysis also provided a clear example of Goodhart’s Law. During the organic-growth phase, DAU/MAU and time per session had a strong positive correlation of **+0.93**. During the gaming phase, the correlation reversed to **-0.96**, showing that the primary engagement metric continued to improve while the counter-metric deteriorated.

These results demonstrate why economic and business metrics should be evaluated with careful attention to measurement definitions, units, counter-metrics, and the behavioral responses created when a metric becomes a target.
