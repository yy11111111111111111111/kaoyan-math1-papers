"""检验 D1：功能类型与高数解答位的关联。必须剔除线代/概率区（科目效应）。"""
import sys, os, random, statistics, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

SEED, ITER = 41, 4000
random.seed(SEED)
rows = [r for r in load() if r['tx'] == '解答' and r['demand'] and r['gslot']]
NEW = {2021, 2023, 2024, 2025, 2026}

for name, sel in [('旧卷型 2004-2020', lambda r: r['yr'] < 2021), ('新卷型 5 样本', lambda r: r['yr'] in NEW)]:
    D = [r for r in rows if sel(r)]
    byyr = collections.defaultdict(list)
    for r in D: byyr[r['yr']].append(r)
    obs = cramers_v([(r['gslot'], r['demand']) for r in D])
    sims = []
    for _ in range(ITER):
        p = []
        for y, rs in byyr.items():
            vs = [r['demand'] for r in rs]; random.shuffle(vs)
            p += [(r['gslot'], v) for r, v in zip(rs, vs)]
        sims.append(cramers_v(p))
    mu, sd = statistics.mean(sims), statistics.stdev(sims)
    pv = sum(1 for s in sims if s >= obs) / len(sims)
    record(
     test_id=f'D1[{name}]', input_sha=input_sha(),
     inclusion_rule=f'{name} 的高数解答题（gslot 非空），共 {len(D)} 道 / {len(byyr)} 年。'
                    '⚠️ 必须剔除线代/概率区：那两位恒为「计算」，是科目效应不是位置效应',
     estimand='给定当年该科解答题的功能类型组成，功能类型与位置是否仍存在关联',
     statistic="Cramér's V(高数解答位 × 功能类型)",
     null_model='年内置换：同一年内打乱功能类型标签，保留当年的证明/积分/计算数量',
     randomization_unit='年 × 科目', iterations=ITER, seed=SEED,
     observed=f'{obs:.4f}', null_summary=f'{mu:.4f} ± {sd:.4f}',
     p_value=f'{pv:.4f}  (单侧)',
     interpretation='有倾向，未达 0.05。不得表述为「功能位绑在题号位置上」。',
     known_contamination='因变量 demand 列的判定以 解法.md 为准，而 解法.md 是 unverified_inference。'
                         '修复方向：改从题面 response requirement 编码（未完成）',
     generated_at='2026-08-27')
