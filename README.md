# Anonymous reproducibility materials: *Gender Without Children—and the Limits of a Natural Experiment*

This package reproduces the **published-aggregate numerical checks, hypothetical sensitivity illustrations, and five original explanatory figures** used in an anonymous commentary. It contains **no author name, affiliation, correspondence information, acknowledgments, funding details, personal data, or confidential Swedish administrative records**.

## Reproduce

Use Python 3.10 or later:

```bash
python -m pip install -r requirements.txt
python run_analysis.py
```

The script regenerates `outputs/validation_ppvs.csv`, `outputs/sample_selection_scenarios.csv`, `outputs/aggregate_checks.json`, and five figures in `figures/`.

## Inputs and provenance

- `data/validation_counts.csv`: manually transcribed confirmed/assessed counts from Herlin et al. (2016), *Human Reproduction*, Supplementary Table SI; DOI https://doi.org/10.1093/humrep/dew220. Printed PPVs in the final rows are misaligned with their source counts. All confidence intervals are recalculated from counts using the two-sided exact Clopper–Pearson method.
- `data/published_effects.csv`: aggregate point estimates and standard errors from *Gender Without Children* (Landais et al., 2026), notably its Figures 8 and 13, Table 4, Appendix Table V.1 and case-flow appendix.
- `data/figure9_approximate.csv`: **visually approximated** point estimates from Figure 9 of the working paper. They are **not** exact author-supplied regression coefficients.

## Figure mapping

- **Figure C1**: Danish either-code vs both-code positive predictive values.
- **Figure C2**: hypothetical arithmetic sample-selection scenario beginning with either the reported 28.4% Figure 8 estimate or an approximate 22% Figure 9 control specification.
- **Figure C3**: approximate readings of different Figure 9 earnings specifications.
- **Figure C4**: fraction of the published gender earnings gap attributed to children by age range, calculated from Figure 13 reported point estimates.
- **Figure C5**: approximate normal 95% confidence intervals for two Table 4 STEM field-share coefficients.

These plots recreate the data and argument of the five figures; they are not guaranteed pixel-for-pixel replicas of the figures in the manuscript, which may use different graphic styling.

## Analytical boundaries

1. The Danish code-specific PPVs **cannot** be assigned directly to the Swedish MRKH sample.
2. The inclusion/exclusion calculation is deliberately a **hypothetical standardized mean-mixture**, not a re-estimation of covariate-adjusted administrative-registry regressions or a causal bias bound.
3. The Figure 9 bar readings are visual approximations. Original tabulated coefficients and SEs are not available in the supplied paper.
4. The dynamic IV model, clinical subtype assignments, and numerical confidence limits for the near-90% decomposition **cannot be independently replicated without the authors' confidential data or estimation outputs**.
5. Published paper text and supplementary data are not redistributed; only small numerical facts and derived calculations needed for independent verification are included.

## Package integrity and anonymity

The files are intentionally author-neutral. No personal names other than authors of cited source publications occur in the package. No personal email, blog URL, institutional affiliation, or repository account is supplied. Bibliographic names identify external research only.
