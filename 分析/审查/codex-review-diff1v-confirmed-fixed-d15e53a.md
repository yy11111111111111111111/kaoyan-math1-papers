# 独立复核 · calc.diff1v.route-selection confirmed_fixed

```yaml
reviewer: review-agent-b（独立复核方，未参与修复）
artifact_head: d15e53a
mode: pure_read_only
files_changed: []
lint: PASS · error 0 · warning 4
git_diff_check: PASS
solutions_read: false
papers_2024_2026_read: false
repair_report_read: false
repair_process_or_branch_history_read: false
initial_overall_verdict: partially_fixed
```

## 逐 blocker 结论

| 项 | verdict | 独立依据 |
|---|---|---|
| BL-1 | confirmed_fixed | 新增显式切线 cell；A12 的可执行字段完成“几何条件→斜率→解 f′(x₀)=k→点斜式”，2004-1 遮 note/minimal_probe 后走通 |
| BL-2 | confirmed_fixed | A14 的 applies/followup/terminal 写全区间凸性到弦、切线及割线斜率结论，并在入口排除单点符号外推 |
| BL-3 | confirmed_fixed | A15 分段消参、保留每支 x 范围、转 A1/A5；2023-3 可判一阶连续与二阶不存在 |
| BL-5 | confirmed_fixed | A2 本地处理单侧/绝对值/取整差商，只把 limit scope 内的一般极限外送；未要求改 frozen limit 族 |

R1/R2、status 未被修复方改动、lint 基线、合法 route/excluded candidate 无不当消失均通过。
`minimal_probe` 完全遮去后四条路线仍可执行。

## 首轮未通过项 D-1

复核发现 B4 状态一致性问题：六个旧 cell 标 `complete_within_declared_universe`，
但 `no_direct_blocker_open` 仍为 false；新增 `explicit_tangent_normal` 又缺 status；
族级 `route_scan_status` 仍为 open。故首轮总体只能 `partially_fixed`，不得直接升 candidate。

复核处方：给新 cell 补 `status: complete_within_declared_universe`，七格
`no_direct_blocker_open: true`，族级 scan 改 complete；随后 bump `doc_version`，追加
confirmed_fixed status history，恢复 candidate 并解除 quarantine，再跑 lint/diff check。

## 附审：mvt A5

`when: 存在有限阶 n 使 F^(n) 可定号` 把事后存在性断言当作入口，判
`not_fixed`（B4 executable-semantics）。`F=sin x` 在 `(0,2π)` 上展示无终止搜索风险。

处方：首次调用声明来源明确的有限预算 N；每层显式计算下一阶并检查当前可观察条件；
只在 `k<N` 且下一层入口当前成立时递归；达到 N 必须在 followup 内非终结退出，
条件匹配时转 A7/A6，否则返回上层 router。同步 A5 applies、N1、counter target 与 fallback。

## status recommendation（首轮）

diff1v 在 D-1 落地前保持 challenged；D-1 机械同步完成且 lint/diff check 通过后可恢复 candidate。
mvt 的 A5 处方须落地并复核，不能用原 candidate 结论掩盖本次新发现。

## confidence limits

缺少《00_数学教学_启动入口.md》，无法执行其中的动作路由；未读任何 papers、solutions、
修复报告或修复分支历史。`global_exhaustiveness: not_established` 仍为常设限制。

