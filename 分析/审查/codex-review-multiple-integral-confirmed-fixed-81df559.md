# 独立复核报告 · calc.multiple-integral.route-selection

```yaml
reviewer: codex-agent-b-mint-independent-revalidator
artifact_head: 81df559
artifact: 分析/方法族-高数-重积分.md
review_mode: pure_read_only
files_changed: []
lint: PASS · error 0 · warning 4
git_diff_check: PASS
working_tree: clean
solutions_read: false
papers_2024_2026_read: false
repair_reports_or_process_read: false
repair_history_read: false
```

## 总结与逐项 verdict

BL-1、BL-2、BL-3、BL-4 的数学路线均为 `confirmed_fixed`。修复已进入
`level_2_candidates + applies_when + followup_actions + terminal_when`，遮去 note、
description、explanation 与 minimal_probe 后仍可执行。

- **BL-1 `confirmed_fixed`**：2006-8/2015-4 可由正式表示互化入口进入 A10；区域、被积、
  完整面积元齐备后合法终止。2009-2 由 A11 逐块定号后必须形成共同序关系才终止。
- **BL-2 `confirmed_fixed`**：2013-15 可从“二重·求值”进入 A7；先恢复同一区域集合、
  重写新限，再按新次序实际算值。画图仅是 supporting heuristic。
- **BL-4 `confirmed_fixed`**：A3 的关系不足以定值时，二重分流 A1/A2，三重分流
  A4/A5/A6；A5/A6 自足实算，A6 不再 action_ref A4 或伪称投影法。
- **BL-3 `confirmed_fixed`（独立重核）**：2015-12 无需奇偶性；区域在坐标置换下不变即可
  进入 A3 轮换支，得到关系但不足以定值时不终止，继续 A4→A1 实算。遮 note/minimal_probe
  仍完整可达。
- **BL-5/R2 `confirmed_fixed`**：A6 仅属三重求值，R2 当前对本族实际生效且双向一致。

顺带复核：positive mapping 原五处冲突已消除；2024–2026 仅按 TSV/原审计核对且
`evidentiary_weight: none`；B4 witness 的内外层变量已修正；B1 一般交换映射命题
`∬_{σ(D)}f=∬_D f∘σ` 正确；原合法 actions/candidates 未见不当删除。

## 新问题与处方

### NF-B4-1 · direct blocker

七格 `no_direct_blocker_open` 全为 false；五格却为 complete，新增两格缺 status，违反
HANDOFF 的状态规则。因此报告初始建议保持 challenged；若 integrator 采纳本报告，则须原子化：

1. 七格 `no_direct_blocker_open: true`；
2. 七格 `status: complete_within_declared_universe`；
3. `route_scan_status: complete_within_declared_universe`；
4. 追加 challenged→candidate 历史，同步顶层 status、解除 quarantine、bump doc_version。

处方落地后 status recommendation 为 `candidate`。

### NB-1 · non-blocking

centroid route universe 的“唯一结构”与保留帕普斯为合法候选矛盾。处方：改为“当前 scope
内主干结构”等非穷尽措辞，保留帕普斯 `dominated_not_excluded`，不得因效率删除。

## Confidence limits

2004–2023 题面仅作 positive-instance 核对；2024–2026 未开 papers；未读 solutions/、
修复报告/过程/历史。工作区缺少《00_数学教学_启动入口.md》。`global_exhaustiveness`
仍为 `not_established`，七格仅声明 universe 内单轮扫描。

## 处方落地后的定向复核

- HEAD `8b1402d`：NF-B4-1 仍为 `not_fixed`。七格与版本/历史均正确，但当前
  `method_family_rule` 缺 `teaching_use`；B 要求显式落 `teaching_use: normal`。
- HEAD `52f546e`：NF-B4-1 `confirmed_fixed`，`files_changed: []`。当前字段明确为
  `status: candidate` + `teaching_use: normal`，唯一剩余处方完整落地。
