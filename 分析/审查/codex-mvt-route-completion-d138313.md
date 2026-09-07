# Codex 交付报告 · mvt-route-completion · d138313

```yaml
executor: codex
assigned_by: claude-code-remote
base_branch: claude/batch3-parallel-family-audit-ekzi6c
base_head_read: d138313
work_branch: codex/mvt-route-completion
date: 2026-08-29
target_family: calc.mvt-proof.route-selection
status_changed: false
solutions_read: false
papers_2024_2026_read: false
```

## 结论

本轮按 BL-1 → BL-2 → BL-4 → BL-5 补齐了中值定理族的四条 open blocker。
正文仍为 `status: challenged` + `teaching_use: quarantine`，`route_scan_status` 仍为 `open`，
各格 `status` 未改。只将四格 `completion_criteria.no_direct_blocker_open` 如实改为 `true`；
这是修复方的自查陈述，不代替另一 agent 的 `confirmed_fixed` 复核。

## 四条 blocker 的处置

### BL-1 · 存在性等式格的零点/介值终结路线

选择复用 A8，不新造一个与 A8 同机制的 action。理由是零点定理在两格里的数学动作相同，
差别只在 terminal 语义：存在性等式格中「存在一个零点」已满足设问；实根个数格中它仍只给下界，
必须接 A9。已同步：

- `level_2_candidates[存在性等式]` 增 A8；
- `A8.eligible_cells` 改为 `[存在性等式, 实根个数]`；
- A8 的 terminal 与 insufficiency note 按两格分开；
- existence route-scan 增 Q5，并同步 route universe、stop rule、counter-witness。

### BL-2 · 逐点估计 + 积分保序

新增 A11，专门表达：

```text
|∫G| ≤ ∫|G| ≤ ∫H
```

其 `applies_when` 要求待证左端含定积分，且已有或可先建立被积函数的逐点界。
已将 A11 同步到不等式格的 level-2 清单、route universe、existing route N4、minimal probe、
preference rule、counter-witness 与 positive-instance mapping。

新增 B8 作为该路线的 failure boundary：不得把 `|∫G|≤∫|G|` 写成恒等，
且须核对逐点界与目标积分使用同一区间。

### BL-4 · A5 逐阶降解与内部最小值

A5 现在允许在 `F′` 不能直接定号、但继续求导会降低复杂度时递归调用 A5。
递归结果可用来判定 `F′` 的单调性/两侧符号，然后回到外层，分两种终结形态：

- 端点/定点支：全区间单调 + 一个定点值/端点极限；
- 最小值支：`F′(x₀)=0` 且 `F′` 由负变正（或严格递增），计算 `F(x₀)` 定号。

guard#5、A5 description/applies_when/followup/terminal/note、B5、minimal probe、N1 与 counter-witness
已全部改为「定点符号（端点或内部最小值）」口径。

### BL-5 · A2 的多后继分支

A2 保留在 `[存在性等式, 不等式]` 两格，未删除合法路线。`followup_actions`
从 `all_of` 改为 `sequence`：先执行三个共同 local operation（改写目标、构造 F、核对合法性并选分支），
再由三个互斥 `when` 过滤出唯一后继：

- A1：一次一阶中值定理即可终结；
- A3：需多次罗尔降到二阶及以上导数；
- A5：原目标是不等式，构造后须判定 F 的符号。

v1.3.1 的 `followup_actions.mode` 不支持嵌套 `sequence -> any_of`；而该 schema 明确规定
先用 item `when` 过滤，再解释 mode。因此「sequence + 互斥 when 分支」在不扩展 schema 枚举的前提下
等价表达了派工单要求的「三步 sequence 后接 any_of{A1,A3,A5}」。

## 载体题 router 走通记录

### 2005-18(I) · BL-1

```text
存在性等式格
→ A8（零点/介值定理）
→ 令 G(x)=f(x)+x−1，验 G 在 [0,1] 连续
→ G(0)=−1<0<G(1)=1
→ A8 terminal：存在 ξ∈(0,1) 使 G(ξ)=0，即 f(ξ)=1−ξ
```

现在不依赖罗尔条件，不再卡在 `F(0)≠F(1)`。

### 2024-19(2) · BL-2

```text
不等式格
→ A11（逐点估计 + 积分保序）
→ G(x)=f(x)−[(1−x)f(0)+xf(1)]
→ 由 (1) 已有 |G(x)|≤x(1−x)/2
→ |∫₀¹G|≤∫₀¹|G|≤∫₀¹x(1−x)/2 dx=1/12
→ A11 terminal：|∫₀¹f−(f(0)+f(1))/2|≤1/12
```

未读取 `papers/` 中 2024–2026 文件；只使用派工单与本族 guard#4 explanation 已给的条件。

### 2012-15 · BL-4 + BL-5

```text
不等式格
→ A2：构造 F=左边−右边
→ A2 的不等式分支 A5
→ A5：F′ 不能直接定号，递归对 F′ 再用 A5
→ F″(x)≥2>0，故 F′ 严格递增；F′(0)=0
→ 回到外层 A5 最小值支：F 在 0 取最小值
→ F(0)=0
→ A5 terminal：F≥0
```

这条路径保留了「构造辅助函数」在不等式格的合法性，同时解决旧 A5
只能「一次求导 + 端点值」的结构缺口。

### 2017-18(II) · BL-5

```text
存在性等式格
→ A2：构造 F=f·f′，核对所需等值点
→ A2 的高阶导数分支 A3
→ A3：对等值点反复用两次罗尔
→ A3 terminal：得到所需高阶导数的零点/相应方程的两个实根
```

旧 `all_of -> A1` 不再强迫这道题只用一次罗尔。

## lint 与机器验收

```text
改前（d138313）：     PASS  error 0 · warning 4
BL-1 route 后：          PASS  error 0 · warning 4
BL-2 route 后：          PASS  error 0 · warning 4
全部改完：              PASS  error 0 · warning 4
router structure assertions: PASS
git diff --check:          PASS
```

四条 warning 仍是已有 `calc.extrema.constraint-selection/A2/A3/A5/A7` 的 S3 backlog，
本轮未改该族。

### 保留的红色/误报

无。本轮新增 A11 后 R2 的两侧声明同步，没有产生 `eligible_cells` 不一致；
其他 lint 也未产生与内容判断冲突的 error，因此没有需要「留红待 integrator 裁定」的条目。

## 范围与 lineage

- 业务内容只修改 `分析/方法族-高数-中值定理与证明.md`。
- 没有修改任何族的 `status`、`teaching_use`或 cell `status`。
- `status_history` 中「当时尚未修复」的旧文保留为历史快照，未覆写。
- 未读取 `solutions/`，未读取 2024–2026 `papers/`。
