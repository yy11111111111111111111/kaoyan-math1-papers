# 交叉复核 · integrator 对 batch3 五族所落修复本身

```yaml
task_id: batch3.integrator_fixes.cross_review
artifact_identity: { branch: claude/batch3-parallel-family-audit-ekzi6c, head: 23800a1 }
reviewed_at: 2026-08-29
why: >
  batch3 五族的独立审查补上了「建族方同时是 integrator」这个缺口，
  但 integrator 依据五份报告落的 10 处修复**又没有任何人看过**——
  缺口只是从「建族方兼 integrator」平移到了「修复方兼 integrator」。
  故派三个仍有上下文的审查 agent 做**交叉派单**：每人审自己**没审过**的族。
assignment:
  claude-batch3-reviewer-1（原审 diff1v）→ lint 补丁 + 三处 R2 对齐方向
  claude-batch3-reviewer-2（原审 int1v）→ mvt guard#4/#6、mint guard#1
  claude-batch3-reviewer-3（原审 mint） → int1v guard#3、diff1v guard#1 + 候选拆分
口径: 三人均只读、未改任何文件；files_changed: [] 已核。
```

## 总判定：10 处修复里 2 处是半修复，1 处引入了新问题，1 处我对用户的陈述有误

| # | 修复 | 交叉复核判定 | integrator 处置 |
|---|---|---|---|
| 1 | lint CELL_ALIAS 补 8 条 | confirmed_fixed | — |
| 2 | lint key 回落 `or c.get('cell')` | confirmed_fixed | — |
| 3 | lint 新增「无一格可解析」error | confirmed_fixed（不误报，可达） | — |
| 4 | diff1v/A12 删「判形态」 | confirmed_fixed（方向对），但**症状被抹掉、BL-1 未点名** | 已在 §3 点名 BL-1 |
| 5 | int1v/A10 补进求值格 | confirmed_fixed | — |
| 6 | 重积分/A6 移出二重格 | confirmed_fixed | — |
| 7 | int1v guard#3 | confirmed_fixed（数学），但**欠标 + 漏前提 + 4 处旧语义遗留（含 2 处假命题）** | 已全部修正 |
| 8 | diff1v guard#1 + 候选拆分 | guard confirmed_fixed；**候选的理由码错、路线仍不可达** | 记为未修完 |
| 9 | mvt guard#4 | **not_fixed**——推导严谨，但 A7 的 followup/terminal_when/remainder_note 未同步 | 判定改回未修复 |
| 10 | 重积分 guard#1 | **not_fixed**——反例全对，但 A3 的 applies_when 未同步；且新 check 过松 | 判定改回未修复 + check 已收紧 |

## 一、我犯了自己刚批评过的同一个错误

reviewer-2 的原话最准：两处补丁都**只改了 guard 文本，没改真正决定可用性的字段**。

- **mvt guard#4**：guard 已改成「定号**或**有界」，但 A7 的
  `description`（「余项定号」）、`followup` 唯一收尾操作（「判定该阶导数在整个区间上的**符号**」）、
  `terminal_when`（「余项**定号后**不等式已成立」）、`remainder_note`（「**必须**在整个区间上定号……
  **只能**用整体信息」）、B4 的结论句、`counter_witness_search` 的 target ——**六处**全是旧语义。
  router 执行的是 followup 那一侧，所以 **2024-19(1) 走到 A7 仍然卡死**。
- **重积分 guard#1**：guard 已拆出轮换分支，但 A3 的 `applies_when` 仍是
  「区域有对称性, **且被积函数在相应变换下有确定的奇偶性**」。
  2015-12 的 `x+2y+3z` 无奇偶性 ⇒ **A3 在 router 层根本进不去**，
  guard 放宽了也没用，L136 的轮换支仍是不可达分支。

**这正是我在原始审查里判五族有罪的同一条罪名**（「guard 与 action 不同步」）。
两条 blocker 的判定**从「已修复」改回「未修复」**，已写入五族的 `status_history`
与 HANDOFF 的 `open_blocker_summary`。

reviewer-2 由此提炼出一条应当固化的收口步骤（NF-4）：
> 改一条 guard ⇒ grep 该结论在 **failure_boundary / action 的 local_operation /
> minimal_probe / route_scan 标签** 四个位置的全部出现点。
> 这四处目前**没有任何 lint 项覆盖**（R1/R2 只查 action_ref 与 eligible_cells）。

## 二、我引入的新问题：`scope:` 不是 v1.3.1 的字段

reviewer-2 扫了全部 11 族的 guards：guard 层的 `scope:` 共 3 处，**全部由我这次的补丁引入**
（mvt 1 处、mint 2 处）。而两族 frontmatter 仍写 `schema_version: CALC-METHOD-FAMILY-v1.3.1`
——文件声称遵循的版本里没有这个字段。lint 对 guard 字段没有白名单，所以它**静默通过**
（与刚修好的 R2 静默空转是同一类问题）。

更糟的是命名冲突：`scope` 在本 schema 里已有两个既定含义（frontmatter 的族 scope、
`route_scan_by_cell.*.scope` 的格范围），我在 guard 里给了它第三个含义。

**不构成 B3**——同样的限定不改数学关系就能表达，而且两条 condition 的正文其实
**已经**写了「沿 A3……」「A3 的奇偶/轮换分支……」，字段本身是冗余的。
**处置：采纳建议 1，三处 `scope:` 全部删除**，限定仅靠 condition 正文承载。已删，lint error 0。

## 三、我对用户的陈述有误：R2 是 9/11 不是 11/11

reviewer-1 自己跑 `load()` 统计，纠正了我的说法：

- **R2 active: 9/11**（vector, ode, series, multivar, diff1v, int1v, multiple-integral, mvt-proof, space-geometry）
- **limit 与 extrema 仍 inactive** —— 但它们既无 `level_2_candidates` 也无任何
  `eligible_cells` 声明，属**无可查**而非**已查**，不应记为生效。

我此前只说「7 族空转」并让人以为修复后全覆盖，这个说法不准确，已更正。

## 四、reviewer-1 发现 R2 的静默通道只堵了一半（NF-1）

我新增的 error 触发前提是 `level_2_candidates` **非空**；而 `if cells:` 仍在，
`cells` 为空时整段 R2 照旧跳过。reviewer-1 的注入测试 t2：
删掉 diff1v 整块 `level_2_candidates`、保留全部 14 个 `eligible_cells` → **PASS error 0，无任何提示**。

`limit` 与 `extrema` 今天正处于这个形状，只因它们碰巧一个 `eligible_cells` 都没声明才无损。

**已按其给的一行修法补上反方向守卫**，并复跑其注入测试 t2 验证：
现在报 `calc.diff1v.route-selection: 有 action 声明了 eligible_cells 但无 level_2_candidates 可比对，R2 将被跳过（R2）` ⇒ FAIL error 1。不是死代码。

## 五、三处 R2 对齐的方向都选对了

reviewer-1 逐处按「哪一边反映这个 action 的**真实数学适用面**」判，而不是按改动量：

- **diff1v/A12**：切线法线的点斜式与「单调/凹凸/极值/拐点」没有数学关系 ⇒ 删声明对，补清单会错。
- **int1v/A10**：对称性/周期性正是**定积分求值**的常规主力（∫_{−1}^{1} x³/(1+x²)dx = 0 一步到位），
  ⇒ 清单漏列才是错的一边，补清单对；反向删 eligible_cells 会真的丢一条合法路线。
- **重积分/A6**：`dV = r dr dθ dz` 与 `ρ²sinφ dρ dφ dθ` 都是三维雅可比，对二重无意义
  ⇒ 删清单对；反向把「二重求值」写进 A6 会造出一条**数学上不存在**的路线。

但 A12 那处附带一个代价（reviewer-1 判为「算症状掩盖，但不算隐瞒」）：
删掉错误声明后，文件里**再没有任何文本线索**指向 BL-1 所说的「缺显式·求切线法线格」。
**已在 diff1v §3 点名 BL-1 及其载体 2004-1。**

## 六、int1v guard#3 的遗留（reviewer-3 NF-1，其中两处是假命题）

我的修复只落在 5 个陈述点里的 1 个：

| 位置 | 原文 | 状态 |
|---|---|---|
| guard#3 | 「要求下限为 0」 | 已改 ✔ |
| B3.`changed_condition` | 「在**下限不为 0** 时被沿用」+ `invalidates` | 过宽 → **已改**为「在 ∫₀^{下限}f ≠ 0 时」 |
| B3.`explanation` | 「该结论依赖 F(0)=0，**而这需要下限为 0**」 | **假命题** → 已改 |
| route_scan V2 标签 | 「B3（**下限须为 0**）」 | 旧语义 → 已改 |
| A7 性质表 | 「f 偶且**下限为 0** ⇒ F 奇」 | 命题仍真（充分），但它是本族唯一**可执行**的那一行，学生按它作答会在 a=√3 型题上答错 → 已改 |

reviewer-3 另指出两点，均已采纳：
- **欠标**：在 f 偶的前提下 `∫₀ᵃf=0` 是**充要**的，标 `necessary` 丢掉了可直接判定
  「F 是奇函数」的那个方向，而 check 其实已在用充分方向 ⇒ 字段与 check 不自洽。
  已改为 `necessary_and_sufficient`。
- **漏前提**：等价号要求 f 在同时含 0 与 a 的区间上可积、且 F 定义域关于原点对称。
  缺 0 点可积性时命题连良构都不成立（f=1/t² 偶、a=1：∫₀ᵃf 发散，F 只活在 (0,∞)）。已写入 condition 与 check。

## 七、重积分轮换 guard：我从「过严」滑到了「过松」

reviewer-2 独立推导确认轮换分支的正确条件（**坐标置换是置换矩阵，|det|=1 ⇒ 自动保测度**，
故 T(Ω)=Ω ⇒ ∭f∘T = ∭f），我写的「对被积没有奇偶性要求」**正确**。
但我的 check 写「只核对区域在置换下是否不变」，按字面可由「存在某个置换使 Ω 不变」
推出全部变量地位相同。**反例**（reviewer-2 构造，integrator 蒙特卡洛复算 3×10⁶ 点确认）：

> Ω = {x,y≥0, x+y≤1, 0≤z≤2}（三棱柱）在 x↔y 下不变，
> ∭x = ∭y = **1/3**（实测 0.3331 / 0.3333），但 ∭z = **1**（实测 0.9990）。
> 只有**被交换的那一对**相等。

**已改**：check 要求「对每一对要断言相等的变量，分别核对区域在该对互换下不变」，
并把「置换须是坐标置换（置换矩阵，|det|=1，因而保测度）」与「被积可积」写进 condition。

## 八、reviewer-2 复核了 mvt guard#4 推导的严谨性（我埋的疑点）

我给 reviewer-2 埋了一个问题：拉格朗日余项里 η₁、η₂ 是**两个不同**的中值点，
我用绝对值放缩绕过去了，这一步严不严谨？

其判定：**成立且严谨，没有被合并，也不需要合并。**
η₁、η₂ 各自留在自己的余项里；取绝对值 + 三角不等式 + |f″|≤1 是**逐项**放缩：
≤ (1/2)[(1−x)x² + x(1−x)²] = (1/2)x(1−x)[x+(1−x)] = x(1−x)/2。
**绝对值放缩恰恰是绕开合并需求的那一步**——若要写成单个 f″(η) 的凸组合形式，
才需要 f″ 连续 + 介值定理，而此处根本没用到。f 只需二阶可导。x∈{0,1} 时两端为 0，平凡成立。

## 九、NF-3：五族降级**一条 status_history 都没记**

reviewer-1 grep 确认：+158 行补丁里 `status_history` 新增 **0 处**。
diff1v 的唯一条目仍是 `from: null → to: candidate, review_kind: author_creation`，
其 open_items 还写着「尚无独立审查」；正文 §3 第 1 条同样仍写「无独立审查」——
在五份独立审查已完成后，**这两句是错的**。
对照先例：ODE 与 multivar 的降级/恢复都在 HANDOFF 与 status_history 中留了痕。
lint 的 C1/C2 查不出（只比对当前值，不看 lineage）。

**已为五族各补一条 `status_history`**：`from: candidate → to: challenged`，
`review_kind: independent_audit`，记 reviewer、报告路径、blocker 摘要、逐条 open_items，
并标注本次交叉复核对「半修复」的改判。

## 十、reviewer-1 顺带发现我漏改了 BL-7

BL-7（diff1v 的 A7 三条真题引用全错）我在原始归档里写的是「未修复，留待下一轮」，
理由是与路线修复一并重做更省事。reviewer-1 指出这是个**独立的事实错误**，不该等。
**已改**：`2015-1、2017-2、2019-2` → `2005-1、2007-2、2012-1、2014-1、2023-1`，并写入更正说明。

## backlog（本轮未做）

- reviewer-2 NF-2 / NF-4：mvt 与 mint 的 `counter_witness_search` target、
  `route_scan` 的 existing_routes 仍是旧口径，随 BL-3 的真正修复一并同步。
- reviewer-1 NF-2：`CELL_ALIAS` 应按 `(family_id, cell)` 键。当前 0 冲突，
  且失效方向是**吵闹的假阳性而非静默漏过**，故不急。
- reviewer-3：diff1v 的导数极限定理路线应**升为正式 route**（现停在 excluded_candidates，
  四种理由码无一贴合，router 不可达）。这是路线设计，留给下一轮。
- 建议新增 lint R3（mandatory followup 的 eligible_cells 必须覆盖源 action 的）与
  guard 字段白名单——后者本可拦下我的 `scope:`。

## 结论

**五族维持 `challenged` + `quarantine`，不得据本次修复恢复 candidate**（reviewer-2 明确要求）。
本轮的净收益是：修好了 6 处、修正了 2 处半修复的**判定**（不是内容）、
删掉了 1 处自己引入的越schema字段、堵上了 R2 的另半条静默通道、
补齐了 5 条 status_history、并纠正了我对用户的一处不准确陈述（R2 覆盖面）。
