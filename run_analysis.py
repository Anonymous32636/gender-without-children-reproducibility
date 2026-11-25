#!/usr/bin/env python3
"""Anonymous reproducibility audit of published aggregate arithmetic.

No person-level register data are distributed or analyzed here.
Figure 9 values are approximate visual readings, not exact coefficients.
The hypothetical selection exercise is not a regression re-estimation.
"""
from pathlib import Path
import csv
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import beta

BASE = Path(__file__).resolve().parent
D = BASE / 'data'
OUT = BASE / 'outputs'; OUT.mkdir(exist_ok=True)
FIG = BASE / 'figures'; FIG.mkdir(exist_ok=True)

def csvrows(path):
    with (D / path).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def savefig(name):
    plt.savefig(FIG/name, dpi=180, bbox_inches='tight')
    plt.close()

def cp_exact(x,n,alpha=.05):
    # Exact Clopper-Pearson interval for a binomial proportion.
    lo=0.0 if x==0 else float(beta.ppf(alpha/2,x,n-x+1))
    hi=1.0 if x==n else float(beta.ppf(1-alpha/2,x+1,n-x))
    return lo,hi

counts=csvrows('validation_counts.csv')
rows=[]
for r in counts:
    x,n=int(r['confirmed']),int(r['assessed'])
    lo,hi=cp_exact(x,n)
    rows.append({'criterion':r['criterion'],'confirmed':x,'assessed':n,
                 'ppv_percent':100*x/n,'ci_lower_percent':100*lo,'ci_upper_percent':100*hi,
                 'printed_ppv_percent':r['printed_ppv_percent']})
with (OUT/'validation_ppvs.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
by_criterion={r['criterion']:r for r in rows}
assert abs(by_criterion['Either Q51.0 or Q52.0']['ppv_percent']-57.1917808)<1e-5
assert abs(by_criterion['Both Q51.0 and Q52.0']['ppv_percent']-92.8571429)<1e-5
# The overlap identity independently checks the either-code counts.
assert 170+206-84==292
assert 112+133-78==167

# Figure C1: Danish predictive value of two code rules.
labels=['Either Q51.0 or Q52.0','Both Q51.0 and Q52.0']
vals=[by_criterion[x]['ppv_percent'] for x in labels]
fig,ax=plt.subplots(figsize=(7,3.1))
ax.barh([0,1],vals,height=.45,color=['#5a8394','#147f82'])
ax.set_yticks([0,1],labels=labels);ax.invert_yaxis();ax.set_xlim(0,105)
ax.set_xlabel('Positive predictive value (%)');ax.grid(axis='x',alpha=.18)
ax.set_axisbelow(True)
for y,v in enumerate(vals):ax.text(v+2,y,f'{v:.1f}%',va='center')
fig.tight_layout();savefig('Figure_C1_danish_code_ppv.png')

# Figure C2: Hypothetical mean-mixture sensitivity. Two baselines; not a re-estimated IV model.
ns=np.array([0,10,25,50])
res=[]
fig,ax=plt.subplots(figsize=(7.2,3.2))
for baseline in (28.4,22.0):
    values=152*baseline/(152+ns)
    for n,v in zip(ns,values):res.append({'baseline_percent':baseline,'wrongly_excluded_added':int(n),'illustrative_premium_percent':float(v)})
    ax.plot(ns,values,marker='o',linewidth=2,label=f'Starting value {baseline:.1f}%')
ax.set_xlabel('Hypothetically restored Type I women');ax.set_ylabel('Illustrative mean earnings premium (%)')
ax.legend(frameon=False);ax.grid(alpha=.2);fig.tight_layout();savefig('Figure_C2_hypothetical_selection.png')
with (OUT/'sample_selection_scenarios.csv').open('w',encoding='utf-8',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['baseline_percent','wrongly_excluded_added','illustrative_premium_percent']);w.writeheader();w.writerows(res)
assert abs(152*28.4/(152+25)-24.4)<.02
assert abs(152*22/(152+50)-16.6)<.05

# Figure C3: Approximate readings of Figure 9; no invented standard errors.
fig9=csvrows('figure9_approximate.csv')
labels=[r['specification'] for r in fig9]
vals=[float(r['approx_effect_percent']) for r in fig9]
fig,ax=plt.subplots(figsize=(7.2,3.4));ax.barh(labels[::-1],vals[::-1],color='#628e96')
ax.set_xlabel('Approximate earnings advantage (%)');ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True)
for i,v in enumerate(vals[::-1]):ax.text(v+.7,i,f'≈{v:.0f}%',va='center')
ax.set_xlim(0,63);fig.tight_layout();savefig('Figure_C3_figure9_visual_readings.png')

# Figure C4: ratios of reported gender gaps, not confidence intervals.
gap_all,resid_all=30.37,8.97
gap_mid,resid_mid=30.57,3.67
exp_all=(gap_all-resid_all)/gap_all*100
exp_mid=(gap_mid-resid_mid)/gap_mid*100
fig,ax=plt.subplots(figsize=(6.9,3.1))
ax.barh(['Ages 20–42','Ages 32–42'],[exp_all,exp_mid],color=['#718f9c','#14888b'])
ax.set_xlim(0,100);ax.set_xlabel('Point-estimate share explained (%)')
for i,v in enumerate([exp_all,exp_mid]):ax.text(v+1,i,f'{v:.1f}%',va='center')
ax.grid(axis='x',alpha=.2);ax.set_axisbelow(True);fig.tight_layout();savefig('Figure_C4_gender_gap_decomposition.png')

# Figure C5: published Table 4 point estimates and normal-approximation 95% CIs.
effects=[3.3,15.2];ses=[9.2,3.0]
fig,ax=plt.subplots(figsize=(7.5,2.7))
for i,(v,se) in enumerate(zip(effects,ses)):
    ax.errorbar(v,i,xerr=1.96*se,fmt='o',capsize=4,color='#147f82')
ax.axvline(0,linestyle='--',color='#8d9aa2')
ax.set_yticks([0,1],['Full adjusted sample','Diagnosed before 18']);ax.invert_yaxis()
ax.set_xlabel('STEM field-share difference (percentage points)')
ax.set_xlim(-22,30);ax.grid(axis='x',alpha=.17);ax.set_axisbelow(True)
fig.tight_layout();savefig('Figure_C5_STEM_effects.png')

# Other disclosed numerical checks; explicitly not regression replications.
summary={
  'swedish_mrkh_cases':259,
  'type_I_cases':152,
  'excluded_cases':107,
  'type_I_retained_percent':152/259*100,
  'excluded_percent':107/259*100,
  'reported_type_I_percent':62.9,
  'reported_excluded_percent':37.1,
  'implied_population_if_prevalence_1_in_6319':259*6319,
  'danish_ppv_either_percent':by_criterion['Either Q51.0 or Q52.0']['ppv_percent'],
  'danish_ppv_both_percent':by_criterion['Both Q51.0 and Q52.0']['ppv_percent'],
  'gender_gap_share_ages_20_42_percent':exp_all,
  'gender_gap_share_ages_32_42_percent':exp_mid,
  'education_explains_fraction_percent':(16.9-11.85)/16.9*100,
  'education_plus_occupation_fraction_percent':(16.9-9.92)/16.9*100,
  'earnings_effect_95ci_percent':[28.4-1.96*5.86,28.4+1.96*5.86],
  'survey_earnings_effect_as_percent_of_control_mean':10514/14236*100,
  'survey_earnings_relative_95ci_holding_mean_fixed':[(10514-1.96*3271)/14236*100,(10514+1.96*3271)/14236*100],
  'stem_full_95ci_pp':[3.3-1.96*9.2,3.3+1.96*9.2],
  'stem_early_95ci_pp':[15.2-1.96*3.0,15.2+1.96*3.0],
  'conditional_unconditional_earnings_identity_reported_mean':91627,
  'conditional_unconditional_earnings_identity_implied_mean':.79*110558,
  'earnings_identity_difference_SEK':91627-.79*110558,
}
with (OUT/'aggregate_checks.json').open('w',encoding='utf-8') as f:json.dump(summary,f,indent=2,ensure_ascii=False)
print('Validated published-count calculations; created five plots and results outputs.')
