# METHOD_FAMILY_HANDOFF

**这份文件的唯一作用**：让一个没有任何聊天上下文的模型，只读
`HANDOFF + 当前 artifact + tests` 就能恢复当前任务并继续。
不复制历史对话。字段以本文件为准；与聊天记忆冲突时，以本文件与 artifact 的
frontmatter 为准。

```yaml
repository: yy11111111111111111111/kaoyan-math1-papers
branch: claude/postgraduate-math-exam-analysis-czoi3t
head_at_last_content_commit: 见分支 tip（本轮合入两个 deepseek 分支后已前移）
# ↑ 指「最近一次改动内容的提交」，不是分支 tip。
#   一个文件无法引用包含它自身修改的那个 commit，硬要对齐就得每次追加一个
#   回填提交，而回填提交本身又让字段落后一位——此前几轮正是这样漂移的。
#   分支 tip 请用 `git rev-parse --short HEAD` 现取，不要以本字段为准。

active_batch: calc.method-families.batch1
artifact: 分析/方法族-高数-第一批.md
schema_version: CALC-METHOD-FAMILY-v1.3.1

family_status:
  limit:
    family_id: calc.limit.method-selection
    status: partially_verified
    frozen: true
  vector:
    family_id: calc.vector-integral.route-selection
    status: candidate
    frozen: false          # 当前唯一 active family
  extrema:
    family_id: calc.extrema.constraint-selection
    status: candidate
    frozen: true
  pedagogical_validation:
    all_families: untested

frozen:
  families: [calc.limit.method-selection, calc.extrema.constraint-selection]
  meaning: >
    不得主动修改。只有 open_blockers 里定义的四类 direct blocker
    才允许 reopen；backlog 项一律不允许。

active_task:
  family: calc.vector-integral.route-selection
  remaining_cells: []            # 四格已全部扫完（v3.5.0）
  state: closed
  protocol: 见本文件「cell scan 协议」一节

next_tasks:
  - Batch 1 已 CLOSED（2026-08-28）。用户决定不再交 GPT 审核，
    按停止规则 vector 保持 candidate、批次关闭。
  - 后续工作转入 Batch 2（新 family），见 batch2_plan

permissions:
  upward_status_change: GPT_only      # candidate → partially_verified 等
  downgrade_on_direct_counter_witness: allowed
  author_upgrade_ceiling: candidate   # Claude / DeepSeek 自主产出上限
  deepseek:
    may_edit_main_artifact: false     # 除非 Claude 显式委派独立文件/独立 patch
    may_change_status: false          # 只能 recommendation
    may_push_to_working_branch: false # 需独立 branch，由 Claude cherry-pick

stop_rule: >
  三格扫完即结束 Batch 1。GPT 最终审核无论判 partially_verified 还是
  remain candidate，只要没有 direct blocker，Batch 1 都必须 CLOSED。
  **不得因为「还能更完善」继续产生新版本。**

open_blockers: []        # 当前无 direct blocker
direct_blocker_definition:
  B1_scope_internal_route_miss: >
    scope 内存在具体题目，使现有 router 无任何合法 action 接收，
    或遗漏一个决定答案的合法候选分支。须给出具体数学构造。
  B2_direct_counter_witness: >
    明确反例直接击穿 guard / mechanism / applicability /
    branch condition / terminal 或 follow-up 语义。须给出完整数学验证。
  B3_schema_expressivity_blocker: >
    v1.3.1 schema 无法在不歪曲数学关系的前提下表达某个真实 route composition。
    「写起来不漂亮」「字段啰嗦」不算。
  B4_semantic_provenance_or_status_error: >
    跨文件状态不一致、action_ref 指向不存在的 action、
    mandatory continuation 可悬空、现行规则实际写的是旧语义、
    provenance 把未验证来源升成 verified。

backlog_non_blockers:
  # 以下一律 record_to_backlog / reopen_family: false
  - preference_rule 还不够细（已知：extrema A8、vector A6 子路线粒度）
  - wording 可以更漂亮
  - 可以再找一个更好的反例
  - 可以再加 teaching note
  - global_exhaustiveness = not_established（这是常设状态，不是缺陷）
  - 某条 route 在 2004–2026 真题中没出现过
  - 某个 open item 还可以一般化（已知：vector F2b 类的一般判据）
  - local_operation 的执行顺序还可以优化
  - schema 可以更抽象
  - 可以增加更多 adversarial examples / 数值验证
  - 非关键字段命名还能统一
  - 未扫 cell 之外的 S3 typing 欠账（按协议随各自 cell scan 迁移，不批量重构）

command_channel:
  branch: ops/commands
  status: deprioritized        # 保留内容，取消强制轮询
  read_when: [有人明确要求, 被卡住时]
  note: >
    interrupt 实测只能停不能唤醒，「门铃」方案不成立，已撤销。
    保留分支是因为在飞的会话已被告知去读它，删除会让它们 fetch 到不存在的分支。
    **不再对该通道追加投入。**协调仍以 分析/协作/看板.md 与各自的交付报告为主。
  hard_limits: [不能凌驾 CLAUDE.md, 不能扩大权限, 只有 integrator 可写]

required_read_order:
  1: CLAUDE.md                        # 唯一规则来源；papers/ 与 solutions/ 的红线
  2: 分析/METHOD_FAMILY_HANDOFF.md    # 本文件
  3: 分析/10_高等数学_资料与覆盖索引.md  # claim labeling 四字段、状态权限表
  4: 分析/方法族-高数-第一批.md         # artifact 本体；frontmatter 为状态权威
  5: 分析/协作/看板.md              # 跨机器协调总线；开工前读，收工后更新自己那一行
  5.1: 分析/tests/README.md
  6: 分析/tests/lint_method_families.py

do_not_before_batch1_closed:
  - 新建 ODE / series / 线代 / 概率 family
  - 重新设计 schema
  - 做教学效果实验
  - 回头优化 limit 或 extrema
  - 批量重构全文件的 follow-up typing
```

---

## cell scan 协议（三格统一）

**口径**：route scan 回答的是「在声明的 route universe 内，有没有漏掉**结构上合法**的
路线」，不是「历年真题主要用了哪些解法」。
历史出现过 ≠ 自动进入；历史没出现过 ≠ 可以排除；frequency 不参与 route legality。
真题只作 positive-instance / source mapping，**不能反过来定义 route**。

每格必须先声明 `cell_id / scope / route_universe / search_budget / stop_rule`。
`route_universe` 限于「当前考研数学一 scope、当前 carrier·kind·ambient 组合下，
数学合法且现实可执行」的路线类型——不得为了「穷尽」硬塞超考纲方法、研究级技巧
或不属于当前对象类型的 route。

固定八步：

| # | 步骤 | 硬要求 |
|---|---|---|
| 1 | 迁移本 cell 可达子图的 S3 typing | 只迁可达子图，不迁全文件；本 cell warning 归零才能开扫 |
| 2 | 枚举现有 route | route_id / action / mechanism / applies_when / failure_boundary |
| 3 | 独立生成可能遗漏路线 | **先不看真题主解**；至少覆盖十个 adversarial 角度（见下） |
| 4 | 与现有候选集做差集 | 排除须注明 `out_of_scope / duplicate_mechanism / invalid / dominated_not_excluded` |
| 5 | guard audit | 严格区分 `necessary / sufficient / supporting_heuristic`；效率偏好不得写成合法性条件 |
| 6 | failure boundary | 四种 effect 不得混写：`invalidates / loses_advantage / becomes_inconclusive / changes_branch` |
| 7 | counter-witness search | 找到写 `verification: verified` 并给推导；没找到只能写 `search_result: not_found`，**不得写 `no_counterexample_exists`** |
| 8 | 真题映射 | 最后才做；`evidentiary_weight` 受题面库 `source_status` 限制 |

第 3 步的 adversarial 角度：direct parameterization / projection、symmetry、
theorem transformation、closure / supplement、singularity handling、
representation conversion、potential / conservative structure、
degeneracy / constant integrand、coordinate simplification、special construction。

**`dominated_not_excluded` 不能删除**——效率低 ≠ 非合法路线。

### cell 完成标准

11 项全 true 才可写 `cell_status: complete_within_declared_universe`；
任一项 false 则 `cell_status: open`：

```yaml
completion_criteria:
  - route_universe_declared
  - reachable_S3_typing_complete
  - current_routes_enumerated
  - independent_route_generation_done
  - legality_guards_checked
  - necessary_sufficient_heuristic_roles_checked
  - key_failure_boundaries_checked
  - counter_witness_search_done
  - source_mapping_done
  - open_items_explicit
  - no_direct_blocker_open
```

禁止用词：`unique` / `exhaustive` / `all possible routes` /
`globally saturated` / `globally_exhaustive`。

---

## 当前进度

```yaml
cells:
  first_kind:                { status: scanned_v3, note: "产出 A1p、A9，并更正 A7 为单向" }
  surface_second_kind:       { status: complete_within_declared_universe, scanned_at: v3.4.0 }
  planar_curve_second_kind:  { status: complete_within_declared_universe, scanned_at: v3.5.0 }
  spatial_curve_second_kind: { status: complete_within_declared_universe, scanned_at: v3.5.0 }

vector_route_scan_status: complete_within_declared_universe
global_exhaustiveness: not_established     # 常设状态，不是缺陷

batch_status:
  lifecycle: closed
  closed_at: 2026-08-28
  vector_final_status: candidate      # 未升级，也未降级
```

```yaml
batch2_plan:
  batch_id: calc.method-families.batch2
  lifecycle: open
  rule: 每个新 family 写入**独立文件**，不改 batch1 的 artifact
  families:
    - { id: calc.ode.route-selection,      file: 分析/方法族-高数-微分方程.md, scope_problems: 24, planned: 40, owner: DeepSeek, status: candidate, note: "v1.0.1 因 Codex 审计 BL-1..4 降 challenged；v1.1.0 修复经 claude 独立复核全部 confirmed_fixed，integrator 恢复 candidate（见 分析/审查/claude-revalidate-ode-fix.md）。scope 依 SB-6 按主考点更正为 24；文件内 §2/evidence 的 count 34（禁用口径）同步为 24 是 integrator 待办" }
    - { id: calc.multivar.route-selection, file: 分析/方法族-高数-多元微分.md, scope_problems: 40, owner: claude（integrator 派出的建族 agent，batch2_plan 原记 codex）, status: candidate, note: "v1.0.0 经独立审查发现 1 blocker（2012-3 B2+B1，D1 误判正确选项为 (A)）降 challenged；integrator 修复（guard#4→(B)、新增 F18、计数同步）后 v1.1.0 复核 confirmed_fixed 恢复 candidate（见 分析/审查/claude-audit-multivar-ee3605c.md）；lint error 0，文件已并入 DOCS" }
    - { id: calc.series.route-selection,   file: 分析/方法族-高数-级数.md,     scope_problems: 29, owner: claude-series, status: delivered_candidate, note: "v1.1.0 经 SB-4 扩写为 29（27 + 2010-3/2016-1）；独立审查 0 blocker，status 保持 candidate（见 分析/审查/claude-audit-series-ee3605c.md）" }
batch3_plan:
  batch_id: calc.method-families.batch3
  lifecycle: four_challenged_one_restored   # 2026-08-29：五族全部经独立审查降 challenged；mvt 已修复并经独立复核恢复 candidate
  completed_at: 2026-08-28
  independently_audited_at: 2026-08-29
  audit_method: >
    integrator 并行派出**五个独立审查 agent**（一族一个，全部只读、不改文件，
    只出 recommendation），补上「建族方同时是 integrator」的结构性缺口。
    integrator 逐条复核后采纳，改动由 integrator 落地。
    五份报告：分析/审查/claude-audit-batch3-{diff1v, int1v, multiple-integral,
    mvt-proof, space-geometry}-a635bd6.md
  audit_outcome:
    calc.diff1v.route-selection:            { status: challenged, blockers: 7, fixed: 2, open: 5 }
    calc.int1v.route-selection:             { status: challenged, blockers: 6, fixed: 2, open: 4 }
    calc.multiple-integral.route-selection: { status: challenged, blockers: 5, fixed: 2, open: 3 }
    calc.mvt-proof.route-selection:         { status: candidate, blockers: 6, fixed: 6, open: 0, note: "**首个走完整条链路的族**：建族 → 独立审查 → 修复（integrator 2 + codex 4）→ 采纳 → 独立复核 confirmed_fixed → 恢复 candidate。见 分析/审查/claude-review-mvt-confirmed-fixed-a29f670.md" }
    calc.space-geometry.route-selection:    { status: challenged, blockers: 5, fixed: 5, open: 0, note: "四条 blocker + 非阻塞的 BL-5 全部由 codex 补完（4bfd8e1），integrator 采纳且**无需补充**。⏳ 待 confirmed_fixed 独立复核后方可恢复 candidate" }
  cross_cutting_finding:
    id: X-1
    class: B4
    title: lint 的 R2 检查对 11 族中的 7 族静默空转
    detail: >
      R2 取 `c.get('cell_id') or CELL_ALIAS.get(c.get('cell'))`，而 CELL_ALIAS 只收录
      batch1 vector 族的四个格名。batch2/batch3 各族用中文 `cell:` 且无 `cell_id`
      ⇒ key 全为 None ⇒ cells 为空 ⇒ `if cells:` 短路 ⇒ **R2 整体跳过**。
      实测生效面：vector / ode / series / multivar 四族；
      空转：limit / extrema / diff1v / int1v / multiple-integral / mvt-proof /
      space-geometry **七族**。
      HANDOFF 此前称「R1 与 R2 是 B4 类的自动化防线，两者均已用注入式测试验证会触发」——
      注入式测试是在 batch1 的文件上做的，因而没暴露这个缺口。
      **「lint error 0」在这七族上此前并不代表 R2 通过。**
    found_by: 三个审查 agent 独立发现（diff1v BL-6 / int1v BLK-5 / multiple-integral BL-5）
    fixed: true
    fix: >
      CELL_ALIAS 补齐 batch3 中格名与 eligible_cells 简称不一致者；
      key 增加回落 `or c.get('cell')`（名称一致的族无需别名）；
      并新增一条 error：level_2_candidates 存在但无一格可解析为 cell key 时报 R2。
    caught_after_fix:   # R2 上线后立刻捞出的三条真实不一致，均已修正
      - calc.diff1v/A12：声明 [参数式, 判形态]，但「判形态」格清单为 [A8,A9,A10,A11] → 删「判形态」
      - calc.int1v/A10：声明含「不定积分与定积分求值」但该格清单无 A10 → 补入该格
      - calc.multiple-integral/A6：自称三重专用却被「二重 · 求值」格列为候选 → 移出二重格
  open_blocker_summary:   # 已复核成立但**未修复**，下一轮的工作面
    B1_route_miss:
      - diff1v BL-1：显式函数的「求切线/法线」无 cell；A12 排除「由斜率反求切点」（2004-1）
      - diff1v BL-2：缺「凸性 ⇒ 弦/切线位置关系」（2014-2、2026-3、2007-5）
      - diff1v BL-3：参数式在 x′(t) **不存在**处无 action；消参有 excluded_candidate 无 action（2023-3）
      - int1v BLK-1：「由图形/几何意义直接读积分值」整族不存在（2007-3、2017-4、2009-3）
      - int1v BLK-2：缺「分段/绝对值拆区间 + 由连续性定各段常数」（2016-2）
      - mint BL-1：设问轴缺「表示互化」与「比较大小」（2006-8、2015-4、2009-2）
      - mint BL-2：「换序作为求值手段」在二重求值格不可达（2013-15）
      - mint BL-4：A3 在三重格无实算出口（2009-12、2010-12、2019-19）
      - ~~mvt BL-1~~ **已补完**（codex e1230df）：A8 扩到存在性等式格，新增 route Q5
      - ~~mvt BL-2~~ **已补完**（codex e1230df）：新增 A11 + boundary B8（witness 经 integrator 复算成立）
      - ~~mvt BL-4~~ **已补完**（codex e1230df）：A5 增自递归边与最小值支，连带同步 guard#5 与 B5
      - geom BL-1：2013-19（母线不在坐标面）无 action 接收
      - geom BL-2：2025-20（绕一般直线旋转）无 action 接收，且 B6 宣布该情形 scope 外
    B2_counter_witness:
      # 2026-08-29 更新：以下两条已由 codex 补完内容（分支 codex/lint-hardening-and-halffix，
      # commit 6b5a7e1），integrator 裁定采纳，见 分析/审查/claude-adjudication-codex-lint-hardening-6b5a7e1.md。
      # 是否记 confirmed_fixed 须由**另一个** agent 复核，本裁定不代行。
      - **mvt BL-3（已补完，待复核）**：guard#4 已改「定号或有界」，但 A7 的 description /
        followup 唯一收尾（「判定该阶导数的符号」）/ terminal_when（「余项定号后」）/
        remainder_note（「必须定号、只能用整体信息」）/ B4 结论句 / counter_witness_search
        **六处**仍是旧语义，router 执行的是 followup 那一侧 ⇒ 2024-19(1) 仍卡死
      - **mint BL-3（已补完，待复核）**：guard#1 已拆出轮换分支，但 A3 的
        applies_when 仍要求「被积函数在相应变换下有确定的奇偶性」⇒ 2015-12 的 x+2y+3z
        无奇偶性，A3 在 router 层进不去，L136 的轮换支仍不可达
      - geom BL-3：A2 的消元结果是投影的**超集**，缺「被消变量实解存在条件」guard
        （反例 {x²+z²=1, y²+z²=1}：消元给 x²=y² 的完整直线，真实投影只有 |x|≤1 的线段）
    B4_semantic:
      - diff1v BL-5：A2/A5 的 continuation 交给 limit 族，而该族 exclusions 明文未纳入该类极限
      - diff1v BL-7：A7 的三个真题引用全错（应为 2005-1/2007-2/2012-1/2014-1/2023-1）
      - int1v BLK-4：13 个题号引用中至少 9 个不符
      - int1v BLK-6：scope 与 exclusions 自相矛盾，2026-20/2008-18 在九族中无家
      - mint NB-1：10 条引用中 5 条与 TSV 冲突
      - ~~mvt BL-5~~ **已补完**（codex e1230df）：all_of → sequence + any_of{A1,A3,A5}（改边而非删点）
      - mvt NB-1：4 条 mapping 中 3 条与题面不符
      - geom BL-4(b)：2013-19/2025-20 挂 A1，与 A1.applies_when、guard#7、B6 三处矛盾
    共通: 五族的 scan_basis 都引用了不存在的 `高数真题题面_2004-2023.md`（**已全部修复**）
  cross_review_of_integrator_fixes:
    reviewed_at: 2026-08-29
    head_reviewed: 23800a1
    why: >
      五族的独立审查补上了「建族方兼 integrator」的缺口，但 integrator 依据五份报告
      落的 10 处修复**又没有任何人看过**——缺口只是平移到了「修复方兼 integrator」。
      故派三个仍有上下文的审查 agent 交叉派单：每人审自己**没审过**的族。
    report: 分析/审查/claude-crossreview-batch3-integrator-fixes-23800a1.md
    outcome:
      confirmed_fixed: 6
      改判为未修复: 2   # mvt BL-3、mint BL-3 —— 只改 guard 文本，未改决定可用性的字段
      integrator 自引入的新问题: 1   # guard 层的 `scope:` 字段，v1.3.1 无此字段，已删
      integrator 对用户的不准确陈述: 1   # R2 覆盖面实为 9/11 非 11/11，已更正
    lesson_L3:
      id: L-3
      title: 结论必须落在**可执行字段**，note 只能复述、不得独家承载
      rule: >
        任何「该怎么做」的结论，必须写进 **可执行字段**——
        `followup_actions` 的 `local_operation` / `action_ref`、`applies_when`、`terminal_when`。
        `note` / `explanation` / `description` / `remainder_note` 只能**复述**它，
        **不得独家承载**。验收方式：读一条 route 时**只看可执行字段**，看能不能走通。
      why: >
        这是同一个病灶的第三次发作，每次都是靠人读出来的，没有任何 lint 能查：
        ① batch3 五族最初被判有罪的罪名之一就是「guard 与 action 不同步」；
        ② integrator 的两处半修复（mvt guard#4 / mint guard#1）——改了 guard 文本，
           没改 followup / applies_when / terminal_when，原 blocker 实际未解除；
        ③ codex 第二轮的 A8——`insufficiency_note` 写了「把待证式移到一边得 G」，
           而 A8 的两条 `local_operation` 里没有这一步；它自己的路由图却依赖这一步。
      applies_to: 建族方、修复方、复核方三方；派工单须逐字带上本条

    lesson:
      id: L-1
      rule: >
        **改一条 guard ⇒ 必须 grep 该结论在 failure_boundary / action 的 local_operation /
        minimal_probe / route_scan 标签 四个位置的全部出现点。**
        这四处目前没有任何 lint 项覆盖（R1/R2 只查 action_ref 与 eligible_cells），
        而 batch3 五族最初被判有罪的罪名之一就是「guard 与 action 不同步」——
        integrator 的修复重犯了同一条。建议固化为收口步骤。
    r2_coverage_corrected:
      active: 9        # vector, ode, series, multivar, diff1v, int1v, multiple-integral, mvt-proof, space-geometry
      inactive: 2      # limit, extrema —— 既无 level_2_candidates 也无 eligible_cells，属「无可查」而非「已查」
      note: 此前记「修复后全覆盖」不准确
    additional_lint_fix:
      id: X-1b
      title: R2 的静默通道原只堵了一半
      detail: >
        新增的 error 以 level_2_candidates **非空**为触发前提；该块整体缺失而
        action 仍声明 eligible_cells 时，R2 照旧静默跳过（注入测试 t2 实测 PASS error 0）。
        已补反方向守卫，并复跑 t2 验证会触发（FAIL error 1），确认非死代码。

  new_lint_rule_proposed:
    id: R3
    rule: >
      mandatory followup（sequence / all_of 中的 action_ref）其目标的 eligible_cells
      必须覆盖源 action 的全部 eligible_cells。
    rationale: R1 只查存在性、R2 只查单个 action 与格的一致性，都查不出 mvt BL-5 类的悬空。
    status: **已实现并驳回（2026-08-29）**
    verdict: >
      规格不成立，已整体移除。codex 忠实实现后在现有 11 族上报出 13 条，
      逐条查证发现多数是误报：`eligible_cells` 的语义是「该 action 可在哪些格**被选中**」
      （入口集），而**强制后继天然落在入口集之外**——
      int1v/A11（几何应用）→A1「把所得定积分交给 A1 求值」、
      重积分/A9（形心质心）→A3「分子分母各自的积分交给 A3」都是完全正当的后继。
      R3 把「真悬空」（mvt A2→A1，A1 是罗尔定理、对不等式题语义上不适用）
      与「正常后继」混为一谈，而区分二者需要语义，lint 做不到。
      ⇒ **mvt BL-5 是内容缺陷，不是结构缺陷**，不存在能捕获它的结构性 lint 规则。
    lesson:
      id: L-2
      rule: >
        **一条新 lint 规则在写进派工单之前，必须先在全部现有 artifact 上试跑一遍**，
        看它报出的是真问题还是规则自身的模型误解。
        本轮 integrator 把交叉复核的「建议新增 R3」照单收下、直接写进派工单，
        未做这一步，导致执行方按「必须 error 0」的约束去**删改内容迎合错规则**。
      corollary: >
        派工单今后须写明：**当 lint 与内容判断冲突时，留红并写进报告，
        不得改内容去迁就 lint。**
  implemented_lint_rules_2026_08_29:
    G1:
      rule: selection_rule.guards 不得出现 v1.3.1 白名单外的字段（condition / logical_role / check / explanation）
      by: codex
      status: 已合入
      note: >
        直接堵住 integrator 上一轮自己捅的洞——往 guard 里塞了 v1.3.1 不存在的 `scope:`，
        lint 静默通过。注入测试：注入 `scope:` → FAIL error 1，捕获正确。
        实现中注明「新增键须同时升 schema_version，不得只放宽白名单」。
  family_worth_criterion:   # geom 审查方提出、integrator 采纳的可复用判据
    id: C1C2C3
    C1: 至少一个 cell 内存在 ≥2 条都合法且 applies_when 互不包含的 route（选错会**无法完成**而不只是变慢）
    C2: 至少一条 guard 的作用是在 route 之间**择路**，而非只校验单条 route 的参数
    C3: C1 的分叉点在 scope 清单的具体题目上被触发过，而非纯理论构造
    verdict: 三条同时满足 ⇒ 值得建族；否则应降格为 分析/高数方法速查.md 的条目
    todo: 用它回扫已建各族（跨族待办）
  rulings_2026_08_29:
    - id: SB-7
      question: 2025-20 主设问是第二类曲面积分（Gauss 补面法），是否应移出 space-geometry？
      ruling: >
        **驳回，维持归本族。** TSV 实测 2025-20 主考点 = 「旋转曲面的方程」，
        次考点才是「高斯公式补面法」。按 scope_boundary_rule（主考点定归属），
        归本族无误，geom BL-2 不因此消解。
    - id: SB-8
      question: 三道场量题（2016-10/2018-11/2026-11）并入 space-geometry 是否牵强？
      ruling: >
        **归并理由牵强，归并结果保留。** 「路由结构相同（认公式→定参数→代入算）」
        在高数里近乎普适、不可证伪，不构成合并的充分理由；且考纲把散度/旋度列在
        「6. 多元函数积分学」，与空间解析几何（第 4 章）分属两章。
        但 vector 族的 objects 声明为四类积分，三题都不含积分，迁入会破坏该声明。
        **采方案 (ii)**：三题留本族，把家族定位的理由改写为「考纲第 4 章 + 第 6 章的
        场量算子部分，三题不足以单开一族」这一明示跨章的实用理由，
        并在 scope.exclusions 写明分界（含积分 → vector；只求算子 → 本族）。TSV 不动。
  goal: 补完高数剩余 101 题，使高数主考点全覆盖
  rule: 每族独立文件；scope 由**本清单逐题定义**（新规矩，不再用关键词计数）
  measured_at: 2026-08-28
  coverage_before: 高数 287 题中已覆盖 183（batch1 三族 + ODE + 级数 + 多元）
  families:
    - id: calc.diff1v.route-selection
      file: 分析/方法族-高数-一元微分学.md
      count: 33
      problems: [2004-1, 2004-8, 2005-1, 2006-7, 2007-2, 2007-5, 2010-9, 2011-1, 2012-1, 2012-18, 2012-2, 2013-11, 2014-1, 2014-2, 2015-1, 2015-16, 2015-18, 2016-4, 2017-1, 2017-2, 2018-1, 2019-2, 2020-10, 2020-2, 2021-1, 2021-12, 2023-1, 2023-17, 2023-3, 2024-4, 2025-19, 2026-13, 2026-3]
    - id: calc.int1v.route-selection
      file: 分析/方法族-高数-一元积分学.md
      count: 36
      problems: [2004-2, 2005-17, 2005-8, 2007-11, 2007-3, 2008-1, 2008-18, 2009-16, 2009-3, 2010-10, 2010-16, 2010-17, 2011-19, 2011-4, 2011-9, 2012-10, 2012-4, 2013-12, 2014-10, 2014-4, 2015-10, 2016-2, 2016-9, 2017-4, 2018-10, 2018-15, 2018-4, 2019-17, 2019-18, 2021-11, 2023-14, 2024-1, 2025-1, 2025-17, 2026-14, 2026-20]
    - id: calc.multiple-integral.route-selection
      file: 分析/方法族-高数-重积分.md
      count: 16
      problems: [2004-10, 2005-15, 2006-15, 2006-8, 2009-12, 2009-2, 2010-12, 2013-15, 2014-3, 2015-12, 2015-4, 2016-15, 2019-19, 2024-17, 2025-4, 2026-4]
    - id: calc.mvt-proof.route-selection
      file: 分析/方法族-高数-中值定理与证明.md
      count: 8
      problems: [2004-18, 2005-18, 2007-19, 2011-17, 2012-15, 2017-18, 2023-20, 2024-19]
    - id: calc.space-geometry.route-selection
      file: 分析/方法族-高数-空间解析几何与场量.md
      count: 8
      problems: [2006-4, 2009-17, 2013-19, 2016-10, 2017-19, 2018-11, 2025-20, 2026-11]
      note: >
        含 2016-10 / 2018-11 / 2026-11「旋度与散度的计算」。它们不属 vector 族
        （该族 objects 是四类积分），单开三题一族不划算；与解析几何同属
        「认公式 → 代入算」的路由结构，故合并，族名含「场量」。
  out_of_scope:
    - { id: 2007-21, reason: 主考点「齐次与非齐次方程组的公共解」属线性代数 }

高数覆盖收口:
  measured_at: 2026-08-28
  method: 集合直接计算（非关键词相减）
  高数题总数: 282
  batch3_五族: 101   # 权威清单，逐题列于 batch3_plan
  其余: 181          # 主考点全部落在 batch1 三族 + ODE + 级数 + 多元
  不重叠: true       # batch3 清单 ∩ 其余 = ∅，且 batch3 ⊆ 高数
  结论: 高数 282 题的主考点已全部有族归属
  caveat: >
    「有族归属」≠「已被验证」。九个高数族中：
    batch1 三族已 CLOSED（limit partially_verified、vector/extrema candidate）；
    ODE / 级数 / 多元 为 candidate 且经过独立审查；
    **batch3 五族已于 2026-08-29 全部经独立审查（一族一个 agent，五个并行），
    结果全部由 candidate 降为 challenged + quarantine。** 建族方同时是 integrator
    这一结构性缺口已补上；但五族现均处 challenged，恢复 candidate 需先修复
    open_blocker_summary 所列各项，再由**另一个** agent 复核 confirmed_fixed。

  scope_boundary_rule:
    decided_at: 2026-08-28
    revised_at: 2026-08-28   # 三条 scope_problems 全部修正，见 correction 段
    decided_by: claude-code-remote（integrator）
    rule: >
      **一道题归属于其「主考点」所在的族**（TSV 考点列的**第一个**）。
      次考点跨族不改变归属，也不允许第二个族把它计入 scope_problems。
    measured_by_main_tag:      # 按上述规则逐行实测，非关键词命中
      calc.series.route-selection:   29   # 27 主考点 + SB-4 判归 2010-3/2016-1
      calc.multivar.route-selection: 40   # 39 + SB-5 判归 2006-19（齐次函数欧拉定理）
      calc.ode.route-selection:      24   # SB-6 更正：主考点实测 24（ODE 文件 34 为禁用口径；SB-1 所记 28 亦偏大），ODE 文件同步为 integrator 待办
    correction: >
      **此前给出的 33（级数）/ 38（多元）/ 34（微分方程）都是错的。**
      33 与 34 用的是「任一考点列命中关键词」口径——那正是本规则明令禁止用于
      scope_problems 的口径；38 是看板与 batch2_plan 未同步。
      claude-series 与 codex 各自独立发现并拒绝自行对齐，处理正确。
      **SB-6 再更正**：微分方程主考点实测 **24**（非 SB-1 曾记的 28）。
      SB-1 的 28 = 24 + SB-1 四题，把主考点归多元族的题又算了进来。
      ODE 文件 §2/evidence 的 count 34 与 §2 正文同步为 24 是 integrator 待办。
    rulings:
      - id: SB-1
        question: 2006-18 / 2014-17 / 2025-18 / 2026-18 归 ODE 还是多元？
        ruling: >
          **归多元族。**四题主考点均为「多元复合函数的二阶偏导数」，
          实测**不在** ODE 的主考点集合内。ODE 族把它们计进自己的 34 题是越界，
          其真实 scope 为 28。codex 判定正确。
      - id: SB-2
        question: 多元族题数 38（看板）还是 39（batch2_plan）？
        ruling: "**39。**实测即 39；看板的 38 是我方笔误，已改。"
      - id: SB-3
        question: 级数族 scope 33 还是 27？
        ruling: "**27。**claude-series 的逐行核对正确，33 是我方用错口径。"
      - id: SB-4
        question: 2010-3 / 2016-1（主考点「反常积分的敛散性判别」）归哪个族？
        ruling: >
          **归级数族**，其 scope 明确扩写为「级数与反常积分的敛散性判别」。
          理由：二者的判别机制同源（与 ∫1/x^p 或 Σ1/n^p 比阶、比较判别法、
          绝对收敛概念），claude-series 自己也指出与本族 P1 同源；
          为 2 道题单开一族不划算。**级数族 scope 相应扩写为 29（27 + 这两题）。**
          ⚠️ 注意方向相反：瑕点处 p<1 收敛、无穷端 p>1 收敛。
          （此前 SB-4 原文写「已计入上述 27」不准确——27 是排除这两题算出的，
          正确总数 29，见 分析/审查/claude-audit-series-ee3605c.md §scope_checked。）
      - id: SB-5
        question: 2006-19（主考点「齐次函数的欧拉定理」）归多元族还是维持 batch2_plan 的 39？
        ruling: >
          **归多元族，scope = 40。**「齐次函数的欧拉定理」是大纲「多元函数微分学的
          应用」的直接内容（f(tx,ty)=t^λ f(x,y) ⇒ x f_x+y f_y=λ f），TSV 主考点即该标签，
          按 scope_boundary_rule 归属多元族。batch2_plan 的 39 是旧口径遗漏，
          正确为 40。TSV 不调整（下游统计映射由 integrator 负责）。
      - id: SB-6
        question: ODE 族 scope 到底是 28 还是 34？
        ruling: >
          **都错，正确为 24。**按主考点口径逐行实测，ODE 主考点 8 个标签合计
          24 题（一阶线性 5 / 二阶非齐次 2 / 二阶齐次 5 / 变量代换 2 / 可分离 2 /
          几何物理应用 1 / 欧拉 2 / 由解反推 5）。ODE 文件的 34 是「任一考点列命中
          关键词」禁用口径；SB-1 所记 28 = 24 + SB-1 四题（主考点归多元族）也偏大。
          特征方程重根情形 2 题（2004-21/2025-21）主考点是线代，不计入。
          ODE 文件 §2/evidence 同步为 24 是 integrator 待办（不阻塞本批次收口）。
    on_dispute: >
      若某族认为某题主考点标错了，**不要自行改归属**：写进报告的 open_questions，
      由 integrator 裁定。TSV 是人工标注层，改它会影响全部下游统计。

  cross_review_rule: >
    谁建的 family 不审自己的。每个新 family 交付后必须由**另一个** agent 独立审。
    calc.ode.route-selection 由 deepseek 建；Codex 审计（BL-1..4，降 challenged）
    后由 claude 完成 targeted revalidation（修复 confirmed_fixed，恢复 candidate）。
    calc.series.route-selection 由 claude-series 建，已由 claude 独立审查
    （0 blocker，candidate 保持，见 分析/审查/claude-audit-series-ee3605c.md）。
    calc.multivar.route-selection 由 claude 建族 agent 建（batch2_plan 原记 codex），
    已由 claude 独立审查（1 blocker：2012-3 B2+B1，D1 误判正确选项为 (A)）→
    integrator 修复（guard#4→(B)、F18、计数同步）→ 复核 confirmed_fixed，
    v1.1.0 恢复 candidate（见 分析/审查/claude-audit-multivar-ee3605c.md）。
  inherited: [schema CALC-METHOD-FAMILY-v1.3.1, cell scan 八步协议, 11 项完成标准, 四类 direct blocker 定义, author_upgrade_ceiling: candidate]
```

四格产出摘要：

- **surface_second_kind**（v3.4.0）：新增 A1q 分项投影 / A10 载体方程代入 /
  A11 向量势 / A12 同边界换面 / A13 逐点定号；补列漏掉的 A7；
  修 A2→A1p 的不可达边；新增 B7 / B8。
- **planar_curve_second_kind**（v3.5.0）：从 A6 拆出 A6p（换路径），
  并给出 B9（两条半圆周，rot F = 0 且都避开原点，答案差 2π）；
  补列漏掉的 A7 / A10 / A13；修 A10 在本格无合法后继的路由缺陷。
- **spatial_curve_second_kind**（v3.5.0）：新增 A4c（空间补线 + Stokes，
  此前空间开曲线无任何补线 route）；补列漏掉的 A6p / A7 / A10 / A13。
- 三格共同暴露的一类错误：**A7 / A10 / A13 的 applies_when 覆盖某格，
  但该格的 cell 清单漏列**。已加 lint R2 双向校验防复发。

---

## 验证

```bash
python3 分析/tests/lint_method_families.py   # 必须 error 0
git diff --check
```

lint 检查项：S1 terminal_when 必存在 · S2 optional_any_of 必带 on_skip ·
S3 followup 必标 kind · T1 never_terminal 不得有非空 terminal_when ·
**R1 action_ref 必须指向真实存在的 action** · **R2 eligible_cells 与
level_2_candidates 清单双向一致** · D1 YAML 重复键 ·
C1 frontmatter status_summary 与正文 status 一致 ·
C2 freeze_status 与正文 frozen 双向一致 · V 废弃字段 · E evidence 索引 ·
P pedagogical_validation 必须 untested · 语义残留正则。

R1 与 R2 是 B4 类（语义级 status / provenance 错误）的自动化防线，
两者均已用注入式测试验证会触发。

当前 `error 0 · warning 4`。4 条 warning 全部在**已冻结的 extrema**
（A2 / A3 / A5 / A7 的 S3 typing 欠账），属 backlog，不构成 reopen 理由。
**vector 族的 S3 warning 已归零。**
