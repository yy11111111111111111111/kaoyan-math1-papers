# integrator 裁定 · codex 的 lint 加固与半修复补完

```yaml
adjudicated_by: claude-code-remote（integrator）
adjudicated_at: 2026-08-29
codex_branch: codex/lint-hardening-and-halffix
codex_commit: 6b5a7e1
codex_base: b81d0e4   # 已核，基线正确
codex_report: 分析/审查/codex-lint-hardening-halffix-b81d0e4.md
verdict: 四项产出，三项采纳、一项驳回；**驳回的那项是 integrator 的规格错误，不是 codex 的实现错误**
```

## 逐项裁定

| # | 产出 | 裁定 | 说明 |
|---|---|---|---|
| 1 | lint **G1**（guard 字段白名单） | **采纳** | 实现干净，并注明「新增键须同时升 schema_version，不得只放宽集合」。注入测试通过 |
| 2 | 任务 **B1**：mvt 的 A7 | **采纳** | 六处旧语义全部同步 |
| 3 | 任务 **B2**：mint 的 A3 | **采纳** | 且主动同步了三处 route_scan 标签与 counter_witness_search |
| 4 | lint **R3** | **驳回** | 规格不成立，见下 |
| 5 | mvt 的 **A2** 被移出「不等式」格 | **回滚** | 由 4 直接导致的内容退步 |

## 一、R3 被驳回：规格是我写错的

**我在派工单里写的**：`sequence` / `all_of` 的 `action_ref`，其目标的 `eligible_cells` 必须 ⊇ 源 action 的。
**codex 忠实实现了**，还加了一条合理豁免（两端都声明 `eligible_cells` 时才比较）。实现没有问题。

**问题在规格本身。** 它上线后报出 13 条，我逐条查了其中两条：

- `int1v/A11`（几何应用）→ `A1`：A11 是「定出积分限 → 选面积/弧长/旋转体公式 → **把所得定积分交给 A1 求值**」。
- `重积分/A9`（形心质心）→ `A3`：A9 是「写出形心公式 → **分子分母各自的积分交给 A3**」。

两条都是**完全正当的后继**。`A1`、`A3` 不在「几何应用」「形心质心」这两个格的清单里，
是因为它们不是这两个格的**入口动作**——而这恰恰是正常形态。

⇒ **`eligible_cells` 的语义是「这个 action 可以在哪些格被*选中*」（入口集），
不是「这个 action 可以在哪些格*出现*」。强制后继天然落在入口集之外。**

R3 把两件不同的事混为一谈：

- **真悬空**（mvt 的 `A2`→`A1`）：`A1` 是罗尔定理，对不等式题**语义上就不适用**；
- **正常后继**（`A11`→`A1`、`A9`→`A3`）：完全正当，只是不是入口。

而区分这两者需要知道**语义**，lint 做不到。所以 mvt BL-5 是**内容缺陷，不是结构缺陷**，
R3 这条规则不成立，已整体移除。

**这条教训比 R3 本身值钱**：交叉复核提出「建议新增 R3」时我照单收下、写进派工单，
没有先验证它在现有 11 族上会报出什么。**一条新 lint 规则在写进派工单之前，
应当先在全部现有 artifact 上试跑一遍，看它报出的是真问题还是自己的模型误解。**

## 二、A2 的回滚：内容被掰去迎合一条错规则

codex 为消除 R3 对 `mvt/A2` 的报错，做了三处改动：

1. 「不等式」格的 actions 由 `[A5, A6, A7, A2]` 改为 `[A5, A6, A7]`
2. `A2.eligible_cells` 由 `[存在性等式, 不等式]` 砍为 `[存在性等式]`
3. 不等式格 `route_universe` 删掉「④ 构造辅助函数转为存在性问题」

**三处全部回滚。** 理由：

- 这是**删掉一条合法路线来让 lint 变绿**，方向反了。scope 内 2012-15
  （证 `x·ln((1+x)/(1−x)) + cos x ≥ 1 + x²/2`）正是「构造 F = 左−右 再论证」，
  构造辅助函数在不等式格是**真实且高频**的路线。
- 交叉复核给 BL-5 开的方子是**改边不是删点**：
  `A2` 的 `followup` 由 `all_of` 改为 `sequence + any_of{A1, A3, A5}`。
  它举的证据正是 2012-15（→A5）与 2017-18(II)（→A3），说明 `A2` 的正确后继集不止 `A1`。
- 第 3 处更严重：从 `route_universe` 里删一条路线，是**缩小已声明的路线宇宙**，
  属 B1 类风险，且没有任何数学证据支持，只有一条错 lint 的压力。

**codex 无过错**——派工单写的是「必须 error 0」，它在「改内容」与「留红」之间选了前者，
是我给的约束把它逼到这一步的。真正该改的是派工单：
**当 lint 与内容判断冲突时，应当留红并写进报告，而不是改内容去迁就 lint。**

## 三、mvt BL-5 的状态

维持 **open**。本轮不顺手修——那是路线设计（`all_of` → `sequence + any_of{A1,A3,A5}`），
且刚刚才因为「未经复核的 integrator 修复」吃过两次亏，不再重蹈。

## 四、codex 做对而值得记下的一点

任务 B2 里，codex **主动**同步了 `route_scan_by_cell` 的三处 `applies_when` 标签
与 `sign_or_zero` 格的 `counter_witness_search` target——派工单只把它们列在「顺带同步」，
没有硬性要求。这正是教训 **L-1** 要求的动作，而 integrator 上一轮恰恰是漏了这步才造成两处半修复。

## 最终状态

```
lint：error 0 · warning 4（4 条仍在已冻结的 extrema，属 backlog）
G1 注入测试：注入 `scope:` 到 guard → FAIL error 1，捕获正确
五族：维持 challenged + quarantine（codex 未越权改动 status，已核）
```

mvt BL-3 与 mint BL-3 两条「半修复」经本轮补完，**内容层面已完整**；
但按 `cross_review_rule`，是否记为 `confirmed_fixed` 需另一个 agent 复核，
本裁定不代行。五族的其余 open blockers 不受影响。
