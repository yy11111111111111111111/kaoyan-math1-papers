# 独立审查 · calc.multiple-integral.route-selection（重积分）

```yaml
task_id: batch3.multiple-integral.independent_audit
reviewer: claude-batch3-reviewer-3（独立审查 agent，未参与建族）
artifact_identity: { branch: claude/postgraduate-math-exam-analysis-czoi3t, head: a635bd6 }
audited_at: 2026-08-29
scope_checked:
  file: 分析/方法族-高数-重积分.md（531 行，16 题）
  cells: [double_integral_value, triple_integral_value, order_exchange, sign_or_zero, centroid]
  actions: A1–A9 全部；guards 9 条全部；boundaries B1–B6 全部复算
  source_tsv_sha256: cbdf1a55989a8f60 与 分析/考点标注.tsv 实测一致
  lint: error 0 · warning 4（与基线一致）
note: integrator 归档；integrator_verdict 为 integrator 的独立复核结论。
```

## findings.blockers

### BL-1 · B1 · 设问轴缺「表示互化」与「比较大小」两个取值
- 设问轴只有 [求值, 换序, 判零或定号, 求形心质心]。
- 2006-8、2015-4（TSV 主考点均为「极坐标与直角坐标下二重积分的互化」）：设问是**表示互化**，不是求值也不是换序。强行落「换序」格只有 A7，其三步 local_operation 全写在直角坐标语境，产不出极坐标形式；A2（极坐标）的 eligible_cells 是 [二重求值]，在换序格不可达。
- 2009-2：正方形被对角线分成 D₁..D₄，I_k=∬_{D_k} y cos x dA，问 max_k I_k。|x|≤1<π/2 ⇒ cos x>0；左右两块按 y 的奇性归零，上块 >0、下块 <0 ⇒ max = I_top。**最后一步「跨区域比较」在本族无载体**。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。

### BL-2 · B1 · 「换序作为求值手段」在二重求值格不可达
- 「二重 · 求值」格候选是 [A1,A2,A3,A6]，A7 的 eligible_cells 只有 [换序]。但 guard#9、A7.applies_when、fallback_policy 三处都写「原次序积不出时换序」——路由却到不了 A7。
- 载体 2013-15（TSV 主考点即「交换积分次序」）：算 ∫₀¹ f(x)/√x dx，f(x)=∫₁ˣ ln(t+1)/t dt。设问是「计算」⇒ 落求值格；A1 可选但内层无初等原函数，直接死路；决定答案的正是 A7。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。

### BL-3 · B2 · guard#1 把奇偶性写成 A3 整条 action 的必要条件，阻断轮换分支
- 原文 guard#1：「A3 的对称性化简要求**区域的对称性**与**被积函数的奇偶性**同时成立，缺一不可」，logical_role: necessary。
- 但 A3 的第三个分支（轮换对称）只需「区域在变量置换下不变」，不需要任何奇偶性。按 guard 字面执行，轮换分支在所有无奇偶性的题上被判不可用。
- scope 内反例 2015-12（TSV 主考点即「三重积分的对称性」）：Ω={x,y,z≥0, x+y+z≤1}，∭(x+2y+3z)dV。Ω 在任意置换下不变 ⇒ ∭x=∭y=∭z ⇒ I=6∭x=6·(1/24)=**1/4**。而 x+2y+3z 在任一变量上既非奇也非偶，Ω 也不关于任一坐标面对称——guard 的两条前提都不成立。
- 纯构造反例：同一 Ω 上 ∭ x/(x+y+z) dV，轮换给 3I=∭1 dV=|Ω|=1/6 ⇒ I=**1/18**。
- **integrator_verdict: ACCEPTED · 已修复**。integrator 独立蒙特卡洛复算（4×10⁶ 点）：∭(x+2y+3z)=0.2495（对 1/4）、∭x/(x+y+z)=0.05545（对 1/18）、∭x=0.04157（对 1/24）。guard#1 已拆成「奇偶分支（scope: A3 的奇偶分支）」与「轮换分支（scope: A3 的轮换分支，对被积无奇偶要求）」两条。

### BL-4 · B1 + B4 · A3 在三重格无实算出口
- A3.followup 是 `mode: any_of`，唯一 action_ref 是 A1（二重·直角累次，eligible_cells: [二重求值]）。三重题用完对称性后需要 A4/A5/A6 继续，A3 没有到它们的边 ⇒ 未终止且无合法后继。A9（形心质心）的 sequence 强制转 A3，继承同一死路。
- 载体：2009-12（∭_{x²+y²+z²≤1} z² dV，轮换给 3I=∭ρ²dV，terminal_when「对称性直接给出积分为 0 或所求比例」不满足——给的是比例不是值，余下必须走球坐标 A6）；2010-12；2019-19。
- **integrator_verdict: ACCEPTED（未修复，open blocker）**。

### BL-5 · B4 · A6 的 eligible_cells 与格清单不一致，且 lint R2 对本文件不执行
- 「二重 · 求值」格列 A6 为候选，而 A6 自称 `description: 柱面坐标或球面坐标换元（三重）`、`applies_when: [三重, …]`、`eligible_cells: [三重求值]`。若在二重格选中 A6，其 followup 强制 action_ref → A4（三重投影法），后继在本格同样非法。
- R2 因 CELL_ALIAS 缺本族格名而整体跳过；用本文件自身格名重跑 R2 逻辑，得到且仅得到这一条 MISMATCH。
- 附带范围：batch2/batch3 各族的 level_2_candidates 都用中文格名且无 cell_id ⇒ R2 对 batch1 以外全部空转。
- **integrator_verdict: ACCEPTED · 已修复**。integrator 实测 R2 覆盖 11 族中的 4 族（vector/ode/series/multivar），对 7 族空转。已修 lint（补 CELL_ALIAS + 回落原始格名 + 无格可解析时报错）；R2 上线后即报本条，已把 A6 从「二重 · 求值」清单移除。

## findings.non_blocking（摘要）
- **NB-1（severity: high）** positive_instance_mapping 10 条引用中 5 条与 TSV 冲突：A7 列 2009-2（应 A3/A8）与 2026-4（应 A3；真正的换序题 2025-4 反而未列）；A2 列 2015-12（是三重题）；A3 列 2010-12（应 A9）；A9 列 2024-17（应 A2，且与形心无关）。**integrator_verdict: ACCEPTED，未修复，记 open item。**
- NB-2 scan_basis 引用不存在的 `高数真题题面_2004-2023.md`；且 **2024-17 在 papers/ 两份 2024 文件中题干均为空**（只有「17.」与【答案】），以它为正例的断言现阶段不可核。**scan_basis 已修复。**
- NB-3 guard#4 把**画图**写成 necessary。数学上必要的是「以区域集合为中介重新定限」；由不等式组直接消元同样正确。「画图」应降 supporting_heuristic。**这是本族唯一一处「执行手段被写成合法性条件」。**
- NB-4 order_exchange 的 route_universe 写「唯一结构 … 没有第二种合法机制」，是变相 exhaustiveness 断言，且被 BL-1 证伪。
- NB-5 B4 witness 的变量指认写反（「外层对 x 积分而其限含 x」——所写表达式外层是对 y 积分）。结论正确。
- NB-6 A6→A4 的 action_ref 把球坐标定限描述成了投影法。
- NB-8 二重格漏了与三重格对称的两条 excluded_candidates（反用格林公式 → duplicate_mechanism；广义极坐标 → dominated_not_excluded）。

## omitted_routes（差集，16 条，摘要）
OM-1 换序进求值格（→BL-2）· OM-2 几何意义直接读值（被积≡c、√(1−x²−y²) 读半球体积）· OM-3 **按被积函数分片点分块**（2005-15 的取整函数、2024-17 的分区域计算，现只作 A1 的一句 local_operation）· OM-4 广义极坐标 · OM-8 三重的一般变量代换 + 雅可比（二重格记了、三重格漏记）· OM-9 立体分割（只出现在 B5.recovery，未作 route）· OM-11 轮换对称（→BL-3）· OM-12 直角↔极坐标互化（→BL-1）· OM-14 分块后逐块归零/定号再合成（2009-2 的实际路线）。

**对靶子③的结论**：三重定限除投影法/截面法外**没有第三种独立的定限机制**——柱/球坐标下的「直接定限」与投影法同属「按不等式逐层定限」，判 duplicate_mechanism（但 A6→A4 的措辞把它错写成投影，NB-6）；**区域分割**是可加性、**一般变量代换 + 雅可比**是独立路线，两者都是三重格的漏列。

## counter_witnesses
- **verified**：B1、B2、B3、B5、B6 全部复算通过。
  - **B1（靶子①）成立且可加强**：D_up={0≤x≤1, x≤y≤1}、D_low={0≤y≤1, y≤x≤1}；f=x 给 1/6 vs 1/3（可检出），f=xy 给 **1/8 vs 1/8**（检不出）。
    **加强版结论（本次独立得出）**：「调换上下限」总是产出 σ(D) 上的积分（σ(x,y)=(y,x)），对**任意** D 成立；于是当 f(x,y)=f(y,x) 时 ∬_{σ(D)}f = ∬_D f∘σ = ∬_D f，错误答案**恒**等于正确答案。已在非对称曲边区域 D={0≤x≤1, 0≤y≤x²}、f=xy+x²y² 上验证（两者均 13/108），另验 f=e^{xy}+cos(x+y) 于原三角形（两者均 0.907326799868913）。**⇒ 自检失效不是 f=xy 的偶然，也不限于三角形区域。**
  - B2：单位圆盘 ∬x dA=0；半圆盘（∩{x+y≥0}）∬x dA=√2/3≈0.4714。被积同为奇，仅区域对称性不同 ⇒ witness 名副其实。**但它只证明区域对称性对奇偶分支必要，不能支撑 guard#1 推广到 A3 整条 action（BL-3）。**
- **refuted**：无。
- **partially_defective**：B4 结论成立、论证措辞有误（NB-5）。
- **integrator_verdict**：B1 的两个 1/8 我已独立数值复算（0.12492 / 0.12508，网格误差内），加强版结论我认为正确且应写回文件——它比原文件「这两个三角形上都等于 1/8」的解释强一个量级。记为 P1 待办。

## guard_audit（9 条）
0 条 sufficient；效率类 3 条全部正确地标 supporting_heuristic，preference_rule 明确自述是效率排序。问题集中在两条 necessary：#1 覆盖过宽、阻断合法路线（BL-3，已修）；#4 把「画图」这个执行手段写成必要条件（NB-3，未修）。#9 定性正确但指向的 A7 在求值格不可达（BL-2）。

## status_recommendation
`challenged` · reopen_family: true

## integrator 处置
- **status: candidate → challenged + quarantine**（BL-3 为已复核 direct counter-witness）。
- 已修复：BL-3、BL-5、scan_basis 文件名。
- 未修复（open blockers）：BL-1、BL-2、BL-4；open items：NB-1、NB-3、B1 加强版结论。
- 五格 `no_direct_blocker_open` 置 false，`cell_status` 回落 `open`。
