---
doc_id: claude.independent_review.series.ee3605c
schema: CALC-METHOD-FAMILY-v1.3.1
reviewer: claude（independent_reviewer，非建者 claude-series）
written_at: 2026-08-28
audited_artifact: 分析/方法族-高数-级数.md
audited_version: 1.1.0
---

# 独立审查报告：calc.series.route-selection（v1.1.0）

本报告只记录意见，不修改任何被审对象。未读 `solutions/`，判断依据仅来自题面
（`分析/高数真题题面_*.md`、`papers/2024–2026` 题面文件、`分析/考点标注.tsv`）。

```yaml
task_id: batch2.series.independent_review_v1.1.0

artifact_identity:
  branch: worktree-batch2-integrator
  head: ee3605c                       # 我实际读取的 HEAD（git rev-parse --short，工作树干净）
  note: >
    被审文件 frontmatter 自注的基线是 d42ea02，而当前 worktree HEAD 为 ee3605c；
    这是「内容提交」与「分支 tip」的正常差别（HANDOFF 顶部有同一说明），不影响审查。
    lint 实测：python 分析/tests/lint_method_families.py → PASS：error 0 · warning 4，
    4 条 warning 全部在已冻结的 extrema（A2/A3/A5/A7 的 S3 欠账），与 artifact §4 自述一致。
    本族 S3 warning = 0，R1（action_ref 存在性）、R2（eligible_cells 双向一致）、
    C1/C2、T1、E（evidence 索引）、D1 均通过。

scope_checked:
  declared: 级数与反常积分的敛散性判别及解路线选择（2004–2026 数学一，扣 2022）
  claimed: 29 = 27（级数主考点）+ 2（2010-3、2016-1，HANDOFF 裁定 SB-4 判归本族）
  verified: 29
  method: 按 考点标注.tsv 逐行核对「主考点=考点列第一个」
  main_tag_breakdown:
    "幂级数的收敛半径与收敛域": [2005-16, 2008-11, 2010-18, 2011-2, 2012-17, 2015-3, 2020-4, 2021-18, 2026-2]
    "级数敛散性的判定与反例": [2006-9, 2009-4, 2019-3]
    "傅里叶级数的收敛定理": [2013-3, 2023-13, 2025-12]
    "函数展开成幂级数": [2006-17, 2019-11, 2024-3]
    "幂级数系数递推与微分方程": [2007-20, 2013-16, 2020-17]
    "绝对收敛与条件收敛": [2023-4, 2025-2]
    "正项级数敛散性的比较判别法": [2004-9]
    "傅里叶级数的奇偶延拓": [2008-19]
    "数项级数求和": [2018-3]
    "逐项积分求和函数": [2017-12]
    "反常积分的敛散性判别": [2010-3, 2016-1]     # SB-4 判归
  scope_verdict: >
    29 题全部命中且无越界认领；无漏认领。5 题次考点命中（2004-18、2009-16、2014-19、
    2016-19、2019-17）按 scope_boundary_rule 正确地不计入。2016-16（主考点
    「二阶常系数齐次线性微分方程」，次考点含「反常积分的敛散性判别」）正确地未认领。
    **SB-4 原文「这两题已计入上述 27」与事实不符——27 是排除 2010-3/2016-1 算出的，
    正确总数 29。** artifact 已在 frontmatter、§2.3、§5#1 如实上报并请求 integrator
    同步 batch2_plan 与 measured_by_main_tag 的 27→29，处理正确，不属本族缺陷。

findings:
  blockers: []        # B1–B4 四类 direct blocker 均未触发，理由见下各节

  non_blocking:
    - id: NB-1
      title: P0 的 followup 图漏列 P4/Q3/Q4 边，这些 route 只靠 minimal_probe 文本可达
      detail: >
        P0（「任何数项级数的第一步」，applys_when 如此声明）的 followup_actions 只有
        P1/P2/P3/Q1/Q2 五条 action_ref。P4（积分判别法，numeric_positive 格）、
        Q3（反例排除）、Q4（部分和直接分析，numeric_alternating_general 格）在各自的
        cell 清单里，但**没有任何 action_ref 指向它们**（全文 grep 证实）。它们的可达性
        完全依赖 minimal_probe 文本的显式分派（"能写成单调减连续函数在整点的值 → P4"、
        "命题真假 → Q3"、"可裂项或是已知级数的线性组合 → Q4"），以及 P0 的
        on_skip: return_to_parent_router 隐式回退。同样的模式存在于 D1→D4/D3
        （D1 的 local_operation 文本写「有零项转 D4 或 D3」但没有 action_ref 边）、
        N1→N2/N3、I1→I5。这不是漏 route（每个格的全部 action 都可由 minimal_probe 到达，
        2019-3、2006-9 等均有合法路径），因此**不构成 B1**；但 declared followup 图与
        minimal_probe 是两套口径，后经者按图索骥会误判 P4/Q3/Q4 不可达（vector 族的
        A2→A1p 不可达边正是同类、被当作 routing_defect 修掉的）。建议给 P0 增补
        P4/Q3/Q4 的 when 分支（并给 D1→D4/D3、N1→N2/N3、I1→I5 补边或注明
        「经 minimal_probe 分派」）。
    - id: NB-2
      title: 2025-12 的 W3 映射把周期写错（2l=4 应为 2l=2）
      detail: >
        fourier 格 W3 的 positive_instance_mapping 写：「−7/2 加周期 4 平移到 1/2
        （延拓后周期为 2l=4，不是 2）」。2025-12 题面 f 定义在 [0,1]（0≤x<1/2 与
        1/2≤x≤1 两段），正弦级数 Σbₙsin(nπx) ⇒ l=1 ⇒ 奇延拓后周期 2l=**2**（与同格式
        2013-3 的 W3 映射「周期 2」一致）。写 2l=4 等价于 l=2，数学错误。答案 S(−7/2)=1/8
        仍正确（−7/2+4 与 −7/2+2·2 都落到 1/2，4 是周期 2 的整数倍，纯属巧合不改变值），
        且 W2/W3 的 mechanism_note 与 fourier 格 focused_check 的 period_is_2l 都写的是
        正确规则「周期 2l」，故这是**实例映射的 basis 笔误**，不击穿任何 guard/mechanism，
        不构成 B2。但必须改正：把该行「2l=4，不是 2」改为「周期 2，−7/2+2·2=1/2」。
    - id: NB-3
      title: 三处陈旧计数（v1.0.0 残留）
      detail: >
        (a) route_scan_status_note 与 scan_basis 写「八格全部扫完（本族首建）」「八格各自
        先做结构穷举」——v1.1.0 已扩为九格（+improper_integral），应为「九格」；
        (b) §3 第 5 条写「15 条 failure_boundary 分别落在 invalidates(7)/
        becomes_inconclusive(5)/changes_branch(2)/loses_advantage(1)」——实际 17 条
        （invalidates 9 / becomes_inconclusive 5 / changes_branch 2 / loses_advantage 1），
        §4.1 已正确写 17，§3 为残留。均为文档级陈旧计数，不影响语义结论（§3 结论
        「四种 effect 未混写」本身仍成立）。
    - id: NB-4
      title: P1 的 applies_when「含对数因子的幂次修正」与其机制不匹配（级数侧无 I4 类比）
      detail: >
        P1 的机制是「定阶到 λ/n^p 与 Σ1/n^p 比较（λ∈(0,∞)）」。对 Σ1/(n·ln^q n)，
        无法写成 λ/n^p（对 p=1 极限为 0、p>1 为 ∞，均不在 (0,∞)），故 P1 的机制实际
        处理不了 q>1 的收敛情形（p=1 会误判发散）。级数侧的对数因子处理只由 P4
        （积分判别法）承载，没有反常积分侧 I4 那样的显式「对数比任何幂弱、只在临界 p
        起作用」route。P1 的 applies_when 却宣称覆盖「含对数因子的幂次修正」，属过度声称。
        2004–2026 无此类题为主解（P4 记 not_found），故不构成 B1。建议：或收窄 P1 的
        applies_when、把对数型通项显式交给 P4；或在 P1 下挂一个 I4 式的对数因子
        followup（级数侧：p 恰为 1 时 Σ1/(n ln^q n) 收敛 ⟺ q>1）。
    - id: NB-5
      title: I3 的「定阶到 A/x^p」不覆盖比任何幂更快衰减的情形（o(1/x^p)，如 e^{−x}）
      detail: >
        improper_integral 格的 route_universe 与 I3 都以「f~A/x^p，p>1 收敛」为表述；
        f=o(1/x^p)（e^{-x} 型，衰减快于任何幂）时极限比较的 λ 不在 (0,∞)，直接套 I3
        不给结论。正确结论（收敛）要靠「f≤g 且 ∫g 收敛」的直接比较，而该格把
        「比较判别法的非极限形式（直接放缩）」排除为 duplicate_mechanism。极限形式
        的推论 f/g→0 且 ∫g 收敛 ⇒ ∫f 收敛是同一比较族，故排除不算错，但 route_universe
        没有显式声明这一子情形。2004–2026 需要它的在 scope 题不存在（2016-16 的
        e^{−x}-类判敛散归属 ODE 族，不在本族 scope），不构成 B1。建议在 route_universe
        或 I3 的 mechanism_note 补一句「比任何幂更快衰减 ⇒ 收敛（直接比较到某 x^{−p}, p>1）」。
    - id: NB-6
      title: 2016-16 未列入 exclusions 枚举
      detail: >
        frontmatter exclusions 枚举的 5 题（2004-18/2009-16/2014-19/2016-19/2019-17）
        全是「极限/中值/定积分应用」主考点+级数次考点；2016-16 是「ODE 主考点+反常积分
        敛散性判别次考点」，按 scope_boundary_rule 正确地不属本族，但 exclusions 未枚举它
        （反常积分敛散性判别自 v1.1.0 起是本族关键词，漏列会造成边界不清）。建议在
        exclusions 补上 2016-16（主考点二阶常系数齐次线性微分方程，归 ODE 族）。
    - id: NB-7
      title: 跨族重叠的 ODE 侧残留
      detail: >
        ODE 族（方法族-高数-微分方程.md）evidence.count=34 含 2007-20/2013-16/2020-17
        三题，但其 scope_note 明写「主路由归级数族、不整体纳入 scope」，且其 open_items
        有「级数-ODE 边界待级数族确认」。本族已确认接收这三题（§0.2、C1/C2/C3），故
        ODE 侧的该项 open_item 可以关闭；但 ODE 的 scope_problems 数字（34 vs 规则口径 28）
        是 integrator 层面的待办，不是本族缺陷。本族对三题的认领正确，无越界。

  candidate_routes:
    - "P4（积分判别法）、X4（直接法展开）、X3（先展开导数）、N1（造辅助幂级数）、I5（反常积分的绝对收敛）：
       2004–2026 无主解实例（historical_instance: not_found），按 route scan 口径
       「未出现≠排除」正确保留，予以确认。"
    - "级数侧的对数因子 route（NB-4 建议）：Σ1/(n ln^q n) 收敛 ⟺ q>1，可作为 P1 的
       子 followup 或并入 P4 的机制说明——结构性合法、大纲内，但与 P4 机制重叠，
       属可选优化而非缺失。"
    - "反常积分的 换元映射（x=1/t 把无穷端变瑕点）：数学上合法，但被 I2/I3 直接覆盖且更繁，
       不单设 action 合理（duplicate/dominated 家族）。"

  rejected_routes:
    - { route: 把 I2 与 I3 合并为一个「带参数的定阶」action, reason: dominated_not_excluded / schema, note: "两类奇点的 p 判据方向相反（瑕点 p<1、无穷端 p>1）。合并后 F16（方向记反）在 schema 上无唯一挂载点；拆分是正确设计（§3.8 论证成立）——不是「更细」，而是方向相反的两个机制，必须保留" }
    - { route: 把 I4 合并进 I2/I3 的 local_operation, reason: duplicate_mechanism, note: "I4 由 I2 与 I3 共同引用，且 2010-3 的 x→1⁻ 端是纯对数型（无幂成分），I2 的「定阶到 A/|x−c|^p」在该端无法执行、必须由 I4 单独给结论；作为 action 保留可避免双份复制。合并可行但更差，不推荐" }
    - { route: I5 作为 Q2 的 duplicate 删除, reason: invalid, note: "载体不同（∫ vs Σ），第一级判定工具不同（I2/I3 vs P1–P4）；I5 的「∫|f| 发散不给结论」语义正确（条件收敛在反常积分上真实存在，如 ∫₁^∞ sin x/x）。非 duplicate_mechanism，保留" }
    - { route: 狄利克雷/阿贝尔型振荡积分判据, reason: out_of_scope, note: 超数学一大纲；含参振荡积分的条件收敛判据不考（本族只走 I5 的绝对收敛通道） }
    - { route: 反常积分的计算/求值, reason: out_of_scope, note: 属一元积分模块，本族只判敛散 }
    - { route: 柯西主值, reason: out_of_scope, note: 超大纲；「收敛」一律指通常意义下各段独立收敛 }
    - { route: 帕塞瓦尔等式求数项级数和, reason: out_of_scope, note: 超数学一大纲；数项求和反解只走 W5 }
    - { route: 拉阿贝/库默尔/高斯判别法, reason: out_of_scope, note: ρ=1 的细化判据超大纲（P2/P3 的 ρ=1 由 P1 承接） }

counter_witnesses:
  verified:
    - { witness: F1, ref: "Σxⁿ/n 与 Σxⁿ/n² 在 x=1 处比值判别法均给 ρ=1，但一散一敛 ⇒ 端点沿用求 R 判别法 becomes_inconclusive", verification: verified }
    - { witness: F2, ref: "Σxⁿ、Σxⁿ/n、Σxⁿ/n² 的 R 均=1，收敛域分别为 (−1,1)、[−1,1)、[−1,1] ⇒ 跳过端点判定 invalidates", verification: verified }
    - { witness: F3, ref: "Σx^{2n} 按 c_k 写，相邻比值 0/0 无定义 ⇒ 直接套比值公式 becomes_inconclusive；D4/D3 都给出 R=1", verification: verified }
    - { witness: F4, ref: "aₙ=(−1)ⁿ/√n+1/n，bₙ=(−1)ⁿ/√n，aₙ/bₙ→1 但 Σaₙ 发散、Σbₙ 收敛 ⇒ 非正项用比较判别法 invalidates", verification: verified }
    - { witness: F5, ref: "aₙ=1/√n+(−1)ⁿ/n（不单调，Σ(−1)ⁿaₙ 发散）与 aₙ=(2+(−1)ⁿ)/n²（不单调，绝对收敛）⇒ 只验趋零 becomes_inconclusive", verification: verified }
    - { witness: F6, ref: "aₙ=(−1)ⁿ/n 与 aₙ=1/n 的第一级 Σ|aₙ| 均发散，但前者条件收敛、后者发散 ⇒ 两级判定不可省", verification: verified }
    - { witness: F7, ref: "绝对→条件 changes_branch：重排定理（黎曼）、Σ|aₙ| 通道、乘有界数列三条在条件收敛时全部失效", verification: verified }
    - { witness: F8, ref: "f 在每个整数处放高 1 宽 4^{−n} 的三角尖峰：∫f=1/6 收敛而 Σf(n)=Σ1 发散 ⇒ 去单调性 invalidates", verification: verified }
    - { witness: F9, ref: "Σxⁿ/n² → 求导 → Σxⁿ⁻¹/n → 再求导，R 恒 1 而收敛域 [−1,1]→[−1,1)→(−1,1) ⇒ 沿用原收敛域 invalidates", verification: verified }
    - { witness: F10, ref: "Σxⁿ/n 先积分得 Σx^{n+1}/(n(n+1)) 更复杂 ⇒ 方向选反 loses_advantage（仍合法，不排除）", verification: verified }
    - { witness: F11, ref: "f(x)=x 于 (−π,π) 周期延拓，x=π 处级数和=0 而 f(π)=π ⇒ 间断点取 f(x₀) invalidates", verification: verified }
    - { witness: F12, ref: "f≡1 于 [0,π]：偶延拓余弦级数在 x=0 给 1，奇延拓正弦级数给 0 ⇒ 延拓方向错 invalidates", verification: verified }
    - { witness: F13, ref: "(n+1)a_{n+1}=(n+1/2)aₙ（a₁=1）漏首项得齐次 (1−x)S′=S/2 ⇒ S≡0 与 a₁=1 矛盾；正确方程 (1−x)S′−S/2=1 ⇒ S=2/√(1−x)−2", verification: verified }
    - { witness: F14, ref: "S(x)=Σxⁿ/n² 在 x=1 收敛端点，逐项求导定理不覆盖 x=1、S′(x)→+∞ 读不出值；G4 由连续性 S(1)=π²/6", verification: verified }
    - { witness: F15, ref: "判敛散（比值/根值/积分/绝对判定）产生二值结论、结构上不产生和的值；求和需闭式表示 ⇒ 设问变化 changes_branch", verification: verified }
    - { witness: F16, ref: "p=1/2：∫₀¹x^{−1/2}=2 收敛、∫₁^∞x^{−1/2}=∞ 发散；p=2 恰好相反 ⇒ 方向记反 invalidates", verification: verified }
    - { witness: F17, ref: "∫₀^∞x^{−1/2}dx 只判 x→0（p<1 收敛）漏掉 ∞ 端（p≤1 发散），实际发散；∫₀^∞x^{−1/2}e^{−x}dx 两端均收敛才整体收敛", verification: verified }
  pending: []
  search_result: >
    对全部 25 条 guard 逐一独立反例搜索：**未找到 F1–F17 之外的击穿性反例**。
    特别核对的反方向构造：(i) 绝对收敛⇒收敛的逆否「Σaₙ 收敛不蕴含 Σ|aₙ| 收敛」
    （条件收敛即反例，已由 Q2/F6 覆盖）；(ii) 内闭一致收敛⇒逐项操作的逆否（不满足
    内闭一致收敛时逐项积分仍可能合法——即「充分非必要」，已由 guard 的 sufficient 标注
    正确表达，无需反例）；(iii) 收敛域端点判定的 R=∞/R=0 退化（D2 mechanism_note
    已单独说明「R=∞ 无端点、R=0 退化单点」，guard 未为其开例外，属非阻断表述瑕疵）。
    对每条 guard 的结果见 guard_audit。

guard_audit:
  # 逐 guard 标 necessary | sufficient | supporting_heuristic，并附定性与反例结果。
  # 全部 25 条中 13 条 necessary、5 条 sufficient、7 条 supporting_heuristic，均与
  # 我的独立判定一致，无标错。
  necessary:
    - "比较判别法（含极限形式）要求两个级数都是正项"  → necessary（F4 击穿非正项使用）verified
    - "莱布尼茨要求 |aₙ| 单调减 且 →0，两条缺一不可" → necessary（F5）verified
    - "绝对/条件必须做两次判定（Σ|aₙ|、Σaₙ 各一次）" → necessary（F6）verified
    - "收敛域=收敛区间+两端点各自单独判定（独立步骤）" → necessary（F2；R=∞/R=0 退化在 D2 mechanism_note 已处理）verified
    - "端点敛散性不得沿用求 R 的比值/根值判别法" → necessary（F1：端点必给 ρ=1）verified
    - "积分判别法要求 f 非负、连续、单调减且 aₙ=f(n)" → necessary（F8 尖峰构造）verified
    - "傅里叶级数在间断点收敛到左右极限平均，非 f(x₀)" → necessary（F11）verified
    - "延拓方式由所求级数类型决定（正弦=奇、余弦=偶）" → necessary（F12）verified
    - "系数递推翻译成方程时求和指标必须对齐" → necessary（F13 漏首项→恒零错误解）verified
    - "逐项求导/积分结论只在收敛区间内部成立；端点另判" → necessary（F9/F14）verified
    - "反常积分 p 判据方向相反（瑕点 p<1、无穷端 p>1）" → necessary（F16）verified
    - "反常积分多奇点必须拆段、每段各判一次" → necessary（F17）verified
    - "缺项幂级数不得直接套 lim|aₙ₊₁/aₙ|" → necessary（F3：比值 0/0 无定义）verified
  sufficient:
    - "内闭一致收敛 ⇒ 可逐项求导/积分且 R 不变" → sufficient（定理充分条件；不满足≠非法，标注正确）verified
    - "Σ|aₙ| 收敛 ⇒ Σaₙ 收敛" → sufficient（反向为条件收敛反例，正确标注）verified
    - "通项不趋零 ⇒ 级数发散" → sufficient（必要条件的逆否，作发散充分判据）verified
    - "比值/根值 ρ<1 ⇒ 收敛、ρ>1 ⇒ 发散" → sufficient（ρ=1 是失效点非「不收敛」，正确标注）verified
    - "端点在收敛域内 ⇒ 端点处和可由单侧极限得到（和函数连续）" → sufficient（端点发散时不适用，正确）verified
  supporting_heuristic:
    - "正项级数先定阶到 1/n^p 再选判别法" → supporting_heuristic（效率偏好；选「不合适」不产生错误结论）verified
    - "求和函数 n 在分母先求导、n 在分子先积分" → supporting_heuristic（F10：选反是 loses_advantage 非 invalidates）verified
    - "求傅里叶点值先不算系数" → supporting_heuristic（W4 也能给答案，只是做成了大题）verified
    - "展开优先间接法 X1–X3，X4 兜底" → supporting_heuristic（X4 合法但需验余项）verified
    - "敛散命题真假优先反例排除" → supporting_heuristic（只单向有效：未找到反例只能记 not_found）verified
    - "反常积分先定阶到 A/x^p，对数因子暂置一旁" → supporting_heuristic（只在临界 p 回头处理，I4）verified
    - "系数含 (−1)ⁿ/奇偶分支优先上极限 D3" → supporting_heuristic（识别偏好）verified

source_evidence:
  - 分析/METHOD_FAMILY_HANDOFF.md（SB-1..SB-4、scope_boundary_rule、direct_blocker 定义、cell scan 协议）
  - CLAUDE.md（仓库根；solutions/ 红线，未违反）
  - 分析/方法族-高数-级数.md（全文 2232 行，被审对象）
  - 分析/考点标注.tsv（逐行核对主考点，sha256 前缀与 frontmatter 一致）
  - 分析/高数真题题面_2004-2010.md / _2011-2016.md / _2017-2020.md / _2021-2023.md（抽查 2010-3、2016-1、2019-3、2019-11、2020-4、2020-17、2013-3、2013-16、2008-11、2008-19、2010-18、2018-3、2006-9、2023-4、2021-18、2005-16、2017-12、2023-13 等题面）
  - papers/2024考研数学一真题+答案.md（2024-3）、papers/2025年数学一真题.md（2025-2、2025-12）、papers/2026年考研数学一真题.md（2026-2）
  - 分析/tests/lint_method_families.py（运行结果 error 0 · warning 4）
  - 分析/方法族-高数-微分方程.md（仅核对 2007-20/2013-16/2020-17 的跨族交接与 exclusions）
  - 分析/考纲.md（§3 一元函数积分学·反常积分；§7 无穷级数·绝对/条件收敛）

recommended_changes:
  # 以下均为 non_blocking 建议，交由 integrator / 建者决定是否落地。
  - { id: NB-1, change: "给 P0 的 followup 增补 P4/Q3/Q4 的 when 分支（或明示这些 route 经 minimal_probe 分派）；同类补 D1→D4/D3、N1→N2/N3、I1→I5 的边或注释", priority: medium }
  - { id: NB-2, change: "fourier 格 W3 的 2025-12 映射 basis 改为「周期 2（l=1，2l=2），−7/2+2·2=1/2」", priority: high }
  - { id: NB-3, change: "把「八格」两处改「九格」；§3 第 5 条计数改 17（invalidates 9）", priority: low }
  - { id: NB-4, change: "收窄 P1 的 applies_when（对数型通项显式交给 P4）或为 P1 增加级数侧对数因子 followup（Σ1/(n ln^q n) 收敛 ⟺ q>1）", priority: low }
  - { id: NB-5, change: "improper_integral 格 route_universe / I3 mechanism_note 补「比任何幂更快衰减（o(1/x^p)，如 e^{−x}）⇒ 收敛」一句", priority: low }
  - { id: NB-6, change: "frontmatter exclusions 补 2016-16（主考点二阶常系数齐次线性微分方程，归 ODE 族）", priority: low }
  - { id: NB-7, change: "ODF 侧的 2007-20/2013-16/2020-17 双计属 integrator 待办；本族无需改动，仅提请 integrator 关闭 ODE 的「待级数族确认」open_item", priority: info }

status_recommendation: >
  candidate（**不变**，未升级、未降级）。无 B1–B4 direct blocker；跨文件状态
  （frontmatter status_summary / freeze_status / evidence 索引 / lint）自洽；
  improper_integral 格（v1.1.0 新增）数学正确、粒度论证成立；scope 29 题核实无误。
  按 author_upgrade_ceiling: candidate，任何升级只能由 GPT 判定；本报告不给升级。

confidence_limits:
  - "题面库 source_status 为 ocr_uncertain（含 2024–2026 题面文件内嵌【答案/解析】段），
    我对 positive_instance_mapping 的复核基于 OCR 转写文本，正确性上界受 OCR 误差限制。
    抽查的 17 道题面上全部数学断言通过独立验证。"
  - "未读 solutions/（红线）；标准答案以纸质版为准。所有 failure_boundary 与 guard 反例
    均为我独立的数学推导，与 artifact 构造一致。"
  - "多元微分族文件未全文读取；「重叠 0 题」仅按 TSV 主考点唯一性结构性确认，未做题面级比对。"
  - "guard_audit 的「无标错」结论基于我对 25 条 guard 的语义与反例独立判定；R=∞/R=0
    退化未在 guard 中开例外，记为非阻断表述瑕疵（NB-3 之外的另一小项，归并记录）。"
```
