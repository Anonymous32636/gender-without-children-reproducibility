# Find the evidence behind each manuscript table and figure

This guide is an **index**, not a claim that confidential registry regressions can be replicated. The original paper and Danish supplement must be consulted for context.

| Manuscript item | Open first | Regenerate/check | Important qualification |
| --- | --- | --- | --- |
| **Table C1**: evidentiary priorities | Manuscript Introduction | Not quantitative | Editorial summary, not a dataset |
| **Table C2**: Danish code PPVs | `data/validation_counts.csv` | `outputs/validation_ppvs.csv`; `verify_package.py` | Exact binomial confidence intervals; corrected from numerator/denominator counts; printed last rows are misaligned |
| **Table C3**: Type II exclusion families | `data/table_c3_code_families.csv` | Compare with commentary and working-paper Appendix Table I.1 | Clinical interpretation of broad ICD families; NOT a reconstructed patient-level exclusion algorithm |
| **Figure C1**: Danish PPV rules | `data/validation_counts.csv` | `figures/Figure_C1_danish_code_ppv.png` | The Danish PPVs do not estimate Swedish sample PPVs |
| **Figure C2**: selection sensitivity | `data/published_effects.csv`, `data/figure9_approximate.csv` | `outputs/sample_selection_scenarios.csv`; `figures/Figure_C2_hypothetical_selection.png` | Hypothetical mean mixture, not a regression re-estimation or bound |
| **Figure C3**: Figure 9 visual readings | `data/figure9_approximate.csv` | `figures/Figure_C3_figure9_visual_readings.png` | Approximate visual readings, NOT author-tabulated estimates/SEs |
| **Figure C4**: gender-gap shares | `data/published_effects.csv` | `outputs/aggregate_checks.json`; `figures/Figure_C4_gender_gap_decomposition.png` | Ratios of model-derived point estimates, not independently estimated uncertainty |
| **Figure C5**: STEM estimates | `data/published_effects.csv` | `outputs/aggregate_checks.json`; `figures/Figure_C5_STEM_effects.png` | Normal ±1.96 SE intervals; group contrast not independently tested |

## Other numerical claims checked

- Swedish sample percentages (152/259 and 107/259), printed-vs-implied shares, and prevalence denominator: `outputs/aggregate_checks.json` from `data/published_effects.csv`.
- Figure 8 earnings 95% interval and reported-control-mean consistency check: same files.
- Early-career education 29.9% and education-plus-occupation 41.3% reductions: same files, from the original paper’s early-career gap and Figure 15 adjustments.
- Survey coefficient expressed relative to the benchmark mean, including conditional-on-mean confidence limits: same files; the denominator is treated as fixed for this illustration.
- Hypothetical 5-percentage-point counterfactual-error decomposition example: `outputs/aggregate_checks.json`; NOT an observed perturbation or confidence interval.

## Distinguish two sets of graphics

- `manuscript_figures/` contains **exact raster graphics used in the anonymous submitted DOCX**. These are provided to facilitate visual matching and are not regenerated pixel-for-pixel by the script.
- `figures/` contains **freshly generated explanatory plots** based on the tabular inputs. They convey the same numerical evidence with slightly different styling.
