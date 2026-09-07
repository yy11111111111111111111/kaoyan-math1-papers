# 独立复核 · calc.mvt-proof.route-selection 的 confirmed_fixed

```yaml
task_id: mvt.confirmed_fixed_review
reviewer: claude-batch3-reviewer-5（审的是 space-geometry 族，**未参与 mvt 的建族 / 审查 / 任何一轮修复**）
artifact_identity: { branch: claude/batch3-parallel-family-audit-ekzi6c, head: a29f670 }
compare_base: a635bd6      # blocker 提出时的 head，用于 regression diff
reviewed_at: 2026-08-29
lint: PASS · error 0 · warning 4（4 条全在 extrema 的 S3 欠账）
verdict: 建议恢复 candidate 并解除 quarantine；未发现任何新的 direct blocker
```

## 六条 blocker 的判定

| blocker | 判定 | 依据（均落在**可执行字段**） |
|---|---|---|
| **BL-1** 存在性等式格缺零点/介值终结路线 | **confirmed_fixed** | `level_2_candidates[存在性等式]` 加 A8；`A8.eligible_cells` 扩两格（R2 双向一致）；A8.followup 新增首条 `local_operation`「移项构造连续辅助函数 G」带 `when`；`terminal_when` 扩写；新增 route Q5，`stop_rule` 四类→五类 |
| **BL-2** 不等式格缺「逐点估计 + 积分保序」 | **confirmed_fixed** | 新增 A11，两侧清单同步；三条 `local_operation` 全部可执行、无一依赖 note；新增 route N4。**六条里修得最干净的一条** |
| **BL-3** guard#4 定号误标 necessary | **partially_fixed**（阻塞成分已解除） | `A7.followup.mode` 由 `sequence` 改 **`any_of`**，拆定号支/取界支——原「强制判定符号」的死路消失；交叉复核点名的六处旧语义**逐处核对，全部已改** |
| **BL-4** A5 缺逐阶降解与最小值定号 | **confirmed_fixed** | `applies_when` 放宽；新增自递归边；followup 第 3/4 项拆为带 `when` 的两支；`terminal_when` 拆两支；guard#5 与 B5 四字段同步 |
| **BL-5** A2 的 mandatory continuation 悬空 | **confirmed_fixed** | `mode` 由 `all_of` 改 `sequence` + 三条互斥 `when` 的 `action_ref{A1,A3,A5}`；**A2 仍在不等式格**（N5 为证） |
| **BL-6** guard#6 族级 necessary 错 | **confirmed_fixed** | route-scope 写进 `condition` **正文**而非字段；G1 合规（上一轮 integrator 塞的非法 `scope:` 字段已清）；check 已吸收「或 A4」 |

### 复核方特别指出的两处「没被同一手法骗过」

- **BL-1**：integrator 把「令 G」从 `insufficiency_note` 挪进了 `local_operation`。
  > 「若它仍只在 note 里，按 L-3 我会判 **not_fixed**。」
- **BL-5**：
  > 「上一轮的假修复手法是**删点**（把 A2 移出不等式格，让悬空消失）；这一轮是**改边**。
  > 悬空由 `when` 过滤消除，而非由删除路线消除。」

## L-3 遮 note 自检（本次复核的核心判据）

方法：遮住 `note` / `explanation` / `description` / `remainder_note` / `construction_note` /
`endpoint_note` / `counting_note` / `insufficiency_note` / `order_note`，
**只读** `level_1_router.rule`、`level_2_candidates`、`applies_when`、
`followup_actions` 的 `local_operation` / `action_ref` / `target` / `when`、`terminal_when`。

| 载体题 | 结果 |
|---|---|
| **2005-18(I)** | 走通。存在性等式格 → A8 → 构造 `G=f+x−1` → `G(0)=−1<0<1=G(1)` → terminal |
| **2024-19(2)** | 走通，**全程零 note 依赖**。→ A11 → 写成 ∫G → `|∫G|≤∫|G|≤∫H` → `∫₀¹x(1−x)/2 = 1/12` |
| **2012-15** | 走通。→ A2（A1/A3 的 `when` 为假跳过）→ A5 → 自递归得 `F″≥2>0` → 最小值支 → `F(0)=0` |
| **2017-18(II)** | 走通。→ A2 凑 `F=f·f′` → 三个等值点 → A3 → 罗尔得两个零点 |
| *（并验）* **2024-19(1)** | router 层不再卡死；`any_of` 的取界支可达 terminal |

> **五条路径全部走通，无一步需要靠 note 才说得通。**

## 复核方独立复算的数值

- `2012-15`：`F(0)=0`、`F′(0)=0`、`F″` 网格 20001 点实测 **min = 2.0 > 0**；
  `F′` 在 `(−1,0)` max `= −2.0e−4 < 0`、`(0,1)` min `= +2.0e−4 > 0` ⇒ x=0 确为内部极小；实测 **min F = 0.0**
- `2024-19(2)`：`∫₀¹(1−x)dx = ∫₀¹x dx = 1/2`（故首步「写成 ∫G」成立）；`∫₀¹x(1−x)/2 dx = 1/12`
- `B8`：`|∫₀¹(x−1/2)| = 0` vs `∫₀¹|x−1/2| = 1/4`
- `B3`：`g=x³−3x` 于 `[−3,3]` 端点异号但实有 3 根（`−√3 / 0 / √3`）

## regression 检查：无条目消失

| 项 | a635bd6 | HEAD | 结论 |
|---|---|---|---|
| route ids | 11 条 | 14 条（+Q5/N4/N5） | **无一消失** |
| `excluded_candidates` | 9 条 | 9 条，逐条对应 | **无删除、无理由降级**；`dominated_not_excluded` 一条未删 |
| `level_2_candidates` / `eligible_cells` | — | 三处删除行**均被更宽版本替换** | **未重犯「删点消错」** |
| `positive_instance_mapping` | 4 条（3 条错挂） | 9 条重挂 | **净修复**，非删除 |

## 复核方新发现（均非阻塞，integrator 已逐条处理）

1. **A5 自递归无终止约束。** 递归的唯一门是「会降低复杂度」——不是可判定谓词，也不是良基的递减度量。
   **不终止见证**：`F = sin x` 于 `(0,2π)`，各阶导数**全部变号**（复核方实测 1–6 阶，四阶循环 ⇒ 对所有阶成立）；
   此时递归 `when` 恒真、两条出口 `when` 恒假 ⇒ **无限下降且无任何字段令其停下**。
   *（integrator 已复算确认，并按其建议补了 `when` 的有限阶条件与 `fallback_policy` 出口。）*
2. **A5.followup[1]「令 F = 左边 − 右边」无 `when` 门** —— 递归调用时对象是 F′，没有「左边/右边」可作差，该步字面不可执行。
   *（已补 `when: 本次为最外层调用`。）*
3. **B4 第二条 witness 仍非具体构造**（「**设**某函数 f″ 在左半段为正、右半段为负」），
   却标 `constructed_counterexample` + `verified` 并列在 `constructed_counterexamples: [B1,B2,B3,B4]` 里
   —— **把未构造的东西记成已构造并已验证**，provenance 虚高。
   *（已把 `kind` 降为 `proof`、从清单移出、加 `kind_note` 说明。）*
4. **A7 取界支的 L-3 残留**：2024-19(1) 真正的关键一步「把两个展开式分别乘 `(1−x)`、`x` 相加，
   使 `f′(x)` 项系数 `−x(1−x)+x(1−x)=0` 抵消」**只写在 guard#4 的 `explanation` 里**。
   *（已补进取界支的 `local_operation`。）*
5. **2017-18(II) 的落格歧义**：题面写「实根」，若落实根个数格则 `A2`/`A3` 都不在该格 ⇒ 无路线。
   目前只靠 guard#3 的 check 拉回来，`level_1_router.rule` 本身没写这条判据。
   *（已在 rule 补：「至少 n 个根 → 存在性等式格；恰好几个 → 实根个数格」。）*
6. **`status_history` 与正文矛盾**：1.0.1 条目的 `reason` 仍逐字写着「BL-1/BL-2/BL-4/BL-5 未修」，
   而正文四条都已补完；H1 标题仍写 `v1.0.0` 而 frontmatter 是 `1.0.1`。
   > 「只读 frontmatter + status_history 的人会得出与正文相反的结论。」
   *（已 bump 到 1.1.0、对齐 H1、给 1.0.1 条目加 `note_2026_08_29` 指向新条目、追加 1.1.0 条目。）*
7. **`route_scan_status: open`** 而四格均 complete —— 复核方判为「codex 有意的保守留白，等复核方」。
   *（已翻为 `complete_within_declared_universe`。）*

## 仍在 backlog 的 non-blocking（复核方逐条确认「确实还在、没被悄悄动过」）

- **NB-2** guard#3 把「必须配 A9」这个具体 action 写成合法性条件（给上界的机制不止 A9：罗尔反证、多项式次数界、凸性）
- **NB-3** `A9.followup[1]` 写「**单调**区间」，而其 `counter_witness_search` 的支撑理由写的是「**严格**单调段上至多一根」——正文与支撑不一致
- **NB-6** 「恒等或有界」格漏「闭区间上连续 ⇒ 有界（最值定理）」，且该格**无任何 scope 正例**（结构性空格）
- **靶子④** 凹凸性的 reason 仍是 `dominated_not_excluded`（原议改 `duplicate_mechanism` of A7），note 仍含频率型措辞「本族 scope 内无正例」
- `A3.counting_note` 与 `B7.changed_condition` 仍是族级措辞，未随 guard#6 一起 route-scope
- `2023-20`（题面截断）与 `2011-17`（方程中 k 丢失）的 positive_instance 宜标 `unverifiable`
- `A11.applies_when` 的「**左端**含定积分」是位置性限定（`1/12 ≥ |∫…|` 字面不命中），宜改「某一侧」；且它接纳「上下界」却只写死了绝对值路线，单侧保序无对应 `local_operation`
- `B8.changed_condition` 有两个并列条款，witness 只覆盖 (a)，(b)「区间一致性」无 witness
- **`sequence + 互斥 when` 这一编码不受任何 lint 约束**（S1/S2/S3/T1 均不校验 `when`）——与 HANDOFF 对 R3 的裁定一致（这是内容缺陷、无结构性 lint 可捕获），正确性靠内容判断维持

## confidence_limits（复核方自述）

- **2024-19 未翻 `papers/`**（模考卷硬口径），其条件全部取自 guard#4 的 explanation 与两份报告；若真实题面与三份文件所记不符，BL-2 与 BL-3 的载体验证需重做
- **2023-20 的 A3 定性无法核验**（题面截断），与原审查一致
- 数值复算用 sympy + 20001 点网格，不构成对全区间的严格证明，但与解析论证一致
- A5 不终止见证只实测到 6 阶（四阶循环使结论对所有阶成立）
- 未读 `solutions/`；未从真题频率推任何 route 的合法性

---

## integrator 处置

**采纳全部结论。`status: challenged → candidate`，解除 `teaching_use: quarantine`，`doc_version → 1.1.0`。**

依据 ODE 与 multivar 的先例：`challenged → candidate` 是恢复到 `author_upgrade_ceiling`，
属 integrator 权限内；`upward_status_change: GPT_only` 管的是 candidate 以上。

复核方列的两条「必办」与四条「建议」**已在同一次提交内全部落地**（见上文各条的斜体注）。
其中第 1、4、5 条是**内容改动**，虽由复核方逐条开出处方，但落地措辞由 integrator 拟定，
**建议下一位接触本族的 agent 顺带扫一眼**——尤其 A5 递归 `when` 的新表述
「且存在有限阶 n 使 F^{(n)} 在目标区间上可定号」是否过强（它把一个存在性断言塞进了执行条件）。

**这是 batch3 五族中第一个走完整条链路的族**：
建族 → 独立审查（6 blocker，降 challenged）→ 修复（integrator 2 条 + codex 4 条）
→ 采纳裁定 → **独立复核** → 恢复 candidate。其余四族照此办理。
