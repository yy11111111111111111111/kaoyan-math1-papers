# 广播命令（所有 agent）

seq: 1

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
```
