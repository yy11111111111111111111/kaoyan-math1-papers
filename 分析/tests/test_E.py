"""检验 E：频次带 → 跨题型分散度。2026-08-27 复核后，原结论在其陈述方向上被否证。"""
import sys, os, random, statistics, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

SEED, ITER = 11, 2000
random.seed(SEED)
rows = load(); subj = subject_map(rows)

def band(n): return '≥8' if n >= 8 else ('5-7' if n >= 5 else ('3-4' if n >= 3 else '1-2'))
def slope(assign):
    d = collections.defaultdict(list)
    for k, c in assign.items():
        d[band(sum(c.values()))].append(norm_entropy([c[t] for t in TYPES]))
    m = {b: statistics.mean(v) for b, v in d.items()}
    return m['≥8'] - m['1-2'], m

obs = collections.defaultdict(collections.Counter)
for r in rows:
    for k in r['kps']: obs[k][r['tx']] += 1
o_slope, o_tab = slope(obs)

opp = collections.defaultdict(collections.Counter)
for r in rows:
    if r['kps']: opp[subj[r['kps'][0]]][r['tx']] += 1

def null_A():
    a = collections.defaultdict(collections.Counter)
    for k, c in obs.items():
        s = subj.get(k, '高数'); w = [opp[s][t] for t in TYPES]; tot = sum(w)
        for _ in range(sum(c.values())):
            x = random.random() * tot; acc = 0
            for t, wt in zip(TYPES, w):
                acc += wt
                if x <= acc: a[k][t] += 1; break
    return a

sims = [slope(null_A())[0] for _ in range(ITER)]
mu, sd = statistics.mean(sims), statistics.stdev(sims)
p = sum(1 for s in sims if s >= o_slope) / len(sims)

record(
 test_id='E', input_sha=input_sha(),
 inclusion_rule='全部 223 个考点标签（主考点+次考点），全部 499 题',
 estimand='控制每个标签的出现次数后，频次与跨题型分散度是否仍正相关',
 statistic='分散度斜率 = mean(归一化熵 | 频次≥8) − mean(归一化熵 | 频次 1-2)',
 null_model='固定每个标签的出现次数 n_i，按该科目的选/填/解机会比例多项分配',
 randomization_unit='考点标签', iterations=ITER, seed=SEED,
 observed=f'{o_slope:.4f}   逐带：' + ' '.join(f'{b}={o_tab[b]:.3f}' for b in ['≥8','5-7','3-4','1-2']),
 null_summary=f'{mu:.4f} ± {sd:.4f}',
 p_value=f'{p:.4f}  (单侧，观测≥零模型)',
 interpretation='观测斜率低于机械基准，原结论「高频=能填任何题型的通用件」在其陈述方向上被否证。'
                '单调表可完全由样本量造出：n=1 的标签分散度必然为 0。',
 known_contamination='考点标签为人工标注；科目归属由三份考法统计的标签集合反查，非 TSV 字段',
 generated_at='2026-08-27')
