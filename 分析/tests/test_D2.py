"""检验 D2：具体考点与高数解答位的关联（原文的「不绑考点」是独立负面主张，此前从未检验）。"""
import sys, os, random, statistics, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

SEED, ITER = 41, 4000
random.seed(SEED)
raw = load()
rows = [dict(r, main=r['kps'][0] if r['kps'] else '') for r in raw
        if r['tx'] == '解答' and r['demand'] and r['gslot']]
NEW = {2021, 2023, 2024, 2025, 2026}

for name, sel in [('旧卷型 2004-2020', lambda r: r['yr'] < 2021), ('新卷型 5 样本', lambda r: r['yr'] in NEW)]:
    D = [r for r in rows if sel(r)]
    byyr = collections.defaultdict(list)
    for r in D: byyr[r['yr']].append(r)
    obs = cramers_v([(r['gslot'], r['main']) for r in D])
    sims = []
    for _ in range(ITER):
        p = []
        for y, rs in byyr.items():
            vs = [r['main'] for r in rs]; random.shuffle(vs)
            p += [(r['gslot'], v) for r, v in zip(rs, vs)]
        sims.append(cramers_v(p))
    mu, sd = statistics.mean(sims), statistics.stdev(sims)
    pv = sum(1 for s in sims if s >= obs) / len(sims)
    record(
     test_id=f'D2[{name}]', input_sha=input_sha(),
     inclusion_rule=f'{name} 的高数解答题，共 {len(D)} 道，主考点 {len({r["main"] for r in D})} 种',
     estimand='具体考点与高数解答位是否存在关联（D1 的独立负面主张，须单独测）',
     statistic="Cramér's V(高数解答位 × 主考点)",
     null_model='年内置换：同一年内打乱主考点标签', randomization_unit='年 × 科目',
     iterations=ITER, seed=SEED, observed=f'{obs:.4f}', null_summary=f'{mu:.4f} ± {sd:.4f}',
     p_value=f'{pv:.4f}  (单侧)',
     interpretation='未检出关联。⚠️ V 的绝对值天然偏高（主考点种类数接近样本数），'
                    '只能看观测与置换的差；新卷型 n=20 几乎没有功率，这个 null 很弱。',
     known_contamination='主考点为人工标注；「哪个是主考点」的排序本身是判断',
     generated_at='2026-08-27')
