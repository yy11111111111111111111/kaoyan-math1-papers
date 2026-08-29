# 独立审查 · calc.mvt-proof.route-selection（中值定理与证明）

```yaml
task_id: batch3.mvt-proof.independent_audit
reviewer: claude-batch3-reviewer-4（独立审查 agent，未参与建族）
artifact_identity: { branch: claude/postgraduate-math-exam-analysis-czoi3t, head: a635bd6 }
audited_at: 2026-08-29
scope_checked:
  file: 分析/方法族-高数-中值定理与证明.md（583 行，8 题）
  cells: [existence_equality, inequality, root_count, identity_or_bounded]（四格全审）
  actions: A1–A10；guards 11 条全部；boundaries B1–B7 全部
  lint: error 0 · warning 4（与基线一致）
note: integrator 归档；integrator_verdict 为 integrator 的独立复核结论。
```

## findings.blockers

### BL-1 · B1 · 存在性等式格缺零点/介值定理这条终结路线
- 载体 2005-18(I)：f 在 [0,1] 连续、(0,1) 可导、f(0)=0、f(1)=1，证 ∃ξ∈(0,1) 使 f(ξ)=1−ξ。
- 待证式含「存在 ξ」⇒ 一级路由必落存在性等式格 = [A1,A2,A3,A4]。四者无一能接：A1 需待证式已是中值定理标准结论；A2 可构造 F(x)=f(x)+x−1，但其 followup 是 `mode: all_of` 且含强制 `action_ref: A1（用罗尔）`——而 F(0)=−1≠1=F(1)，罗尔条件不成立；A3 需二阶导；A4 是 never_terminal 且后继只有 A1/A3（都是罗尔系）。
- 唯一合法解法是零点定理：F 连续、F(0)=−1<0、F(1)=1>0 ⇒ ∃ξ，F(ξ)=0。而 A8（零点定理）的 eligible_cells 只有 [实根个数]。
- 内部矛盾：level_1_router 规则写「不含导数走零点/介值」，该格 route_universe 也把零点、介值列入定理清单——**规则承诺的分支在 level_2 不存在**。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。integrator 已核对题面（分析/高数真题题面_2004-2010.md）与四格清单，确如所述。

### BL-2 · B1 · 不等式格缺「逐点估计 + 积分保序」
- 载体 2024-19(2)：由 (1) 的逐点估计 |f(x)−[(1−x)f(0)+x f(1)]| ≤ x(1−x)/2，两边在 [0,1] 上积分并用 |∫g|≤∫|g|，得 |∫₀¹f − (f(0)+f(1))/2| ≤ ∫₀¹x(1−x)/2 dx = 1/12。
- 机制是「逐点不等式 ⇒ 积分不等式」的保序性，既非 A5（作差求导定号）、非 A6（拉格朗日估界）、非 A7（泰勒余项定号）、非 A2（转存在性）。不等式格的 route_universe 四条全不覆盖。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。

### BL-3 · B2 · guard#4「A7 要求余项导数整区间定号」被 2024-19(1) 直接击穿
- 载体 2024-19(1)：f 二阶可导、**|f″(x)| ≤ 1**，证 |f(x) − f(0)(1−x) − f(1)x| ≤ x(1−x)/2。
- 在 x 处展开：f(0)=f(x)−f′(x)x+f″(η₁)x²/2；f(1)=f(x)+f′(x)(1−x)+f″(η₂)(1−x)²/2。前式乘 (1−x)、后式乘 x 相加，f′(x) 项系数 −x(1−x)+x(1−x)=0 抵消，得
  (1−x)f(0)+x f(1) − f(x) = (1−x)x²f″(η₁)/2 + x(1−x)²f″(η₂)/2。
  取绝对值并用 |f″|≤1：≤ (1/2)x(1−x)[x+(1−x)] = x(1−x)/2。∎
- **全程未用 f″ 的符号，只用了 |f″| 的界；f″ 完全可以变号**（取 f″=cos 20x 即为一实例）。
- 连带 B1 侧面：A7 的 followup 是 sequence，第三步强制「判定该阶导数在整个区间上的符号」——2024-19(1) 无法执行这一步。
- 附带：B4 的第二条 witness 标 `kind: constructed_counterexample`，但正文是「**设**某函数在左半段为正、右半段为负」，没有给出任何具体函数，**名不副实**。
- **integrator_verdict: ACCEPTED · 已修复**。integrator 独立复核了泰勒相加的代数（f′(x) 项确实抵消）。guard#4 已改为「须有在 ξ 全范围上一致的估计：定号（定方向）**或**有界（定绝对值）」，并写入完整推导。

### BL-4 · B1 · A5 缺「逐阶降解」与「最小值定号」
- 载体 2012-15：证 x·ln((1+x)/(1−x)) + cos x ≥ 1 + x²/2，−1<x<1。令 F 为左减右，F(0)=0，F′(0)=0 但 **F′ 无法直接定号**；须再降一层：F″(x)=2/(1−x²)+2(1+x²)/(1−x²)²−cos x−1 ≥ 2>0（数值最小值实测 2.0）⇒ F′ 严格增、F′(0)=0 ⇒ F 在 x=0 取最小值 0 ⇒ F≥0。
- A5 的 applies_when 明写「导数**易定号**」（此处不成立），且 followup 是三步定长 sequence，没有「对 F′ 再走一次同样流程」的自递归边；A5 只有「单调性 + 端点值」，而本题 F 在区间**内部**取最小值，单调性+端点值推不出符号。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。

### BL-5 · B4 · A2 的 mandatory continuation 悬空
- A2 的 `eligible_cells: [存在性等式, 不等式]`，followup 是 `mode: all_of`，最后一项是强制 `action_ref: A1`。而 A1 的 eligible_cells 只有 [存在性等式]，不等式格的清单也不含 A1。
- ⇒ 在**不等式格**选中 A2 后，强制后继指向一个本格不可用的 action，正命中 B4 定义的「mandatory continuation 可悬空」。
- 语义上也错：2012-15（构造 F 后走单调性）与 2017-18(II)（构造 F=f·f′ 后走**两次**罗尔即 A3）都表明 A2 的正确后继是 any_of{A1, A3, A5}。
- lint 缺口：R1 只查 action_ref 存在性，R2 只查单个 action 与格的一致性，都查不出「强制后继在源 action 可用的每个格里是否也可用」。建议新增 R3。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。integrator 已核对 A2 的 `mode: all_of` 与两族 eligible_cells，确如所述。R3 的建议合理，记为跨族待办。

### BL-6 · B2 · guard#6 的族级 necessary 定性被反例击穿（靶子③）
- 原文：「要证 f^{(n)}(ξ)=0 需要 **n+1** 个等值点」，logical_role: necessary，check「数一下手上有几个等值点；不够则先用 A2 补」。
- **计数本身正确**：k 个等值点 ⇒ 罗尔给 f′ 的 k−1 个零点（对 f′ 而言又是等值点，值同为 0，递推可继续）⇒ f^{(n)} 有 k−n 个零点；要 ≥1 得 k ≥ n+1。
- **但族级 necessary 是错的**——n+1 个等值点是 A3 这条路线的条件，不是命题的必要条件。反例：f(x)=x³ 于 [−1,1]，f″(x)=6x 连续且 f″(−1)=−6<0<6=f″(1)，介值定理即得 ξ=0 使 f″(ξ)=0，**用到的等值点个数为 0**。更一般地，题给 f′(a)=f′(b) 时对 f′ 用一次罗尔即得 f″(ξ)=0。
- check 还会主动误导（「不够则先用 A2 补」）：2007-19 的正解是用最值定理+介值定理（A4）造点。
- **integrator_verdict: ACCEPTED · 已修复**。guard#6 已 route-scope 到 A3（`scope: A3`），并写入计数递推与 f=x³ 反例。

## findings.non_blocking（摘要）
- **NB-1** positive_instance_mapping 四条中三条与题面不符——**这解释了 BL-1/BL-2/BL-4 为何能漏过：建族方看来没把 8 道 scope 题真的过一遍路由器**。
  - `A7 ← 2007-19`：该题证的是 ∃ξ 使 f″(ξ)=g″(ξ)（**等式**不是不等式），正解 F=f−g，最值+介值造第三个零点再两次罗尔（A4→A3）。
  - `A7 ← 2017-18`：该题证「方程至少有两个实根」，正解构造 F=f·f′（注意 (f f′)′=f f″+(f′)²）再两次罗尔，即 A2→A3，与泰勒无关。
  - `A2 ← 2012-15, basis: 存在性等式`：2012-15 是**不等式**题，basis 定性错。
- NB-2 guard#3 后半句「问个数必须配单调性分段（A9）」把一个具体 action 写成合法性条件。给根数上界的机制不止 A9：① 罗尔反证（f^{(k)} 恒不为零 ⇒ 至多 k 个根，典型：证 e^x=ax²+bx+c 至多 3 根）；② 多项式次数界；③ 凸性。
- NB-3 A9 只说「求导定出全部**单调**区间」，但「每段至多一根」需要**严格**单调；counter_witness_search 的 note 自己写的就是「严格单调段上至多一根」——正文与其支撑理由不一致。
- NB-4 existence_equality 的 route_universe 写「限于大纲内的**四个**定理」，却列了六个。
- NB-5 scan_basis 引用不存在的 `高数真题题面_2004-2023.md`；scope 含 2024-19 而题面库止于 2023，未声明来源。**已修复。**
- NB-6 identity_or_bounded 格漏了「闭区间上连续 ⇒ 有界（最值定理）」这条最直接的终结路线；该格在 8 题中无任何正例，属结构性空格。

## 四个靶子的正面裁定

**① A2 无一般算法，是否构成 B3 类 schema 表达力 blocker？→ 不构成 B3。**
判据三条：
- (a) **非确定性候选生成能否表达？** 能。`action_kind: framework` + `produces: subproblems` + `terminal_policy: never_terminal` 就是「本步只产出待定子问题、不宣告结论」的忠实编码。可枚举的部分（construction_note 的四条对应表）可直接改写成 `followup mode: any_of` 的四个分支，各带自己的 applies_when（f′+λf → F=f e^{λx}；ξf′+kf → F=x^k f；f′/g′ → 柯西；f 与 ∫f → 变限积分），外加一个「以上均不匹配」的开放分支。不歪曲任何数学关系。
- (b) **验证回路（试→验→换一个再试）能否表达？** 部分能。验证步已在；缺的是**失败回边**。但可用 schema 已有手段无歪曲地表达：给 A2 加 failure_boundary `{effect: changes_branch, recovery: 换一条对应表分支重试，或转 A4}`——`changes_branch` 这个 effect 值正是为分支切换准备的。
- (c) **「创造」本身需要被表达吗？** 不需要。schema 描述路线选择，不是构造算法；一个 action 内部搜索空间开放，不等于 route composition 无法表达。若把「A2 没有一般算法」升为 B3，任何含启发式步骤的 action 都会变成 schema 缺陷，与 HANDOFF 对 B3 的限定相悖。
- 若真要指出缺哪个字段：缺的是 followup 层的**失败回边**（`on_failure`）与**候选池开放性标记**（`candidate_pool: open | enumerated`）。但由 (b) 的等价写法存在，这两个字段属「schema 可以更抽象」= HANDOFF 明列的 backlog 项。
- **integrator_verdict: 同意。不构成 B3；记 backlog。**

**② B3 标 `becomes_inconclusive` 而非 `invalidates` 对吗？→ 正确。**
四值区分：invalidates = 结论变假/推理不成立；becomes_inconclusive = 路线仍可执行、结论仍为真，但答不了所问。用零点定理回答「有几个根」时，「至少有一个根」**依然为真**，推理没有一步失效，失效的是所答非所问。对照：B1（缺罗尔条件）标 invalidates 正确，因为那时结论可假（|x| 的例子里 ξ 根本不存在）。两者在本文件里自洽。
- 补强建议：witness 应给**一对**满足同样假设、根数不同的函数（h=x 与 g=x³−3x 同在 [−3,3] 连续、端点异号，前者 1 根、后者 3 根），才真正证明「定理的输入无法区分二者」。
- **integrator_verdict: 同意分类正确；补强记 backlog。**

**③ A3 的 n+1 计数对吗？→ 计数正确，但 necessary 定性错。** 见 BL-6。

**④ 凹凸性（琴生）该升为正式 route 吗？→ 不该升；但现有 `dominated_not_excluded` 标错，应改 `duplicate_mechanism`（of A7）。**
- 不能是 dominated：其 note 自陈「对含 f((a+b)/2) 或加权平均的不等式**确实更直接**」，而 dominated_not_excluded 的语义是「合法但效率更低」——note 与标签自相矛盾。
- 也不该升为独立 route：机制与 A7 同源。两点情形即在中点作带一阶拉格朗日余项的泰勒展开，f″≥0 相加即得 f(a)+f(b) ≥ 2f(m)；n 点加权是同一展开式 f(x_i) ≥ f(m)+f′(m)(x_i−m) 乘 λ_i 求和，只比 A7 多一个「加权求和」的 local_operation，没有新的合法性依据。
- 另注：该条 note 里「本族 scope 内无正例」是**频率型措辞**，按协议不得作为 route 定性依据，应删。
- 不等式格**另有**四条被漏掉的合法路线：积分保序放缩（BL-2）、逐阶降解+最小值（BL-4）、麦克劳林逐项比较、对称性减半。
- **integrator_verdict: 同意全部四点。记 open item。**

## counter_witnesses
- **verified**：B1、B2、B3、B5、B6、B7 全部复算通过（B2：f=x³−x 于 [−2,2]，平均变化率 3，ξ=±√(4/3)≈±1.1547 两个且都在内部，中点 f′(0)=−1≠3）。
- **refuted**：guard#4 + B4 第二半 witness（BL-3）；guard#6 的族级定性（BL-6）；guard#3 后半句（NB-2）。
- **pending**：2023-20 的题面在题面库中**被截断**（分析/高数真题题面_2021-2023.md 只有「设函数 f(x) 在 [−a,a] 上具有 2 阶连续导数. 证明:」，待证结论整段缺失）⇒ `A3 ← 2023-20` 的定性无法从本族声明的任何来源核验。**该定性若不是来自题面，就只能来自记忆或 solutions/（后者是推断阶段红线）。** 建议标 source_incomplete 并写入 分析/待确认.md。
- **integrator_verdict**：2023-20 题面截断我已核实。这条提示很重要，记为必办项。

## guard_audit（11 条）
「把效率偏好写成合法性条件」这个方向**没有发现**——四条 heuristic（#8–#11）与 preference_rule 定性均得当。发现的是**反方向**的错误：三条 necessary（#3、#4、#6）实际上是 route 内部的充分/执行条件，被提升成族级合法性条件，其中 #4 被 scope 内题目直接击穿。
- 其它：2011-17 的题面有缺陷——「求方程 arctan x − x = 0 不同实根的个数, 其中 k 为参数」，**k 未出现在方程中**（应为 k·arctan x − x = 0）。建议在 待确认.md 单列。

## status_recommendation
`challenged` · reopen_family: true

## integrator 处置
- **status: candidate → challenged + quarantine**（BL-3、BL-6 均为已复核 direct counter-witness）。
- 已修复：BL-3、BL-6、scan_basis 文件名。
- 未修复（open blockers）：BL-1、BL-2、BL-4、BL-5；open items：NB-1、NB-2、NB-3、靶子④、2023-20 与 2011-17 的题面问题。
- 四格 `no_direct_blocker_open` 置 false，`cell_status` 回落 `open`。
