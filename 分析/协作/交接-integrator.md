# integrator 交接说明

```yaml
handed_over_at: 2026-08-29
from: claude-code-remote（云端，本轮 integrator）
to: 接手 integrator 的人/agent
branch: claude/batch3-parallel-family-audit-ekzi6c
codex: 继续在岗，本机，有 GitHub 推送权限
一句话: batch3 五族里两族已闭环，三族还剩 11 条 blocker；流程已跑通两遍，照抄即可。
```

---

## 一、还剩多少（这是你最想知道的）

| 族 | 状态 | 剩余 blocker | 派工单 |
|---|---|---|---|
| 中值定理与证明 | ✅ `candidate` | 0 | — |
| 空间解析几何与场量 | ✅ `candidate` | 0 | — |
| **一元微分学** | `challenged` | **4**（BL-1/2/3/5） | ✅ **已写好**：`派工-codex-2026-08-29-第四轮.md` |
| **一元积分学** | `challenged` | **4**（BLK-1/2/4/6） | ❌ 需要写 |
| **重积分** | `challenged` | **3**（BL-1/2/4） | ❌ 需要写 |

**总计 11 条 blocker、3 个族。** 每族一个循环，所以是 **3 个循环**。

一个循环 = codex 修（1 轮）→ 你核验采纳 → 派一个**没碰过该族**的 agent 做 `confirmed_fixed` 复核 → 你落复核方的处方 + 恢复 `candidate` + 同步下游。
前两个循环各花了大约「一次 codex 往返 + 一次复核 agent 往返」。

**做完这三个循环，batch3 就整体收口了。** 之后是 backlog（非阻塞项，几十条，不急）。

---

## 二、流程模板（已跑通两遍，照抄）

```
1. 写派工单 → 分析/协作/派工-codex-<日期>-第N轮.md
2. codex 自开分支修 → 推 GitHub → 告诉用户分支名
3. 你：git fetch → 核对基线/文件范围/status 未被动 → cherry-pick → 跑 lint
4. 你：写裁定 → 分析/审查/claude-adjudication-codex-<...>.md
5. 派复核 agent（必须没碰过该族）做 confirmed_fixed
6. 你：落复核方的处方 → status challenged→candidate → 解除 quarantine
   → bump doc_version → 追加 status_history → 归档复核报告
   → 同步 HANDOFF / 看板 / 交接说明-教学AI §2.3 / GPT接入包
7. lint 必须 error 0
```

**范本**（照这两份写，格式和详略都对）：
- 裁定：`分析/审查/claude-adjudication-codex-geom-route-completion-4bfd8e1.md`
- 复核：`分析/审查/claude-review-geom-confirmed-fixed-180fe5f.md`

---

## 三、三条踩出来的教训，派工单必须逐字带上

写在 `METHOD_FAMILY_HANDOFF.md` 的 `lesson` / `lesson_L3` / `cross_review_of_integrator_fixes.lesson`。

- **L-1** 改一条结论 ⇒ grep 它在 `failure_boundary` / `local_operation` / `minimal_probe` / `route_scan`（`route_universe`、`existing_routes`、`counter_witness_search`、`stop_rule`）的**全部出现点**。
- **L-2** **lint 与内容判断冲突时留红并写进报告，不得改内容去迁就 lint。**
  > 第一轮派工单写死「必须 error 0」，把 codex 逼到**删掉一条合法路线**让 lint 变绿。那是派工方的错。
- **L-3** 结论必须落在**可执行字段**（`followup` 的 `local_operation` / `action_ref`、`applies_when`、`terminal_when`）；`note` / `explanation` / `description` **只能复述，不得独家承载**。
  > 验收法：**遮住所有 note，只看可执行字段，看 route 能不能走通。** 这是两次 `confirmed_fixed` 复核的核心判据。

**这三条不是文风建议，是三次真实事故的产物**（batch3 五族最初的罪名之一、integrator 自己的两处半修复、codex 的 A8）。

---

## 四、你会踩的坑（我都踩过）

1. **`main` 分支上 `分析/` 是空的。** 全部内容只在 `claude/batch3-parallel-family-audit-ekzi6c` 上。给任何人地址都必须带 `-b <分支>`，否则对方拿到空壳还以为资料不存在。
2. **别自己发明 lint 规则就写进派工单。** 我把交叉复核建议的 R3 照单收下，结果它在 11 族上报出 13 条、多数是误报（`eligible_cells` 是**入口集**，强制后继天然落在入口集之外），最后整条驳回，还连累 codex 删了内容。
   **新规则先在全部现有 artifact 上试跑一遍**（教训 L-2 的推论）。
3. **YAML 陷阱**：序列项不能以 `*` 开头（别名标记），要加引号；往 `exclusions:` 这类列表中间插 mapping 键会截断后续条目。
4. **新增 boundary 后要同步 `constructed_counterexamples` 索引**，否则 lint 报 `evidence 索引缺 [...]`。
5. **`challenged → candidate` 是 integrator 权限**（恢复到 `author_upgrade_ceiling`，有 ODE / multivar / mvt / geom 四次先例）；**`candidate` 以上是 `GPT_only`**。
6. **别自己既修又判。** 我在 mvt 那轮于采纳阶段补了两处，等于把执行方和审查方的活揽了过来。geom 那轮我一个字没补、所有补充都在复核之后且来自复核方处方 —— **后者才是对的形态**。

---

## 五、待裁定 / 悬着的事

1. **`minimal_probe` 在 L-3 遮 note 自检时算不算「可见」？**
   两次复核都按「可见」处理，但 geom 复核方明说：**若 `minimal_probe` 也被遮蔽，2026-11 存在被 A5 接住并算成 3 的错误路径**。
   这条会影响后面三族的复核标准，**下一份派工单/复核任务书里应当明确**。
2. **`mint BL-3` 已补完但从未独立复核。** codex 第一轮补的 `A3.applies_when`，当时没随重积分族一起送复核。
   **重积分那一轮的 `confirmed_fixed` 复核必须把它一并纳入。**
3. **diff1v BL-1 的归属问题。** 2015-16 / 2023-17 / 2012-18 是「由切线条件反求 f」，实际要建并解 ODE。
   按主考点归 diff1v，但解法主体在 `calc.ode`。派工单已要求 codex 只补「反求切点」这一步、把归属写进 `open_questions` 交你裁定。
4. **`分析/方法族-高数-第一批.md` 是 `frozen` 的**（limit / vector / extrema）。
   diff1v 的 BL-5 涉及 limit 族的 `exclusions`，**修法是本族自理，不许动 limit 族**。派工单已写死。
5. **mvt 的 A5 自递归 `when`** 我拟的措辞「且存在有限阶 n 使 F^{(n)} 可定号」**可能过强**（把存在性断言塞进了执行条件），已在归档里点名，请下一位接触该族的 agent 顺带扫一眼。

---

## 六、教学侧的现状（别忘了同步）

每次有族恢复 `candidate`，**必须同步改三处**，否则教学 GPT 会继续按旧名单办事：
- `分析/交接说明-教学AI.md` §2.3 的九族状态表 + 隔离名单计数
- `分析/GPT接入包.md` 档 3 的可传清单 + 那段 ⚠️ 警告 + Custom GPT Instructions 第 4 条
- `分析/METHOD_FAMILY_HANDOFF.md` 的 `audit_outcome` 与 `lifecycle`

**当前可用六份**：第一批 / 微分方程 / 级数 / 多元微分 / 中值定理 / 空间几何。
**仍隔离三份**：一元微分学 / 一元积分学 / 重积分。

---

## 七、codex 怎么用

它在本机、有推送权限、干得不错（第三轮四条全采纳且 integrator 无需补充）。
给它派活的模板见三份已有派工单。**要点**：

- 自开分支，别推 integrator 的分支
- 只动目标族一个文件
- 不得改任何族的 `status`，不得自行改 `cell_status`
- 禁读 `solutions/`；**2024–2026 三年是用户的模考卷，题面不许去 `papers/` 翻**
- 报告写 `分析/审查/`（append-only），更新看板自己那一行

**下一步直接可用**：`分析/协作/派工-codex-2026-08-29-第四轮.md`（diff1v）已就绪，把仓库地址 + 分支发给它即可开工。
