# Anonymous reproducibility materials — *Gender Without Children—and the Limits of a Natural Experiment*

This package accompanies an **anonymous commentary** on the 2026 working paper *Gender Without Children*. It allows readers to independently check the commentary’s **published-aggregate arithmetic, hypothetical sensitivity illustrations, and five explanatory figures**.

**Scope:** This is a reproducibility package for *the commentary’s independent checks*, **not** a replication of the underlying Swedish administrative-register study. It includes no person-level data, unpublished Swedish estimates, or re-estimated causal regressions.

## Quick start (Windows, macOS or Linux)

1. Extract the complete ZIP. Install **Python 3.10+**, and open a command prompt / terminal **inside the extracted folder** (the folder containing `run\_analysis.py`).
2. Install the three required packages and regenerate numerical checks and graphs:

```bash
   python -m pip install -r requirements.txt
   python run\_analysis.py
   python verify\_package.py
   ```

   On Windows, use `py` instead of `python` if that is your Python launcher. No login, API token, internet download of data, or proprietary statistical software is needed **after** dependencies are installed.

3. Read `CLAIM\_TO\_FILE\_GUIDE.md` to find the source and calculation for a particular figure, table or numerical criticism.

**Expected result:** the scripts print `PASS`; the `outputs/` folder contains three result files, and `figures/` contains five generated plots. The analysis can be rerun in place without changing input CSV files. Minor graph rendering differences across Matplotlib versions are not evidence of changed calculations.

Optional: before the first run, `python verify\_package.py --strict-archive` verifies every file against the archived SHA-256 manifest. The normal `python verify\_package.py` checks source hashes and calculated numeric results after regeneration.

## What's inside

|Location|Purpose|
|-|-|
|`run\_analysis.py`|Read documented CSV inputs, perform arithmetic checks, generate plots and outputs|
|`verify\_package.py`|Independently check source-file hashes, published-count arithmetic, main results, and PNG presence|
|`data/validation\_counts.csv`|Herlin et al. (2016) Supplementary Table SI numerators, denominators and printed PPVs|
|`data/published\_effects.csv`|Published aggregate values/standard errors with source pointers|
|`data/figure9\_approximate.csv`|Clearly labeled approximate visual readings of Figure 9|
|`data/table\_c3\_code\_families.csv`|Commentary’s interpretive Table C3, linking broad code families to descriptions|
|`outputs/`|Calculated diagnostic PPVs/CIs, sample-selection illustrations, further checks|
|`figures/`|Five script-generated numerical plots|
|`manuscript\_figures/`|The exact five raster figures embedded in the anonymous manuscript|
|`CLAIM\_TO\_FILE\_GUIDE.md`|Item-by-item map from manuscript tables, figures and claims to evidence|
|`manifest\_sha256.json`|Original-archive integrity hashes (excludes its own hash)|

All input rows are **transcribed from public publications or explicitly labeled commentary interpretations**; they are not individual-level observations. The analysis script reads values from the CSV files rather than silently duplicating published estimates as hard-coded constants. Deliberately hypothetical values, such as the number of possibly excluded cases restored (0, 10, 25, 50), remain in the code and are explicitly labeled.

## Sources and provenance

* **Landais, Lundborg, Pazem, Plug \& Vikström (2026), *Gender Without Children*, 2 March working paper:** Figures 8, 9, 13 and 15, Table 4, Appendix Table V.1, case-identification appendix and Appendix Table I.1. Public working-paper URL: https://econ.lse.ac.uk/staff/clandais/cgi-bin/Articles/GenderWithoutKids\_Complete.pdf
* **Herlin et al. (2016), *Prevalence and patient characteristics of Mayer–Rokitansky–Küster–Hauser syndrome*, <i>Human Reproduction</i>, Supplementary Table SI:** https://doi.org/10.1093/humrep/dew220

Both sources are external works authored by researchers being discussed; their names are **bibliographic citations, not identities of this commentary’s author(s)**. The working paper and Danish supplementary PDF are **not redistributed** in this package; their numerical values sufficient for the listed checks are transcribed with source pointers.

## What the five figures show

* **C1:** 167/292 = **57.2%** Danish either-code PPV versus 78/84 = **92.9%** both-code PPV; Clopper–Pearson exact 95% intervals calculated from counts. The Danish supplement’s last four printed PPVs/CIs are shifted relative to their patient counts.
* **C2:** Hypothetical arithmetic addition of potentially wrongly excluded Type I patients to 152 retained, under a comparison-group-mean assumption. The 28.4% starting point is published Figure 8; approximately 22% is read visually from Figure 9. **Not an adjusted-regression re-estimation or a causal bias bound.**
* **C3:** Approximate visually read Figure 9 bar heights; no exact bar coefficient, SE, or CI is invented.
* **C4:** Shares 70.5% (ages 20–42) and 88.0% (ages 32–42), ratios independently calculated from published gender gaps. These are model-derived point estimates, not uncertainty bounds.
* **C5:** Two Table 4 STEM estimates with conventional normal ±1.96 SE intervals; overlapping intervals do not test the difference between subgroup and overall specifications.

## Analytical limitations and correct interpretation

1. The Danish PPVs **cannot be directly transferred to the Swedish MRKH cohort**. The code rules and clinical assessment process may differ.
2. The selection sensitivity assumes restored excluded women earn the comparison-group average. It is a **simple arithmetic thought experiment**, not a statistical bound, covariate-adjusted result, or demonstration that bias exists.
3. Exact coefficients and confidence intervals for Figure 9 are **not supplied as tables by the authors**; the approximate figure input is therefore not raw regression output.
4. Dynamic IV estimates, medical Type I classification, model-based counterfactuals and standard errors for the near-90% share **cannot be verified from published aggregates alone**.
5. The survey’s coefficient-to-mean transformation treats the reported comparison mean as fixed; it is **not an interval accounting for uncertainty in that denominator**.
6. Numerical estimates, source interpretations and unexplained publishing inconsistencies are identified separately; **the package does not claim a causal effect is conclusively refuted**.

## Anonymous-review handling

This release intentionally includes no manuscript-author name, address, ORCID, funding declaration, project account link, or acknowledgments. The dates attached to ZIP members are normalized. Its public URLs point only to the papers being critiqued, not to an identifiable author profile.
