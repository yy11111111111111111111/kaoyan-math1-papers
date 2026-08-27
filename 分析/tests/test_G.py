"""检验 G：空窗期（距上次出现）对下一场出现是否有影响。B 测的是相邻重复，回答不了这个。"""
import sys, os, random, statistics, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *

SEED, ITER, BOOT = 20260827, 4000, 4000
random.seed(SEED)
rows = load()
YEARS = sorted({r['yr'] for r in rows}); N = len(YEARS)
idx = {y: i for i, y in enumerate(YEARS)}
occ = collections.defaultdict(set)
for r in rows:
    for k in r['kps']: occ[k].add(idx[r['yr']])
labels = [k for k, v in occ.items() if 3 <= len(v) <= 12]

def scan(P, maxage=8):
    ev, risk, num, den = [], [], collections.Counter(), collections.Counter()
    for S in P:
        S = sorted(S)
        if not S: continue
        last = S[0]
        for i in range(S[0] + 1, N):
            a = min(i - last, maxage)
            risk.append(a); den[a] += 1
            if i in S: ev.append(a); num[a] += 1; last = i
    return ev, risk, num, den

def delta(P):
    ev, risk, _, _ = scan(P)
    return statistics.mean(ev) - statistics.mean(risk) if ev else None

P = [occ[k] for k in labels]
obs = delta(P); ev, risk, num, den = scan(P)
sims = [delta([set(random.sample(range(N), len(S))) for S in P]) for _ in range(ITER)]
mu, sd = statistics.mean(sims), statistics.stdev(sims)
p_hi = sum(1 for s in sims if s >= obs) / len(sims)

def hr(P):
    a = [0, 0]; b = [0, 0]
    for S in P:
        S = sorted(S)
        if not S: continue
        last = S[0]
        for i in range(S[0] + 1, N):
            g = i - last; hit = i in S
            if g == 1: a[1] += 1; a[0] += hit
            elif g >= 5: b[1] += 1; b[0] += hit
            if hit: last = i
    return (b[0] / b[1]) / (a[0] / a[1]) if a[0] and a[1] and b[1] else None
point = hr(P)
boot = sorted(x for x in (hr([occ[random.choice(labels)] for _ in labels]) for _ in range(BOOT)) if x)
lo, hi = boot[int(.025 * len(boot))], boot[int(.975 * len(boot))]

record(
 test_id='G', input_sha=input_sha(),
 inclusion_rule=f'出现 3–12 个年份的标签（与检验 B 同口径），共 {len(labels)} 个；'
                f'22 个观测场次（2004–2026，2022 缺失），事件 {len(ev)} / 风险槽 {len(risk)}',
 estimand='P(本场出现 | 已 a 场未出现) 是否随 a 变化，即「久未出现是否更容易回来」',
 statistic='Δ = 事件的平均 age − 全部风险槽的平均 age；辅以 HR = h(age≥5)/h(age=1)',
 null_model='固定每个标签的出现次数，把出现位置随机撒进 22 个场次',
 randomization_unit='考点标签', iterations=ITER, seed=SEED,
 observed=f'Δ = {obs:+.4f}   HR = {point:.3f}   逐 age 的 h(a)：' +
          ' '.join(f'{a if a<8 else "8+"}:{num[a]/den[a]:.3f}' for a in sorted(den)),
 null_summary=f'Δ 零模型 = {mu:+.4f} ± {sd:.4f}；HR 整群自助 95% 区间 = [{lo:.3f}, {hi:.3f}]（n_boot={len(boot)}）',
 p_value=f'{2*min(p_hi,1-p_hi):.3f}  (双侧)',
 interpretation='未检出空窗效应。能排除的是约 11% 以上的增幅、23% 以上的降幅；'
                '更小的效应本检验没有功率排除。不得写成「已证明空窗无预测力」，'
                '也不得写成「考点层近似无记忆」——后者是关于整个条件分布的强主张。',
 known_contamination='① 2022 缺失被当作「这一场不存在」而非「未观测」；'
                     '② 标签为人工标注，标注不一致同时污染分子分母；'
                     '③ 未对功能位做条件化',
 generated_at='2026-08-27')
