# 独立审查 · calc.int1v.route-selection（一元积分学）

```yaml
task_id: batch3.int1v.independent_audit
reviewer: claude-batch3-reviewer-2（独立审查 agent，未参与建族）
artifact_identity: { branch: claude/postgraduate-math-exam-analysis-czoi3t, head: a635bd6 }
audited_at: 2026-08-29
scope_checked:
  file: 分析/方法族-高数-一元积分学.md（645 行，36 题，全文逐行）
  cells: 5 格全部；actions A1–A11 全部；guards 12 条全部；boundaries B1–B8 + revision_history 的 retired_rule
  lint: error 0 · warning 4（与基线一致）
note: integrator 归档；integrator_verdict 为 integrator 的独立复核结论。
```

## findings.blockers

### BLK-1 · B1 · 「由图形/几何意义直接读积分值」这条路线整族不存在
- 载体：2007-3（在 36 题清单内）。f 只由图形给出（[-3,-2] 与 [2,3] 上直径 1 的上下半圆周，[-2,0] 与 [0,2] 上直径 2 的下上半圆周），无解析式。F(x)=∫₀ˣf。
- A1–A5 全部要求被积式可写出；A6 给 F′=f 但设问要的是 F 在四点的数值比例；A7 的性质表四行都判不出；A9/A10/A11 均不接收。
- 正确路线：∫₀²f=π/2、∫₂³f=−π/8、∫_{-2}^{0}f=−π/2、∫_{-3}^{-2}f=π/8 ⇒ F(3)=3π/8、F(2)=π/2、F(−3)=3π/8 ⇒ F(−3)=(3/4)F(2)。全程只用「半圆面积 ½πr²」。
- 同类：2017-4（速度曲线三块阴影面积 10/20/3 求位移）、2009-3（由 f 图形选 F 图形）、2012-10（配方后拆奇函数 + 半圆面积 π/2）。
- 该路线既不是 action，也不在任何 route_universe，也不在 excluded_candidates。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。

### BLK-2 · B1 · 缺「分段/绝对值拆区间 + 由连续性定各段常数」
- 载体：2016-2。f=2(x−1) (x<1)、ln x (x≥1)，问 f 的一个原函数。四选项在 x<1 分支完全相同，差别只在 x≥1 的常数。
- A1–A5 逐段都能积出，但 terminal_when 均为「已积出」——(A) x(ln x−1) 与 (D) x(ln x−1)+1 在 x>1 上导数都等于 ln x，无法区分。
- 决定答案的唯一条件是 F 在 x=1 连续：F(1⁻)=0；(A) 给 F(1⁺)=−1≠0；(D) 给 0 ✓ ⇒ (D)。
- 「连续性定常数」在 artifact 中不存在。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。

### BLK-3 · B2 · guard#3 把充分条件登记为 necessary，check 是假命题
- 原文：condition「『f 偶 ⇒ F 奇』要求**下限为 0**」，logical_role: necessary，check「下限非 0 时该结论不成立」。
- 反例：f(t)=t²−1（偶），下限 a=√3。G(x)=∫_{√3}^{x}(t²−1)dt = x³/3−x，**是奇函数**。根因 ∫₀^{√3}(t²−1)dt=0。
- 一般结论：F(x)=∫ₐˣf = ∫₀ˣf − ∫₀ᵃf，∫₀ˣf 恒奇 ⇒ **F 奇 ⟺ ∫₀ᵃf=0**。「a=0」只是充分条件。
- B3 的 witness（f=t²+1, a=1）只证明「a=0 是不可省的充分性前提」，支撑不了 necessary。
- 内部矛盾：A7 性质表写的是「f 偶且下限为 0 ⇒ F 奇」（充分，正确），与 guard#3 的 necessary 冲突。
- **integrator_verdict: ACCEPTED · 已修复**。integrator 独立数值复算：G(1)=−0.666666667、G(−1)=+0.666666667，G(1)+G(−1)=4.3e−11；∫₀^{√3}(t²−1)dt=−1.1e−11。condition 改为「∫₀^{下限}f=0（等价 F(0)=0）」，check 与 explanation 同步重写。

### BLK-4 · B4 · positive_instance_mapping 13 个题号引用中至少 9 个不符
- A6 ref「2004-7、2008-1、2010-9、2011-9、2016-9」：2004-7 不在本族清单；2010-9 主考点归 diff1v；2011-9 是弧长题（主设问 A11）；2016-9 是极限题（A6 不产生答案）。仅 2008-1 正确。
- A7 ref「2010-16、2014-4」basis 写「变限积分的奇偶性与周期性判定」：2010-16 求单调区间与极值；2014-4 是二元极值 + 定积分求值。两题都不是。
- A8 ref「2005-8、2007-3」basis 写「比较定积分大小」：2005-8 是 A7 性质表题；2007-3 是图形面积题。两题都不是比大小。
- A9 ref「2012-4、2018-4」basis 写「反常积分求值」：**两题都不是反常积分**（都是比大小）。而 scope 内真有三道 A9 正例（2013-12、2021-11、2026-14）一条未引。
- A11 ref「2011-19、2019-18」basis 写「面积与弧长」：2011-19 是二重积分；2019-18 是递推。真正的 A11 正例（2009-16、2019-17、2011-9）一条未引。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。evidentiary_weight: none 只限制权重，不豁免事实正确性。

### BLK-5 · B4（R2 类）· A10 的 eligible_cells 与格清单不一致，且 lint R2 对本文件不执行
- A10 声明 `[积分的性质与比大小, 不定积分与定积分求值]`，evidence 里也确以 route I6 出现在 antiderivative_and_definite 格，但该格 actions 清单无 A10。
- R2 因 CELL_ALIAS 缺本族格名而整体跳过（复现见 diff1v 报告 BL-6）。
- **integrator_verdict: ACCEPTED · 已修复**。修 lint 后 R2 即报出本条；已把 A10 补进「不定积分与定积分求值」的 actions。

### BLK-6 · B4 + B1 · scope 与 exclusions 自相矛盾，两题在九族中无家
- scope.exclusions 写「用积分做的中值定理证明」属 calc.mvt-proof，但 2026-20、2008-18 就在本族 36 题清单里，而 mvt 族清单不含它们。
- 2026-20：证 ∃a>0 使 F(a)=∫₀¹f、∃ξ 使 F″(ξ)=0——设问动词是「证明」，第二轴四个取值都不含。
- 2008-18(I) 要求**用定义**证 F′=f，而 A7 的做法是查性质表（用被证结论证它自己）。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。按 `on_dispute`，归属由 integrator 裁定，留待下一轮。

## findings.non_blocking（摘要）
- NB-1 A7 声明覆盖单调性，但四行 local_operation 里没有单调性那一行。
- NB-2 guard#8「A2 换元须一一对应」对**定积分**非必要（∫₀^{5π/2} sin t cos t dt = 1/2 = ∫₀¹x dx，φ=sin t 非单调）；对不定积分回代才必要。
- NB-3（靶子②）A9 的 boundary_note「只管求值」与其自身第三条 local_operation、B5/B6 冲突——A9 事实上在用定义判敛散。边界切得对，表述应改为「用**定义**判敛散+求值归本族；**比较/比阶**判别归级数族」。会卡中间的：参数型题（先级数族判别、再回本族求值）只有单向 handoff；2019-17（无穷多块面积 → 等比级数）三处都没声明该复合路线。
- NB-4（靶子①）guard#4「∫₀ᵀf=0」定性 necessary 正确但**过弱**：实为**充要**，且 ∫₀ᵀf=c≠0 时 F(x+nT)=F(x)+nc 无界 ⇒ F **不以任何数为周期**。**integrator_verdict: 与 integrator 的独立推导一致（F(x+T)−F(x)=∫ₓ^{x+T}f=∫₀ᵀf 与 x 无关）。记 backlog。**
- NB-5（靶子④）三条 `dominated_not_excluded` 的裁定：
  - **万能代换 t=tan(x/2)**：考纲含「三角函数有理式的积分」⇒ 理由用得**对**。
  - **帕普斯-古尔丁定理**：考纲定积分应用只有面积/体积/弧长，无此定理 ⇒ 数学合法但**超纲**，正确理由应为 `out_of_scope`，现状是**理由误用**。
  - **积分中值定理比大小**：定理在大纲内，当工具用不与「证明题归 mvt 族」冲突 ⇒ 用得**对**。
- NB-6（靶子③）retired_rule 反例 ∫₀^{x²}t dt = x⁴/2 成立（x=0.1→5.000e−05，x=0.01→5.000e−09），确实击穿了**如其所写**的无限定表述。保留意见：对「上限恰为 x 且 f~ct^k」的版本规则实际成立，应在 note 里点明，避免后来者以为 ∫₀ˣ 版本也错。
- NB-7 12 条 guard 中 0 条 sufficient；NB-4 与修正后的 BLK-3 都是充要，三分法应至少出现一次。
- NB-8 §3 边界表列了四条邻族边界，独缺 calc.limit 与 calc.diff1v，而 2016-9/2025-1/2010-17(II)/2019-18(II) 的决定性步骤都在族外。

## omitted_routes（差集结果）
OR-1 几何/物理意义读值（→BLK-1）· OR-2 分段+连续性定常数（→BLK-2）· OR-3 区间再现换元 x→a+b−x · OR-4 构造辅助积分联立 · OR-5 积分方程两边求导 + 由初值定 C（2004-2）· OR-6 和式极限化定积分 · OR-7 无穷多块面积 → 级数求和（2019-17）· OR-8 变限积分 + 洛必达求极限（2016-9）· OR-9 平移/伸缩换元标准化 · OR-10 退化短路。

## counter_witnesses
- **verified**：B1、B2、B5、B6、B7、B8、B4、retired_rule 全部复算通过。B4 反例（f=sin+1 时 F(1)=1.45970、F(1+2π)=7.74288，差 6.28319=∫₀^{2π}f）成立。
- **refuted**：B3 支撑不了 guard#3 的 necessary 定性（见 BLK-3）。
- **search_result: not_found**（另做的四轮反例搜索）：A9 逐段收敛相加、A4 部分分式重根、A6 补齐后、A10 周期平移。

## guard_audit（12 条）
necessary 正确 7 条；**necessary 错误 1 条**（#3，BLK-3）；necessary 过强 1 条（#8，NB-2）；supporting_heuristic 正确 3 条；sufficient 0 条。**「效率偏好写成合法性条件」未发现**——preference_rule、A7 efficiency_note、A3 LIATE 定性均正确。

## status_recommendation
`challenged` · reopen_family: true

## integrator 处置
- **status: candidate → challenged + quarantine**（BLK-3 为已复核 direct counter-witness）。
- 已修复：BLK-3、BLK-5、scan_basis 文件名。
- 未修复（open blockers）：BLK-1、BLK-2、BLK-4、BLK-6。
- 五格 `no_direct_blocker_open` 置 false，`cell_status` 回落 `open`。
