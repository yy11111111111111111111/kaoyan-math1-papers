# integrator 裁定 · codex 第三轮：空间解析几何与场量族路线补全

```yaml
adjudicated_by: claude-code-remote（integrator）
adjudicated_at: 2026-08-29
codex_branch: codex/geom-route-completion
codex_commit: 4bfd8e1
codex_base: 095696f        # 已核，与自报一致
codex_report: 分析/审查/codex-geom-route-completion-095696f.md
verdict: 四条 blocker + 三条顺带项**全部采纳**，integrator 无需补充
lint: error 0 · warning 4
```

## 合规性核查

| 项 | 结果 |
|---|---|
| 基线 | 基于 `095696f` ✓ |
| 文件范围 | 只动 geom 一族 + 报告 + 看板行 ✓ |
| `status` / `cell_status` / `scope` | **一处未触及** ✓（维持 `challenged` + `quarantine`） |
| L-3 遵守 | ✓ 见下 |
| 上两轮的错是否重犯 | 未重犯。无「删点消错」，无 note 独家承载 |

## 四条 blocker

### BL-1 · 采纳 —— 新增 **A1b**（消参法）
`applies_when: [旋转轴为坐标轴, 母线为不满足 A1 坐标面前提的一般空间曲线且可参数化]`，
`eligible_cells: [旋转曲面]`，新增 route **R2**。
原先被误标 `duplicate_mechanism` 而逐出候选集的路线，现已是正式 action。
positive_instance 重挂：`A1b ← 2013-19`，basis 写明
「母线 (1−t,t,t) 绕 z 轴：z=t，x²+y²=(1−t)²+t²，消参得 **x²+y²=2z²−2z+1**」
—— 与 integrator 早先的独立复算一致（t=1/3 时 x₀²+y₀²=5/9；2z²−2z+1|_{z=1/3}=5/9）。

### BL-2 · 采纳 —— 新增 **A1c**（一般轴旋转），选的是方案 (i)
`applies_when: [旋转轴为不必平行于任一坐标轴的一般直线, 母线可参数化]`，新增 route **R3**。
positive_instance：`A1c ← 2025-20`，得 **xy+yz+zx=0** —— 与 integrator 用 Rodrigues 公式的
独立复核一致（五个角度残差 <1e−12）。
**未自行改 scope**，符合硬约束。

**B6 的「witness 与命题错配」已修**：`recovery` 现为
「轴为坐标轴但母线不在坐标面时转 **A1b**；轴为一般直线时转 **A1c**」，
全文 **"超出本族 scope" 字样已清零**。witness 保留为 proof（它证的本就是「口诀不适用」，
现在支撑的也正是这个命题）。`guard#7` 同步为「依次选 A1 / A1b / A1c」。

### BL-3 · 采纳 —— A2 补值域约束 + 新增 **B7**
**关键是它进了可执行字段而非 note**（L-3）：A2 新增两条 `local_operation`——
「回到原方程组，解回被消变量并写出存在实解的条件（如判别式非负、平方项非负或参数值域）；
消元中出现平方/乘除时同时恢复分支与非零条件」与
「将消元必要方程、实解存在/值域/分支条件与目标坐标面联立」；
`terminal_when` 同步为「…且被消变量的实解存在条件与值域/分支限制已保留」。
新增 guard「A2 的消元方程只是**必要条件**」，新增 boundary **B7**，
route J1 的 `failure_boundary` 改为 `B4 · B7`。

### BL-4(b) · 采纳
`positive_instance_mapping` 重挂：2013-19 → A1b、2025-20 → A1c，
不再与 `A1.applies_when` / `guard#7` / `B6` 冲突。
（2009-17 仍挂 A1，正确，未动；integrator 上轮修的
`A6 ← 2016-10、2018-11` 与 `A7/A5 ← 2026-11` 的旋度归属亦保持。）

## 三条顺带项：全部落地，且有一条做得比要求更好

- **BL-5**：不止改了失实的 note，而是**新增了正式 action A7**（复合算子恒等式），
  `applies_when: [所求表达式含 grad/curl/div 的复合, 且各层算子所需导数存在]`，新增 route F3。
  positive_instance：`A7 ← 2026-11`，「由内到外识别 `div(rot(rot A)) = div(curl B)`，
  在正则性前提下用 `div(curl B)=0` 终止」。**这比派工单要求的「改写 note」更进一步。**
- **SB-8 归并理由**：§0 已改写为跨章的实用理由
  （「空间解析几何主要落在高数第四章，而 div/curl 属第六章的向量微分算子…样本仅三题，
  单开一族会过碎」），并补上了**可判的边界准则**：
  > 「归属边界以**题目是否含曲线/曲面积分**为准，而不是以是否出现向量场为准。」
  原先那条不可证伪的「认公式 → 定参数 → 代入算」已删。
- **「不分叉」自我刻画**：全文已清零。

## integrator 补充

**无。** 这是三轮里第一次不需要 integrator 补任何东西。

## 本族现状

```yaml
blockers: BL-1 / BL-2 / BL-3 / BL-4(b) 全部落地；BL-5（非阻塞）亦已处理
status: challenged + quarantine（未变）
next: 需由**未碰过 geom** 的 agent 做 confirmed_fixed 复核
```

按 mvt 的先例，复核通过后方可恢复 `candidate`。
执行方（codex）与采纳方（integrator）均不得代行。
