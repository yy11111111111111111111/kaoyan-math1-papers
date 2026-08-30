# codex 接管 integrator 的任务书

```yaml
issued_at: 2026-08-29
issued_by: claude-code-remote（离任 integrator）
to: codex（本机，有 GitHub 推送权限，可派子 agent）
change: codex 由「执行方」升为「执行方 + integrator」，独立复核由**它自己派的子 agent**承担
```

## ⚠️ 这次变更最大的风险：独立性坍缩

此前的流程之所以能抓出错，是因为**三个角色由三方担任**：建族 / 修复 / 复核。
现在你一人兼两职、第三职由你的子 agent 担任 —— **独立性比之前弱**。
项目里已经有两次血的教训，都发生在「同一方既做又判」的时候：

- batch3 五族最初被判有罪，原因就是**建族方同时是 integrator**；
- 上一任 integrator 落完修复后没人复核，交叉复核查出**两处半修复**（只改 guard 文本、
  没改真正决定可用性的 `applies_when` / `followup` / `terminal_when`）和**一处自己引入的越 schema 字段**。

所以你必须做到三条，否则这套流程就白建了：

1. **修复与复核必须是不同的子 agent。** 派去做 `confirmed_fixed` 复核的那个，
   **不得**是本轮修过该族的那个，也不得读过你的修复过程。给它干净的任务书，让它自己读文件。
2. **你不得替复核方下结论。** 复核方说 `not_fixed`，你就得改；你不同意，
   **把分歧写进裁定报告**，而不是压下去。上一任的做法可参照
   `分析/审查/claude-adjudication-codex-lint-hardening-6b5a7e1.md`
   ——那次 integrator 驳回了一条规则，但明写「**这是我自己的规格错误，不是执行方的实现错误**」。
3. **报告里如实写「这一轮谁改的、谁复核的」。** 若某一步实际上没有独立第三方，
   就写明「本轮该环节独立性不足」，不要粉饰。

---

## 一、先读什么

```bash
git clone -b claude/batch3-parallel-family-audit-ekzi6c \
  https://github.com/yy11111111111111111111/kaoyan-math1-papers.git
cd kaoyan-math1-papers
git rev-parse --short HEAD
python3 分析/tests/lint_method_families.py      # 基线：error 0 · warning 4
```

> ⚠️ **必须带 `-b`。`main` 上 `分析/` 下一个文件都没有。**

按序读：
1. `分析/协作/交接-integrator.md` —— **最重要**，剩余量、流程模板、六个坑、五条待裁定项
2. `CLAUDE.md` —— 唯一规则来源
3. `分析/METHOD_FAMILY_HANDOFF.md` —— 四类 blocker、`open_blocker_summary`、三条教训
4. 范本各一份：`分析/审查/claude-adjudication-codex-geom-route-completion-4bfd8e1.md`（裁定）、
   `分析/审查/claude-review-geom-confirmed-fixed-180fe5f.md`（复核）

## 二、要做的：三族 11 条 blocker

| 族 | blocker | 派工单 |
|---|---|---|
| 一元微分学 | 4（BL-1/2/3/5） | ✅ `派工-codex-2026-08-29-第四轮.md` 已就绪 |
| 一元积分学 | 4（BLK-1/2/4/6） | 你自己写 |
| 重积分 | 3（BL-1/2/4） | 你自己写 |

已闭环:中值定理、空间几何(均 `candidate`)。四条的完整论证在
`分析/审查/claude-audit-batch3-*-a635bd6.md` 对应那份里。

## 三、每族一个循环

```
① 你修（只动该族一个文件）
② 派子 agent 做 confirmed_fixed 复核 —— 必须是没参与本轮修复的那个
③ 你按复核方的处方落地 + 写裁定报告（分歧照写）
④ status challenged → candidate、解除 quarantine、bump doc_version、
   追加 status_history、归档复核报告
⑤ 同步四处：METHOD_FAMILY_HANDOFF / 协作/看板.md /
   交接说明-教学AI §2.3 / GPT接入包（档 3 + 那段 ⚠️ + Instructions 第 4 条）
⑥ lint 必须 error 0
```

## 四、三条教训，逐字带进每份子 agent 任务书

- **L-1** 改一条结论 ⇒ grep 它在 `failure_boundary` / `local_operation` / `minimal_probe` /
  `route_scan`（`route_universe`、`existing_routes`、`counter_witness_search`、`stop_rule`）的**全部出现点**。
- **L-2** **lint 与内容判断冲突时留红并写进报告，不得改内容迁就 lint。**
  （第一轮派工单写死「必须 error 0」，把你逼到删掉一条合法路线让 lint 变绿 —— 那是派工方的错。）
- **L-3** 结论必须落在**可执行字段**（`followup` 的 `local_operation` / `action_ref`、
  `applies_when`、`terminal_when`）；`note` / `explanation` / `description` **只能复述、不得独家承载**。
  > **验收法：遮住所有 note，只看可执行字段，看 route 能不能走通。** 这是两次复核的核心判据。

## 五、你必须自己裁定的五件事

1. **`minimal_probe` 在遮 note 自检时算不算「可见」？** 两次复核都按「可见」办，
   但 geom 复核方明说：**若它也被遮蔽，2026-11 存在被 A5 接住并算成 3 的错误路径**。
   **在给子 agent 的任务书里写死你的选择**，否则三族的复核标准不一致。
2. **`mint BL-3` 已补完但从未独立复核**（你第一轮补的 `A3.applies_when`）。
   **重积分那轮的复核必须把它一并纳入。**
3. **diff1v BL-1 的归属**：2015-16 / 2023-17 / 2012-18 是「由切线条件反求 f」，实际要建解 ODE。
   按主考点归 diff1v，解法主体在 `calc.ode`。只补「反求切点」这一步，归属你定，写进报告。
4. **mvt 的 A5 自递归 `when`** 措辞「且存在有限阶 n 使 F^{(n)} 可定号」**可能过强**
   （把存在性断言塞进了执行条件）—— 上一任拟的，请顺带扫一眼。
5. **int1v 与重积分的派工单**由你写；照 `第四轮` 那份的骨架即可。

## 六、红线（越过就是越权）

- **`challenged → candidate` 是 integrator 权限**（恢复到 `author_upgrade_ceiling`）；
  **`candidate` 以上是 `GPT_only`**，你不得自升。
- **`分析/方法族-高数-第一批.md` 是 `frozen`**（limit / vector / extrema）。
  diff1v 的 BL-5 涉及 limit 族的 `exclusions`，**修法是本族自理，不许动 limit 族**。
- **禁读 `solutions/`**（CLAUDE.md 红线）。
- **2024 / 2025 / 2026 三年是用户的模考卷**：题面不许去 `papers/` 翻，也不要在报告里展开题干。
  需要的构造都已在审查报告里。另：`papers/2026` 对 2026-11 的 OCR 解析给出 "1+z"，
  **经两次独立复算判定为错**（正确为 0），不要采信。
- **只动目标族一个文件**（外加你的报告与看板行）。

## 七、几个会绊住你的坑

1. **别自己发明 lint 规则就上。** 上一任把交叉复核建议的 R3 照单收下写进派工单，
   结果它在 11 族上报出 13 条、多数是误报（`eligible_cells` 是**入口集**，
   强制后继天然落在入口集之外），整条驳回，还连累你删了内容。
   **新规则先在全部现有 artifact 上试跑一遍。**
2. **YAML**：序列项不能以 `*` 开头（别名标记），要加引号；
   往 `exclusions:` 这类列表中间插 mapping 键会截断后续条目。
3. **新增 boundary 后要同步 `constructed_counterexamples` 索引**，否则 lint 报 `evidence 索引缺 [...]`。
4. **改完记得回头看 `§N 当前未解决的`**：里面常年写着「无独立审查」，闭环后就是假陈述；
   H1 标题的版本号也要和 frontmatter 对齐 —— 这两处两次复核都点过名。

## 八、收工

三族全部闭环后：
- `METHOD_FAMILY_HANDOFF.md` 的 `batch3_plan.lifecycle` 改为全部恢复
- `交接说明-教学AI.md` §2.3 的隔离名单清空，九族全部可用
- 在 `分析/审查/` 留一份收口报告，写清三族各自的 blocker 去向与复核方
