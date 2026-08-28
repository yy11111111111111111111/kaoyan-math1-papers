# Codex 独立审查报告 · calc.ode.route-selection

> 报告文件名沿用派工时给的 `240c1dc`。**我实读的 head 是 `0e8fba8`**；
> 被审文件 `分析/方法族-高数-微分方程.md` 与 `分析/tests/lint_method_families.py`
> 在 `240c1dc → 0e8fba8` 之间**逐字节未变**（`git diff` 为空），
> 中间三个 commit 只动 HANDOFF / 看板 / AGENT_COLLAB_PROMPT。
> 因此本报告的结论对两个 head 同时成立。

```yaml
task_id: batch2.ode.independent_audit
role: independent_reviewer

commands_executed:            # ops/commands，按 id 去重
  - CMD-0001   # 分支名以实际为准，与看板预写不同不算 inconsistency
  - CMD-0002   # 派工权威源 = HANDOFF.batch2_plan + scope_boundary_rule；§10 不再内联派工
  - CMD-0003   # batch1 closed ≠ 三族全冻结；vector 是 active。三族均不动
  - CMD-0004   # interrupt = 门铃；拉取时机增为五个
  - CMD-0005   # 额度 allowed_warning：优先交付而非打磨；已照办（见下 delivery_posture）
  - CMD-2001   # F1–F5 / 2004-4 / 2006-18 / lint 改动已由 integrator 核过，不重复
  - CMD-2002   # 重点判「缺项优先于线性」的排序是否会误路由
  - CMD-2003   # 我的 3 处 mismatch 与已知三处的比对；先 pull 主分支再定稿
  - CMD-2004   # 定稿前区分「被审对象的问题」与「协作文档的问题」
command_channel_conflicts: none
  # 八条命令全部是 clarification / priority_change，无一条要求升级 status、
  # 推 claude/* 分支或改冻结 family。与 CLAUDE.md 无冲突。

delivery_posture:                # 依 CMD-0005
  已做: 六格独立重扫 · F6–F10 逐条复推 · 15 条 guard 定性 · 34 题双向核对 · lint 复跑
  未做: 第二轮重扫 · 额外数值验证 · 措辞打磨（一律按 backlog 记录，不再迭代）
  已在 11 项 completion_criteria 判定上给出结论后即定稿，未为 backlog 项多跑一轮。

# ── 依 CMD-2003：我上报的 3 处 mismatch 与「已知三处」的比对 ──
mismatch_reconciliation:
  已知三处_是否命中:
    "①  §10 内联过时派工（scope 40）": 未写进 findings
      # 我读的是 3981c9f 的 §10，确实仍有该残留；但它与 ODE 族的审查无关，
      # 我从一开始就未把它当 finding。eef6d69 已修复，此处仅作确认。
    "②  §10「三族全部冻结」": 未写进 findings
      # 同上，未曾据此推断任何结论；vector 是 active 已由 CMD-0003 确认。
    "③  分支名/head 与预写不同": 未写进 findings
      # 我上报的第 1 处（head 240c1dc vs 实际 tip）属此类，按 CMD-0001 不算
      # inconsistency。已改为在报告抬头如实标注实读 head，不计入 findings。
  我的另外两处_是新发现:
    - id: MM-A
      kind: 协作文档问题（非被审对象）
      text: >
        看板第 43 行写「多元微分，38 题」，HANDOFF.batch2_plan 写
        `scope_problems: 39`（= 多元关键词命中 48 − 归 extrema 的 9）。
        在 0e8fba8 上仍并存。按 CMD-0002，派工权威源是 batch2_plan，故应为 39；
        我不自行对齐，请 integrator 裁一次。
      blocks: 任务 B 的 scope 数
    - id: MM-B
      kind: 被审对象 × 协作文档的交叉问题
      text: >
        ODE 族 evidence 计 34 题，与 3981c9f 新立的 scope_boundary_rule
        （按主考点归属）实测的 24 题不相容。详见 §source_evidence.scope_audit。
      blocks: 任务 B 能认领哪些题（四题主考点为多元复合函数的二阶偏导数）

# ── 依 CMD-2004：两类内容的分界 ──
findings_scope_separation:
  被审对象自身的问题:            # 只有这些参与 status_recommendation
    blockers:    [BL-1, BL-2, BL-3, BL-4]
    non_blocking: [NB-1, NB-2, NB-3, NB-4, NB-5, NB-6, NB-7, NB-8, NB-9, NB-11, NB-12]
    note: >
      四条 blocker 全部是 ODE 族文件内部的数学 / 路由 / witness 问题，
      与协作文档无关。status_recommendation 只由这四条驱动。
  协作文档的问题:                # **不参与** status_recommendation
    items: [MM-A, MM-B, NB-10]
    note: >
      MM-A 是看板与 HANDOFF 的数字不一致；MM-B 是新规则对旧文件的追认欠账
      （规则立于 3981c9f，文件建于 2578d44，非 DeepSeek 之过）；
      NB-10 是 frontmatter 的陈旧派工字段。三者均记 backlog，
      **均未计入 blocker，也未影响 status_recommendation**。

artifact_identity:
  branch: codex/audit-ode-240c1dc
  head: 0e8fba8                      # 实读；被审文件与 240c1dc 完全一致
  audited_file: 分析/方法族-高数-微分方程.md
  audited_version: 1.0.0
  family_id: calc.ode.route-selection
  author: DeepSeek
  prior_independent_review: none

scope_checked:
  covered:
    - F6–F10 五条 failure boundary 的数学正确性（含 witness 是否名副其实）
    - 全部 15 条 guard 的 necessary / sufficient / supporting_heuristic 定性
      （任务书写「12 条」，实测 15 条：necessary 9 · sufficient 2 · supporting_heuristic 4）
    - 六个 cell 的 route universe 独立重扫与差集
    - 逆向 route（A6 / B7 / B8）的 produces 与 terminal_when 表达力
    - 一级 router「缺项信号先于线性」的排序是否造成误路由（CMD-2002 指定重点）
    - 34 题 scope 划定（与 考点标注.tsv + 高数真题题面_*.md 逐题比对）
    - frontmatter / provenance / 跨文件状态一致性
    - lint 独立复跑
  excluded_per_CMD-2001:
    - F1–F5 的数学推导（integrator 已手算复核）
    - 2004-4、2006-18 的真题引用（integrator 已逐字核对）
    - lint 的多文件改动（integrator 已确认只做泛化）
  verification_tooling: sympy 符号验证（F6 反例、G11 反例）；lint 复跑 error 0 · warning 4，与基线一致
```

---

## findings

```yaml
findings:
  blockers:

    - id: BL-1
      class: B1                      # scope 内具体题目导致漏解 / 遗漏决定答案的合法分支
      severity: highest
      title: 一级 router 的「缺项优先」把全部自治方程送进 second_order_reducible，B1/B2/B3 在该格不可达
      where:
        - level_1_router.rule
        - selection_rule.minimal_probe.action（第 2 行）
        - level_2_candidates.second_order_reducible.actions（只有 [B4, B5]）
      current_text: >
        「二阶分支先查『缺项信号』（不含 y 或缺 x）再查线性 …… 若缺项，
        直接落 second_order_reducible。否则按 线性 × 系数 × 齐次性 落格」
      mathematical_construction: |
        「缺 x」的标准含义是**方程中不显含自变量 x**（自治方程），
        即可写成 y″ = f(y, y′)。

        任何**二阶常系数齐次**方程 y″ + py′ + qy = 0，都可以写成
            y″ = −p·y′ − q·y = f(y, y′)，
        右端不含 x。**所以每一个常系数齐次方程都是「缺 x」方程。**

        按 level_1_router 的现行规则，它们全部在一级就被「直接落
        second_order_reducible」。该格 actions 只有 [B4, B5]，
        **B1（特征方程）在该格不可达**——而 B1 正是这些题唯一给得出答案的 action。

        scope 内被误路由的具体题目（题面逐字取自 分析/高数真题题面_*.md）：

          · 2017-10  y″ + 2y′ + 3y = 0，求通解
                     → 缺 x → reducible 格 → 只有 B4/B5 → 无法给出
                       e^{−x}(C₁cos√2x + C₂sin√2x)
          · 2016-16  y″ + 2y′ + ky = 0 (0<k<1)，证 ∫₀^{+∞}y dx 收敛
                     → 收敛性由**特征根实部**判定，只有 B1 的 terminal 分支能给
          · 2020-11  f″ + af′ + f = 0 (a>0)，求 ∫₀^{+∞}f dx
                     → 同上
          · 2023-2   y″ + ay′ + by = 0 解在 (−∞,+∞) 有界 → a=0, b>0
                     → 答案完全由特征根位置决定，reducible 格给不出
          · 2008-3   三阶常系数齐次逆向（y = C₁e^x+C₂cos2x+C₃sin2x）
                     → 同样不含 x → 缺 x → reducible 格，B7 也不在该格

        **同一缺陷的第二个面（缺 y 侧）**：
          · 2006-18  f″ + f′/u = 0        —— 缺 f，同时是欧拉形 u²f″+uf′=0
          · 2025-18  u²f″ + uf′ = 1       —— 缺 f，同时是欧拉形
          · 2026-18  u f″ + f′ = 1        —— 缺 f，同时是欧拉形
          三题都被「直接落 reducible」，**B3（欧拉）在该格不可达**。
          而本文件自己的 positive_instance_mapping 把 2025-18 同时映到
          B3（second_order_linear_variable 格）与 B4——**router 与
          instance mapping 直接互相矛盾**。

        注：2006-18 走可降阶确实成立（CMD-2002 已确认），本条**不否认**这一点。
        本条否认的是「若缺项，**直接**落 reducible」这个**排他性**跳转：
        它把一个正确的观察（可降阶不要求非线性）写成了一条会切断其它
        合法 action 的硬路由。
      internal_contradiction: |
        文件内部对这条排序的定性自相矛盾：
          · selection_rule.guards 第 12 条把它标为 supporting_heuristic，
            explanation 明写「效率偏好 + 路由正确性偏好 …… **不是合法性条件**」；
          · 但 level_1_router.rule 与 minimal_probe 把它写成**强制且排他**的跳转
            （「直接落」），效果上就是合法性条件。
        F9 更把这层排他性追认为设计意图：「这正是 B4/B5 的 eligible_cells
        只含 reducible 格、常系数格以 B1/B2 为主的理由」——
        即用**效率理由**去限定 eligible_cells。两条规则合起来的净效果是：
        缺项常系数方程既进不了常系数格（被 router 拦下），
        B4/B5 也进不了常系数格（被 eligible_cells 拦下），
        中间那条「B1 更省」的话没有任何机制承载。
      why_not_backlog: >
        不是 preference_rule 粒度问题。按现行 router 逐字执行，
        2017-10 / 2016-16 / 2020-11 / 2023-2 / 2008-3 这五道 scope 内真题
        拿不到能给出答案的 action，命中 B1 定义「遗漏一个决定答案的合法候选分支」。
      recommended_patch: |
        两处任选其一，推荐 (a)：

        (a) 把「缺项」从**排他跳转**改成**并行候选**（改 level_1_router.rule）：
            缺项信号命中时，second_order_reducible 的 B4/B5 进入候选集，
            **同时仍按 线性 × 系数 × 齐次性 落格**，两组候选并存，
            由 preference_rule 排序（常系数 → B1/B2 优先；欧拉形 → B3 优先；
            变系数且非欧拉形而缺项 → B4/B5 优先，2006-18 即此类）。
            这样 2006-18 仍然走 B4（变系数非欧拉…注：2006-18 本身是欧拉形，
            B3 亦合法，两条并存正是应有结果），2017-10 仍然走 B1。

        (b) 收紧「缺 x」的判据，明写「缺 x 指**非常系数**方程中不显含 x」。
            但这会把 2006-18 之外的自治非线性方程判据搞脏，且需要另设例外，
            不如 (a) 干净。

        无论采哪条，都应把 B4/B5 的 eligible_cells 扩到常系数两格
        （F9 已论证它们在那里**合法**，只是 dominated_not_excluded），
        并把 F9 里「这正是 …… eligible_cells 只含 reducible 格 …… 的理由」
        一句删掉——那句用效率理由限定了合法性。

    - id: BL-2
      class: B1                      # 兼有 B4 的 mandatory continuation 可悬空
      severity: high
      title: 逆向 route（A6 / B7 / B8）没有回到正向求解的 action_ref，terminal_when 在答案之前就终止
      where:
        - candidate_actions.A6.followup_actions / terminal_when
        - candidate_actions.B7.followup_actions / terminal_when
        - candidate_actions.B8.followup_actions / terminal_when
        - §3 「B3 可表达性核查」第 3 条
      current_text: >
        B7: followup_actions.mode: sequence，actions 只有一条
            local_operation「把反推出的方程/参数代回全部已知解逐一验证」；
            terminal_when: [方程、参数或通解已确定且与题面给出的全部结构一致]。
            A6 / B8 同构。
      mathematical_construction: |
        **2009-10（填空，题面逐字）**：
          「若二阶常系数线性齐次微分方程 y″+ay′+by=0 的通解为 y=(C₁+C₂x)e^x，
            则非齐次方程 y″+ay′+by=x 满足 y(0)=2, y′(0)=0 的解为 y = ____」

          第一层（逆向，B7 子路线①）：(C₁+C₂x)e^x ⇒ r=1 为二重根
                                  ⇒ r²+ar+b=(r−1)² ⇒ a=−2, b=1。
          第二层（正向，B2）：解 y″−2y′+y=x。设 y*=Ax+B ⇒
                            y*″−2y*′+y* = −2A + Ax + B = x ⇒ A=1, B=2 ⇒ y*=x+2。
                            通解 y=(C₁+C₂x)e^x + x + 2。
                            y(0)=2 ⇒ C₁+2=2 ⇒ C₁=0；
                            y′=(C₂+C₂x)e^x+1，y′(0)=C₂+1=0 ⇒ C₂=−1。
                            **答案 y = −x e^x + x + 2。**

          B7 的 terminal_when 在「a=−2, b=1 已确定且与已知结构一致」处即可终止，
          而**该题的答案不是 a、b**。B7 的 followup 里没有任何
          `action_ref: B2`，第二层无法从 B7 走到。

        **2012-9（填空，题面逐字）**：
          「若函数 f(x) 满足方程 f″+f′−2f=0 及 f″+f=2e^x，则 f(x)=____」

          本文件把它归入 B7 子路线④「联立两个方程解未知函数」。实际机制是：
            两式相减：(f″+f′−2f) − (f″+f) = f′ − 3f = −2e^x，
          得到的是一个**一阶线性方程**，须走 A2：
            f = e^{3x}(∫ −2e^x·e^{−3x}dx + C) = e^{3x}(e^{−2x} + C) = e^x + Ce^{3x}。
          再用第一式约束（f 必属 {C₁e^x + C₂e^{−2x}}）⇒ C=0 ⇒ **f(x)=e^x**。
          验证：f″+f′−2f = 1+1−2 = 0 ✓；f″+f = 2e^x ✓。

          B7 的 followup 同样没有 `action_ref: A2`，这条真实 route 走不通。

        **A6 侧**：applies_when 写「问的是方程/参数/**另一解表达式**」，
          但 produces: result_object、followup 只有代回验证。
          若设问是「另一解」，反推出 p、q 之后仍须解一次 ODE（A1 或 A2），
          A6 没有到 A1/A2 的 action_ref，同样悬空。
          （2016-3 问的是 q(x)，恰好落在 terminal 之内，所以现有真题没暴露它。）
      not_B3: >
        **这不是 schema 表达力不足。**同一 schema 下 B4 的 followup 已经用
        `{kind: action_ref, action: A2}` 做了完全同类的跨格续接，B3 也用
        action_ref 接到 B1/B2。所以 v1.3.1 完全能表达「逆向 → 正向」的组合，
        是本文件没有写。§3 第 3 条断言「逆向反推的产物 …… followup 只做代回验证
        → **可表达**」，把「没写」误记成了「已表达」。
      recommended_patch: |
        B7.followup_actions 改为 mode: any_of（或 sequence + 条件项），加：
          - { kind: local_operation, operation: 把反推出的方程/参数代回全部已知解逐一验证 }
          - { kind: action_ref, action: B2, when: 反推出方程后设问仍要求求解非齐次方程/初值问题 }
          - { kind: action_ref, action: B1, when: 反推出方程后设问要求写齐次通解 }
          - { kind: action_ref, action: A2, when: 联立消元后化为一阶线性方程（2012-9 型） }
        并把 terminal_when 收窄为「**设问所求的量**已确定且与全部已知结构一致」，
        不再是「方程、参数或通解已确定」。
        A6 同法加 `action_ref: A1 / A2`（when: 设问要求另一解或通解）。
        B8 同法加 `action_ref: B6`（when: 反推出 p、q 后仍要求求解）。
        §3 第 3 条相应改写：从「可表达」改为「schema 可表达，v1.0.0 未表达，已补」。

    - id: BL-3
      class: B2                      # direct counter-witness，击穿 F6 的 witness
      severity: high
      title: F6 的 witness 数学上不成立——反推出的一阶线性方程**确实**同时以 y₁、y₂ 为解
      where: failure_boundaries.F6.witness（标着 verification: verified）
      current_text: >
        「y₁ − y₂ = 1/(1−x) − 1/(2−x) 不是常数，因而不是「齐次部分 y′=0」的解
          （y′=0 的解都是常数）。若按线性逆向去反推「p、q」，得到的方程
          **无法同时以 y₁、y₂ 为解**。」
      counter_derivation: |
        取 F6 自己给的 y₁ = 1/(1−x)、y₂ = 1/(2−x)（都确为 y′=y² 的解）。
        按 A6 的 mechanism_note 反推：
          d  = y₂ − y₁ = −1 / ((2−x)(1−x))
          p  = −d′/d   = (2x−3) / ((x−2)(x−1))
          q  = y₁′ + p·y₁ = −1 / ((x−2)(x−1))
        代回检验（sympy 符号验证，两式均恒等于 0）：
          y₁′ + p·y₁ − q ≡ 0   ✔
          y₂′ + p·y₂ − q ≡ 0   ✔
        **两个解都满足反推出的方程。** witness 的断言被直接推翻。

        而且这不是巧合，是恒成立的：对任意两个处处不等的可微函数 y₁、y₂，
        线性方程组
            y₁′ + p y₁ = q
            y₂′ + p y₂ = q
        以 (p, q) 为未知量，系数行列式为 y₁ − y₂ ≠ 0，故**必有唯一解**，
        且由构造两式同时成立。所以「反推出的方程容不下两个解」**永不发生**。
      what_is_actually_true: |
        F6 的**结论**（逆向反推不能用于非线性方程）仍然成立，但理由完全不同：
        反推恒能得到**某个**一阶线性方程 y′+py=q，它同时以 y₁、y₂ 为解；
        但它**不是原方程** y′=y²。若设问是「反推原方程」，
        得到的是错误答案，且**代回验证发现不了**（两个解都通过）。
        真正的失效点是「不可辨识」，不是「无解」。
      side_effect_on_A6: |
        由此还推出一条对 A6 的独立警告：A6 的 terminal_when 要求
        「与**全部已知解**一致」——当已知解恰好只有两个时，
        这个一致性检查**恒真**，不构成任何检验。只有给到第 3 个解
        （或额外约束）时它才有判别力。2016-3 正是只给两个解的情形。
      recommended_patch: |
        F6.witness.ref 改写为：
          y′=y²（非线性），y₁=1/(1−x)、y₂=1/(2−x) 均为其解。
          按线性逆向反推得 p=(2x−3)/((x−2)(x−1))、q=−1/((x−2)(x−1))，
          该一阶线性方程**确实**同时以 y₁、y₂ 为解（可代回验证），
          但它不是原方程 y′=y²：例如 y₃=1/(3−x) 也是 y′=y² 的解，
          却不满足 y′+py=q。
          ⇒ 逆向反推施于非线性方程会给出一个**与原方程不同**的方程，
            且代回两个已知解无法发现错误。invalidates 成立，
            但失效模式是「不可辨识」而非「反推无解」。
        同时删除「齐次部分 y′=0」的说法——非线性方程没有齐次部分，
        这是把线性结构强加给非线性方程。
        并在 A6 的 guards 里补一条：**两个解的代回一致性检查恒真，不构成验证**。

    - id: BL-4
      class: B2                      # direct counter-witness，击穿一条标 sufficient 的 guard
      severity: high
      title: guard「二阶常系数非齐次已知 3 个解足以确定其通解」标 sufficient，反例存在
      where:
        - selection_rule.guards 第 11 条（logical_role: sufficient）
        - failure_boundaries.F7.recovery（「3 个解可定全」）
        - route_scan_by_cell.second_order_linear_constant_nonhomogeneous.existing_routes.CN2.applies_when
        - 同格 focused_checks_required_by_protocol.reverse_three_solutions
      current_text: >
        condition: 「二阶常系数非齐次方程已知 3 个解」足以确定其通解
        logical_role: sufficient
        check: 两两作差得到 2 个线性无关齐次解，任取一个解作特解
      counter_derivation: |
        取方程 y″ − y = 1。其齐次解空间 span{e^x, e^{−x}}，特解 y = −1。
        取三个**互不相同**的解：
          y₃ = −1,  y₁ = −1 + e^x,  y₂ = −1 + 2e^x
        （sympy 验证：三者均满足 y″ − y = 1 ✔）

        两两作差：y₁ − y₃ = e^x，y₂ − y₃ = 2e^x，y₁ − y₂ = −e^x。
        **三个差全部线性相关**，只张成一维空间 span{e^x}。
        由这 3 个解只能恢复一个特征根 r=1；第二个特征根无从确定：
        对任意 μ ≠ 1，方程 y″ − (1+μ)y′ + μy = −μ 都以 y₁、y₂、y₃ 为解
        （验证：其齐次解为 e^x、e^{μx}，特解 y=−1）。
        故通解 y = −1 + C₁e^x + C₂e^{μx} 随 μ 变化，**不被 3 个解确定**。

        ⇒ guard 里「3 个解 ⇒ 通解」的 sufficient 断言为假。
        check 字段写的「两两作差得到 **2 个线性无关**齐次解」已经偷偷用掉了
        独立性，但 condition 没有把它写进条件里——这正是断言失效的缝隙。
      why_2013_10_still_works: >
        2013-10（y₁=e^{3x}−xe^{2x}, y₂=e^x−xe^{2x}, y₃=−xe^{2x}）的差
        y₁−y₃=e^{3x}、y₂−y₃=e^x 恰好线性无关，所以该题结论正确。
        它是 guard 成立的一个实例，不是 guard 的证明。
      recommended_patch: |
        guard 第 11 条 condition 改为：
          「二阶常系数非齐次方程已知 3 个解，**且其中两两之差张成二维空间**
            （等价于三解不共仿射直线），足以确定其通解」
        logical_role 保持 sufficient（补上条件后确实充分）。
        F7.recovery 改为「补足解的个数**并核验差的线性无关性**（3 个解且差张成
        二维即可定全）」。CN2.applies_when 与 focused_check 同步加这一条件。

  non_blocking:            # 全部 record_to_backlog / reopen_family: false

    - id: NB-1
      title: 一阶非线性格漏了一条合法路线——互换自变量（视 x 为 y 的函数）
      class: route_omission
      detail: |
        first_order_nonlinear 的 route_universe 列了四类（A1 可分离 / A3 三种代换 /
        A4 全微分 / A0 建模），**没有**「把 x 看作因变量」这条。
        它是数学一大纲「会用简单的变量代换解某些微分方程」下的标准手法，
        结构上合法、scope 内可执行，且与 A3 的三种代换机制不同（不是对 y 做代换，
        是交换自变量与因变量的角色）。
        构造：(y² − 6x)y′ + 2y = 0 对 y 非线性，但改写为
          dx/dy − (3/y)x = −y/2，是关于 x(y) 的**一阶线性**方程，走 A2 即可。
        排除清单里也没有它——既未列为 route，也未注明排除理由，属清单缺口。
      action: record_to_backlog
      reopen_family: false
      recommended_patch: >
        在 A3 的 description 增列「互换自变量 x ↔ y，化为关于 x(y) 的一阶线性/伯努利」，
        或新增 A5（当前 action_id 恰好空着 A5，A4 之后直接跳到 A6）。
      note: 无 scope 内真题依赖它，故不构成 B1。按口径 3，「没考过」不是排除理由。

    - id: NB-2
      title: B5（缺 x 降阶）的 followup 漏了 A2 / A3，B4 漏了 A4
      class: routing_defect
      detail: |
        B5.followup_actions 只列 `action_ref: A1`（可分离）与 `action_ref: A4`（全微分）。
        但缺 x 降阶后得到 p·dp/dy = f(y,p)，该一阶方程可以是**线性**或伯努利。
        构造：y″ = −y(y′)² + y′（不含 x，缺 x 型）。
          令 p=y′(y)，y″ = p·dp/dy ⇒ p·dp/dy = −y p² + p ⇒ dp/dy = −y·p + 1，
          这是关于 p(y) 的一阶线性方程（非可分离），须走 A2 —— 而 B5 到不了 A2。
        B4 侧对称地漏了 A4（降阶后为全微分形）。
      action: record_to_backlog
      reopen_family: false
      note: 缺 x 型在 2004–2026 无真题（文件已如实写 not_found），故不构成 B1。

    - id: NB-3
      title: 常系数齐次格漏了「方程两端积分」这条求反常积分值的路线
      class: route_omission
      detail: |
        2020-11 求的是 ∫₀^{+∞}f dx 的**值**。B1 的 local_operation 只写
        「由特征根位置给出有界性/反常积分**收敛结论**」，产不出值。
        标准且更短的路线是对方程两端在 [0,+∞) 积分：
          f″+af′+f=0，a>0 ⇒ 两特征根之和 −a<0、之积 1>0 ⇒ 实部均负 ⇒
          f(+∞)=0, f′(+∞)=0。
          ∫₀^∞f″ + a∫₀^∞f′ + ∫₀^∞f = 0
          ⇒ (0 − n) + a(0 − m) + I = 0 ⇒ **I = am + n**。
        该 route 与 B1 机制不同（不需要写出通解），未被枚举也未被排除。
      action: record_to_backlog
      reopen_family: false
      note: >
        不判 B1：先解出通解再积分同样能到答案，故不构成「漏解」。
        但 B1 现有 local_operation 的措辞（只到「收敛结论」）确实覆盖不到 2020-11 的
        设问，建议一并补。

    - id: NB-4
      title: 变系数格漏了「由两个线性无关解直接写通解」（不反推 p、q）
      class: route_omission
      detail: >
        B8 反推 p、q。但若设问只要通解，由解的结构定理直接写 C₁y₁+C₂y₂ 即可，
        无须知道方程。这是与 B8 不同的合法 route（机制是解空间的线性结构，
        不是 Wronskian 求系数），未枚举也未排除。非齐次侧同理
        （给若干特解 ⇒ 通解，不必知道方程）。
      action: record_to_backlog
      reopen_family: false

    - id: NB-5
      title: 「常数变易法（一阶）」的排除理由标成 out_of_scope，应为 duplicate_mechanism
      class: exclusion_reason_mislabel
      where: route_scan_by_cell.first_order_linear.findings.excluded_candidates
      detail: >
        A2 的通解公式 y=e^{−∫P}(∫Qe^{∫P}dx+C) **就是**常数变易法的产物，
        两者给出逐字相同的结果。按口径 2 的四选一，正确标签是
        `duplicate_mechanism`（同机制），不是 `out_of_scope`（超纲）。
        标成 out_of_scope 会让人以为一阶常数变易在数学一里非法，而它只是
        与 A2 同机制。二阶的常数变易标 out_of_scope 则是对的（大纲只列待定系数）。
      action: record_to_backlog
      reopen_family: false

    - id: NB-6
      title: A3 把两种不同机制并成一条「ax+by+c 平移代换」
      class: wording / mechanism_conflation
      detail: >
        y′=f(ax+by+c) 用 u=ax+by+c 是**直接代换**（2024-14 的 y′=1/(x+y)² 即此型，
        文件的 instance basis 自己写的也是「u=x+y 代换化可分离」）；
        而 y′=f((a₁x+b₁y+c₁)/(a₂x+b₂y+c₂)) 才需要**平移代换**化齐次型。
        A3 的 description 只写「ax+by+c 平移代换」，把前者也叫平移代换，
        与自己的 instance basis 不一致。
      action: record_to_backlog
      reopen_family: false

    - id: NB-7
      title: B3 的 followup 用 mode: sequence 承载两条互斥的条件分支
      class: schema_usage
      detail: >
        B3.followup_actions.mode: sequence，但 actions 里第 2、3 项分别是
        `action_ref: B1, when: 化得的常系数方程为齐次` 与
        `action_ref: B2, when: …为非齐次`——两者互斥，不可能「依次执行」。
        语义上应是 local_operation 之后接一个 any_of。lint 不查 mode 与 when 的
        相容性，所以没报。B4/B5 用的就是 any_of，写法不统一。
      action: record_to_backlog
      reopen_family: false

    - id: NB-8
      title: fallback_policy.candidate_actions 只列 [A1, A2, A3, A4]，二阶 guard 失败后无候选
      class: field_coverage
      detail: >
        fallback_policy.when_guard_fails 里有四条是二阶的（特征方程 guard、
        待定系数 guard、逆向 guard、缺项换元），但同一节的
        candidate_actions 只有一阶的四个 action，B1–B8 一个都没有。
        看起来是从一阶那节复制下来未改。
      action: record_to_backlog
      reopen_family: false

    - id: NB-9
      title: evidence 把 2021-13 归入「解答」，实际是填空
      class: provenance_minor
      detail: >
        evidence.positive_problem_ids.解答 含 2021-13。
        考点标注.tsv 第 2021 年该行 question_type 为「填空」，
        高数真题题面_2021-2023.md 的 2021-13 亦标 `question_type: 填空`
        （题面：「欧拉方程 x²y″+xy′−4y=0 满足 y(1)=1, y′(1)=2 的解为 y=」）。
        解答/填空两栏的计数因此各错一个（16/18 应为 15/19），总数 34 不变。
      action: record_to_backlog
      reopen_family: false

    - id: NB-10
      title: frontmatter 的 batch_status.family_status 停在 assigned
      class: stale_field
      detail: >
        本文件 frontmatter 写 `batch_status.family_status: assigned`，
        而 HANDOFF.batch2_plan 对同一 family 写 `status: delivered_candidate`，
        正文 method_family_rule.status 写 `candidate`。三处三个值。
        lint 的 C1 只比对 frontmatter.status_summary 与正文 status（这两处一致），
        查不到 family_status 这一项，所以没报。
      action: record_to_backlog
      reopen_family: false
      note: >
        单独看属陈旧字段而非语义错误（三个值分属不同维度：派工态 / 交付态 / 成熟度），
        故不判 B4。但建议 integrator 交付时一并刷新，或给 lint 加一条 C3。

    - id: NB-11
      title: A4「由大纲要求」的说法在本仓库内无可追溯来源
      class: provenance_traceability
      detail: >
        A4 的 historical_instance 写 `not_found  # …结构上合法（大纲要求），不排除`。
        保留 A4 本身完全正确（口径 3：没考过不构成排除）。但「大纲要求」这个
        **理由**在本仓库里查不到出处：分析/考纲.md 第 72–73 行对常微分方程只写到
        「一阶方程、可降阶方程、高阶线性方程、常系数线性方程、欧拉方程」，
        没有「全微分方程」这一粒度。
      action: record_to_backlog
      reopen_family: false
      recommended_patch: >
        要么把理由改成 `dominated_not_excluded`（不依赖大纲条文即可成立），
        要么由 integrator 把大纲的方程类型粒度补进 分析/考纲.md 再引用。
        我不据外部记忆断言大纲条文——那超出本仓库可核验范围。

    - id: NB-12
      title: 一阶格没有「五型都不匹配」的出口
      class: router_completeness
      detail: >
        level_1_router.rule 为二阶写了出口（「二阶非线性且不缺项 → 无一般方法，属 scope 外」），
        一阶没有对应的一句。y′ = x² + y²（黎卡提型）会落进 first_order_nonlinear 格，
        A1/A3/A4 全不适用，而该格没有声明「无合法 action → scope 外/转 pending」。
      action: record_to_backlog
      reopen_family: false
      note: 此类题不在 2004–2026 scope 内，故不构成 B1。

  candidate_routes:        # 我独立生成后与现有候选集做差集，判定「应补入」的
    - { id: NB-1, route: 互换自变量 x↔y 化一阶线性/伯努利, cell: first_order_nonlinear }
    - { id: NB-3, route: 方程两端在 [0,+∞) 积分求反常积分值, cell: second_order_linear_constant_homogeneous }
    - { id: NB-4, route: 由两个线性无关解经解的结构定理直接写通解, cell: second_order_linear_variable }

  rejected_routes:         # 我独立想到但判定**不应**补入的，逐条附理由
    - { route: 常数变易法（一阶）,            reason: duplicate_mechanism, note: 与 A2 的通解公式同机制、同结果；文件现标 out_of_scope，见 NB-5 }
    - { route: 常数变易法（二阶）,            reason: out_of_scope,        note: 大纲二阶只列待定系数法，文件判定正确 }
    - { route: y^(n)=f(x) 直接积分 n 次,      reason: duplicate_mechanism, note: 是 B4 的迭代应用，文件判定正确，予以确认 }
    - { route: 幂级数解法,                    reason: out_of_scope,        note: 归 calc.series.route-selection，边界正确 }
    - { route: Clairaut / 奇异解与包络,       reason: out_of_scope,        note: 超大纲，文件判定正确 }
    - { route: 一阶常微分方程组,              reason: out_of_scope,        note: 数学一不考，文件判定正确 }
    - { route: 拉普拉斯变换解常系数 ODE,      reason: out_of_scope,        note: 数学一不考（我独立想到，文件未列，不列亦可） }
    - { route: 积分因子的一般判别式 μ(x)/μ(y), reason: dominated_not_excluded, note: 文件已在 open_items 记为 backlog，处理正确 }
    - { route: 数值解（欧拉折线/RK）,         reason: out_of_scope,        note: 文件 exclusions 已列 }
    - { route: 定性理论 / 相平面,             reason: out_of_scope,        note: 文件 exclusions 已列 }
```

---

## counter_witnesses

```yaml
counter_witnesses:
  verified:

    - id: CW-1
      targets: failure_boundaries.F6.witness
      claim_refuted: 「按线性逆向反推得到的方程无法同时以 y₁、y₂ 为解」
      construction: |
        y′ = y²；y₁ = 1/(1−x)，y₂ = 1/(2−x)（均为原方程的解）。
        p = −(y₂−y₁)′/(y₂−y₁) = (2x−3)/((x−2)(x−1))
        q = y₁′ + p·y₁       = −1/((x−2)(x−1))
        则 y₁′ + p y₁ − q ≡ 0 且 y₂′ + p y₂ − q ≡ 0。
      generalization: |
        对任意处处不等的可微 y₁、y₂，以 (p,q) 为未知量的线性方程组
          [y₁ 1; y₂ 1]·(p,q)ᵀ = (−y₁′, −y₂′)ᵀ
        行列式 = y₁ − y₂ ≠ 0，必有唯一解且两式同时成立。
        故该失效模式（「反推出的方程容不下两个解」）恒不发生。
      verification: verified
      method: sympy 符号化简，两残差恒等于 0
      consequence: F6 的 effect（invalidates）保留，但 explanation 与 witness 须重写；见 BL-3

    - id: CW-2
      targets: selection_rule.guards 第 11 条（logical_role: sufficient）
      claim_refuted: 「二阶常系数非齐次方程已知 3 个解足以确定其通解」
      construction: |
        y″ − y = 1；y₃ = −1，y₁ = −1 + e^x，y₂ = −1 + 2e^x（三个互异的解）。
        差：y₁−y₃ = e^x，y₂−y₃ = 2e^x，y₁−y₂ = −e^x —— 全部线性相关。
        对任意 μ ≠ 1，y″ − (1+μ)y′ + μy = −μ 同样以这三者为解
        （齐次解 e^x、e^{μx}，特解 −1）。通解随 μ 变化，未被确定。
      verification: verified
      method: sympy 验证三解满足 y″−y=1；μ 族由构造直接给出
      consequence: guard 须补「两两之差张成二维」的条件；见 BL-4

    - id: CW-3
      targets: level_1_router.rule（「若缺项，直接落 second_order_reducible」）
      claim_refuted: 该跳转对全体二阶方程是安全的
      construction: |
        y″ + py′ + qy = 0 恒可写成 y″ = −p y′ − q y = f(y, y′)，右端不显含 x，
        故**每个常系数齐次方程都满足「缺 x」**，全部被排他地送进 reducible 格，
        而 B1 不在该格的 actions 里。
        scope 内实例：2017-10、2016-16、2020-11、2023-2、2008-3。
        缺 y 侧：2006-18、2025-18、2026-18 为欧拉形，同样被切断到 B3 的路。
      verification: verified
      method: 直接由 router 文本与 level_2_candidates.actions 清单逐条推演
      consequence: 见 BL-1

  pending: []

  search_result_not_found:
    - target: F8（待定系数用于 tan x 型右端）
      note: >
        未找到能推翻 F8 结论的反例——右端 tan x 确实不属
        P_n(x)e^{λx} / e^{αx}(Acosβx+Bsinβx) 族，becomes_inconclusive 成立。
        `search_result: not_found`。
        但 witness 本身选得不好：它取的试探解 Acosx+Bsinx **恰是齐次解**，
        代入必得 0，失效原因是共振（F2 的机制），不是「右端超出可待定族」（F8 的机制）。
        读者按 F2 的办法乘 x 会以为能修好。建议换成 y″+y = ln x 之类不共振的右端，
        或直接论证「tan x 的任意有限参数 ansatz 不闭合于 L 的像空间」。
        属 backlog（可以再找一个更好的反例），非 blocker。
    - target: F9（常系数走可降阶 loses_advantage）
      note: 数学复核通过——y″+y′=0 两条路都给 y=C₁+C₂e^{−x}，效果分类正确。`search_result: not_found`
    - target: F10（正向 ↔ 逆向 changes_branch）
      note: >
        分类正确，2009-10 / 2013-10 的描述与题面相符。`search_result: not_found`。
        唯一措辞问题：explanation 写「同题的逆向设问**不允许**先正向硬解」，
        对 2013-10 这类方程未知的题是事实（无从正向解），但作为一般规则是效率
        偏好而非合法性禁令。属 backlog。
    - target: B8 在 scope 内是否可执行
      note: >
        可执行。由 y_i″+p y_i′+q y_i=0 (i=1,2) 解 2×2 线性方程组，
        系数行列式 = y₁′y₂ − y₂′y₁ = −W(y₁,y₂)，两解线性无关时（由阿贝尔公式）
        在整个区间上非零，故 p、q 唯一确定。所用工具只有解二元一次方程组与求导，
        scope 内可执行。**保留 B8 的判断正确。**
        两点小注：(1) mechanism_note 说「分母为 Wronskian W(y₁,y₂)」，
        实际行列式是 −W，差一个符号，不影响结果；
        (2) 与 CW-1 同源的性质：任给两个函数总能构造出以它们为解的二阶线性方程，
        所以 B8 的「代回验证」同样是恒真检查，不构成判别。`search_result: not_found`
```

---

## guard_audit

任务书写「12 条 guard」，实测 **15 条**（necessary 9 · sufficient 2 · supporting_heuristic 4）。逐条定性：

| # | guard（摘要） | 现标 | 我的判定 | 理由 |
|---|---|---|---|---|
| G1 | 一阶线性须化标准形，P、Q 区间上连续可积 | necessary | **同意** | 公式 μ=e^{∫P} 的成立前提；xy′ 型在 x=0 处确实不可直接套 |
| G2 | 可分离须能写成 f(x)g(y)，**且补检 g(y)=0** | necessary | **部分不同意** | 前半（可写成 f·g）是 necessary ✔；后半（补检常数解）不是适用性条件，是**执行义务**，且其失效 F4 是 `becomes_inconclusive` 而非 `invalidates`。两件事捆在一条 guard 里标同一个 role，掩盖了这个差别。建议拆成两条：applicability(necessary) + completeness_obligation |
| G3 | 齐次型须 y′=f(y/x)；伯努利须 n≠0,1 | necessary | **同意** | 结构识别条件，n=0/1 的归属处理正确 |
| G4 | 全微分须 M_y=N_x（单连通），否则须找积分因子 | necessary | **同意但与 G10 重叠** | M_y=N_x 对恰当性是必要的（C¹ 下），G10 又说它是充分的。两条其实是同一个双条件命题的两半，分列两条且给不同 role，读者会以为是两个独立条件。建议合并为一条并写明「单连通区域上是充要」 |
| G5 | 特征方程只适用常系数 | necessary | **同意** | F1 已给出成立的 witness（CMD-2001 范围内，未复核） |
| G6 | 待定系数须右端可待定，**且特解按重数乘 x^k** | necessary | **部分不同意** | 与 G2 同型：前半是 applicability(necessary) ✔，后半是执行义务。且 F2（漏乘 x^k）判 invalidates、F8（右端超族）判 becomes_inconclusive，两个不同 effect 被同一条 necessary guard 覆盖 |
| G7 | 欧拉变换须用替换表 x²y″=D(D−1)y | necessary | **不同意 role** | 这是**运算正确性**要求，不是 route 的适用性条件。写错替换表不会让欧拉 route 变得不合法，只会算错。建议降为 execution_rule（若 schema 无此 role，则移入 B3 的 local_operation，不占 guard 位） |
| G8 | 可降阶换元必须匹配缺项类型 | necessary | **不同意（过强）** | 文件自己的 focused_check 写「同时缺 x 与 y（如 y″=f(y′)）**两条都可用**」——那就不是「必须匹配」。且缺 x 误用缺 y 换元时 F5 判 becomes_inconclusive（走不动），不是 invalidates（非法）。necessary 与该 effect 不相容。建议改为 supporting_heuristic 或 execution_rule |
| G9 | 逆向反推只对线性成立；且需足够数量的线性无关齐次解 | necessary | **同意，但理由须重写** | 结论对 ✔。但支撑它的 F6 witness 是错的（BL-3）：真正的失效不是「反推不出方程」而是「反推出的方程不是原方程且验不出来」。role 不变，explanation 须改 |
| G10 | 「M_y=N_x 且单连通」是 A4 的充分条件 | sufficient | **同意** | 定性正确，且 check 里「不满足不等于 A4 不可用」写得好——正确避免了把充分当必要 |
| G11 | 「已知 3 个解」足以确定二阶常系数非齐次的通解 | sufficient | **不同意——已证伪** | 见 BL-4 / CW-2。反例 y″−y=1，三解 −1、−1+e^x、−1+2e^x，差全相关。condition 缺「差张成二维」这一条件，而 check 字段已经偷用了它 |
| G12 | 二阶先扫缺项信号，再谈线性 | supporting_heuristic | **role 标对了，但被 router 违反** | explanation 明写「不是合法性条件」——这个定性正确。问题在 level_1_router 用「**直接落**」把它实现成了排他的硬路由，F9 又用它去限定 eligible_cells。**标签与实现不一致**，这正是 BL-1 |
| G13 | 欧拉形立即换元 x=e^t | supporting_heuristic | **同意** | 识别信号驱动的偏好，定性正确 |
| G14 | 常系数非齐次优先待定系数（比常数变易省） | supporting_heuristic | **同意** | 明确写了「省」，是效率偏好，标对了 |
| G15 | 应用题先列方程（A0） | supporting_heuristic | **同意** | 流程偏好，标对了 |

**「把效率偏好写成合法性条件」的专项结论**（任务书点名要判的）：

- **直接写反的：0 条。** 四条 supporting_heuristic（G12–G15）全部老实标了 heuristic，
  三条里两条还在 explanation 里主动声明「不是合法性条件」「比常数变易省」。
  这一层做得比 batch1 的 extrema 干净。
- **但发生了更隐蔽的一种：标签写对了，实现把它当合法性条件用。** G12 标
  supporting_heuristic，`level_1_router.rule` 却把它实现成排他跳转，
  F9 进一步用它限定 `eligible_cells`。**净效果与「把偏好写成合法性条件」相同**，
  而且因为标签是对的，guard 层的检查发现不了。见 BL-1。
- **另有一类混淆值得记录**：G2 / G6 / G7 / G8 把**执行义务**（补常数解、乘 x^k、
  抄对替换表、选对换元）标成 `necessary`。它们不是「route 是否合法」的条件，
  而是「route 执行得对不对」的条件。区别是可检验的：违反 necessary 应导致
  `invalidates`，而这四条对应的 failure boundary 有两条是 `becomes_inconclusive`
  （F4、F5）。schema 目前没有 execution_rule 这个 role，建议 integrator 考虑
  是否需要（**这不构成 B3**——用 local_operation 表达完全够，不歪曲数学关系）。

---

## source_evidence

```yaml
source_evidence:
  problem_bank:
    files: [分析/高数真题题面_2004-2010.md, _2011-2016.md, _2017-2020.md, _2021-2023.md]
    source_status: ocr_uncertain
    evidentiary_weight: none          # 与被审文件的处理一致，我未升级任何一条为 witness
    note: >
      我用它做逐字核对（题面 vs 文件的 instance basis），**不作为 witness**。
      被审文件在每格 positive_instance_mapping 里都写了
      `evidentiary_weight: none` 并说明理由——这一层处理正确，无越权。
  papers_direct:
    used_for: [2024-14, 2025-18, 2026-18]   # 这三年不在题面库（留作模考，2026-11-29 前不入库）
    files: [papers/2024考研数学一真题+答案.md, papers/2025年数学一真题.md, papers/2026年考研数学一真题.md]
    caveat: >
      **披露**：papers/ 的 2024–2026 三个文件按 CLAUDE.md §2.4 混有
      【答案】/【解析】段落。我取 2025-18 的题面时，同一文件区块内的解析文字
      不可避免地进入了视野。**我没有把它作为任何判断的依据**：
      本报告对 2025-18 的全部结论（缺 f、同时为欧拉形、因此被 router 排他地
      切断到 B3 的路）只依赖题面给出的方程 u²f″+uf′=1 本身。
      solutions/ 目录**全程未读**。
  tsv:
    file: 分析/考点标注.tsv
    sha256_prefix: cbdf1a55989a8f60
    check: >
      与被审文件 frontmatter 的 source_tsv_sha256 **逐字相符**（我独立算过）。
      provenance 这一项无问题。
  syllabus:
    file: 分析/考纲.md
    note: 第 72–73 行对常微分方程只到章节粒度，支撑不了 A4 的「大纲要求」措辞，见 NB-11
  baseline_commits:
    "2578d44": exists    # creation_provenance 引用，git cat-file 确认
    "4d7d333": exists    # 同上
  lint:
    command: python3 分析/tests/lint_method_families.py
    result: "PASS：error 0 · warning 4"
    warnings: extrema A2/A3/A5/A7 的 S3 typing 欠账（已冻结族，backlog，与基线一致）
    note: 与 HANDOFF 声明的基线完全一致，被审文件未引入任何新 error 或 warning
```

### scope 核对：34 题的划定

**逐题比对结论：ODE 主考点的题一道没漏，但 34 这个数与 3981c9f 新立的 `scope_boundary_rule` 冲突。**

```yaml
scope_audit:
  method: >
    1) 对 考点标注.tsv 全部 499 行做关键词扫描（微分方程/欧拉方程/特征方程/通解/特解/
       可降阶/伯努利/变量可分离/一阶线性/齐次方程/积分因子/全微分方程），命中 46 行，
       人工剔除线代命中（齐次方程组、特征方程重根等）；
    2) 反向扫描：对题面库全部题面正文扫 微分方程|欧拉方程|通解|特解，命中 27 题，
       与被审文件的 34 题清单做差；
    3) 逐题核对被审文件的 instance basis 与题面原文。

  missing_from_the_34: []      # 无漏题
  reverse_scan_residue:
    ids: [2004-20, 2005-21, 2006-20, 2008-21, 2010-20, 2012-20, 2017-20, 2019-13]
    verdict: 全部为线性代数题（「齐次方程组基础解系与通解」等），非 ODE，正确未纳入

  arithmetic_check:
    claimed: "31 核心（一阶 14 + 二阶 17）+ 3 级数-ODE 边界 = 34"
    recomputed: 一阶 14 ✔ · 二阶 17 ✔ · 级数边界 3 ✔ · 合计 34 ✔
    verdict: 自洽，算术无误

  conflict_with_scope_boundary_rule:
    rule_source: 分析/METHOD_FAMILY_HANDOFF.md · batch2_plan.scope_boundary_rule（decided_at 2026-08-28）
    rule_text: 一道题归属于其「主考点」所在的族（TSV 每行考点列的第一个）；次考点跨族不改变归属
    measured_by_me:
      ode_as_primary_tag: 24
      ids: [2004-4, 2004-16, 2005-2, 2006-2, 2007-13, 2008-3, 2008-9, 2009-10,
            2010-15, 2011-10, 2012-9, 2013-10, 2014-11, 2015-2, 2016-3, 2016-16,
            2017-10, 2018-18, 2019-10, 2019-15, 2020-11, 2021-13, 2023-2, 2024-14]
      ode_as_secondary_tag_only: 10
      breakdown:
        主考点=幂级数系数递推与微分方程: [2007-20, 2013-16, 2020-17]   # 文件已自行让给级数族 ✔
        主考点=多元复合函数的二阶偏导数:   [2006-18, 2014-17, 2025-18, 2026-18]
        主考点=参数方程的切线:             [2012-18]
        主考点=导数的几何意义与切线方程:   [2015-16, 2023-17]
    verdict: >
      被审文件把这 10 题全部计入 evidence（其中 3 题已声明主路由归级数族，处理正确）。
      但按 scope_boundary_rule，另外 7 题的**归属**在别的族，
      「次考点跨族不改变归属，也不允许第二个族把它算进自己的 scope_problems」。
      于是 34 这个数与该规则不相容：合规的写法是 **24（scope）+ 10（次考点共享的
      positive instance）**。
    timing: >
      **这不是 DeepSeek 的错。**scope_boundary_rule 立于 3981c9f，
      晚于本文件建档（基线 2578d44）。文件写作时该规则不存在。
    classification: 我不判 B4。
    why_not_B4: >
      B4 要求「跨文件状态不一致」。这里两侧其实一致地记着同一个数：
      HANDOFF.batch2_plan 对 ODE 写的就是 `scope_problems: 34` 并附注「计划 40
      实测 34」。真正冲突的是**同一文件内**的 batch2_plan 条目与
      scope_boundary_rule 两节，属规则新增后的追认欠账，
      且不改变任何 route 的合法性判定。按停止规则记 backlog。
    action: record_to_backlog
    reopen_family: false
    but_blocks_task_B: >
      **这条对任务 B 是硬前置。**2006-18 / 2014-17 / 2025-18 / 2026-18 四题的
      主考点是「多元复合函数的二阶偏导数」，正是 calc.multivar.route-selection
      的地盘。在 integrator 裁定之前，多元族与 ODE 族会对同一批题给出竞争路由。
      我按 scope_boundary_rule 的 on_dispute 条款处理：**不自行改归属**，
      写进 open_questions 等裁定。
```

---

## recommended_changes

```yaml
recommended_changes:
  # 我不改被审对象；以下由 integrator 判断采纳与否。按建议优先级排列。

  - ref: BL-1
    priority: 1
    file: 分析/方法族-高数-微分方程.md
    sections: [level_1_router.rule, selection_rule.minimal_probe, F9, B4/B5 的 eligible_cells]
    change: >
      把「缺项 → 直接落 second_order_reducible」从排他跳转改为并行候选：
      缺项命中时 B4/B5 进入候选集，同时仍按 线性×系数×齐次性 落格，
      由 preference_rule 排序。B4/B5 的 eligible_cells 扩到常系数两格
      （F9 已证它们在那里合法）。删除 F9 中用效率理由限定 eligible_cells 的那句。
    note: 改动会触发 lint 的 R2 双向一致校验，须同步更新 level_2_candidates 的 actions 清单。

  - ref: BL-2
    priority: 2
    sections: [A6, B7, B8 的 followup_actions 与 terminal_when；§3 第 3 条]
    change: >
      给三条逆向 action 补 action_ref（B7→B2/B1/A2，A6→A1/A2，B8→B6），
      terminal_when 收窄为「**设问所求的量**已确定」。
      §3 第 3 条从「可表达」改为「schema 可表达，v1.0.0 未表达，已补」。

  - ref: BL-3
    priority: 3
    sections: [F6.witness, F6.explanation, A6 的 guards]
    change: >
      重写 F6 的 witness（失效模式是「不可辨识」不是「反推无解」），
      删除「齐次部分 y′=0」的提法，并补一条 guard：
      「只有两个已知解时，代回一致性检查恒真，不构成验证」。

  - ref: BL-4
    priority: 4
    sections: [guards 第 11 条, F7.recovery, CN2.applies_when, 同格 focused_check]
    change: 四处同步补上「两两之差张成二维空间」这一条件。

  - ref: [NB-1, NB-2, NB-3, NB-4]
    priority: 5
    change: 补入三条遗漏 route 与两处 followup 缺口（A5 位当前空着，可用于互换自变量）。

  - ref: [NB-5, NB-6, NB-7, NB-8, NB-9, NB-10, NB-11, NB-12]
    priority: 6
    change: 排除理由改标、措辞与字段修补，无一影响 route 合法性判定。

  - ref: scope_audit
    priority: 1                        # 与 BL-1 并列，因为它卡住任务 B
    file: 分析/METHOD_FAMILY_HANDOFF.md
    change: >
      裁定 2006-18 / 2014-17 / 2025-18 / 2026-18（主考点=多元复合函数的二阶偏导数）
      与 2012-18 / 2015-16 / 2023-17 的归属，并把 ODE 的 scope_problems 表述改为
      「24（scope）+ 10（次考点共享 instance）」或明确 scope_boundary_rule 不追溯适用。
      同时 batch2_plan 的 multivar `scope_problems: 39` 与看板的「38 题」需对齐。
```

---

```yaml
status_recommendation:
  current: candidate
  recommended: challenged            # 仅为 recommendation，我无权执行
  rationale: >
    存在四条 direct blocker，其中 BL-1 使 scope 内五道真题（2017-10、2016-16、
    2020-11、2023-2、2008-3）在现行 router 下拿不到能给出答案的 action，
    BL-3 与 BL-4 各有一条已符号验证的 direct counter-witness 击穿了
    标着 `verification: verified` 的 witness 与标着 `sufficient` 的 guard。
    按 AGENT_COLLAB_PROMPT §3，我能做的唯一状态动作是**推荐** challenged，
    由 integrator 依其权限决定是否 quarantine。
  explicitly_not_recommended:
    - 任何向上的状态变更（candidate → partially_verified 等）
    - 对 pedagogical_validation 的任何改动（保持 untested）
  driven_only_by:
    - BL-1, BL-2, BL-3, BL-4          # 全部为被审对象自身的问题
  explicitly_excluded_from_this_recommendation:
    - MM-A, MM-B, NB-10               # 协作文档问题，依 CMD-2004 不参与定级
  note: >
    若 integrator 判定 BL-1/BL-2 属「修一处措辞即可」而不愿 quarantine，
    我不反对——四条 blocker 的**修补成本都很低**（都是加候选、加 action_ref、
    改 witness 文本、补一个条件），没有一条需要重做 route scan。
    但在修补落地之前，`route_scan_status: complete_within_declared_universe`
    这个断言在 second_order_reducible 与两个常系数格上不成立
    （11 项里的 `no_direct_blocker_open` 为 false）。

confidence_limits:
  search_budget: |
    · 六格各做一轮独立结构穷举（先不看真题主解），按八步协议第 3 步的十个
      adversarial 角度逐条过；
    · F6–F10 逐条重推，其中 F6、F7/G11 用 sympy 做了符号验证；
    · 15 条 guard 逐条判 role，并交叉检查「guard 的 role」与「其对应 failure
      boundary 的 effect」是否相容——这是我发现 G2/G6/G8 问题的路径；
    · 34 题双向扫描（TSV 正扫 + 题面库反扫）+ 逐题 basis 核对；
    · lint 独立复跑一次。
  not_checked:
    - F1–F5 的数学推导、2004-4 与 2006-18 的引用、lint 的多文件改动
      （CMD-2001 指明已由 integrator 核过，我未重复；**因此我对它们不背书**）
    - 未做第二轮独立重扫；未与外部教材的路线清单做系统比对
    - 未核 mechanism.statement 里每一条公式的排版细节（只核了被 route 引用到的）
    - 2024–2026 三题只有 papers/ 一个来源（题面库尚未收录），
      无法做「题面库 vs papers」的双源比对
    - teaching_policy 一节未审（不在派工范围）
  known_weakness_of_this_review: >
    BL-1 的成立依赖「缺 x」采标准含义（方程不显含自变量 x）。若 integrator
    认为本族语境下「缺 x」另有窄义（例如默认排除常系数），那么 BL-1 的
    常系数半边不成立——但缺 y 半边（2006-18 / 2025-18 / 2026-18 的欧拉形被
    切断到 B3 的路）**不依赖这个解释**，仍然成立。
    我未自行采用窄义，因为文件里没有任何地方定义过它。

files_changed:
  - 分析/审查/Codex-audit-ode-240c1dc.md      # 本报告（新建）
  - 分析/协作/看板.md                          # 只改 codex-audit-ode 自己那一行
audited_file_diff: empty                       # 被审对象逐字节未动，已 git diff 确认
```
