# 修复方自述 · 重积分族路线补全

```yaml
task_id: agent-a.multiple-integral.route-completion
role: 修复方子 agent A
base_head: 576fb0c
branch: agent-a/mint-route-completion
target_family: calc.multiple-integral.route-selection
files_changed:
  - 分析/方法族-高数-重积分.md
  - 分析/审查/agent-a-multiple-integral-route-completion-576fb0c.md
solutions_read: false
papers_2024_2026_read: false
status_changed: false
doc_version_changed: false
status_history_changed: false
```

## 1. 口径与自检

- L-1：每项结论修改后均检查 `failure_boundaries`、action 的 `local_operation`、`minimal_probe`、`fallback_policy` 与 `route_scan` 的 `route_universe / existing_routes / counter_witness_search / stop_rule`。历史 `status_history` 保持原样，未把历史审查结论改写成当前状态。
- L-2：本轮 lint 与内容判断没有冲突；没有为追求绿色删除合法路线，也没有保留需上报的 lint 红项。
- L-3：按 integrator 裁定，同时遮住全部 `note / *_note / description / explanation` 与整个 `minimal_probe`，仅检查 `level_1_router + level_2_candidates + applies_when + followup_actions + terminal_when`。BL-1、BL-2、BL-3、BL-4 的路线均可执行到 terminal。
- “画图”已降为 `supporting_heuristic`；A7 的必要条件改为以同一区域集合为中介重新定限。不等式消元直接重述同一区域同样合法。

## 2. 三条 blocker 的可执行路径

### BL-1 · 表示互化与跨区域比较

1. `2006-8 / 2015-4`：`二重 + 表示互化 → 表示互化 cell → A10`。
   - 直角到极坐标分支从区域不等式/边界确定 `θ` 与逐角 `r` 范围，代换被积并显式写 `dA=r dr dθ`；
   - 反向分支先恢复区域集合，再按 X-型或 Y-型写 `dxdy / dydx`；
   - 目标坐标下区域范围、被积与完整面积元写出且题目不求值时直接 terminal。
2. `2009-2`：`二重 + 跨区域比较 → 跨区域比较 cell → A11`。A11 的第一个 sequence step 逐块核对区域对称、`y cos x` 的奇偶与符号：左右块由关于 `y` 的配对归零，上块为正、下块为负；第二个 sequence step 强制把四块结论放在同一序关系中比较，选出上块积分为最大者后才 terminal，不会停在“各块定号”。

### BL-2 · 换序作为二重求值手段

`2013-15`：`二重 + 求值 → 二重·求值 cell → A7`。A7 从原限恢复同一区域集合，按另一方向判型/分块并写新限；当原次序内层无初等原函数或难积且设问要求求值时，第四个 sequence step 强制按新次序算出，只有“换序后的累次积分已算出”才 terminal。`eligible_cells` 与两个入口 cell 已双向同步，guard、fallback 与 route scan 同步为这一口径。

### BL-4 · A3 三重后继

`A3.followup_actions` 改成带 `when` 的 conditional sequence：完成奇偶或轮换化简后，若关系本身尚未确定所求值，则按已经选择的真实计算路线互斥地进入：

- 二重直角 / 极坐标：A1 / A2；
- 三重投影 / 截面 / 柱球坐标：A4 / A5 / A6。

A5 与 A6 均已有自足的实算步骤和 terminal；A6 不再把球坐标定限误称为投影法。`2009-12` 的轮换关系不能单独 terminal，选择球坐标后进入 A6；`2010-12 / 2019-19` 经 A9 进入 A3 后，直接归零的分量可 terminal，仍需实算的分量按 A4/A5/A6 的所选路线继续。

## 3. BL-3 独立修核

遮住 note、description、explanation 与 minimal_probe 后，`2015-12` 的路线仍为：

`三重 + 求值 → A3.applies_when 的轮换支（只要求可积且区域在所用坐标置换下不变，不要求奇偶） → local_operation 建立 ∭x=∭y=∭z 并合并 x+2y+3z → 关系未单独给值，不 terminal → 选择三重直角投影路线 A4 → 外层二重积分交 A1 → 累次积分算出 terminal`。

因此无奇偶性的 `x+2y+3z` 可进入轮换分支并继续求值；没有依赖 note 才可见的入口或终止条件。最终是否记 `confirmed_fixed` 留给独立复核方 B。

## 4. 顺带项

- NB-1：按 TSV 主考点重做 positive mapping；A7 不再误列 `2009-2 / 2026-4`，补入真实换序载体 `2025-4`；A2、A3、A9 的错配一并更正，并新增 A10/A11 映射。2024–2026 仅使用现有 TSV 注记，未读取这些年份 papers。
- NB-3：A7 必要条件改为“以区域集合为中介重新定限”，画图另列为 supporting heuristic。
- NB-4：order_exchange 的 route universe 删除“唯一结构/没有第二种机制”的排他断言，改记共同必要骨架及画图/不等式消元两种实现。
- NB-5：B4 witness 更正为“外层对 y 积分而下限含内层哑变量 x”。
- NB-6：A6 在新坐标中直接由立体不等式定限并实算，不再 action_ref 到 A4。
- B1 加强：写入一般交换映射 `σ(x,y)=(y,x)` 及 `∬_{σ(D)}f=∬_D f∘σ`；当 `f=f∘σ` 时，自检对任意可测 D 都会掩盖错误，不限于 `f=xy` 或三角形区域。

## 5. lint 与文件范围

```text
baseline @ 576fb0c:                         PASS error 0 · warning 4
after BL-1/BL-2 action and cell routes:      PASS error 0 · warning 4
after route_scan/fallback/L-1 synchronization: PASS error 0 · warning 4
final after hide-note executable-field audit: PASS error 0 · warning 4
```

四条 warning 均为基线既有的 `calc.extrema.constraint-selection/A2/A3/A5/A7` S3 迁移提醒。本族没有 error 或新增 warning。`git diff --check` 通过。

实际改动严格限于目标族文件与本自述报告；未改 `status / teaching_use / doc_version / status_history`，族仍维持 `challenged + quarantine`。

