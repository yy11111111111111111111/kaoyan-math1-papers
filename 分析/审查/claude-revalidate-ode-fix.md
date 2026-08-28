# Claude 独立复核报告 · calc.ode.route-selection 修复（revalidation）

> 只读复核。被审对象 = `分析/方法族-高数-微分方程.md` 的**未提交工作区改动**
> （git diff 相对 ee3605c：53 insertions / 35 deletions，仅此一个文件）。
> 我实读的就是这个工作区状态；solutions/ 全程未读。
> 数学断言全部用 `PYTHONUTF8=1 py` + sympy 独立复算，结论不照抄修复声明。

```yaml
task_id: batch2.ode.revalidate_fix_review
role: independent_reviewer

artifact_identity:
  head: ee3605c                          # worktree 基线（我复核时的 git HEAD）
  audited_state: 工作区未提交 diff（v1.0.1 → 待定 v1.1.0）
  audited_file: 分析/方法族-高数-微分方程.md
  audited_version: 1.0.1（doc_version 尚未 bump，改动即待定 v1.1.0 的内容）
  family_id: calc.ode.route-selection
  author: DeepSeek（v1.0.0 建档）；integrator = Claude Code（v1.0.1 降级落地 + 本次修复）
  prior_review: Codex-audit-ode-240c1dc.md（BL-1..4，recommended 降 challenged）

verification_tooling:
  - "lint：py 分析/tests/lint_method_families.py → PASS：error 0 · warning 4"
  - "sympy 符号验证：BL-3 F6 witness、BL-4 充分/不充分双例、2006-18 欧拉形判别"
  - "全文件 grep：旧语义残词（直接落 / 只含 reducible / 齐次部分 / 旧 terminal_when）"
```

## findings

```yaml
findings:
  blockers: []                      # 修复后无 B1–B4（四格全部 verified，见 per_blocker_review）

  non_blocking:
    - id: RES-1
      class: wording / 事实性误标（在**现行** level_1_router.rule 内）
      where: level_1_router.rule（L118）
      text: "「变系数且非欧拉形而缺项 → B4/B5 优先，**2006-18 即此类**」"
      why_wrong: >
        2006-18 题面 f″+f′/u=0 乘 u² 即 u²f″+uf′=0，**正是欧拉形**（a=1,b=0）。
        我独立核过：欧拉路线 B3 对 2006-18 成立（x=e^t 变换得 D²f=0 → f=C₁lnu+C₂），
        与 B4（缺 f 降阶）结果一致。把它归入「变系数且**非**欧拉形」是事实性误标。
      routing_impact: none
        # 不影响路由：2006-18 同时命中「欧拉形→B3 优先」与「缺项→B4/B5 优先」两子句，
        # 两条路都可达、答案相同（均出自审计 recommended_patch 内嵌的同款矛盾注）。
      recommended_patch: 删去「2006-18 即此类」，或改为「欧拉形亦缺项（如 2006-18）→ B3/B4 并存」。

    - id: RES-2
      class: 旧语义残留（guard 层；BL-1 修复未扫到）
      where: selection_rule.guards 第 12 条 check（L422）
      text: "「缺项直接进可降阶格」"
      why_wrong: >
        修复后 level_1_router.rule / minimal_probe / reducible 格 note 三处均已是
        **非排他**语义（「B4/B5 进入候选，同时仍按线性×系数×齐次性落格」），
        仅此 guard 的 check 仍写旧排他表述「直接进可降阶格」。
      severity_call: 我判 **非 blocking**，但它是四类 blocker 修复里唯一残留的旧语义字样
        （B4 定义含「现行规则实际写的是旧语义」）。理由：
        (a) 该 guard 是 supporting_heuristic，explanation 明写「不是合法性条件」；
        (b) 权威路由文本（level_1_router.rule）已正确；
        (c) 按字面执行会退回 BL-1 的 bug，故应修，但当前路由结果不受影响。
      recommended_patch: check 改为「缺项信号命中时 B4/B5 进入候选，同时仍按线性×系数×齐次性落格」。

    - id: RES-3
      class: 设计理由的事实错误（§0.1，v1.0.0 遗留，修复未更正）
      where: §0.1 修正②（L47-48）
      text: "「若先按线性把它分进『变系数』格，该格只有欧拉与已知一特解两条候选，对 2006-18 都**不适用**」"
      why_wrong: >
        与 RES-1 同源：欧拉（B3）对 2006-18 **是适用的**（上式已证）。
        该句是 v1.0.0 时代为「缺项先于线性」辩护的理由，结论（缺项信号有用）仍对，
        但论据假。修复把路由改对了，却没同步更正这条 rationale。
      routing_impact: none   # §0.1 是设计说明，不是现行规则。
      recommended_patch: 把「对 2006-18 都不适用」改为「欧拉在该格可用，但缺 f 降阶更直接」之类的准确表述。

    - id: RES-4
      class: provenance / 版本标注（NB-10 同族，非新）
      where: frontmatter doc_version=1.0.1；§3 第 3 条「v1.0.1 已补：B7→B2/B1/A2…」
      note: >
        本次修复内容被 §3 标成「v1.0.1 已补」，而 status_history 里的 v1.0.1 条目
        是**修复前**的降级记录（「恢复 candidate 需 targeted revalidation」）。
        同一版本号指向两个内容态，落地 v1.1.0 时应一并刷新 doc_version、§3 措辞，
        并考虑在 status_history 加一条「fixes landed，pending revalidation」记录。
        lint C1 不受影响（正文 status=challenged 与 frontmatter status_summary=challenged 一致）。

  per_blocker_review:
    BL-1:
      verdict: confirmed_fixed
      note: >
        一级 router 已从「若缺项，直接落 second_order_reducible」改为「缺项命中时
        B4/B5 进入候选集，同时仍按 线性×系数×齐次性 落格」（非排他，preference_rule 排序）。
        复算：2017-10（y″+2y′+3y=0，常系数齐次缺 x）→ 缺 x 信号使 B4/B5 入候选，
        同时落 constant_homogeneous 格 → B1 可达，preference 把 B1 排前 ✔；
        2006-18（f″+f′/u=0，欧拉形且缺 f）→ 同时命中「欧拉形→B3 优先」与「缺项→B4/B5 优先」，
        B3 与 B4 并存 ✔。B4/B5 eligible_cells 扩到常系数两格后，R2 双向一致成立
        （lint error 0）。F9 旧句「这正是…eligible_cells 只含 reducible 格…的理由」已删改
        （现为「dominated_not_excluded 候选（效率低≠非法），不删除；preference 把 B1/B2 排前」）✔。
        残留排他表述仅 guard 12 的 check（RES-2）与设计理由误标（RES-1/RES-3），
        均不改路由结果。
    BL-2:
      verdict: confirmed_fixed
      note: >
        A6/B7/B8 的 followup 已补 action_ref 且 R1 校验全部指向真实 action：
        A6→A1/A2（mode any_of）、B7→B2（2009-10 型）/B1（齐次通解）/A2（2012-9 型）、
        B8→B6。语义核对：2009-10 先 B7 反推 a=−2,b=1 再 B2 解非齐次初值 → 通 ✔；
        2012-9 联立相减得 f′−3f=−2e^x 一阶线性 → A2 ✔；齐次通解设问 → B1 ✔。
        terminal_when 已收窄为「设问所求的量已确定…」：对「只问 p、q/方程」的设问
        （如 2016-3 只问 q(x)）量就是 p/q/方程，仍可在该点合法终止，未收过头 ✔。
        §3 第 3 条已从「可表达」改为「schema 可表达，v1.0.0 未写，v1.0.1 已补」✔
        （版本号标注见 RES-4）。
    BL-3:
      verdict: confirmed_fixed
      note: >
        F6 witness 已重写为「不可辨识」失效模式，我独立复算：
        y₁=1/(1−x)、y₂=1/(2−x) 代入 p=(2x−3)/((x−2)(x−1))、q=−1/((x−2)(x−1))，
        y₁′+p·y₁−q≡0、y₂′+p·y₂−q≡0（sympy 残差均为 0）✔；
        y₃=1/(3−x) 是 y′=y² 的解（y₃′−y₃²=0）但 y₃′+p·y₃−q = 2/(x⁴−9x³+29x²−39x+18) ≠ 0 ✔。
        全文件「齐次部分」字样已清除（grep 0 命中）✔。
        A6 相关 guard（selection_rule 逆向 guard 的 explanation）已补
        「仅两个已知解时代回一致性检查恒真，不构成验证（BL-3）」✔。
    BL-4:
      verdict: confirmed_fixed
      note: >
        guard 第 11 条 condition 已补「两两之差张成二维空间（等价于三解不共仿射直线）」，
        数学上充分：差张成二维 ⇒ 得 2 个线性无关齐次解 ⇒ 定常系数 p、q ⇒ f 由任一解代回
        确定 ⇒ 通解确定。复算两例：
        (1) 充分例 y″−y=1，三解 −1 / −1+e^x / −1+e^{−x}：差 e^x、e^{−x} 的
        Wronskian=−2≠0（二维）→ 反推 p=0、q=−1、f=1，定全 ✔；
        (2) 不充分例 y″−y=1，三解 −1 / −1+e^x / −1+2e^x：差全张 span{e^x}（比值 1/2 常数，
        一维），且对任意 μ≠1，y″−(1+μ)y′+μy=−μ 同以三者为解（sympy 残差全 0）→ 不定全 ✔。
        F7.recovery / CN2.applies_when / focused_check reverse_three_solutions 三处已同步
        补该条件（grep「两两之差张成二维」命中 4 处 + guard check 1 处，无遗漏）✔。

  new_issues: [RES-1, RES-2, RES-3, RES-4]
    # 均为 wording / 标注级，无一构成 B1–B4；RES-2 是唯一「现行 guard 内旧语义残留」，
    # 建议随 v1.1.0 一起清掉，否则读者按 guard 字面执行仍会退回 BL-1 的排他跳转。

counter_witnesses:
  verified:
    - id: CW-A   # BL-4 充分例（差张成二维 → 定全）
      construction: y″−y=1，三解 −1 / −1+e^x / −1+e^{−x}；差 Wronskian=−2≠0；反推 p=0,q=−1,f=1
      method: sympy 符号化简
      result: 定全 ✔
    - id: CW-B   # BL-4 不充分例（差张成一维 → 不定全，原反例可复用）
      construction: y″−y=1，三解 −1 / −1+e^x / −1+2e^x；差比值 1/2 常数；μ 族同解
      method: sympy 符号化简（μ 族三式残差均 0）
      result: 不定全 ✔
    - id: CW-C   # BL-3 新 F6 witness
      construction: y′+py=q（p=(2x−3)/((x−2)(x−1))、q=−1/((x−2)(x−1))）同时含 y₁、y₂；
                   y₃=1/(3−x) 为 y′=y² 解但不满足 y′+py=q
      method: sympy 符号化简（y₁、y₂ 残差 0；y₃ 残差非 0）
      result: 失效模式确为「不可辨识」✔
    - id: CW-D   # BL-1 路由可达性
      construction: 2017-10 → B1 可达；2006-18（乘 u² 即欧拉形）→ B3 与 B4 并存
      method: 由 router 文本 + 欧拉形判别逐步推演
      result: 可达性成立 ✔
  pending: []

lint_result:
  command: PYTHONUTF8=1 py 分析/tests/lint_method_families.py
  error_count: 0
  warning_count: 4
  warnings_detail: 全部在已冻结 extrema（A2/A3/A5/A7 S3 typing 欠账），与基线一致，非 ODE 引入

recommended_changes:
  # 全部为非 blocking 措辞/标注清理；无一条 blocker。按建议优先级：
  - { id: RES-2, file: 分析/方法族-高数-微分方程.md, priority: 1, change: "guard 12 的 check「缺项直接进可降阶格」改为非排他表述（这是修复后唯一残留的旧排他语义）" }
  - { id: RES-1, file: 分析/方法族-高数-微分方程.md, priority: 2, change: "level_1_router.rule L118 删去「2006-18 即此类」（2006-18 是欧拉形，非『非欧拉形』）" }
  - { id: RES-3, file: 分析/方法族-高数-微分方程.md, priority: 3, change: "§0.1 L47-48「对 2006-18 都不适用」更正（欧拉 B3 适用 2006-18）" }
  - { id: RES-4, file: 分析/方法族-高数-微分方程.md, priority: 4, change: "落地 v1.1.0 时 bump doc_version；§3 的「v1.0.1 已补」改 v1.1.0；status_history 补一条 fixes-landed 记录" }

status_recommendation:
  current: challenged
  recommended: candidate（恢复为候选态，撤销 quarantine）
  rationale: >
    四条 direct blocker 的修复我全部独立验证成立（BL-1 路由可达性、BL-2 action_ref 语义、
    BL-3 新 witness 数学、BL-4 充分/不充分双例）。无残留 B1–B4。剩余仅 4 处
    wording / 版本标注问题，均不改路由结果。
    依 HANDOFF，状态动作只能由 integrator 执行，我给 recommendation：
    接受本次 revalidation 后可将 challenged → candidate；建议先清 RES-2（guard 层旧语义残留）
    再定稿，或至少在落地 v1.1.0 时一并处理。
  explicitly_not_recommended:
    - 任何 upward 到 partially_verified 及以上的动作（作者升级上限 candidate，仅 GPT 可再升）
    - 对 pedagogical_validation 的任何改动（保持 untested）

confidence_limits:
  checked:
    - 四条 blocker 修复的数学/路由逐条独立复算（sympy + router 推演）
    - 全文件 grep 旧语义残词（直接落/只含 reducible/齐次部分/旧 terminal_when/恒真 等）
    - lint 独立复跑（error 0 · warning 4）
    - R1/R2 双向一致性、C1 状态一致性
  not_checked:
    - F1–F5、F8 的数学推导（非本次修复范围）
    - 2024–2026 三题仅 papers/ 单源，未做双源比对（同原审计）
    - teaching_policy 一节（不在复核范围）
    - 未读 solutions/
  known_weakness:
    - RES-1/RES-3 依赖「2006-18 是欧拉形」的判别（乘 u² 后 a=1,b=0），我已符号验证，
      但若 integrator 认为本族「欧拉形」默认排除 b=0 退化情形，则措辞严重性下降
      ——不影响路由结果，只影响要不要改那两句。
    - 本次复核的是未提交工作区 diff；若 integrator 在定稿前再次改动，本报告结论
      以「当前工作区」为准，需重新比对。
```

## 核心结论（返回给 integrator）

- **BL-1 · confirmed_fixed**：缺项改为并行候选后，2017-10 → B1 可达、2006-18 → B3 与 B4 并存；R2 双向一致（lint error 0）。
- **BL-2 · confirmed_fixed**：A6/B7/B8 的 action_ref 全部指向真实 action，2009-10/2012-9/齐次通解语义正确；terminal_when 收窄未误伤「只问 p、q/方程」的设问。
- **BL-3 · confirmed_fixed**：新 F6 witness 符号验证成立（y₁/y₂ 残差 0、y₃ 残差非 0），「齐次部分」已全清，A6 guard 已补「两解代回恒真」。
- **BL-4 · confirmed_fixed**：guard 11 补「差张成二维」后充分（Wronskian −2 例）且原反例（差一维例）仍不定全；F7/CN2/focused_check 三处同步，无遗漏。
- **lint**：error 0 · warning 4（全部在冻结的 extrema，基线不变，非 ODE 引入）。
- **新问题**：无 B1–B4；4 处 wording/标注残留（RES-1..4，见报告），其中 **guard 12 的 check「缺项直接进可降阶格」是修复后唯一残留的旧排他语义**，建议定稿前清掉；RES-1（「2006-18 即此类」误标欧拉形为非欧拉形）与 RES-3（§0.1 称欧拉不适用 2006-18）同源误标；RES-4 为版本号标注（v1.0.1 vs 待定 v1.1.0）。
- **状态建议（仅 recommendation）**：四条 blocker 已全部确认修复，可考虑 challenged → candidate（撤销 quarantine），由 integrator 依权限执行；建议先清 RES-2 再定稿。
