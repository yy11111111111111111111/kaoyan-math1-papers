# 给 claude-series 的命令

seq: 1

```yaml
- id: CMD-1001
  issued_at: 2026-08-28
  to: claude-series
  supersedes: null
  kind: clarification
  body: >
    你上报的 3 处 recovered_state 不一致已核实，**全部属实，坑在 integrator
    这边，已于 eef6d69 修复**。你没有自行对齐而是停下报告，是正确的。
    裁定：① §10 的 calc.ode.route-selection 派工是上一个 agent 的残留，
    与你无关；② 「三族全部冻结」是错的，见 CMD-0003；
    ③ 分支名差异不算 inconsistency，见 CMD-0001。
    请 git pull 后重读 AGENT_COLLAB_PROMPT.md 与 METHOD_FAMILY_HANDOFF.md，
    然后开工。

- id: CMD-1002
  issued_at: 2026-08-28
  to: claude-series
  supersedes: null
  kind: scope_change
  body: >
    你的 scope 是 **33 题**，family_id `calc.series.route-selection`，
    产出 `分析/方法族-高数-级数.md`。三条归属裁定（详见 HANDOFF 的
    scope_boundary_rule）：
    ① **2014-19 不属于你**——次考点虽是「正项级数敛散性的比较判别法」，
       但主考点是「夹逼准则求极限」，归已冻结的 limit 族；
    ② 2019-3 属于你（主考点「级数敛散性的判定与反例」）；
    ③ 你与多元微分族实测重叠 **0 题**，不必担心撞车。
    若你认为某题主考点标错了，**不要自行改归属**，写进报告的
    open_questions 由 integrator 裁定——TSV 是人工标注层，改它会影响
    全部下游统计。
```
