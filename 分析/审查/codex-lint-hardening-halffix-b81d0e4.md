# Codex 交付报告 · lint-hardening-halffix · b81d0e4

```yaml
executor: codex
base_branch: claude/batch3-parallel-family-audit-ekzi6c
base_head_read: b81d0e4
work_branch: codex/lint-hardening-and-halffix
date: 2026-08-29
task_order: [A, B]
status_changed: false
solutions_read: false
```

## 结论

任务 A 与任务 B 已按顺序完成。五个 batch3 族的当前状态均未改动，机器核对仍为
`challenged + quarantine`。

R3 上线后首轮共报 14 条 error，包含派工单预期的
`calc.mvt-proof.route-selection/A2`。B1 收口时同步将 A2 从「不等式」格移除：A2 的定义是
构造 `F′(ξ)=0` 并强制后继到 A1（罗尔定理），因此它只在「存在性等式」格可达；
同步修改 `level_2_candidates` 与 `eligible_cells`后，R2 与 R3 一致，该条 R3 已消失。

## 任务 A

### A1 · guard 字段白名单

对当前 11 族的 `selection_rule.guards` 实际数据统计得到 148 条 guard，键全集为：

```text
condition, logical_role, check, explanation
```

`condition` / `logical_role` / `check` 各出现 148 次，`explanation` 出现 94 次。lint 新增 G1，
任一 guard 含白名单外键即报 error；注释明确约束新键必须与 `schema_version` 升级同步。

注入验收：临时在 `calc.mvt-proof.route-selection/guard#1` 注入 `scope: A3`，得到：

```text
✘ calc.mvt-proof.route-selection/guard#1: 含白名单外字段 ['scope']（G1）
FAIL：error 15 · warning 4
```

随后已移除注入字段，G1 错误消失。

### A2 · R3 mandatory continuation 可达性

新增 R3：对 `followup_actions.mode in {sequence, all_of}` 的每个 `action_ref`，
若源与目标 action 均显式声明 `eligible_cells`，则要求目标集合覆盖源集合。
`any_of` 不受此约束。未显式声明 `eligible_cells` 的 action 沿用 R2 的既有豁免，
R3 不臆造其可用格。

## 任务 B

### B1 · mvt/A7 余项定号或取界

- `description` 改为「余项定号或一致取界」。
- `followup_actions` 改为 `any_of` 两支：定号支定不等号方向；取界支用三角不等式逐项放缩。
- `terminal_when` 拆为两条，`remainder_note` 同步为「定号或统一界」。
- B4 的 `changed_condition` 原样保留；仅改 witness 结论，明确 B4 只打掉「变号时仍定方向」，
  不打掉绝对值取界支。
- `route_universe` / `existing_routes` / `counter_witness_search` 的旧「只能定号」口径已同步。
- 2024-19(1) 可走 A7 取界支：两个余项分别取绝对值，再代入 `|f″|≤1` 的统一界。
- 为收口预期 R3，同步修正 A2 的格可达性，不再将其列入「不等式」格。

### B2 · multiple-integral/A3 轮换入口

- `description` 改为「奇偶性配对或坐标轮换」。
- `applies_when` 拆成奇偶支与轮换支；轮换支只要求可积且区域在所用坐标置换下不变，
  不要求被积函数有奇偶性。
- `pairing_note`、二重/三重/判零格的 `existing_routes`、以及 `sign_or_zero.counter_witness_search`
  均已同步两支口径。
- 2015-12 的 `x+2y+3z` 虽无奇偶性，但因单纯形区域在坐标置换下不变，现可进入 A3 轮换支。

## R3 新揭示的其他族问题（未改 artifact）

依派工单约束，以下 13 条只记录，未顺手修改：

1. `calc.ode.route-selection/B3 -> B1`：缺 `second_order_linear_variable`。
2. `calc.ode.route-selection/B3 -> B2`：缺 `second_order_linear_variable`。
3. `calc.series.route-selection/N1 -> D1`：缺 `numeric_sum`。
4. `calc.series.route-selection/N1 -> G1`：缺 `numeric_sum`。
5. `calc.series.route-selection/N1 -> G2`：缺 `numeric_sum`。
6. `calc.series.route-selection/D1 -> D2`：缺 `coefficient_recursion`。
7. `calc.series.route-selection/X5 -> N2`：缺 `expansion`。
8. `calc.series.route-selection/C2 -> N2`：缺 `coefficient_recursion`。
9. `calc.series.route-selection/C3 -> N2`：缺 `coefficient_recursion`。
10. `calc.series.route-selection/W5 -> W4`：缺 `numeric_sum`。
11. `calc.int1v.route-selection/A11 -> A1`：缺「几何应用」。
12. `calc.multiple-integral.route-selection/A4 -> A1`：缺「三重求值」。
13. `calc.multiple-integral.route-selection/A9 -> A3`：缺「形心质心」。

这些条目需要判断是「转换后 cell 改变」、「条件分支被误标 sequence」，还是目标 action
确实缺少格归属；均属内容判断，超出本轮权限。

## 验收记录

```text
base lint:                 PASS  error 0  · warning 4
A1 scope injection:       FAIL  error 15 · warning 4（含 G1）
A 上线后:                FAIL  error 14 · warning 4（含预期 mvt/A2）
B1 后:                    FAIL  error 13 · warning 4（mvt/A2 已消失）
B2 / final lint:          FAIL  error 13 · warning 4
py_compile:               PASS
git diff --check:         PASS
router data assertions:   PASS
```

final lint 未达 `error 0` 的唯一原因是 R3 新揭示的上述 13 条既存跨格后继；
派工单明确要求「逐条记报告，不要顺手改 artifact」，故本轮未将它们硬压或越权修复。
