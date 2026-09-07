# 独立审查 · calc.diff1v.route-selection（一元微分学）

```yaml
task_id: batch3.diff1v.independent_audit
reviewer: claude-batch3-reviewer-1（integrator 派出的独立审查 agent，未参与建族）
artifact_identity: { branch: claude/postgraduate-math-exam-analysis-czoi3t, head: a635bd6 }
audited_at: 2026-08-29
scope_checked:
  file: 分析/方法族-高数-一元微分学.md（691 行，33 题）
  actions: A1 A2 A3 A4 A4b A5 A6 A7 A8 A9 A10 A11 A12 A13（14 条）
  guards: 11 条全查
  failure_boundaries: B1–B8 全部符号推导 + 数值复算
  cells: 6 格独立重枚举（先枚举后做差集）
  lint: error 0 · warning 4（与基线一致）
note: >
  本文件由 integrator 归档。审查 agent 的原始结论保留在 findings 各条；
  integrator_verdict 字段是 integrator 的独立复核结论，不是审查方的话。
```

## findings.blockers

### BL-1 · B1 · 「显式 · 求切线/法线」无 cell、A12 排除「由斜率反求切点」
- 载体：2004-1「曲线 y=ln x 上与直线 x+y=1 垂直的切线方程」。正解 k=1 ⇒ 解 1/x=1 得切点 (1,0) ⇒ y=x−1。
- 缺陷：一级路由第二轴「求切线法线」在六格中只有「参数式 · 求导或切线」，显式函数的切线题无格可落；越格取 A12 也不行——A12 的 `applies_when: [已知切点与该点导数值]` 在本题不成立（切点未知）。
- 同类：2015-16 / 2023-17 / 2012-18（切线条件反求 f，实际要建 ODE），本族无向 calc.ode 的 boundary_note。
- **integrator_verdict: ACCEPTED（未修复，记为 open blocker）**。A12 的 applies_when 与六格清单我已核对，确如所述。修复需新增 cell 与拆分 applies_when，属路线设计，留待下一轮。

### BL-2 · B1 · 缺「凸性 ⇒ 弦/切线位置关系」分支
- 载体：2014-2、2026-3（TSV 主考点即「凹凸性与弦的位置关系」）、2007-5。
- 2014-2：f″≥0 ⇒ f 凸 ⇒ f(x)=f((1−x)·0+x·1) ≤ (1−x)f(0)+x f(1)=g(x) ⇒ (D)。
- 缺陷：A8 的 terminal_when 是「各区间凹凸性已判定」，判完即止，不含「凸 ⇒ 位于弦下方/切线上方」；A11（泰勒）要求各阶导可算，本题 f 抽象。
- **integrator_verdict: ACCEPTED（未修复，记为 open blocker）**。

### BL-3 · B1 · 参数式在 x′(t) 不存在处无 action
- 载体：2023-3，x=2t+|t|, y=|t|sin t，x′(0) 不存在（右 3、左 1）。
- A4/A4b 的 applies_when 均含 x′(t)≠0；fallback_policy 只写「x′(t)=0 → 单独讨论」，未覆盖「不存在」，且「单独讨论」不是 action。
- 合法路线是分段消参：t≥0 ⇒ y=(x/3)sin(x/3)；t<0 ⇒ y=−x sin x。f′(0)=0 存在且连续，f″(0⁺)=2/9、f″(0⁻)=−2 ⇒ f″(0) 不存在 ⇒ (C)。数值：f″₊≈0.2222222、f″₋≈−2.0000000。
- 消参在文件中只作 `dominated_not_excluded` 存在，**无对应 action ⇒ 事实上不可执行**。
- **integrator_verdict: ACCEPTED（未修复，记为 open blocker）**。

### BL-4 · B2 · 导数极限定理被判 invalid
- 原文 excluded_candidates：`{ 由导函数极限判可导, reason: invalid }`；guard#1 无前提禁令「不得对两侧表达式分别求导后取极限代入」，logical_role: necessary。
- 反证：导数极限定理成立——f 在 x₀ 连续、去心邻域可导、lim f′(x)=A 有限 ⇒ f′(x₀)=A。
  实例 f=sin x (x<0)、f=ln(1+x) (x≥0)：两侧连续于 0，lim f′ 左右均为 1，定理给 f′(0)=1，与定义算得一致（中心差商 ≈0.99999975）。
- B8（x²sin(1/x)）只证单向：lim f′ 不存在 ⇏ 不可导。正确 effect 是 `becomes_inconclusive`，不是 `invalidates`。文件把单向结论写成了双向禁令。
- **integrator_verdict: ACCEPTED · 已修复**。guard#1 加前提；excluded_candidates 拆为「无前提代替 → invalid」与「导数极限定理 → dominated_not_excluded」两条。

### BL-5 · B4 · A2/A5 的 continuation 悬空至 limit 族的 exclusions
- A2 的 boundary_note 把差商极限交给 calc.limit.method-selection，但该族 scope.exclusions 明文未纳入「单侧极限的分支讨论 / 含绝对值或取整的分段讨论」。
- A5 产出的正是单侧差商极限；2018-1 / 2019-2 / 2023-3 / 2016-4 全落在该类。
- **integrator_verdict: ACCEPTED（未修复，记为 open blocker）**。修复方向：本族自理该类极限，不动已冻结的 limit 族。

### BL-6 · B4 · lint R2 对本族静默失效，并掩盖 A12 的真实不一致
- `lint_method_families.py` 的 R2 取 `c.get('cell_id') or CELL_ALIAS.get(c.get('cell'))`；CELL_ALIAS 只收 batch1 vector 的四个格名。本族用中文 `cell:` 且无 `cell_id` ⇒ cells 为空 ⇒ `if cells:` 短路 ⇒ **R2 整体跳过**。
- 被掩盖的不一致：A12.eligible_cells=[参数式, 判形态]，而「判形态」格的清单是 [A8,A9,A10,A11]，不含 A12。
- **integrator_verdict: ACCEPTED · 已修复**。integrator 实测：R2 在 11 族中对 7 族（limit / extrema / diff1v / int1v / 重积分 / mvt / space-geometry）空转，只覆盖 vector / ode / series / multivar。已补 CELL_ALIAS + 回落到原始格名 + 无格可解析时报错；R2 上线后即捞出三条真实不一致（本条 + int1v/A10 + 重积分/A6），已全部修正。

### BL-7 · B4 · A7 的三个真题引用全错
- 原文 `{ A7, ref: "2015-1、2017-2、2019-2", basis: 渐近线条数与斜渐近线求法 }`。
- 实际：2015-1 = f″ 图形判拐点个数；2017-2 = f·f′>0 比较 f(±1)、|f(±1)|；2019-2 = 分段函数 0 处可导性/极值。三题均与渐近线无关。
- scope 内真正的渐近线题 2005-1 / 2007-2 / 2012-1 / 2014-1 / 2023-1 一条未列。
- **integrator_verdict: ACCEPTED（未修复，记为 open blocker）**。与 BL-1..3 的路线修复一并重做 positive_instance_mapping 更省事，故留待下一轮。

## findings.non_blocking（摘要）
- NB-1 A6←2016-4、NB-2 A9←2021-1：决定答案的 action 挂错（应为 A5/A2）。
- NB-3 scan_basis 引用不存在的 `高数真题题面_2004-2023.md`。**已修复。**
- NB-4 guard#5「拐点判据是 f″ 变号」按字面读作充分条件时被 f=1/x 击穿（f″=2/x³ 在 0 两侧变号，但 x=0 不在定义域）。A10 的候选集实际堵住了它，故非漏解，但 guard 与 A10 不同步。
- NB-5 A10 的「考察两侧符号是否改变」默认每侧 f″ 定号；f″=x²sin(1/x) 型两侧均无定号，该操作无定义。
- NB-6（靶子③）「代入具体函数验证选项」标 `invalid` 定性不准：用于**否定**选项与 X1 同机制（应为 duplicate_mechanism），只有用于**肯定**才是 invalid。**integrator_verdict: 同意，记 backlog。**
- NB-7 2006-7（微分与增量比较）、2025-19（导函数单调性充要条件）的设问不在第二轴取值内。
- NB-8 A1 的法则清单不含变限积分求导（2010-9 次考点），无跨族 boundary_note。
- NB-9 第一轴缺「隐式 F(x,y)=0」一档。

## counter_witnesses
- **verified**：B1–B8 八条 witness 的数学本体全部复算通过。
  - B1（靶子①）：f=x+2x²sin(1/x)，f′(0)=1；f′(x)=1+4x sin(1/x)−2cos(1/x)，在 x=1/(2kπ) 处 =−1。integrator 独立复算一致（k=1/5/50 均为 −1，中心差商 −1.0000000±5e−8）。
  - B6 的第二例 x=t²,y=t⁴ 是决定性的：真值 y″=2，错误式 y″/x″=6t² 在 t=1 给 6。
- **refuted**：无。被推翻的是从 B8 引申出的排除性定性（BL-4），不是 B8 本身。
- **pending**：2024-4 / 2025-19 / 2026-13 / 2026-3 题面不在题面库，只据 TSV 主考点。

## guard_audit（11 条）
9 条 necessary、2 条 supporting_heuristic。**未发现把效率偏好写成合法性条件**；preference_rule 明确自述「这是效率排序，不是合法性判断」。唯一方向性错误是反过来的：guard#1 把有前提的合法路线写成非法（BL-4，已修）。guard#3 的 check 只写「先解 x′(t)=0」，未覆盖「不存在」（BL-3）。

## status_recommendation
`challenged` · reopen_family: true

## integrator 处置
- **status: candidate → challenged + teaching_use: quarantine**（依 `permissions.downgrade_on_direct_counter_witness: allowed`，BL-4 为已复核的 direct counter-witness）。
- 已修复：BL-4、BL-6、NB-3。
- 未修复（open blockers，需下一轮路线设计）：BL-1、BL-2、BL-3、BL-5、BL-7。
- 六格的 `no_direct_blocker_open` 已全部置 false，`cell_status` 回落 `open`。
