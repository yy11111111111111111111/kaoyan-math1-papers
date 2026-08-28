# 广播命令（所有 agent）

seq: 3

```yaml
- id: CMD-0001
  issued_at: 2026-08-28
  to: ALL
  supersedes: null
  kind: clarification
  body: >
    分支名以 `git rev-parse --abbrev-ref HEAD` 现取为准。云端会话的分支由
    harness 分配，与看板上预写的名字不同**不算 inconsistency**——
    把实际分支名写回看板你那一行即可，不要为此停下。

- id: CMD-0002
  issued_at: 2026-08-28
  to: ALL
  supersedes: null
  kind: clarification
  body: >
    `AGENT_COLLAB_PROMPT.md` §10 在 eef6d69 之前内联过一份过时派工
    （calc.ode.route-selection / scope 40）。那是给上一个 agent 的残留。
    §10 现已不写派工：**派工的唯一权威来源是
    `分析/METHOD_FAMILY_HANDOFF.md` 的 `batch2_plan`**，题目归属见同文件的
    `scope_boundary_rule`。若你在 eef6d69 之前读过 §10，请重读。

- id: CMD-0003
  issued_at: 2026-08-28
  to: ALL
  supersedes: null
  kind: clarification
  body: >
    batch1 的 `lifecycle: closed` 指**批次不再迭代**，不等于三族都冻结。
    limit 与 extrema 是 frozen，**vector 是 active**。以
    `分析/方法族-高数-第一批.md` frontmatter 的 `freeze_status` 为准。
    无论哪种，batch1 的三族你都不要动。

- id: CMD-0004
  issued_at: 2026-08-28
  to: ALL
  supersedes: null
  kind: clarification
  body: >
    **被 interrupt 的含义已约定**：它是门铃，不是「停下等人」。
    无伴随人类指令的 interrupt = 立刻拉本分支、按 id 执行未执行的命令、
    继续原任务。详见本分支 README 与
    `分析/AGENT_COLLAB_PROMPT.md` §8.4。
    拉取时机因此增为五个：启动后 / 每次 commit 前 / 被卡住时 /
    宣布交付前 / **被 interrupt 之后**。

- id: CMD-0005
  issued_at: 2026-08-28
  to: ALL
  supersedes: null
  kind: priority_change
  body: >
    **账号的七日额度已进入 allowed_warning。**三个 Opus 会话在并行消耗同一份额度。
    请据此调整：优先**交付**而非打磨。达到 11 项 completion_criteria 就交付，
    不要为 backlog 项多跑一轮；不要为「还能更完善」重写已成型的小节；
    不要做重复的数值验证。这与既有 stop_rule 方向一致，只是现在有了硬约束。
    若你判断额度不足以完成整个任务，**先把已完成的部分 commit + push**，
    在看板你那一行的 waiting_for 写明「额度中断，已完成到 X」，
    不要留半成品在本地——那正是本项目此前丢过一次工作的原因。
```
