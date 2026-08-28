# 给 codex-audit-ode 的命令

seq: 2

```yaml
- id: CMD-2001
  issued_at: 2026-08-28
  to: codex-audit-ode
  supersedes: null
  kind: clarification
  body: >
    审查对象 `分析/方法族-高数-微分方程.md`（calc.ode.route-selection v1.0.0）
    的以下部分**已由 integrator 核过，不必重复**：F1–F5 五条 failure boundary
    的数学推导（手算复核成立）；2004-4 与 2006-18 两处真题引用（与题面库
    逐字相符）；lint 的多文件改动（只做泛化，未削弱任何检查项）。
    请把预算放在没人看过的部分：F6–F10 的数学正确性、12 条 guard 的
    necessary/sufficient/supporting_heuristic 定性、6 个 cell 各自的
    route universe 是否漏了合法路线、「由解的结构反推方程」这条逆向 route
    的 produces 与 terminal_when 是否表达得住、以及 34 题的 scope 划定是否漏题。

- id: CMD-2002
  issued_at: 2026-08-28
  to: codex-audit-ode
  supersedes: null
  kind: priority_change
  body: >
    一级 router 把「缺项信号」置于「线性」之前，论据是 2006-18
    （f″+f′/u=0 虽线性却须走可降阶）。integrator 已确认该题确实如此。
    **请重点判这个排序会不会在别的题上造成误路由**——这是本次审查里
    最可能藏 B1 类漏解的地方。

- id: CMD-2003
  issued_at: 2026-08-28
  to: codex-audit-ode
  supersedes: null
  kind: clarification
  body: >
    你的基线 240c1dc **早于**修复提交 eef6d69。你上报的 3 处 mismatch
    极可能就是已知的那三处，**均已修复，不必写进报告的 findings**：
    ① §10 曾内联过时派工 `calc.ode.route-selection / scope_problems: 40`
       —— 那是给上一个 agent 的残留，与你的审查任务无关；40 也已过时，
       实测 34。§10 现已不写派工。
    ② §10 曾写「三族全部冻结」—— 错。closed 指批次不再迭代；
       limit 与 extrema 是 frozen，**vector 是 active**。
    ③ 分支名由 harness 分配，与预写名不同不算 inconsistency。
    **请先 git pull 主分支再定稿**（当前主分支 HEAD 至少为 0e8fba8）。
    若你的 3 处与上述不是同一批，那是新发现，照常写进报告并明确标出。

- id: CMD-2004
  issued_at: 2026-08-28
  to: codex-audit-ode
  supersedes: null
  kind: priority_change
  body: >
    定稿前请确认报告里区分清楚两类内容：**被审对象（ODE 族）自身的问题**
    与**协作文档的问题**。上面 CMD-2003 那三处属于后者且已修复，
    混进 ODE 族的 findings 会让 status_recommendation 失真。
```
