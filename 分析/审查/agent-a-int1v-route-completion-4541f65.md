# 修复方自述 · calc.int1v.route-selection 路线补全

```yaml
task: agent-a.int1v-route-completion
role: 子 agent A（修复方；本实例接续审阅同一分支上的未提交草稿）
base_head: 4541f65
branch: agent-a/int1v-route-completion
target_family: calc.int1v.route-selection
status_changed: false
doc_version_changed: false
solutions_read: false
papers_2024_2026_read: false
```

## 1. 结论

完成派工单列出的 BLK-1、BLK-2、BLK-4、BLK-6，并顺带处理 NB-1、NB-2、
NB-4、NB-6。族级 `status: challenged`、`teaching_use: quarantine`、
`doc_version: 1.0.1` 及既有 `status_history` 均未修改；状态裁定留给 integrator。

本实例接手时，目标族文件已有约 186 行未提交改动。我先完整审阅该草稿和独立审查报告，
保留其中正确部分，再补齐 A12 对 2009-3 的可执行图形分支、A12 在“变限积分”格的登记，
以及对应 route scan；没有丢弃前一修复实例的工作。

## 2. blocker 逐条处置与载体路径

### BLK-1 · 图形/几何意义直接读积分值

新增 A12，并同时登记到 `变限积分` 与 `几何应用` 两格。

- 2007-3：`变限积分` → A12（函数只由图形给出，问 F 的点值/比例）→
  按零点和半圆分段、轴上记正轴下记负 → 按 x 相对下限 0 的方向累计 →
  得各指定点 F 值并匹配比例 → terminal。
- 2017-4：`几何应用` → A12（速度图与阴影面积，问追及）→
  把每段阴影读成两人位移差的有向累计量，并合并初始距离 10 →
  累计位置差首次为 0 时 terminal。
- 2009-3：`变限积分` → A12（由 f 图形选 F 图形）→
  从 F(0)=0 出发，用 F′=f 的符号判各段增减，再以累计有向面积确定关键值/零点 →
  图形唯一匹配时 terminal。此分支是接续审阅时补入，避免 positive mapping 独家承载结论。
- 2012-10：`几何应用` → A12（被积式配方/平移后成为半圆）→
  以圆心为新原点，把额外乘子拆成中心奇函数项与常数项，在对称区间消去奇项 →
  把剩余部分化成半圆面积并按符号累计 → 定积分值得出时 terminal。

同步位置：A12 的 `applies_when / followup_actions / terminal_when / failure_boundary`、
一级分格登记、V3/G2 的 `route_universe / existing_routes / counter_witness_search /
stop_rule`、fallback 与 positive mapping。

### BLK-2 · 分段原函数连续定常数

新增 A13。2016-2 路径为：`不定积分与定积分求值` → A13（分段函数求整体原函数）→
在 x<1 与 x≥1 分别积分并保留独立常数 → 使用“原函数可导，所以在 x=1 连续”写
`F_-(1)=F_+(1)` → 联立常数 → 逐段求导并复核拼接连续性 →
只剩一个全局加法常数时 terminal。

同步位置：A13 的所有可执行字段、I7 的 route universe/existing route/counter witness/stop rule
及 fallback。

### BLK-4 · positive_instance_mapping 重做

删除审查已证伪的旧映射，重建为：A6=2008-1；A7=2005-8；
A12=2007-3/2017-4/2009-3/2012-10；A13=2016-2；
A9=2013-12/2021-11/2026-14；A11=2009-16/2019-17/2011-9；
A14=2008-18；A15=2026-20。

2004–2023 引用只读四份题面汇编核验，未读 `solutions/`。
2026-14、2026-20 仅采用派工单与独立审查中已核验的路由结论，映射的 `basis`
已明确写出该证据边界；未读取 2024–2026 的 papers。

### BLK-6 · 2008-18 / 2026-20 归属与路线

- 2008-18(I)：`变限积分 · 证明与存在性` → A14 →
  写 `[F(x+h)-F(x)]/h=(1/h)∫_x^{x+h}f(t)dt` → 减 f(x) 后以连续性作 ε 控制
  （或积分中值定理得到 ξ_h→x）→ 差商极限为 f(x) → terminal。
  路线明确禁止调用 A7 的待证性质，故不循环。
- 2026-20：`变限积分 · 证明与存在性` → A15 → 定义显式辅助函数 F 与区间/正则条件 →
  action_ref A6 求导，将原条件改写为具体函数值/导数或端点差条件 →
  零点型子问题由连续性与端点异号/介值性本地终止；中值定理型子问题则必须形成
  “辅助函数 + 明确区间 + 端点条件 + 区间内可导性 + 目标导数等式”的
  `transformed_problem` 后交 `calc.mvt-proof.route-selection` → terminal。

scope/exclusions 已按主考点粒度改写：积分只作辅助且主考点为中值定理者归 mvt；
主考点为变限积分基本性质/求导结构的证明仍归 int1v。

## 3. 顺带项

- NB-1：A7 新增单调性可执行分支，并同步 V2。
- NB-2：A2 将“一一对应”限定为不定积分回代时的必要检查；定积分分支改为检查可微换元、
  新被积式有效与同步换限。
- NB-4：周期性 guard 改为充要关系；c≠0 时明确用 `F(x+nT)=F(x)+nc` 排除任何正周期。
- NB-6：retired rule 的 note 补回“上限恰为 x 且 f(t)~ct^k”时成立的附加条件版本。
- 帕普斯-古尔丁定理由 `dominated_not_excluded` 改为 `out_of_scope`。

## 4. L-1 / L-2 / L-3 自检

L-1：对 A12–A15 逐条 grep，检查了 action 本体及 `failure_boundary`、
`local_operation`、`minimal_probe`、`route_scan.route_universe`、`existing_routes`、
`counter_witness_search`、`stop_rule` 的全部出现点。新路线不依赖 `minimal_probe`；
相应 cell 的 route scan 均已登记。

L-2：没有为了 lint 改变数学结论，也没有压制误报。本轮没有判断为 lint 误报的红项。
一次 R2 真错误来自补登记 A12 时误把 A11 的 eligible cell 改动到错误 action；已按清单事实修正，
最终 R2 一致。族的 challenged/quarantine 与 route scan 的 integrator 状态红项按权限原样保留。

L-3：遮去所有 `note / explanation / description / minimal_probe` 后，仅看
`level_2_candidates + applies_when + followup_actions + terminal_when`：

- 2007-3/2017-4/2009-3/2012-10 均能进入 A12，并分别以点值/比例、累计量、F 图形、
  定积分值终止；
- 2016-2 能进入 A13，以逐段导数正确且拼接连续终止；
- 2008-18(I) 能进入 A14，以差商极限得到 F′=f 终止；
- 2026-20 能进入 A15，本地零点证明或完整 mvt transformed_problem 二者之一终止。

因此没有结论只落在 note 或 minimal_probe 中。

## 5. lint 与文件范围

| 检查点 | 结果 |
|---|---|
| 派工基线 | `PASS：error 0 · warning 4` |
| 接续实例首次检查（已有 A12–A15 草稿） | `PASS：error 0 · warning 4` |
| 补 A12 图形分支并同步分格时 | `FAIL：error 2 · warning 4`；均为本族 R2 eligible_cells 真不一致 |
| 修正 A11/A12 eligible_cells 后 | `PASS：error 0 · warning 4` |
| 最终 | `PASS：error 0 · warning 4` |

四条 warning 均为基线既有的 `calc.extrema.constraint-selection/A2/A3/A5/A7` S3，
不在本任务文件范围。`git diff --check` 通过（仅 Git 提示该工作区未来可能进行 LF→CRLF 转换）。

实际改动文件仅：

1. `分析/方法族-高数-一元积分学.md`
2. `分析/审查/agent-a-int1v-route-completion-4541f65.md`
