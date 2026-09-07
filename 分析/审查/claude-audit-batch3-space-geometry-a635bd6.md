# 独立审查 · calc.space-geometry.route-selection（空间解析几何与场量）

```yaml
task_id: batch3.space-geometry.independent_audit
reviewer: claude-batch3-reviewer-5（独立审查 agent，未参与建族）
artifact_identity: { branch: claude/postgraduate-math-exam-analysis-czoi3t, head: a635bd6 }
audited_at: 2026-08-29
scope_checked:
  file: 分析/方法族-高数-空间解析几何与场量.md（484 行，8 题）
  cells: [surface_of_revolution, curve_projection, distance, field_quantity]
  actions: A1–A6；guards 8 条；boundaries B1–B6
  problems: 2006-4 / 2009-17 / 2013-19 / 2016-10 / 2017-19 / 2018-11 / 2025-20 / 2026-11
  lint: error 0 · warning 4（与基线一致）
note: integrator 归档；integrator_verdict 为 integrator 的独立复核结论。
```

## findings.blockers

### BL-1 · B1 · 2013-19 在本族 router 下无 action 接收
- 题：直线 L 过 A(1,0,0)、B(0,1,1)，绕 z 轴旋转一周得 Σ，求 Σ 的方程。L 的参数式 (1−t, t, t)，**不含于任何坐标面**（三个坐标同时变动）。
- A1 的 `applies_when: [母线为坐标面内的曲线, 旋转轴为某个坐标轴]` 第一条不满足；guard#7 进一步明写「母线不在坐标面内…A1 的口诀不适用」，其 explanation 把这种情形推给「坐标变换，超出本族 scope」。
- 正确路线（消参法 / 到轴距离不变）：z=z₀ 且 x²+y²=x₀²+y₀²；消 t 得 **x²+y² = (1−z)²+z² = 2z²−2z+1**。（t=1/3 时母线点 (2/3,1/3,1/3)，x₀²+y₀²=5/9；2z²−2z+1|_{z=1/3}=5/9 ✔）
- 该路线在 excluded_candidates 中被标 `duplicate_mechanism`，**从未进入 candidate_actions**，其 note 还把适用面误限于「一般轴」，漏掉本例的「坐标轴 + 一般空间母线」。
- 而 positive_instance_mapping 却把 2013-19 记作 A1 的正例。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。integrator 已核对 A1.applies_when、guard#7、TSV（2013-19 主考点 = 旋转曲面的方程，确在本族 scope）。`duplicate_mechanism` 在此是**理由误用**：一条在两道题上唯一可行的路线不是 A1 的冗余表述。

### BL-2 · B1 + B4 · 2025-20 同样无 action 接收，且 B6 宣布该情形 scope 外
- 题：Σ 由直线 {x=0, y=0}（z 轴）绕直线 (x,y,z)=(t,t,t) 旋转一周得到。**旋转轴是 x=y=z，不是坐标轴** ⇒ A1.applies_when 第二条不满足。
- 构造：轴单位向量 d=(1,1,1)/√3，等距条件给
  x²+y²+z² = (x+y+z)² ⇔ **xy+yz+zx = 0**（以 x=y=z 为轴的圆锥）。
- 这正是 B6 与 excluded_candidates 判为 `out_of_scope`、「大纲未含」的情形，**可它本身就在本族的 8 题 scope 清单里**——两处直接冲突。
- **对靶子④的回答：B6 不是合理的 scope 限制，而是漏解。** 考纲依据不足：分析/考纲.md 对该章只写到「向量运算、平面与直线、曲面与空间曲线」，粒度不足以裁定「一般轴旋转超纲」；而 2025-20 是 papers/ 内的真实真题，是反向的硬证据。
- 结构性问题：B6 的 witness 是一段**正确的 proof**，但它证明的是「口诀不适用」，被用来支撑「这类题不在本族」——**witness 与它所支撑的命题不匹配**。这正是本次审查要求检查的「witness 是否真的证明了它声称证明的东西」的失败点。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。
  - integrator 独立复核：用 Rodrigues 公式显式旋转 (0,0,1) 绕 (1,1,1)/√3，取 θ=0/0.7/1.9/3.3/5.0 五个角度，每个像点均满足 xy+yz+zx=0（|值|<1e−12），且 x²+y²+z²−(x+y+z)²=0。构造成立。
  - **审查方提出的 OQ-1（2025-20 主设问是第二类曲面积分，是否应移出本族）经 integrator 裁定：驳回。** TSV 实测 2025-20 主考点 = **旋转曲面的方程**，次考点才是「高斯公式补面法」。按 HANDOFF 的 `scope_boundary_rule`（主考点定归属），2025-20 归本族无误，BL-2 不消解。
  - 说明：为裁定此项，integrator 读取了 papers/2025年数学一真题.md 的题干；该文件混有【解析】段（CLAUDE.md §2.4），integrator 的 xy+yz+zx=0 系独立推导 + 数值验证得出，未采用其中任何解析结论。

### BL-3 · B2 · A2 的 terminal 语义被反例击穿（消元结果是投影的**超集**）
- A2 的 followup 第二步写「投影柱面与该坐标面联立，**即为**投影曲线」，terminal_when「投影曲线的方程组已写出」。
- 反例：C = { x²+z²=1, y²+z²=1 }（两正交柱面的交线，在 `applies_when: [曲线由两个曲面方程给出]` 内）。
  按 A2 消 z：两式相减得 **x²−y²=0**，与 z=0 联立给出两条**完整直线** y=±x。
  真实投影：z∈[−1,1] ⇒ x=±√(1−z²)、y=±√(1−z²)，故投影 = {(x,y): x²=y², **|x|≤1**}，是四条**线段**。
  分离点 (2,2)：满足 x²=y²，但回代需 z²=1−4=−3，无实解 ⇒ 不在投影上，却在 A2 产出的「投影曲线」上。
- effect: invalidates。缺的是一条 necessary guard：**消元后必须补回被消变量的实解存在条件**（z²=1−x²≥0 之类）。现有 guard#2 只防「令 z=0」（B4 方向），完全没防这个方向。
- 该 cell 的 `counter_witness_search: { target: "A2 在正确消元后是否仍可能出错", search_result: not_found }` **被本反例证伪**。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。integrator 独立复核：消元确实只给 x²=y²，丢失了 |x|≤1 的值域约束。这是经典且真实的缺陷。

### BL-4 · B4 · positive_instance_mapping 与 scan_basis 的语义级错误
- **(a) 三道旋度题被挂到 A5（散度）。** A5 = `div F`（产标量），A6 = `curl F`（产向量）。
  - 2016-10 题面（分析/高数真题题面_2011-2016.md）：「向量场 A(x,y,z)=(x+y+z)i+xy j+z k 的**旋度** rot A = ___」。复算 rot A = (0, 1, y−1)。纯 curl ⇒ 应挂 A6。
  - 2018-11：求 rot F，F=(xy, −yz, zx)，复算 rot F = (y, −z, −x)。纯 curl ⇒ 应挂 A6。
  - 2026-11：div(rot(rot A))，A=(x+y², y+z², z+x²)。复算 rot A = (−2z,−2x,−2y)，rot(rot A) = (−2,−2,−2)（常向量），div = **0**（亦可由 div∘rot ≡ 0 一步得出）。是 A6∘A6∘A5 的复合。
  - 结果：**A6 在全族 positive_instance_mapping 中挂零，而它恰是三题共同的核心算子。**
  - （附带记录：papers/2026 的 OCR 解析给出 "1+z"，与独立复算的 0 不符。仅记录，不据其推断。）
- **(b) 2013-19、2025-20 被挂到 A1**，与 A1.applies_when、guard#7、B6 三处直接矛盾（BL-1、BL-2）。这不是 evidentiary_weight 问题，是 mapping 断言了一个被本文件自己的 guard 禁止的适用关系。
- **(c) scan_basis 引用 `高数真题题面_2004-2023.md`，该文件不存在**（实为四分册）；且 2025-20 与 2026-11 不在题面库覆盖年份内，其 positive instance 在 scan_basis 中没有任何声明来源。
- **integrator_verdict: ACCEPTED · (a) 与 (c) 已修复**。integrator 独立复算三题旋度，与审查方一致；TSV 三题主考点均为「旋度与散度的计算」。mapping 已改为 A6（2016-10、2018-11）与 A6+A5（2026-11），并写入更正说明；scan_basis 已改为四分册并标注 2024–2026 无覆盖。(b) 随 BL-1/BL-2 的路线修复一并处理，暂留 open。

### BL-5 · B2（边界情形）· field_quantity 的 excluded_candidates 事实错误
- 原文：「用恒等式（如 div curl F ≡ 0）先化简 … 本族 scope 内三题**均为直接场，用不上**但不排除」。
- 2026-11 求 div(rot(rot A))，正是**复合场**，且 div∘rot ≡ 0 一步给出答案 0。「三题均为直接场」是事实错误，且它是本族**唯一存在真实路线竞争**的题（恒等式秒杀 vs 三层硬算），却被这条 note 抹掉。
- route_universe 只列「① 按定义逐项求偏导；② 用向量恒等式化简后再算」，缺「**复合算子** rot∘rot、div∘rot、curl∘grad 的处理」这一独立分支及其 guard。
- 审查方自评：不构成 B1（硬算 A5/A6 仍能到达答案），严格读法下可降 non_blocking，但事实错误必须改。
- **integrator_verdict: ACCEPTED 为 non_blocking（采审查方的严格读法）。未修复，记 open item。**

## findings.non_blocking（摘要）
- NB-1 B1 的 witness 正文自相矛盾：「例如点 (0,0,1) 在前者上（…实际检验 z²=x²+y² ⇒ 1≠0，该点不在）」——先断言在、随即自我否定。B1 的**结论**仍成立（同段的分离点 (1,1,0) 复算正确：在 y²=x²+z² 上，1=1+0 ✔；不在 z²=x²+y² 上，0≠2 ✔）。属 witness 文本缺陷。
- NB-2 「六族里唯一不分叉」「对象一旦认清，公式是唯一的」是错误的自我刻画，见靶子①。
- NB-3 D2 的 failure_boundary 写作自由文本而非引用 B-id；A4 是全族唯一没有对应 boundary_id 的 route。
- NB-4 guard#5 是唯一一条没有 explanation 的 necessary guard。
- NB-5 B5 归因不完整：把增根归给「两边平方」，但 A1 的 followup 第二步写的就是「换成 **±**√(…)」——± 本身已引入另一支，平方只是第二重来源。
- NB-6 2009-17(II) 求体积、2017-19(II) 求质量属第一类曲面积分/重积分，本族 target_tasks 不含，terminal 之后的去向悬空。

## omitted_routes（差集，10 条）
OR-1 母线为一般空间曲线绕坐标轴（消参法）→ BL-1 · OR-2 绕一般直线旋转 → BL-2 · OR-3 退化情形（母线平行/垂直于轴、母线即轴）· OR-4 消元 + 被消变量值域约束 → BL-3 · OR-5 投影退化 · OR-6 点到直线的勾股（投影分解）法 d=√(|P₀P|²−(P₀P·s/|s|)²)（与 A4 由 Lagrange 恒等式等价，宜标 duplicate_mechanism 但应显式列出）· OR-7 距离格的退化情形 · OR-8 复合算子分支 → BL-5 · OR-9 由 Gauss/Stokes 的通量密度/环量密度定义反求 div、rot（大纲含 Gauss/Stokes，不宜简单判 out_of_scope）· OR-10 柱/球坐标下的 div、rot 公式（判 out_of_scope 合理，但应显式写出理由）。

## 四个靶子的正面裁定

**① 一个不分叉的领域是否值得建族？→ 值得，但必须先撤回「不分叉」这个自我刻画——该刻画是错的，而且正是它掩盖了本次发现的三个 blocker。**

审查方提出的可复用判据：
- **C1（真实决策点）**：至少一个 cell 内存在 ≥2 条**都合法**的 route，且 applies_when 互不包含——即选错 route 会导致**无法完成**而不只是变慢。
- **C2（guard 择路）**：至少一条 guard 的作用是在 route 之间**择路**，而不只是校验单条 route 的参数。
- **C3（scope 内实例）**：C1 的分叉点在 scope 清单的具体题目上被触发过，而非纯理论构造。
三条同时满足 ⇒ 值得建族；只满足 C3 或全不满足 ⇒ 应降格为方法速查条目并入 分析/高数方法速查.md。

应用到本族：
- C1 满足。旋转曲面格实有三条 applies_when 互不包含的合法 route：R1 口诀（母线⊂坐标面 ∧ 轴=坐标轴）、R2 消参法（轴=坐标轴，母线任意）、R3 一般轴（垂足参数守恒）。**R1 对 2013-19 不是慢，是不可用。** 场量格实有两条：定义硬算 与 复合恒等式。
- C2 满足。择路判据可写死：「母线是否含于坐标面 / 轴是否为坐标轴」二维分类；「场是否为复合算子作用的结果」。
- C3 满足。8 题里 3 题落在分叉点上（2013-19、2025-20、2026-11）。
- 距离格（1 题）与投影格（1 题）确实近乎不分叉，单独成族不满足 C1，但作为本族的两个 cell 挂靠可接受。

审查方的反向 caveat：**若 integrator 选择不补这三条 route 而维持现状，剩下的确实就是一张四条公式的核对表，那时结论反转为「不值得建族」**，应并入 分析/高数方法速查.md。即：这个族值不值得建，取决于 blocker 怎么修，不取决于文风。
- **integrator_verdict: 采纳该判据与结论。** 这是本次五份报告里最有价值的方法论产出——它把「值不值得建族」从审美问题变成了可判定问题，且可复用于其余八族。记为跨族待办：用 C1/C2/C3 回扫已建各族。

**② B4 反例复算 → 成立，且确实支撑它所标注的 failure_boundary。**
代 z=−(x+y) 入 x²+y²+z²=6 得 2x²+2y²+2xy=6，即 **x²+y²+xy=3**（判别式 1−4=−3<0，确为椭圆）。令 z=0 一支：{x²+y²=6, x+y=0} ⇒ (±√3, ∓√3, 0)，恰两点。「一条椭圆 vs 两个点」的量级差异支撑 effect: invalidates。
- integrator 独立复算：代入化简得 x²+y²+xy=3 ✔；抽样点 (t, y(t), z(t)) 对 t=0.3/1.1/2.0 回代球面得 6.000000 且 x+y+z=0 ✔。
- **但该反例只封住 A2 的一个失效方向**；反方向（消元结果是严格超集）无任何 boundary 覆盖 ⇒ BL-3。

**③ 三道场量题的归并是否牵强？→ 归并理由牵强（应改写），归并结果可暂时接受。**
- 「路由结构相同（认公式→定参数→代入算）」**不构成合并的充分理由**：这个结构在高数里近乎普适——点到平面距离、旋度、格林公式、二阶常系数通解、泰勒展开都符合它。以它为判据会把大量互不相干的考点吸进同一族，且**不可证伪**。族的边界应由 objects/target_tasks 与考纲章节决定，不由「解题动作的抽象形状」决定。
- **考纲证据直接反对这个归并**：分析/考纲.md 把散度与旋度写在「**6. 多元函数积分学** — 格林公式、高斯公式、斯托克斯公式、散度与旋度」，而空间解析几何写在「**4. 向量代数和空间解析几何**」。两者分属不同章，且散度/旋度与 vector 族的三大公式在同一行。本族的合并跨了考纲章界，文件却完全没提这一点。
- 但与 vector 族的边界在 objects 上不自然：vector 族声明的 objects 是四类积分，而这三题都不含积分。
- 三选一（审查方倾向 (ii)）：(i) 迁入 vector 族并扩写其 objects；(ii) 保留在本族，但把家族定位的理由从「路由结构相同」改为「考纲第 4 章 + 第 6 章的场量算子部分，三题不足以单开一族」这一**明示跨章**的实用理由，并在 scope.exclusions 说明与 vector 族的分界（含积分 → vector；只求算子 → 本族）；(iii) 单开 calc.field-operator 微族。
- **integrator_verdict: 采纳 (ii)。** 理由诚实、边界可判、不动 TSV（TSV 三题主考点均为「旋度与散度的计算」，按 scope_boundary_rule 无须改归属）。记为 open item。

**④ B6 是合理的 scope 限制还是漏解？→ 漏解（B1）。** 见 BL-2。

## counter_witnesses
- **verified**：B1（结论成立，witness 文本有 NB-1 的自相矛盾句）、B2（|n|=3，分子 |2+4+3−1|=8，d=8/3≈2.6667；自检点 (0,0,1) 在平面上且到 (1,2,3) 距离 3 ≥ 8/3，与 8 矛盾 ✔）、B3（div(x,y,z)=3, curl=0；div(−y,x,0)=0, curl=(0,0,2) —— 双向反例成立，「互不蕴含」被完整证明，**这是全族最干净的 witness**）、B4（见靶子②）、B5（proof，z=√(x²+y²) 平方后得双叶锥，解集确被扩大；归因不完整见 NB-5）。
- **refuted**：B6（数学内容正确，但被用来支撑「不在 scope」，witness 与命题错配）· curve_projection 的 `search_result: not_found`（被 BL-3 证伪）· field_quantity 的「三题均为直接场」（被 2026-11 证伪）。
- **pending**：surface_of_revolution 与 distance 的 counter_witness_search 在受限条件下同样 not_found，**但这两个 target 的措辞把「位置不合规」的情形排除在搜索之外，属于把搜索范围收窄到自己已知安全的区域**。建议重述 target。
- **integrator_verdict**：最后这条观察（搜索 target 自我收窄）值得推广到其余各族复查。

## guard_audit（8 条）
- 无一条标 sufficient；level_1_router 的「对象基本决定了设问」实质是一条 sufficiency 主张，却未以 guard 形式落到 logical_role 里被审。
- **未发现「把效率偏好写成合法性条件」**——guard#8（叉积法通常比先求垂足短）正确标为 supporting_heuristic，preference_rule 也明写「这是效率判断，不是合法性判断」。**这一点本族做得好。**
- guard#4（div 产标量 / curl 产向量）是全族定性最扎实的一条，B3 双向反例支撑充分。
- guard#7 的 **condition 正确但 explanation 错误**：「一般情形需先做坐标变换，超出本族 scope」——2013-19 与 2025-20 证明这两类都在 scope 内，且坐标变换对 2013-19 根本无用（轴已经是坐标轴，问题出在母线）。**这条 guard 的 explanation 是 BL-1/BL-2 的直接载体。**
- 主要问题不是定性错，而是 guard **覆盖面漏了两个方向**（旋转曲面的适用性、投影的值域约束）。

## excluded_candidates 四种理由的使用
`invalid`（令被投影变量为 0）✔ · `out_of_scope`（由散度/旋度反推场）✔、（绕一般直线旋转）**误用** · `duplicate_mechanism`（到轴距离不变）**误用** · `dominated_not_excluded` 五处定性均正确且都未删除，符合协议，唯 field_quantity 那条的 note 内容失实。

## status_recommendation
`challenged` · reopen_family: true

## integrator 处置
- **status: candidate → challenged + quarantine**（BL-3 为已复核 direct counter-witness；BL-1/BL-2 为已复核 scope 内漏解）。
- 已修复：BL-4(a) 旋度 mapping、BL-4(c) scan_basis。
- 未修复（open blockers）：BL-1、BL-2、BL-3、BL-4(b)；open items：BL-5、NB-1..6、靶子①③ 的改写。
- 四格 `no_direct_blocker_open` 置 false，`cell_status` 回落 `open`。
- **OQ-1 裁定：驳回**（2025-20 主考点实测为「旋转曲面的方程」，归本族无误）。**OQ-2 裁定：采 (ii)**（三题留本族，改写归并理由为跨章实用理由）。
