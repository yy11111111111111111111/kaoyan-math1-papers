# integrator 裁定 · codex 第二轮：中值定理族路线补全

```yaml
adjudicated_by: claude-code-remote（integrator）
adjudicated_at: 2026-08-29
codex_branch: codex/mvt-route-completion
codex_commit: e1230df
codex_base: d138313        # 已核，基线正确，与其自报一致
codex_report: 分析/审查/codex-mvt-route-completion-d138313.md
verdict: 四条 blocker 全部采纳；integrator 另补两处小缺口
lint: error 0 · warning 4（未出现需留红的误报，与 codex 自报一致）
```

## 合规性核查

| 项 | 结果 |
|---|---|
| 基线 | 基于 `d138313` ✓（自报与实测一致） |
| 文件范围 | 只动了 mvt 一族 + 自己的报告 + 看板行 ✓ |
| `status` | 未触及，维持 `challenged` + `teaching_use: quarantine` ✓ |
| `cell_status` | **未自行改动** ✓（派工单保留给复核方） |
| `no_direct_blocker_open` | 四格由 false → true。四条 blocker 确已补完，改动**成立** |
| 上轮错误是否重犯 | **未重犯**。BL-5 用的是「改边」（`all_of` → `sequence + any_of{A1,A3,A5}`），而不是上轮那种「把 A2 移出不等式格」 |

## 四条 blocker 的裁定

### BL-1 · 采纳
`A8` 扩到存在性等式格（`eligible_cells: [存在性等式, 实根个数]`，两个格清单同步），
`terminal_when` 扩写，`insufficiency_note` 按格拆开（存在性格可直接 terminal；实根个数格仍须配 A9）。
新增 route `Q5` 进 `route_universe` 与 `existing_routes`，`stop_rule` 由「四类」改「五类」。

### BL-2 · 采纳
新增 **A11**（逐点估计 + 积分保序），`eligible_cells: [不等式]`，格清单同步。
自带 `order_note` 与新 boundary **B8**。
B8 的 witness 经 integrator 独立复算成立：`G(x)=x−1/2` 于 `[0,1]`，
`∫₀¹G = 0`（实测 0.0000000000）而 `∫₀¹|G| = 1/4`（实测 0.2500000000）
⇒ `|∫G| = ∫|G|` 确非恒等，只能用 `≤`。

### BL-4 · 采纳
`A5` 增自递归边（`action_ref: A5`，带 `when`）与「最小值支」，`applies_when` 放宽，
`terminal_when` 拆两支，`endpoint_note` 重写。
连带同步 guard#5（「端点值」→「定点上的符号信息」）与 **B5**
（`changed_condition` / `explanation` / `witness` / `recovery` 四处全改）。

### BL-5 · 采纳
`A2.followup` 由 `all_of` 改 `sequence` + 三条带 `when` 的 `action_ref{A1, A3, A5}`，
`terminal_note`、`applies_when`、`description`、`construction_note` 同步。
**这正是交叉复核开的方子**，且保住了 A2 在不等式格的位置。

## codex 做得好、超出要求的三点

1. **L-1 纪律执行到位。** 每条结论都 grep 了全部出现点：
   `minimal_probe` ③④、`preference_rule`、`fallback_policy`、
   `route_universe` / `existing_routes` / `stop_rule` 全部同步。
2. **主动纠了两处未被要求的错。**
   - `mechanism.statement` ① 原写「**一切**存在性结论最终都归到罗尔定理」——
     这被 BL-1 直接证伪（零点/介值可独立终结），已改写为分含导数/不含导数两种。
   - `route_universe` 原写「限于大纲内的**四个**定理」却列了六个（审查方 NB-4），已改。
3. **重做了 `positive_instance_mapping`。** 审查方 NB-1 指出原四条中三条与题面不符
   （2007-19 是存在性等式却挂 A7、2017-18 是实根个数却挂 A7、2012-15 的 basis 定性错）。
   新版按实际路线逐条重挂，并补了 A5/A11/A8 的正例。

## integrator 另补的两处

### ① A8 的构造步骤只在 note 里，不在可执行字段里
codex 报告给出的 2005-18(I) 路由是
`存在性等式格 → A8 → **令 G(x)=f(x)+x−1** → 验异号 → terminal`，
但「令 G」**不是 A8 的 local_operation**，只写在 `insufficiency_note` 的散文里；
A8 的第一步是「验连续性，找出使函数值异号的两点」——对**谁**验，可执行字段没说。

这正是前两轮造成「半修复」的同一类缺陷（note 说了、可执行字段没说）。
已补一条带 `when` 的 `local_operation`，内容与 note 一致，不引入新语义。

### ② §3「当前未解决的」第 1 条仍写「无独立审查」
mvt 已由 claude-batch3-reviewer-4 审过。已改写为实况，并写明
**本族仍为 challenged + quarantine，恢复 candidate 须由另一个 agent 复核**。

## 本族现状

```yaml
blockers:
  BL-1: 已补完（codex）
  BL-2: 已补完（codex）
  BL-3: 已补完（codex 第一轮）
  BL-4: 已补完（codex）
  BL-5: 已补完（codex）
  BL-6: 已修（integrator）
  ⇒ 六条 direct blocker 全部落地
non_blocking_remaining:
  - NB-2 guard#3「问个数必须配 A9」把具体 action 写成合法性条件（上界机制不止 A9）
  - NB-3 A9 需「**严格**单调」，正文与其 counter_witness_search 的支撑理由不一致
  - NB-6 「恒等或有界」格漏「闭区间上连续 ⇒ 有界（最值定理）」，且该格无 scope 正例
  - 2023-20 题面在题面库中截断，其 positive_instance 不可核验（已记 待确认.md §九）
status: challenged + quarantine（未变）
```

**这是本批次里第一个 direct blocker 清零的族。** 但按 `cross_review_rule`，
`confirmed_fixed` 与恢复 `candidate` 须由**另一个** agent 复核——
codex（执行方）与 integrator（采纳方）均不得代行。下一步应派一个未碰过 mvt 的 agent 做复核。
