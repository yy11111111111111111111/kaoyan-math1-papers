# 独立定向复核 · mvt A5 有限递归

```yaml
reviewer: review-agent-b（独立复核方，未参与本族修复）
mode: pure_read_only
files_changed: []
review_chain: [4541f65, c740d08, 30bc823, 1a14c47]
final_artifact: 1a14c47
lint: PASS · error 0 · warning 4
git_diff_check: PASS
final_verdict: confirmed_fixed
solutions_read: false
papers_2024_2026_read: false
```

## 发现与迭代

首轮附审判原条件“存在有限阶 n 使 F^(n) 可定号”为事后存在性入口，缺少有限预算与
可执行失败出口，属于 B4 executable-semantics blocker。integrator 接受并将本族暂降
challenged/quarantine。

后续三次只读复核依次发现并由 integrator 按处方修正：递归状态未推进/失败补集不全/
local operation 伪装 action dispatch；预算 off-by-one 与 success/failure 顺序；
失败补集遗漏“子调用成功但当前层仍无法定号”以及直接入口未定义 F。

## 最终 confirmed_fixed 依据

- 直接进入 A5 时显式构造 `F=左边−右边`；由 A2 传入时接收其 target，所有入口均定义 F。
- 最外层初始化 `{root_target,G₀=F,k=0,N≥1}`；递归子调用继承同一 N/root_target。
- 每层先计算 `G_{k+1}` 并判 success；仅在尚未成功、`k+1<N` 且下一层入口成立时递归。
- 递归前严格执行 `k:=k+1`，排除无限递归和预算越界。
- 子调用成功后显式向上回传，直到 `G₀=F`；只有成功回传到根才满足 terminal。
- 所有成功、递归与回传处理后仍未 `A5_succeeded`，即完整标记 `A5_failed`，无静默结束。
- 失败后 A7/A6 是真实 action_ref，target 为原始 `root_target`；两者均不适用则非终结返回 router。
- A5 applies、N1、counter-witness 与 fallback 已同步。

## 最终建议

该 blocker `confirmed_fixed`，本族可恢复 candidate；inequality cell 与族级 route scan 可恢复
`complete_within_declared_universe`，解除 quarantine。四条 lint warning 均为 frozen extrema 的既有 S3 欠账。

## 限制

缺少《00_数学教学_启动入口.md》，无法执行其动作路由；本次未读 papers、solutions 或修复方报告。
