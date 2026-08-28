---
doc_id: claude.independent_review.multivar.ee3605c
reviewer: claude（independent_reviewer，非建者）
audited_artifact: 分析/方法族-高数-多元微分.md
audited_version: 1.0.0
written_at: 2026-08-28
schema: CALC-METHOD-FAMILY-v1.3.1
---

# 独立审查报告：calc.multivar.route-selection（v1.0.0）

本报告只记录意见，不修改被审对象。**全程未读 `solutions/`（含 `分析/解法.md`）**，
判断依据仅来自题面（`分析/高数真题题面_*.md`、`分析/考点标注.tsv`）、大纲（`分析/考纲.md`）、
HANDOFF 与独立数学复算。

```yaml
doc_id: claude.independent_review.multivar.ee3605c
reviewer: claude（independent_reviewer，非建者）
audited_artifact: 分析/方法族-高数-多元微分.md
audited_version: 1.0.0

artifact_identity:
  branch: worktree-batch2-integrator
  head: 6c1ed4c
  worktree_clean: true
  note: 被审文件 frontmatter 自注 generated_at 2026-08-28、source_tsv_sha256 cbdf1a55989a8f60；TSV 实测逐行一致。

scope_checked:
  declared: 40（frontmatter「共 40 题」+ §2 表格 + evidence.positive_problem_ids.count=40）
  claimed: 40
  verified: 40
  method: >
    写独立脚本解析 考点标注.tsv，按每行**考点列第一个（主考点）**推导出
    「主考点 ∈ 认领标签集」的全部题号，与建者 40 题清单双向比对；
    再逐题核对题型（解答/选择填空）与主考点字符串。未复用建者判断。
  main_tag_breakdown:
    "隐函数求偏导": [2004-19, 2010-2, 2015-11, 2016-11, 2026-1]
    "隐函数求导": [2008-10, 2013-9, 2014-16, 2017-17]
    "隐函数存在定理的条件判定": [2005-10]
    "多元复合函数的二阶偏导数": [2005-9, 2006-18, 2009-9, 2011-16, 2014-17, 2017-15, 2024-12, 2025-18, 2026-18]
    "多元复合函数求偏导": [2007-12, 2019-9, 2021-2]
    "变限积分求偏导": [2011-11, 2020-12]
    "方向导数计算": [2005-3, 2017-3, 2025-13]
    "方向导数与梯度的最大值": [2015-17, 2019-16]
    "梯度的计算": [2008-2, 2012-11]
    "多元函数可微的充分必要条件": [2012-3, 2020-3]
    "曲面的切平面与法向量": [2010-19, 2013-2, 2014-9, 2018-2, 2023-12, 2024-18]
    "齐次函数的欧拉定理": [2006-19]
  解答: 14
  选择填空: 26
  scope_verdict: >
    40 题清单与 TSV 主考点推导**完全一致，无漏认领、无越界认领**。2006-19（主考点
    「齐次函数的欧拉定理」）按 SB-5 裁定归本族**正确**——题面确为 f(tx,ty)=t^{-2}f(x,y)
    证 ∮y f dx − x f dy=0，是大纲「多元函数微分学的应用」直接内容，主考点不属任何其它族。
    SB-1 四题（2006-18/2014-17/2025-18/2026-18）主考点均为「多元复合函数的二阶偏导数」，
    归本族**正确**；ODE 族不得重复认领（见 NB-1）。与 series 族（29 题）0 重叠；
    与 batch1 extrema 族旧 evidence 的 4 题重叠（2004-19/2015-17/2019-16/2024-18）为
    HANDOFF 已知的旧宽松口径遗留，本族已在 §5 第 3 条如实上报，未越界。
    排除项全部按主考点判定且理由正确：extrema 12（条件极值 4 + 无条件极值 7 + 有界闭区域最值 1）、
    空间解析几何 7、一元参数方程 5、旋度散度 3——out_of_scope 判定均与 TSV 一致。
    limit_continuity 格 declared 0（not_found）：TSV 全量扫描确认 2004–2026 无多元极限/
    连续主考点题（含「极限/连续」的 17 个主考点全部是一元语境），LC1/LC2 按大纲结构保留、
    以 not_found 记录、不因未出现而排除，**合规**。

findings:
  blockers:
    - id: B1
      class: B2（direct counter-witness）兼 B1（scope 内路由错误）
      title: >
        D1 的 mechanism_note / sufficient guard #4 / positive_instance_mapping 三处把
        2012-3 的正确选项判为 (A)，实际正确选项是 (B)；guard「lim f/(|x|+|y|) 存在 ⇒ 可微」
        被 f=|x|+|y| 直接击穿
      detail: >
        **被审文件的三处断言**（均指向同一错误）：
        (i) D1 mechanism_note（第 331 行）「2012-3 的 (A)：lim f/(|x|+|y|) 存在 ⇒
        f=o(|x|+|y|)=o(ρ) ⇒ 可微（f_x=f_y=0）」；
        (ii) sufficient guard #4（第 555–558 行）「「lim f(x,y)/(|x|+|y|) 存在」⇒
        「f(0,0) 可微」（f(0,0)=0 时）」，check 为「极限存在即 f=o(|x|+|y|)=o(ρ)」；
        (iii) D1 positive_instance_mapping（第 1133 行）「lim f/(|x|+|y|) 存在 ⇒ f=o(ρ) ⇒
        可微（该选项为真）」。
        三处都断言「极限存在（不要求为 0）⇒ f=o(|x|+|y|)」，这在数学上**不成立**。
        **独立反例（完整数学验证）**：取 f(x,y)=|x|+|y|。
        ① f 在 (0,0) 连续：|x|+|y|→0=f(0,0)；② lim f/(|x|+|y|) = lim 1 = 1，存在；
        ③ 但 f 在 (0,0) 不可微：∂f/∂x(0,0)=lim_{h→0}(|h|+0)/h 不存在
        （右极限 +1、左极限 −1，sympy 实测两侧极限 ±1）。故 guard 的前提「极限存在」满足、
        结论「可微」失败——**直接击穿该 sufficient guard 与 mechanism_note**。
        **2012-3 正确选项**：题面（本仓 `高数真题题面_2011-2016.md` §2012-3）确认
        (A)(B)(C)(D) 四个命题。正确答案是 **(B)**：lim f/(x²+y²) 存在（记 L）时，
        由 f 连续得 f(0,0)=0，f=L(x²+y²)+o(x²+y²)=o(ρ)，故可微（梯度为 0）；
        (A) 是经典陷阱（极限存在≠极限为 0），(C)(D) 反例取 f≡1（或非零常数）即可。
        独立 WebSearch 亦确认官方答案为 (B)。本族 D1 若被求解者使用，会把 2012-3
        引向错误选项 (A)；正确分支 (B)（「lim f/(x²+y²) 存在 ⇒ 可微」，f=o(ρ²)=o(ρ)）
        在本族 D1 中**完全缺失**。
        **严重性**：2012-3 在本族 scope 内（主考点「多元函数可微的充分必要条件」），
        differentiability 格仅 D1/D2 两个 action，2012-3 唯一落入 D1。guard 是
        schema 层面的可引用规则，不是无害的实例映射笔误——它会在判据题上给出错误结论，
        属 B4 类语义级错误之外的**数学级错误**，按 HANDOFF 的 B2 定义（明确反例直接击穿
        guard/mechanism）与 B1 定义（scope 内题目路由到错误分支、遗漏决定答案的合法分支）
        均为 direct blocker。
      recommended_change: >
        ① sufficient guard #4 改为「lim f/(x²+y²) 存在 ⇒ f(0,0) 可微」（(B) 的机制，
        充分条件，f=Lρ²+o(ρ²)=o(ρ)），并去掉 |x|+|y| 版本；
        ② D1 mechanism_note 改为「2012-3 真选项为 (B)：lim f/(x²+y²) 存在 ⇒ 可微；
        (A) 是陷阱：lim f/(|x|+|y|) 存在（≠0 亦可）不蕴含可微，反例 f=|x|+|y|」；
        ③ D1 positive_instance_mapping basis 改为「(B) 为真；其余选项用
        f=|x|+|y|（(A) 反例）与 f≡1（(C)(D) 反例）否定」；
        ④ 建议在 differentiability 格 focused_checks 补「(|x|+|y|)-阶极限 ≠ o(ρ)，
        (x²+y²)-阶极限 = o(ρ²)=o(ρ)」的对照（F14 路径思想同源）。

  non_blocking:
    - id: NB-1
      title: ODE 族 evidence 仍挂 SB-1 四题，count 34 与 SB-1 裁定 28 未同步（跨族残留）
      detail: >
        `分析/方法族-高数-微分方程.md` 的 evidence.positive_problem_ids 仍含
        2006-18/2014-17/2025-18/2026-18，count=34；HANDOFF SB-1 已裁定此四题归多元族、
        ODE 真实 scope 为 28。本族对这四题的认领正确、且对其中 ODE 求解子步骤以
        local_operation 承接（不跨族 action_ref，全文无第二个 action_ref），故不构成
        本族缺陷；但 ODE 侧的计数残留是 integrator 层面的待办，本族 §5 只上报了
        extrema 侧旧 evidence（2004-19/2015-17/2019-16/2024-18），未提及 ODE 侧。
      recommended_change: 提请 integrator 同步 ODE 族 count 34→28（SB-1）；本族 §5
        open_questions 可补一条 ODE 侧残留说明。
      priority: medium
    - id: NB-2
      title: IC2 的 followup 未显式把「求解所得 ODE」列为 local_operation 子步骤
      detail: >
        SB-1 四题（2006-18 II、2014-17、2025-18、2026-18）在链式求导后都要解一个
        常微分方程（可降阶 f″+f′/u=0 / 常系数非齐次 / 欧拉形）。本族 §5 第 6 条只写明
        「求极值判定段、后续曲面积分/线积分计算段均以 local_operation 承接」，未提
        ODE 求解段；IC2 的 followup 最后一步是「代入指定点求值，或按设问组合成
        ∂²z/∂x²+∂²z/∂y² 型线性式」，不含「解所得 ODE」。设计意图（全部跨族子步骤走
        local_operation，不跨族 action_ref）是明确且正确的，故不构成 B1；但建议显式化，
        与 series 族 C1 承接 ODE 同型地记一句。
      recommended_change: IC2 followup 增补「解所得 ODE（可降阶/常系数/欧拉形）以
        local_operation 承接，不跨族 action_ref」，或在 §5 第 6 条补「ODE 求解段」。
      priority: low
    - id: NB-3
      title: IC6 basis「x=1 交点处」表述不精确
      detail: >
        IC6 对 2021-2 的 basis 写「f(x+1,e^x) 与 f(x,x²) 各求导一次，x=1 交点处联立解
        f_u(1,1)、f_v(1,1)」。实测两条路径在 (u,v)=(1,1) 相交：路径1 在参数 x=0 处取到
        (1,1)（x+1=1、e^x=1），路径2 在参数 x=1 处取到 (1,1)。「x=1 交点处」对路径1
        不成立（x=1 处路径1 是 (2,e)）。机制与结论（df=dy，选项 (C)）经我独立复算正确，
        仅措辞不精确，不构成任何 blocker。
      recommended_change: 改为「两条路径在 (u,v)=(1,1) 相交（路径1 参数 x=0、路径2 参数 x=1），
        各求导一次联立解 f_u(1,1)、f_v(1,1)」。
      priority: low
    - id: NB-4
      title: lint DOCS 未含本文件（自动化覆盖缺口）
      detail: >
        `分析/tests/lint_method_families.py` 的 DOCS 只列 第一批/微分方程/级数 三文件，
        本族不在其中；基线「error 0 · warning 4」实际未覆盖本文件。我用注入脚本把
        本文件单独加入 DOCS 实测 **error 0 · warning 0**（R1/R2/C1/C2/T1/S1/S2/S3/E/D1/P
        全过）。建者 §4 已自述「本文件在 integrator 将其加入 DOCS 后须保持 error 0」，
        属已认知项；建议 integrator 把本文件并入 DOCS 使基线真正生效。
      recommended_change: integrator 将 方法族-高数-多元微分.md 加入 lint DOCS。
      priority: low

counter_witnesses:
  verified:
    - { witness: D1-guard#4, ref: "f=|x|+|y|：lim f/(|x|+|y|)=1 存在、f 连续、f(0,0)=0，但 ∂f/∂x(0,0)=lim|h|/h 不存在 ⇒ 不可微 ⇒ 击穿「lim f/(|x|+|y|) 存在 ⇒ 可微」", verification: verified }
    - { witness: F1, ref: "z=u+v, u=x, v=x²：真值 1+2x，漏 v 路径得 1，差 2x", verification: verified }
    - { witness: F2, ref: "z=uv, u=x, v=xy：真 ∂²z/∂x∂y=2x，漏 f_v·v_xy 项得 x，差 x", verification: verified }
    - { witness: F3, ref: "x²+y²+z²=1 于 (1/2,0,√3/2)：正确 −1/√3，写反 −√3", verification: verified }
    - { witness: F4, ref: "单位球面于 (1,0,0)：F_x=2≠0 ⇒ x 可解，F_z=0 ⇒ z 不可由 (x,y) 解出（z=±√(1−x²−y²) 双支）", verification: verified }
    - { witness: F5, ref: "同点 F_z=0 ⇒ −F_x/F_z=−2/0 无定义 becomes_inconclusive", verification: verified }
    - { witness: F6, ref: "∫₀^{xy} sin t dt：∂F/∂x=y·sin(xy)；(π/6,2) 处正确 √3 vs 漏因子 √3/2", verification: verified }
    - { witness: F7, ref: "f=xy/√(x²+y²)：f_x=f_y=0 但沿 y=x 余项/ρ=1/2 不趋于 0，不可微", verification: verified }
    - { witness: F8, ref: "f=|x|+|y|：连续但 ∂f/∂x 两侧极限 ±1 不存在，不可微", verification: verified }
    - { witness: F9, ref: "f=x 沿 (1,1)：正确 1/√2，未单位化 1=√2·(1/√2)", verification: verified }
    - { witness: F10, ref: "f=x+y：|∇f|=√2 是标量，梯度 (1,1) 是方向", verification: verified }
    - { witness: F11, ref: "z=x²+y² 于 (1,1,2)：正确法向量 (2,2,−1)，误取 (2,2,1) 得另一平面", verification: verified }
    - { witness: F12, ref: "λ 取 2 时代入旋度得 −4f≠0（正确 −2f−(−2f)=0）", verification: verified }
    - { witness: F13, ref: "对称情形 P=yf,Q=−xf 写反旋度巧合同为 0（文件已注明）；一般 P,Q 写反必变号", verification: verified }
    - { witness: F14, ref: "f=xy²/(x²+y⁴)：沿一切直线 y=kx 极限 0，沿抛物线 x=y² 极限 1/2", verification: verified }
    - { witness: F16, ref: "n=(1,0,−1)×(x,y,x)=(y,−2x,y)，|·|/ρ 沿 y=0 为 2、沿 x=0 为 √2 ⇒ 非 o(1)", verification: verified }
    - { witness: F17, ref: "f(u,v)=u²+v², u=x², v=y²：展开与链式 ∂²z/∂x∂y 均 0，一致（loses_advantage 而非 invalidates）", verification: verified }
    - { witness: HE1/HE2, ref: "f(tx,ty)=t^{-2}f(x,y) ⇒ x f_x+y f_y=−2f（用 f=(x²+y²)^{-1} 实测）；P=yf,Q=−xf 旋度 −2f−(x f_x+y f_y)=0，上半平面单连通格林公式得环量 0", verification: verified }
    - { witness: D2/2020-3, ref: "n·(x,y,f)=f_x x+f_y y−f=−o(ρ) ⇒ (A) 极限存在；叉积/α⊥n 点积一般 O(ρ)，(B)(C)(D) 假（用 f=x, α=(0,1,0) 实测 α·(x,y,f)=y，|y|/ρ 沿 y=0 为 0、沿 x=0 为 1）", verification: verified }
    - { witness: IC6/2021-2, ref: "路径1 于 x=0 求导 f_u+f_v=1；路径2 于 x=1 求导 f_u+2f_v=2 ⇒ f_v=1,f_u=0 ⇒ df=dy=(C)", verification: verified }
    - { witness: DG3/2019-16, ref: "∇z=(6a,8b)∥(−3,−4) 且 |∇z|=10 ⇒ λ=2 ⇒ a=b=−1", verification: verified }
  pending: []
  search_result: >
    F1–F17 之外的**击穿性反例未再找到**（search_result: not_found）。重点复核的反向构造：
    (i) D1 的「|x|+|y| 阶」已找到反例（上述 verified 第 1 条，即 blocker）；(ii) ST2 的
    「切平面与 xOy 面垂直 ⇔ 法向量 z 分量为 0」、DG1 的「单位化」、F14 的「直线一致不足
    证存在」等均无新增反例；(iii) LC1/LC2 的「无主考点真题」经 TSV 全量扫描确认属实
    （not_found 非「不存在」），合规。

guard_audit:
  necessary:
    - "链式法则必须覆盖 z→u,v→x,y 的所有路径" → necessary（F1 击穿漏路径）verified
    - "隐函数求偏导必须用 ∂z/∂x=−F_x/F_z" → necessary（F3 写反）verified
    - "隐函数存在定理须核验某偏导 ≠0 才断言可解" → necessary（F4）verified
    - "变限积分求偏导必须乘内层极限导数因子" → necessary（F6）verified
    - "方向导数的方向向量必须单位化" → necessary（F9）verified
    - "最大方向导数是标量 |∇f|，非梯度向量" → necessary（F10）verified
    - "可微判定必须核验余项为 o(ρ)，偏导存在与连续都不充分" → necessary（F7/F8）verified
    - "切平面法向量：显式 (−f_x,−f_y,1) / 隐式 ∇F，写法须与平面方程一致" → necessary（F11）verified
    - "欧拉恒等式 λ 必须与齐次指数一致" → necessary（F12）verified
    - "格林公式旋度项是 ∂Q/∂x − ∂P/∂y" → necessary（F13）verified
  sufficient:
    - "「f 可微」⇒「f 连续且偏导存在」" → sufficient（可微是更强条件；反向不成立）verified
    - "「偏导数连续」⇒「可微」" → sufficient（充分非必要，标注正确）verified
    - "「f(tx,ty)=t^λ f(x,y)（f 可微）」⇒「欧拉恒等式」" → sufficient（定理充分保证）verified
    - "「lim f/(|x|+|y|) 存在」⇒「可微」" → **sufficient 标注错误，实际为假**（B2，见 blocker；
      反例 f=|x|+|y|，极限存在但不 可微。正确充分条件是 (B) 的「lim f/(x²+y²) 存在」）refuted
    - "「F 在某点某偏导 ≠0」⇒「该变量可由其余变量解出」" → sufficient（隐函数存在定理）verified
  supporting_heuristic:
    - "复合求偏导先画复合关系树再沿路径写链式项" → supporting_heuristic（效率/防漏偏好）verified
    - "二阶复合先求一阶再嵌套，f 二阶连续时 f_uv=f_vu 合并" → supporting_heuristic（书写顺序偏好）verified
    - "隐函数求导优先公式法，直接法作等价备用" → supporting_heuristic（两种都合法）verified
    - "方向导数与梯度题先求梯度再处理方向/模" → supporting_heuristic（效率偏好）verified
    - "切平面题先判断显式/隐式再取法向量" → supporting_heuristic（识别偏好）verified
    - "可微判据题优先 o(ρ) 定义，常备反例 xy/√(x²+y²) 与 |x|+|y|" → supporting_heuristic（反例只能否定不能证成）verified
  summary: >
    21 条 guard 中 10 necessary + 5 sufficient + 6 supporting_heuristic。除 sufficient
    第 4 条（2012-3 (A)）被击穿外，其余 20 条标注与语义均正确。

lint_result:
  command: >
    (1) 基线：PYTHONUTF8=1 py 分析/tests/lint_method_families.py
    (2) 注入式单文件：py <$CLAUDE_JOB_DIR/tmp/lint_multivar.py>（把 DOCS 只指向本文件）
  error_count: 0（基线与单文件均）
  warning_count: 4（基线，全部在已冻结 extrema A2/A3/A5/A7 的 S3 typing 欠账）；本文件单跑 0
  warnings_detail: >
    calc.extrema.constraint-selection/A2, A3, A5, A7「followup 项未标 kind（S3）」——
    与 HANDOFF 记载的基线完全一致，且在本文件之外。
    本文件单跑通过 S1/S2/S3/T1/R1/R2/C1/C2/U1/D1/E/P 全部检查：
    R1（HE1→HE2 的 action_ref 指向真实 action）、R2（各 action 的 eligible_cells 与
    level_2_candidates 清单双向一致）均实测通过。
  note: 本文件不在 lint DOCS 里，见 NB-4。

status_recommendation: >
  **challenged**。理由：存在 1 个 B2 direct counter-witness（兼 B1 scope 内路由错误）
  ——D1 对 2012-3 的正确选项判定为 (A)，实际为 (B)；sufficient guard #4 的蕴含关系被
  f=|x|+|y| 直接击穿，且正确分支（(B) 的 o(ρ²)=o(ρ) 机制）在 D1 中缺失。按 HANDOFF，
  direct blocker 触发 unfreeze，status 应降为 challenged 并修复后方可恢复 candidate。
  **不升级**（author_upgrade_ceiling: candidate 保持不变；升级只能由 GPT 判定）。
  scope 40 题、F1–F17 数学、其余 20 条 guard、lint（error 0）与词汇纪律均通过，
  修复点集中在 differentiability 格的一处事实错误。

confidence_limits:
  - "题面库 source_status 为 ocr_uncertain（含 2024–2026 题面文件内嵌【答案/解析】段），
    我对实例映射的复核基于 OCR 转写文本；但 blocker 涉及的 2012-3 题面在
    高数真题题面_2011-2016.md 中完整清晰，且结论经独立数学推导 + WebSearch 官方答案双确认。"
  - "未读 solutions/（红线）；标准答案以纸质版为准。所有反例均为独立数学推导，未把建者
    报告当结论。"
  - "F6 的 2020-12（f=∫₀^{xy} e^{xt²}dt）sympy 直接积分给出带 Piecewise/erf 的怪异形式，
    属符号积分实现产物；我用标准 Leibniz 规则拆出边界项 y·e^{x³y²} + ∫₀^{xy} t²e^{xt²}dt
    验证，数学结论不受影响。"
  - "guard_audit 的「20/21 无标错」结论基于逐条语义与反例独立判定；sufficient #4 除外。"
```

---

# 修复复核（2026-08-28，只读，不改被审文件）

integrator 已按本报告 recommended_change 对被审文件应用修复（D1 mechanism_note / sufficient
guard #4 / positive_instance_mapping / 新增 F18 / 计数同步）。以下复核全部只读完成，未读
`solutions/`。结论：**confirmed_fixed**。

```yaml
fix_recheck:
  status: confirmed_fixed
  checked_at: 2026-08-28
  (a)_B2_eliminated: true
    detail: >
      sufficient guard #4 现为「「lim f(x,y)/(x²+y²) 存在」⇒「f(0,0) 可微」」（L557–561），
      是真命题、标注 sufficient 正确；check/explanation 描述 (B) 机制（f=Lρ²+o(ρ²)=o(ρ)，
      f_x=f_y=0），并显式注明 (A)「lim f/(|x|+|y|) 存在」不充分、反例 f=|x|+|y|（F18）。
      全文 grep「|x|+|y|」10 处，均以「陷阱/不充分/反例」框架表述，**无残留**旧假蕴含。
  (b)_B1_patched: true
    detail: >
      正确分支 (B) 已存在于 guard #4、D1 mechanism_note（L331）、positive_instance_mapping
      （L1151）三处；(A) 标注为陷阱并给反例；MD1 route 的 failure_boundary 已加 F18（L1116）。
      求解者沿 D1 走 2012-3 将指向正确选项 (B)。
  (c)_F18_math: true
    detail: >
      F18（L922–935）结构完整（boundary_id/changed_condition/effect: invalidates/explanation/
      witness/verification: verified/recovery）。sympy 独立复算：
      ① f=|x|+|y|：f(0,0)=0、连续、lim f/(|x|+|y|)=1 存在；
      ② ∂f/∂x(0,0)=lim|h|/h，右 +1 左 −1 ⇒ 不存在 ⇒ 不可微 ⇒ invalidates 成立；
      ③ 「|x|+|y|=Θ(ρ) 非 o(ρ)」成立（|x|+|y|/ρ ∈ [1,√2] 不趋于 0）；
      ④ 反证「L=0 时 (A) 亦足可微」并不推翻标注——文件措辞为「不保证」，反例 L=1 即证伪。
  (d)_new_issues: none
    checks:
      - "effect 分布 §5 item 6：18 条 = invalidates(15)+becomes_inconclusive(1)+changes_branch(1)+loses_advantage(1)。逐条比对 F1–F18 的 effect 字段：invalidates=F1,2,3,4,6,7,8,9,10,11,12,13,14,16,18（15）；becomes_inconclusive=F5（1）；changes_branch=F15（1）；loses_advantage=F17（1）。一致。"
      - "constructed_counterexamples（L1437）=[F1..F14,F16,F17,F18] 共 17 项；F15 为 proof 型（changes_branch），正确排除于 counterexample 清单。"
      - "differentiability 格 new_failure_boundaries=[F7,F8,F16,F18]（L1124），search_budget/existing_routes/completion_criteria 均同步（L1111–1124）。"
      - "无残留「17 条」计数；2012-3 全文 13 处提及（L174,331,334,560,929,933,970,1101,1112,1151,1461,1534）全部一致表述 (B) 为真、(A) 为陷阱。"
      - "(C)(D) 反例：建者改用 f=x（我原建议 f≡1）。两者均合法：f=x 可微，(C) lim x/(|x|+|y|) 沿 (x,0)/(0,y) 分别 1/−1/0 ⇒ 不存在；(D) lim x/(x²+y²) 沿 y=0 为 1/x→+∞ ⇒ 不存在。sympy 实测成立。"
      - "lint（注入式单文件，对修复后文件重跑）：PASS error 0 · warning 0；基线 3 文件不受本文件改动影响（error 0 · warning 4 冻结 extrema）。"
  status_recommendation_after_fix: >
    blocker 已确认消除 → 本族 status 恢复为 **candidate**（与文件 §4 自述一致；author_upgrade_ceiling
    仍为 candidate，不升级）。NB-1..NB-4 为非阻断项，可在 integrator 编排时顺手处理。
```
