#!/usr/bin/env python3
"""Reviewer-facing audit: input/source integrity and independent arithmetic checks.

Standard library only. Run after run_analysis.py. Does not require source papers
or person-level data. Use --strict-archive BEFORE regenerating files to check
all archive byte-for-byte hashes (plots may differ on other Matplotlib versions).
"""
from pathlib import Path
import csv, hashlib, json, math, sys
B=Path(__file__).resolve().parent
manifest=json.loads((B/'manifest_sha256.json').read_text(encoding='utf-8'))
strict='--strict-archive' in sys.argv
key_files=['README.md','run_analysis.py','verify_package.py','requirements.txt','CLAIM_TO_FILE_GUIDE.md']
key_files += sorted('data/'+p.name for p in (B/'data').glob('*.csv'))
key_files += sorted('manuscript_figures/'+p.name for p in (B/'manuscript_figures').glob('*.png'))
check_paths=sorted(manifest) if strict else key_files
for name in check_paths:
    if name not in manifest:raise AssertionError('Missing hash entry: '+name)
    f=B/name
    if not f.is_file():raise AssertionError('Missing required file: '+name)
    if hashlib.sha256(f.read_bytes()).hexdigest()!=manifest[name]:
        raise AssertionError('SHA256 mismatch: '+name)
print('PASS: '+ ('whole archived snapshot' if strict else 'documented source files and manuscript images')+' verified.')

def tab(name):
    with (B/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))
def close(a,b,tol=1e-7):
    if not math.isclose(float(a),float(b),rel_tol=tol,abs_tol=tol):
        raise AssertionError(f'Mismatch: {a} vs {b}')
source={r['measure']:float(r['value']) for r in tab('data/published_effects.csv')}
c={r['criterion']:r for r in tab('data/validation_counts.csv')}
p={r['criterion']:r for r in tab('outputs/validation_ppvs.csv')}
for name,row in c.items():
    close(float(p[name]['ppv_percent']),int(row['confirmed'])/int(row['assessed'])*100)
close(p['Either Q51.0 or Q52.0']['ppv_percent'],167/292*100)
close(p['Both Q51.0 and Q52.0']['ppv_percent'],78/84*100)
summary=json.loads((B/'outputs/aggregate_checks.json').read_text(encoding='utf-8'))
close(summary['type_I_retained_percent'],100*source['Retained Type I cases']/source['Initial cases'])
close(summary['excluded_percent'],100*source['Excluded cases']/source['Initial cases'])
close(summary['gender_gap_share_ages_20_42_percent'],100*(30.37-8.97)/30.37)
close(summary['gender_gap_share_ages_32_42_percent'],100*(30.57-3.67)/30.57)
close(summary['survey_earnings_effect_as_percent_of_control_mean'],100*source['Survey adjusted earnings coefficient']/source['Survey comparison earnings mean'])
close(summary['education_explains_fraction_percent'],100*(16.9-11.85)/16.9)
close(summary['education_plus_occupation_fraction_percent'],100*(16.9-9.92)/16.9)
close(summary['decomposition_example_share_after_5pp_adjustment_percent'],100*(30.57-8.67)/30.57)
scenarios=tab('outputs/sample_selection_scenarios.csv')
for r in scenarios:
    baseline=float(r['baseline_percent']);n=int(r['wrongly_excluded_added'])
    close(r['illustrative_premium_percent'],source['Retained Type I cases']*baseline/(source['Retained Type I cases']+n))
for i in range(1,6):
    for f in [(B/'manuscript_figures'/f'Figure_C{i}.png')]:
        if f.read_bytes()[:8] != bytes.fromhex('89504e470d0a1a0a'):raise AssertionError('Not a PNG: '+str(f))
for f in (B/'figures').glob('*.png'):
    if f.read_bytes()[:8] != bytes.fromhex('89504e470d0a1a0a'):raise AssertionError('Not a PNG: '+str(f))
if len(list((B/'figures').glob('Figure_C*.png'))) != 5:raise AssertionError('Expected five regenerated figures')
print('PASS: Source-count arithmetic, published-estimate checks, illustrative scenarios, and figures verified.')
print('LIMIT: No Swedish individual-level administrative data or exact Figure 9 coefficients are supplied.')
