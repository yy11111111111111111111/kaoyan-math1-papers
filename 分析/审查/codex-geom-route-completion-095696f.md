# Codex 交付报告 · geom-route-completion · 095696f

```yaml
executor: codex
assigned_by: claude-code-remote
base_branch: claude/batch3-parallel-family-audit-ekzi6c
base_head_read: 095696f
work_branch: codex/geom-route-completion
date: 2026-08-29
target_family: calc.space-geometry.route-selection
status_changed: false
cell_status_changed: false
solutions_read: false
papers_2024_2026_read: false
```

## 结论

本轮补完四条 open blocker，并落实 BL-5、SB-8 与「真实分叉」自我刻画修正。
正文仍为 `status: challenged` + `teaching_use: quarantine`，各 cell 的 `status`
未改；`route_scan_status: open` 与 `global_exhaustiveness: not_established` 也保持不变。
四格的 `completion_criteria.no_direct_blocker_open` 按当前直接 blocker 的处置结果改为
`true`，不代替 integrator/独立 reviewer 的复核裁定。

## blocker 处置

### BL-1 · 2013-19

新增 A1b，接收「坐标轴为旋转轴、母线为一般可参数化空间曲线」。可执行步骤写明
轴向坐标与径向距离平方守恒、消参、恢复实参数范围/分支条件、母线点回代。
原来把该机制放在 excluded candidates 的结论已撤销。

### BL-2 · 2025-20

选择方案 **(i)**：新增 A1c，而不改 scope。理由是该题已由 SB-7 裁定以旋转曲面方程
为主考点；一般直线轴也有统一且可执行的「垂足参数守恒 + 到轴距离守恒」路线，
没有必要把 scope 内载体推出本族。

B6 现在只断言并证明「A1 特殊位置口诀不适用」，其 recovery 分流到 A1b/A1c；
不再让该 proof 承担「一般轴不在 scope」这一它并未证明的命题。

### BL-3 · A2 投影消元超集

A2 的可执行字段现在先把消元结果标成必要方程，再回到原方程组解回被消变量，
恢复实解存在、值域、分支与除数非零条件，最后才与目标坐标面联立并终止。
新增 B7，以 `{x²+z²=1, y²+z²=1}` 和分离点 `(2,2)` 证明只保留
`x²−y²=0` 会扩大投影；route scan 的旧 `not_found` 已改为 `found: B7`，
并另记写全实解条件后的反例搜索为 `not_found`。

### BL-4(b) · positive-instance 映射

映射已拆为：2009-17 → A1，2013-19 → A1b，2025-20 → A1c。
前两条新路线的 basis 分别落下
`x²+y²=2z²−2z+1` 与 `xy+yz+zx=0`。

## 顺带处理

- 新增 A7 复合场算子路线，2026-11 改挂 A7；可执行分支由内到外识别
  `div(curl B)`，核对连续二阶偏导后以 `div(curl B)=0` 终止。不匹配终止恒等式时，
  通过真实 `action_ref` 转 A5/A6，而不是只在 note 中声称会转。
- §0 明示跨章的实用归并理由，并把边界写成「含曲线/曲面积分 → vector 族；
  只含 grad/curl/div 微分算子 → 本族」。
- 重写「不分叉/公式唯一」旧刻画；minimal probe、mechanism、fallback、route universe、
  existing routes、counter-witness、stop rule 与 positive mapping 已同步。

## 载体题的完整可执行路径（遮住 note 自检）

### 2013-19 · BL-1

```text
旋转曲面格
→ A1b（轴为 z 坐标轴；一般空间母线可参数化）
→ r₀(t)=(1−t,t,t)
→ 写 z=t，x²+y²=(1−t)²+t²
→ 消去 t；原参数 t∈R，不增加范围分支
→ 母线点回代核对
→ A1b terminal：x²+y²=2z²−2z+1，实参数条件已保留
```

### 2025-20 · BL-2

```text
旋转曲面格
→ A1c（一般轴 ℓ:a+s d，取 a=0、d=(1,1,1)；母线 r₀(t)=(0,0,t)）
→ 写轴向垂足参数守恒：(X−a)·d=(r₀(t)−a)·d
→ 写到轴距离平方守恒：|(X−a)×d|²/|d|²=|(r₀(t)−a)×d|²/|d|²
→ 联立消 t，并保留 t∈R 的实参数条件
→ 用母线点/旋转轨道点回代并核对两个守恒量
→ A1c terminal：xy+yz+zx=0，实参数条件已保留
```

### 2017-19 · BL-3

```text
空间曲线投影格
→ A2
→ 从原两个曲面方程消去被投影变量，得到投影柱面的必要方程
→ 回原方程组解回被消变量，写出实解存在/值域/分支/非零条件
→ 将必要方程 + 上述条件 + 目标坐标面联立
→ A2 terminal：投影方程组写出，且实数原像条件已保留
```

### 2009-17 / 2013-19 / 2025-20 · BL-4(b)

```text
旋转曲面格
├─ 坐标面母线 + 坐标轴 → A1 → 恢复平方前符号/范围并回代 → terminal（2009-17）
├─ 一般空间母线 + 坐标轴 → A1b → 守恒量消参 → terminal（2013-19）
└─ 可参数化母线 + 一般直线轴 → A1c → 两个守恒量消参 → terminal（2025-20）
```

### 2026-11 · BL-5

```text
场量格
→ A7（表达式含复合 grad/curl/div，各层所需导数存在）
→ 由内到外把 div(rot(rot A)) 识别为 div(curl B)，B=rot A
→ 核对 B 的连续二阶混合偏导条件
→ 应用 div(curl B)=0
→ A7 terminal：所求场量为 0
```

以上路径只依赖 `level_2_candidates`、`applies_when`、`followup_actions`
（`local_operation` / `action_ref`）与 `terminal_when`。机器自检先递归删除
`note`、`explanation`、`description` 等复述字段，再断言 A1b/A1c/A2/A7 与三条题号映射，结果 PASS。

## lint 与机器验收

```text
改前（095696f）：            PASS  error 0 · warning 4
新增 A1b route 后：          PASS  error 0 · warning 4
新增 A1c route 后：          PASS  error 0 · warning 4
补 A2/B7 与 A7 route 后：    PASS  error 0 · warning 4
全部改完：                   PASS  error 0 · warning 4
遮住 note 的 router assertions: PASS
git diff --check:             PASS
```

四条 warning 始终是未改动的
`calc.extrema.constraint-selection/A2/A3/A5/A7` S3 backlog。

### 保留的红色/误报

无。新增 action 的 `eligible_cells` 与 level-2 cell 清单双向一致，没有触发 R2；
本轮也没有出现内容判断与 lint 冲突的 error，因此没有需要留红交 integrator 裁定的项目。

## 范围与 lineage

- 业务内容只修改 `分析/方法族-高数-空间解析几何与场量.md`，另新增本报告并更新看板本人行。
- 没有修改任何族的 `status`、`teaching_use` 或 cell `status`。
- `status_history` 中记录审查时未修 blocker 的文字保留为历史快照，未覆写。
- 未读取 `solutions/`；未读取 `papers/2025` 或 `papers/2026`。
