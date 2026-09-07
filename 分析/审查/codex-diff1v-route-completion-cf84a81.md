# 修复方自述 · calc.diff1v.route-selection 路线补全

```yaml
task_id: codex.diff1v.route-completion.round4
role: 子 agent A（修复方）
branch: agent-a/diff1v-route-completion
base_head_read: cf84a81
target_file: 分析/方法族-高数-一元微分学.md
source_audit: 分析/审查/claude-audit-batch3-diff1v-a635bd6.md
solutions_read: false
papers_2024_2026_read: false
status_fields_changed: false
teaching_use_changed: false
cell_status_changed: false
doc_version_changed: false
```

## 1. 修复摘要

- BL-1：新增「显式 · 求切线法线」cell，并把 A12 拆成「已知切点」与「由斜率/几何条件反求切点」两个 `applies_when`。反求切点的求解步骤落在 `followup_actions.local_operation`；反求未知函数的 ODE 主体仅声明交给 `calc.ode`。
- BL-2：新增 A14，把凸/凹的整体弦不等式、切线支撑不等式与割线斜率单调性写入可执行字段；`failure_boundary` 要求整个区间已知凸/凹或 `f″` 定号，不允许从单点符号外推。
- BL-3：新增 A15 消参路线，要求分支、保留每支 `x` 范围，再转 A1/A5；A4/A4b 的 `failure_boundary`、guard、fallback 均同步覆盖 `x′(t)=0` 或不存在。
- BL-5：A2 先分类差商极限；单侧/绝对值/取整分支在本族用 `local_operation` 自理，只将 limit 族现有 scope 内的一般极限外送。
- NB-1/NB-2/NB-4/NB-6：分别改挂 2016-4 至 A5、2021-1 至 A2；拐点 guard 补「函数在候选点连续」；「代具体函数」拆成用反例否定的 `duplicate_mechanism` 与用单例肯定普遍命题的 `invalid`。

## 2. 载体题的完整可执行路径（遮 note 口径）

### 2004-1

`显式 · 求切线法线` → A12（「已知几何条件，可化为目标切线斜率」分支）→
`local_operation` 将与 `x+y=1` 垂直化为 `k=1`，解 `f′(x₀)=1/x₀=1`，得 `x₀=1`、`y₀=0` →
`local_operation` 写点斜式 `y=x−1` → A12 `terminal_when: 方程已写出`。

### 2014-2

`判形态（单调/凹凸/极值/拐点）` → A14（整个 `[0,1]` 上 `f″≥0`）→
`local_operation` 确认凸性 → `local_operation` 取 `a=0,b=1,λ=x`，写
`f(x)≤(1−x)f(0)+xf(1)=g(x)` →
A14 `terminal_when: 弦/切线位置关系已推出`。

### 2023-3

`参数式 · 求导或切线` → A15（`x′(0)` 不存在，但可分段解 `t=t(x)`）→
`local_operation` 分 `t≥0/t<0` 两支并保留定义域：
`y=(x/3)sin(x/3), x≥0`；`y=−x sin x, x<0` →
A1 求每支内点的导数 → A5 对拼接点按设问阶数逐层比左右导数，其左右差商由 A2 在本族处理 →
`local_operation` 比较得 `f′(0⁺)=f′(0⁻)=0`、`f″(0⁺)=2/9`、`f″(0⁻)=−2` →
A15 `terminal_when: 所问导数/正则性已判定`。

### 2019-2（BL-5 载体）

`分段 · 正则性或分段点导数` → A5 →
A2 分别接收左/右差商 → A2 `local_operation` 先判为单侧且含分段表达式，分别代入 `h<0` 下的 `x|x|` 支与 `h>0` 下的 `x ln x` 支，约分/用基本极限求值 →
A5 `local_operation` 比较左右导数 → A5 `terminal_when: 左右导数均已判定并比较完毕`。

## 3. lint 与格式检查

| 时点 | 结果 |
|---|---|
| 改前基线 | `PASS：error 0 · warning 4` |
| 新增显式切线 cell / A12 路线后 | `PASS：error 0 · warning 4` |
| 新增 A14 路线后 | `PASS：error 0 · warning 4` |
| 新增 A15 路线后 | `PASS：error 0 · warning 4` |
| A2 分支差商路线改完后 | `PASS：error 0 · warning 4` |
| 全部修复完成后 | `PASS：error 0 · warning 4` |

四条 warning 始终是本轮范围外的 `calc.extrema.constraint-selection/A2/A3/A5/A7` 的 S3 迁移提示；本族无新增 warning。

`git diff --check`：通过；只有 Git 对工作区 LF/CRLF 转换的提示，无 whitespace error。

## 4. 遮 note 自检

已从 YAML 中遮掉 `note`、所有 `*_note`、`description`、`explanation` 与整个 `minimal_probe`，只打印并检查：

- `level_2_candidates`；
- A2/A12/A14/A15 的 `applies_when + followup_actions + terminal_when + failure_boundary`；
- T1/T2、P1–P4、R1/R2、H1–H5 的 `existing_routes`。

结果：2004-1、2014-2、2023-3、2019-2 的上述路径均可不依赖 note/minimal_probe 走到 terminal；YAML 可成功解析。

## 5. 保留的红色/误报

无。lint 未产生 error；四条既有 warning 不属于误报，但对象均在本轮禁改的其他族，因而保留。

## 6. open_questions

- **BL-5 是否必须修改 limit 族：否。**接收方已明文排除单侧/含绝对值/含取整的分段讨论；把它们传给已冻结 limit 族会继续悬空。A2 现已在本族给出分支、化简/夹逼、比较单侧结果的可执行步骤；只将接收方 scope 内的一般极限外送，故无需 reopen 或修改 limit 族。

## 7. 资料约束

已完整读取 `CLAUDE.md`、第四轮派工单与指定审查报告。仓库中不存在派工上下文要求的 `分析/00_数学教学_启动入口.md`或同名 `(1)` 副本，因此无法由它继续路由；本轮严格依派工单的直接修复范围执行。未读 `solutions/`，未读 2024–2026 `papers/`。
