# 独立复核 · calc.space-geometry.route-selection 的 confirmed_fixed

```yaml
task_id: geom.confirmed_fixed_review
reviewer: claude-batch3-reviewer-4（审的是 mvt 族，**未参与 geom 的建族 / 审查 / 任何一轮修复**）
artifact_identity: { branch: claude/batch3-parallel-family-audit-ekzi6c, head: 180fe5f }
compare_base: 095696f
reviewed_at: 2026-08-29
lint: PASS · error 0 · warning 4（与基线逐字一致）
verdict: 四条 blocker 全部 confirmed_fixed；非阻塞的 BL-5 亦 confirmed_fixed 且**超额**；建议恢复 candidate，附两条必办
note: 本次复核首次派出时因 session rate limit（HTTP 429）中断、未产出任何结论，本报告为重派后的产物
```

## 一、blocker 判定：四条 + 一条全部 confirmed_fixed

| blocker | 判定 | 依据（全部落在可执行字段） |
|---|---|---|
| **BL-1** 2013-19 无 action | confirmed_fixed | 新增 **A1b**；`level_2_candidates[旋转曲面]` 由 `[A1]` 扩为 `[A1, A1b, A1c]`，R2 双向一致；四条 `local_operation` 全可执行，第 2 条逐字给出守恒量「z=z₀(t)，x²+y²=x₀(t)²+y₀(t)²」；新增 route R2。**原 `duplicate_mechanism` 条目是升格进 candidate_actions，不是删除** |
| **BL-2** 2025-20 无 action 且 B6 判 scope 外 | confirmed_fixed | 新增 **A1c**，五条 `local_operation` 写全「垂足参数守恒 + 到轴距离平方守恒 + 消参 + 回代」；B6 的 `recovery` 改指 A1b/A1c，**全文「超出本族 scope」grep 0 命中**；witness 保留 `proof`（它证的本就是「口诀不适用」）⇒ **witness 与命题的错配已消除**；guard 同步为「依次选 A1/A1b/A1c」；scope 未被改动 |
| **BL-3** A2 消元得超集 | confirmed_fixed | **进了可执行字段**：`followup` 由 2 步扩为 3 步，新增「解回被消变量并写出存在实解的条件（判别式非负、平方项非负或参数值域）」；`terminal_when` 同步；新增 guard 与 **B7**；J1 的 `failure_boundary` 改 `B4 · B7`；**被证伪的旧 `search_result: not_found` 已改为 `found, witness: B7`，没有被静默保留** |
| **BL-4(b)** 两题挂 A1 | confirmed_fixed | mapping 拆为三条，basis 里写出具体结果式；三处矛盾逐处复核，均已不冲突 |
| **BL-5**（非阻塞） | confirmed_fixed · **超额** | 不止改 note，而是新增正式 action **A7** + route F3；失实句「三题均为直接场」随条目升格一并消失 |

**复核方指出的两处「没被同一手法骗过」**
- BL-3：值域约束进的是 `local_operation` 与 `terminal_when`，而 `elimination_note` 现在**只复述旧结论、没有独家承载任何新结论** —— 符合 L-3。
- BL-1/BL-2：这轮走的是**加点**，不是第一轮批评过的「删点消错」；被误标的两条候选去向是 `candidate_actions`，可追踪可复核。

## 二、L-3 遮 note 自检：四题全部走通

| 载体题 | 结果 |
|---|---|
| **2013-19** | A1 的 `applies_when` 判假 ⇒ 弃 → **A1b** → 参数化 → `z=t, x²+y²=(1−t)²+t²` → 消 t → 回代 → terminal。得 **x²+y²=2z²−2z+1** ✓ |
| **2025-20** | A1、A1b 均因「轴非坐标轴」判假 → **A1c** → 垂足 `x+y+z=t` → 距离守恒 `(3(x²+y²+z²)−(x+y+z)²)/3 = 2t²/3` → 消 t → 得 **xy+yz+zx=0** ✓（只用到 `\|u×v\|²=\|u\|²\|v\|²−(u·v)²`，非 note 依赖） |
| **2017-19** | A2 → 消 z 得 `x²+y²=2x` → **新增的 op2 解回 z**（`z²=2x` 要求 x≥0）→ 联立 z=0 → terminal。得 `(x−1)²+y²=1` ✓。**新增步骤在此不改变答案但确实被执行**，说明它不是只为反例而设的死步骤 |
| **2026-11** | 场量格 → 判为复合 → **A7** 分支 1 → B=rot A=(−2z,−2x,−2y) 为多项式 ⇒ C^∞ ✓ → `div(curl B)=0` → terminal。得 **0** ✓，**未采信 papers/2026 OCR 的 "1+z"** |

复核方独立数值复算：2013-19 六个母线参数点 + 三个旋转像点残差为 0；2025-20 用 Rodrigues 对 5×5=25 个像点，`max|xy+yz+zx| = 5.3e−15`；2017-19 圆周 721 点全部满足且 x≥0；B7 分离点 (2,2) 回代得 `z²=−3`。

## 三、新增内容审计（复核方的实质发现）

### ① A1 / A1b / A1c 不是划分，但不留致命缝
`A1c.applies_when` 写「**不必平行于**任一坐标轴」⇒ 形式上**吞并** A1 与 A1b。
复核方实算验证：A1c 用到 2013-19（a=0、d=(0,0,1)）时两个守恒量退化为与 A1b 逐字相同。
⇒ A1 ⊂ A1c、A1b ⊂ A1c；A1 与 A1b 由「母线是否在坐标面内」互斥。
**无害**（`minimal_probe` 给了全格上的确定性判定顺序），但 `preference_rule` 说「三者由几何位置做**合法性**分流」**过强**——
A1→A1b 确是合法性，A1b→A1c 是**纯泛化**（A1c 对 2013-19 同样合法，只是更长）。

**真正的缝（scope 外）**：A1b/A1c 都要求「母线**可参数化**」。母线以两个曲面方程隐式给出且不在坐标面内时（如 `{x²+y²+z²=1, x+y+z=1}` 绕 z 轴），三条都不接，而合法路线存在（四元消元）。8 题内无此形 ⇒ backlog。

**另一处**：`A1.applies_when` 只要求「母线为坐标面内的曲线」，**未要求该坐标面含旋转轴**；母线⊂xOy、轴=z 轴时「另一个变量」有两个候选，字面不可执行。scope 内 2009-17 不触发。

### ② A2 的值域约束：可执行，实测挡住 (2,2)
对 `{x²+z²=1, y²+z²=1}` 逐步走：op1 得 `x²−y²=0`；**op2 的「平方项非负」直接命中本例判据类型**，由 `z²=1−x²≥0` 得 `|x|≤1`；op3 联立。**(2,2) 在 op2 处被排除** ✓。且 `terminal_when` 要求「实解存在条件已保留」，跳过 op2 则无法宣告终止。

### ③ A7 的正则性：`applies_when` 偏弱，但正确条件已在 `local_operation`
复核方给出反例：`B=(0,0,f)`，`f=xy(x²−y²)/(x²+y²)`（Peano 例）。
`f_x(0,y)=−y`、`f_y(x,0)=+x` ⇒ `f_xy(0,0)=−1`、`f_yx(0,0)=+1`，**两者都存在但不相等**，
此时 `div(curl B) = f_yx − f_xy = 2 ≠ 0`，而「各层算子所需导数存在」是满足的。
⇒ **仅凭导数存在，恒等式可假**；需要二阶混合偏导**连续**。
**但** `followup` 分支 1、2 的 `local_operation` 各自写着「核对二阶混合偏导连续后」——
正确条件在可执行字段里，遮 note 后仍在 ⇒ **BL-5 的 confirmed_fixed 不受影响**，属「入口门与执行门不同步」。
*（integrator 已按其建议收紧 `applies_when` 并把该反例落成 **B8**。）*

附带：`any_of` 的分支 1、2 **没有 `when`**，门控藏在 operation 的散文里；lint 的 S2 只管 `optional_any_of`，`any_of` 不受约束。
又附带：`A5.applies_when`「给出向量场并求散度」字面上也接纳 2026-11，而 A5 无「先算内层场」这一步，照字面走会算出 `div A = 3`（错）；拦下它的是 `level_1_router.rule` 与 `minimal_probe`，不是 A5 自己。

### ④ B7 的 witness：名副其实
有具体曲线、具体分离点 (2,2)、回代 `z²=−3`、并补出真实约束 `|x|≤1`。
**这是真正的构造**，与本族 B6、mvt 族 B4 那种「设某函数…」的假设式陈述不同类。
`kind: constructed_counterexample` 名实相符，`effect: invalidates` 正确（照旧路线会写出一个**错的、过大的**答案，不是无结论）。

## 四、regression：无合法内容消失

| 项 | 095696f | HEAD | 结论 |
|---|---|---|---|
| `route_id` | 6 条 | 9 条（+R2/R3/F3） | **无一消失** |
| `level_2_candidates` / `eligible_cells` | — | 原 6 条逐字未动 | **只增不减** |
| `excluded_candidates` | 9 | 6 | 三条的去向**全部是升格为正式 action** |
| `dominated_not_excluded` | 5 | 4 | 见下 |

**那条「消失」的 `dominated_not_excluded`**（`用恒等式先化简`）→ 升格为 **A7 / F3**。
复核方特别说明：只看计数会把 5→4 读成「删了一条、违反协议」。
> **它不是被删，是被提拔。** 协议禁止删除的理由是「效率低 ≠ 非合法路线」，
> 而这里把它从「合法但被支配」直接提升为正式候选 action —— 是该规则所保护目标的**最强实现**，
> 不是它所防范的失败模式。**判：不构成 regression。**

## 五、SB-8 边界准则：从「不可证伪」变成「可判但会误判」

- **进步是真的**：旧理由不可证伪；新准则「以题目是否含曲线/曲面积分为准」**是可判的**，对中心情形也判得对。
- **但有 scope 内反例**：**2017-19** 的 (II) 是求薄片质量（第一类曲面积分），而 vector 族的 objects 正是四类积分 ⇒ 按新准则字面，2017-19 **整题应归 vector 族**；可它就在本族 8 题清单里、还是 A2 的唯一正例。
- **另一反例**：**2009-17(II)** 求体积，两者都不含，却也不在本族 `target_tasks` 里，落地后无处安放（与仍开着的 NB-6 同一件事）。
- **病根是粒度**：准则写「**题目**是否含…」，而 HANDOFF 的 `scope_boundary_rule` 用「**主考点**」。多小问的题上必然打架。
- **风险定级**：与原 BL-2 是**同一错误模式**（一条边界声明把 scope 内的题判出族外），只是从 B6 挪到了 §0/exclusions。
  **此刻不构成 blocker** —— 2017-19 仍在清单、仍走通 A2、无题因此失去路线，是声明与清单的不一致，不是路由失败。**若后来者照字面执行，才会退化成真的 B1/B4。**

*（integrator 已按其建议改为主考点粒度，并新增 `scope.subquestion_handoff` 显式安置两个小问的去向，同时关闭 NB-6。）*

## 六、非阻塞项：五条仍在，无一被悄悄改动

| 项 | 状态 |
|---|---|
| NB-1 B1 witness 自相矛盾句 | 仍在，逐字未动（B1 结论仍成立） |
| NB-3 自由文本 `failure_boundary` | 仍在**且变多**（原 D2，本轮新增 R2、F3）→ *integrator 已把 R2/F3 补成 B9/B8，D2 留 backlog* |
| NB-4 guard 缺 explanation | 仍在；⚠️ **编号因新 guard 插入而顺延**（原 guard#5 → 现 guard#6） |
| NB-5 B5 归因不完整 | 仍在（`± √(…)` 本身已引入另一支，平方只是第二重） |
| NB-6 小问交棒悬空 | 仍在，且与 SB-8 新准则叠加 → *integrator 已用 `subquestion_handoff` 关闭* |
| NB-2 「不分叉」自我刻画 | **已关闭**，grep 0 命中 |

**复核方另发现 8 项**（A1c 措辞歧义、preference_rule 过强、A7 的 `any_of` 缺 when、A5/A6 的 `applies_when` 过宽、A5 成为全族唯一零正例的 action、两格对 route_universe 处理不一致等），均非阻塞，已分别落地或记 backlog。

## status_recommendation

`challenged → candidate`，解除 `quarantine`；`reopen_family: false`；**未发现任何新的 B1/B2/B3/B4**。

复核方同时关闭了原审查留下的一个悬念：
> 原审查曾把「值不值得建族」挂在「取决于 blocker 怎么修」上。
> 现在 **C1**（A1/A1b/A1c 与 A5/A6/A7 两组真实分叉）、**C2**（guard 与 level_1_router 择路）、
> **C3**（2013-19 / 2025-20 / 2026-11 三题触发）**三条全部满足 ⇒ 建族成立**。

## confidence_limits（复核方自述）

- **2025-20 与 2026-11 未翻 `papers/`**（模考卷硬口径）；对两题做的是独立复算（Rodrigues 25 个像点、rot∘rot 逐分量展开）。若真实题面与三份文件所记不符，BL-2 与 BL-5 的载体验证需重做。**未采信** papers/2026 OCR 的 "1+z"。
- 未读 `solutions/`；未从真题频率推任何 route 的合法性。
- 环境无 sympy/numpy，A7 反例的混合偏导用差分（±0.9998，与解析值 ∓1 相符）；**解析推导独立成立**：`f_x(0,y)=−y ⇒ f_xy(0,0)=−1`；`f_y(x,0)=x ⇒ f_yx(0,0)=+1`。
- 「A1c 吞并 A1b」是对「不必平行于」的字面解读；若建族方本意是「**不平行于**」（排除坐标轴），则三条构成真划分，关于 preference_rule 的发现随之作废 —— **该措辞歧义建议顺带澄清**。*（integrator 已澄清为「含坐标轴在内」。）*
- 遮 note 自检时把 `level_1_router.rule` 与 `minimal_probe` 视为可见（与 mvt 复核范本口径一致）。第三节 ③ 的 A5/A6 观察对此敏感：**若 `minimal_probe` 也被遮蔽，2026-11 存在被 A5 接住并算成 3 的路径** —— 建议下一轮明确 `minimal_probe` 的遮蔽归属。
- 2013-19 未逐字核题面（其构造在两份报告中一致且已复算自洽）。

---

## integrator 处置

**采纳全部结论。`status: challenged → candidate`，解除 `quarantine`，`doc_version → 1.1.0`。**

两条必办 + 三条建议**已在同一次提交内全部落地**（见上文斜体注与 `status_history` 的 `fixed_with_this_change`）。
其中 SB-8 的粒度修正与 A7 的正则性收紧是**内容改动**，处方由复核方逐条开出、落地措辞由 integrator 拟定，
**建议下一位接触本族的 agent 顺带扫一眼**。

**geom 是第二个走完整条链路的族。** 与 mvt 不同的是：本轮 integrator 在**采纳阶段未作任何补充**，
所有补充都发生在**复核之后**、且全部来自复核方的处方 —— 这比 mvt 那轮更接近预期的分工形态。
