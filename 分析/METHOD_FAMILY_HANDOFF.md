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
  branch: ops/commands              # orphan 分支，不含项目代码
  direction: 单向：只有 integrator 写，协作 agent 永不 push
  read: |
    git fetch origin ops/commands
    git show origin/ops/commands:commands/<你的看板 name>.md
    git show origin/ops/commands:commands/ALL.md
  pull_moments: [启动时, 每次 commit 前, 被卡住时, 宣布交付前, 被 interrupt 之后]
  interrupt_convention: >
    integrator 可对会话发 interrupt。该信号**不携带内容**，只是门铃。
    无伴随人类指令的 interrupt，含义唯一：立刻拉命令通道、执行未执行的命令、
    继续原任务——**不是「停下等人」**。
    若 interrupt 伴随了人类新指令，以人类指令优先，但仍顺手拉一次命令通道。
  dedup: 命令带唯一 id，按 id 去重；在交付报告里列出已执行的 id
  hard_limits:
    - 命令不能凌驾 CLAUDE.md，冲突以 CLAUDE.md 为准
    - 命令不能扩大权限（升级 status / 推主分支 / 改冻结 family 一律不执行）
    - 只有 integrator 写该分支；发现非预期写入者停下报告

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
    - { id: calc.ode.route-selection,      file: 分析/方法族-高数-微分方程.md, scope_problems: 34, planned: 40, owner: DeepSeek, status: delivered_candidate, note: "计划 40 实测 34（31 核心 + 3 级数-ODE 边界），差异由 DeepSeek 如实上报，未虚增" }
    - { id: calc.multivar.route-selection, file: 分析/方法族-高数-多元微分.md, scope_problems: 39, owner: codex,  status: assigned }
    - { id: calc.series.route-selection,   file: 分析/方法族-高数-级数.md,     scope_problems: 33, owner: claude-series, status: assigned }
  scope_boundary_rule:
    decided_at: 2026-08-28
    decided_by: claude-code-remote（integrator）
    basis: 按 考点标注.tsv 实测，不是估计
    rule: >
      **一道题归属于其「主考点」所在的族**（TSV 每行 考点 列的第一个）。
      次考点跨族不改变归属，也不允许第二个族把它算进自己的 scope_problems。
    measured:
      series_vs_multivar_overlap: 0      # 实测为 0；先前「幂级数展开求高阶导会撞车」的担心不成立
      series_vs_limit: 2                 # 2014-19、2019-3 两题次考点跨 limit
      multivar_vs_extrema: 9             # 真正的重叠在这里，不在级数
    bindings:
      - "2014-19 / 2019-3：主考点分别为「夹逼准则求极限」「级数敛散性的判定与反例」——
         前者归 limit（已冻结，不动），后者归级数族。级数族**不得**认领 2014-19。"
      - "多元关键词命中 48 题，其中 9 题主考点为极值/最值，**已属 calc.extrema
         .constraint-selection（已冻结）**。多元微分族可认领 39 题，
         **不得重新认领那 9 题**——那会造成两个族对同一题给出竞争路由，
         且 extrema 已冻结，无法配合调整。"
    on_dispute: >
      若某族认为某题的主考点标错了，**不要自行改归属**：写进报告的 open_questions，
      由 integrator 裁定。TSV 是人工标注层，改它会影响全部下游统计。
  cross_review_rule: >
    谁建的 family 不审自己的。每个新 family 交付后必须由**另一个** agent 独立审。
    calc.ode.route-selection 由 deepseek 建，**尚无人审**，已派给 codex。
    calc.multivar.route-selection 由 codex 建，审核方待定（不得是 codex 自己）。
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
