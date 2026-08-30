# 独立复核报告 · calc.int1v.route-selection

```yaml
reviewer: codex 子 agent B（独立复核方；未参与修复）
artifact: 分析/方法族-高数-一元积分学.md
artifact_HEAD: 6b160a1a1f48a981cee797dc4472379e41e2ca93
review_mode: pure_read_only
files_changed: []
lint: "PASS：error 0 · warning 4"
git_diff_check: pass
solutions_read: false
papers_2024_2026_read: false
forbidden_fix_report_read: false
forbidden_commit_history_read: false
```

证据边界：B 只读当前目标族、原始独立审计、`METHOD_FAMILY_HANDOFF.md`、lint
脚本/说明与允许的 2004–2023 四份题面分册；未读修复方报告、过程、分支或提交历史。
工作区未找到 AGENTS.md 所要求的《00_数学教学_启动入口.md》，故无法执行其路由步骤。

## 逐项结论

| 项目 | verdict | 独立复核要点 |
|---|---|---|
| BLK-1 图形/几何直读 | `confirmed_fixed` | A12 同时进入变限积分与几何应用格；有向面积、反向变限、累计量、`F'=f` 图形判别均在可执行字段，遮 note/minimal_probe 仍可走通。抽查 2007-3、2017-4、2009-3、2012-10 匹配。 |
| BLK-2 分段原函数 | `confirmed_fixed` | A13 逐段积分保留独立常数，以整体原函数可导推出拼接连续，最后逐段求导核验；2016-2 路线闭环。 |
| BLK-4 mapping | `confirmed_fixed` | 原审计证伪错引已清除；2004–2023 新映射独立抽查匹配。2026-14/20 仅依仓库已有审计/HANDOFF 证据，未开 papers。 |
| BLK-6 scope/证明 | `confirmed_fixed` | 2008-18 由 A14 走非循环差商定义证明；2026-20 由 A15 先形成辅助函数、区间、端点/可导条件、目标导数等式的完整 transformed_problem 才交 mvt。两题仍留在 int1v 主考点 scope。 |

顺带项均为 `confirmed_fixed`：A7 单调性严格条件、A2 定积分换元条件、周期原函数
充要条件及非零周期积分的排除链、retired rule 限定、帕普斯－古尔丁 `out_of_scope`。

Regression 通过：A1–A11 与原合法/排除路线未见不当消失；R2 双向一致；修复方未改
顶层 status/teaching_use/doc_version/history；L-1 全局同步通过。遮去所有 note、description、
explanation、minimal_probe 后，A12–A15 仍能依分格入口、applies_when、typed followup、
terminal_when 完成路由。

## 新发现 NF-B4-1 与处方

内容 blocker 均已修复，但六格的 `completion_criteria.no_direct_blocker_open` 仍为 false；
五格声称 `complete_within_declared_universe`、proof 格缺 status，同时全局 route scan 仍 open，
三层状态矛盾。B 将其定为 direct blocker，当前建议暂留 challenged。

B 的字段级处方：六格 `no_direct_blocker_open` 全改 true；六格均明确
`status: complete_within_declared_universe`；全局 `evidence.route_scan_status` 同步为
`complete_within_declared_universe`；然后由 integrator bump 版本、追加历史、解除 quarantine、
恢复 candidate。处方完成后 status recommendation 为 `candidate`。

## Confidence limits

BLK-1/2、2004–2023 mapping、2008-18、顺带项、regression 与新状态 blocker 为 high；
2026-14/20 为 medium。未读 solutions/ 与 2024–2026 papers；图形题依题面库 linked figure
与 OCR 题干；`global_exhaustiveness: not_established` 为常设状态，不构成 blocker。

