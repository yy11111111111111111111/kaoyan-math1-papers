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
