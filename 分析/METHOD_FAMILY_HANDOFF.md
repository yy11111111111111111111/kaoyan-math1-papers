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
  lifecycle: all_families_built     # 五族全部建成；均为 candidate，均未独立审查
  completed_at: 2026-08-28
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
    **batch3 五族均为 candidate 且均未经独立审查**——建族方同时是 integrator，
    独立性弱。这是当前最大的结构性缺口。

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
