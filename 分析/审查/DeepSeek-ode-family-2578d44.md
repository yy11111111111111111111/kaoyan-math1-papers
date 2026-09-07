---
doc_id: deepseek.reports.ode-family.2578d44
schema: CALC-METHOD-FAMILY-v1.3.1
written_at: 2026-08-28
---

# DeepSeek 交付报告：calc.ode.route-selection（Batch 2 主执行）

```yaml
task_id: batch2.ode.family_construction
role: primary_executor        # 非 reviewer：本报告对应「创建」而非「独立审查」

artifact_identity:
  branch: deepseek/ode-family           # 见 分析/协作/看板.md 中 name: deepseek-ode-family 一行
  head: 2578d44                          # 我实际读取的内容基线（含全部 batch2 文件）
  note: >
    开工基线 = 2578d44。收工前按用户指示 git pull 了仓库更新（origin 分支
    2578d44..69d5df1，仅涉及 分析/协作/ 与 分析/DEEPSEEK_COLLAB_PROMPT.md、
    METHOD_FAMILY_HANDOFF.md），fast-forward 合入；协作类更新不涉及 ODE 内容，
    方法族判定与解法推断不受影响。分支 tip = 69d5df1 + 本次交付 commit。

scope_checked:
  declared: 2004–2026 数学一，扣 2022（与 CLAUDE.md §7 生效范围一致）
  problems_declared: 40                # batch2_plan.scope_problems
  problems_verified: 34                # 实测
  breakdown:
    core: 31                           # 一阶 14 + 二阶 17（若干题多标签重叠）
    series_boundary: 3                 # 2007-20、2013-16、2020-17：主路由归级数族
  scope_note: >
    40 是排期估计，未经题面实点。实测 34（考点频次 + 高数方法速查 §10 + 逐题题面
    核对）。差异如实上报，不虚增；级数-ODE 边界题的 ODE 子步骤已在本族注明归属。

findings:
  blockers: []                          # 四类 direct blocker 均未触发（见 §3 正文）
  non_blocking:
    - "scope_problems 40 vs 实测 34 的出入（见上）"
    - "2026-18 的 (1) 问在 待确认.md §2.1 有存疑标记（f″(u)−f(u)=Cu 与常规
       f″+f′/u=1/u 不符）；本族 mapping 中只作形式描述，evidentiary_weight: none"
    - "A4 全微分/积分因子、B5 缺 x 可降阶、B6 已知一特解、B8 变系数逆向：2004–2026
       无真题主解（historical_instance: not_found），按 §5 口径**不构成排除理由**，保留"
  candidate_routes:
    cell_routes:
      first_order_linear: "A0 建模 → A1 可分离（齐次特例）/ A2 积分因子公式 / A6 一阶逆向"
      first_order_nonlinear: "A0 建模 → A1 可分离 / A3 代换（齐次型·伯努利·ax+by+c）/ A4 全微分"
      second_order_reducible: "B4 缺 y（p=y′(x)）/ B5 缺 x（p=y′(y)，y″=p·dp/dy）"
      second_order_linear_constant_homogeneous: "B1 特征方程三型 / B7 逆向（2008-3 三阶）"
      second_order_linear_constant_nonhomogeneous: "B2 待定系数 / B7 逆向（三解·特解反推·联立）"
      second_order_linear_variable: "B3 欧拉（x=e^t）/ B6 已知一特解降阶 / B8 Wronskian 逆向"
    router_delta_vs_suggestion: >
      采纳建议链 阶数→线性→常数→齐次，做两处修正：
      ① 一阶非线性按「形式」在二级细分（可分离/齐次型/伯努利/ax+by+c/全微分）；
      ② 二阶**先查缺项信号再查线性**（2006-18 线性却走可降阶，先分线性会漏解）。
  rejected_routes:
    - { route: 常数变易法（一阶与二阶）, reason: out_of_scope, note: 数学一大纲只列通解公式与待定系数；常数变易不考 }
    - { route: 幂级数解法, reason: out_of_scope, note: 归属 calc.series.route-selection；真题 2007-20/2013-16/2020-17 均以级数题出现 }
    - { route: 伯努利 n=0 / n=1, reason: duplicate_mechanism, note: 分别即一阶线性（A2）与可分离（A1） }
    - { route: 三阶直接积分形 y‴=f(x), reason: duplicate_mechanism, note: 缺 y 的连续两次应用（B4 的 local_operation 链） }
    - { route: 特征方程法用于变系数, reason: invalid, note: 特征根变成 x 的函数无意义（F1） }
    - { route: 变系数一般通解公式, reason: invalid, note: 无闭式解；只有欧拉/已知一特解/幂级数三类受限 route }
    - { route: 一阶线性右端按待定系数设特解, reason: invalid, note: 二阶常系数非齐次的方法，一阶无特征方程 }
    - { route: 一阶非线性幂级数解 / Clairaut 奇异解理论 / 常微分方程组 / 数值解法 / 稳定性理论, reason: out_of_scope, note: 超大纲 }
    - { route: "右端 tan x、sec x、ln x 的一般处理", reason: out_of_scope, note: 需常数变易，数学一不考（F8 边界写明） }
    - { route: 可降阶用于常系数（y″+y′=0 也走 B4）, reason: dominated_not_excluded, note: 合法保留，常系数时特征方程更省（F9 loses_advantage） }

counter_witnesses:
  verified:
    - "F1 变系数误用特征方程（y″+xy′=0 → 特征根 −x 非常数）：invalidates，构造验证"
    - "F2 待定系数漏乘 x^k（y″−2y′+y=e^x：Ae^x、Axe^x 都恒零，须 Ax²e^x）：invalidates，构造验证"
    - "F3 欧拉漏 −D（x²y″ 误写 D²y）：invalidates，以 2004-4 构造验证"
    - "F4 可分离漏 g(y)=0（y′=y², y(0)=0：分离公式无解，真解 y≡0）：becomes_inconclusive，构造验证"
    - "F5 缺 x 误用缺 y 换元（y″=2yy′：p′=2yp 降阶不彻底）：becomes_inconclusive，构造验证"
    - "F6 逆向用于非线性（y′=y² 两解之差非常数，非齐次解）：invalidates，构造验证"
    - "F7 逆向解不足（二阶非齐次仅 2 解 → 只定一个特征根，方程不确定）：becomes_inconclusive，proof"
    - "F8 待定系数用于非特殊右端（y″+y=tan x：设特解恒为零）：becomes_inconclusive，构造验证"
    - "F9 常系数上可降阶（y″+y′=0 双解合法）：loses_advantage，构造验证"
    - "F10 正向→逆向设问切换（2009-10 同题两方向、2013-10 三解无法正向表达）：changes_branch，proof"
  pending: []

guard_audit:
  necessary: [一阶线性须化标准形且 P、Q 连续可积, 可分离须写 f(x)g(y) 且补检常数解, 齐次型/伯努利结构识别, 全微分须 M_y=N_x 或积分因子, 特征方程只用于常系数, 待定系数须右端可待定且乘 x^k, 欧拉须用 D(D−1) 替换表, 可降阶换元须匹配缺项类型, 逆向只对线性且解数足够]
  sufficient: [M_y=N_x 且单连通是势函数法充分条件, 二阶常系数非齐次已知 3 解足以定全通解]
  supporting_heuristic: [二阶先扫缺项信号再谈线性, 欧拉形立即换元, 常系数非齐次优先待定系数, 应用题先列方程]
  note: 效率偏好一律按 supporting_heuristic 处理，未写成合法性条件。

source_evidence:
  bases: [解法.md(unverified_inference), 高数方法速查.md §10(human_synthesis), 高数逐考点认知模型.md 模块10(human_synthesis), independent_route_generation(human_synthesis), 高数真题题面_2004-2023.md(human_annotation), papers/2024考研数学一真题+答案.md, papers/2025年数学一真题.md, papers/2026年考研数学一真题.md]
  evidentiary_weight: none              # 题面库 source_status 为 ocr_uncertain，全部 positive-instance 均不升为 witness
  annotation_dependence: material
  derivation: human_synthesis

recommended_changes:
  - "open items 全部按 backlog 处理（record_to_backlog / reopen_family: false），详见方法族文件每格 open_items"
  - "级数-ODE 边界 3 题（2007-20、2013-16、2020-17）待 calc.series.route-selection 建好后复核归属"
  - "建议 reviewer 复核两处 router 修正（一阶非线性细分、二阶缺项优先）的合法性，以及 F7/F10 两个 proof 型 witness"

status_recommendation:
  recommendation: keep_candidate         # 只做 recommendation，不自行升级
  note: 六格 route_scan_status 全为 complete_within_declared_universe；global_exhaustiveness 常设 not_established

confidence_limits:
  not_checked:
    - 第二轮独立重扫（每格只做单轮结构穷举）
    - 外部教材/大纲路线的系统清单比对
    - 数值/符号验证（witness 均为解析构造）
    - B5/B6/B8 无真题实例的适用性只能靠结构论证
  search_budget: 每格单轮结构穷举 + 既有 action 适用性逐条比对 + 每条新 route 构造 failure boundary

files_changed:
  - 分析/方法族-高数-微分方程.md      # 新建：calc.ode.route-selection（主产出）
  - 分析/tests/lint_method_families.py # 修改：DOC 改为 DOCS，扫描 batch1 + 本族两个文件
  - 分析/协作/看板.md                  # 修改：更新 deepseek-ode-family 一行
  - 分析/审查/DeepSeek-ode-family-2578d44.md  # 本报告
```
