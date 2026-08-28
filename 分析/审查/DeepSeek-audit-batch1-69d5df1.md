# DeepSeek 独立审查报告：batch1

```yaml
task_id: batch1.independent_audit
role: independent_reviewer

artifact_identity:
  branch: claude/postgraduate-math-exam-analysis-czoi3t
  head: 69d5df1
  head_note: >
    任务书初给 HEAD 为 a997650；开工后用户提示仓库有更新，git pull 到 69d5df1
    （新增 分析/协作/看板.md，更新 DEEPSEEK_COLLAB_PROMPT.md 与 HANDOFF）。
    被审对象 分析/方法族-高数-第一批.md 在两版 HEAD 间未变，审查内容对两版 HEAD 均成立。
    本报告按 §9 约定写**实际读的 commit**：69d5df1。
  doc_version: 3.5.1
  schema_version: CALC-METHOD-FAMILY-v1.3.1

scope_checked:
  - 分析/方法族-高数-第一批.md 三族全部（limit / vector-integral / extrema）
  - 三族所有 failure_boundaries 的 witness 数学真值（逐条数值独立复核）
  - 三个第二类 cell 的 route universe 独立枚举（先不看现有候选集，枚举后做差集）
  - 所有 guard 的 necessary / sufficient / supporting_heuristic 定性
  - action reachability（action_ref 可达性）与 eligible_cells 一致性
  - source mapping 越权检查
  - revision_history / status_history 中「已更正」旧语义是否在正文残留

findings:
  blockers: []        # 未发现 B1–B4
  non_blocking:
    - id: NB-1
      severity: medium（reachability 缺陷，非 blocker）
      what: >
        A10（载体方程代入）的 followup_actions 只有「定理（闭合）/ 补域（不闭合）」
        两类后继，缺三条合法边：A5l（平面挖奇点）、A5s（曲面挖奇点）、A4c（空间补线）。
        其 substitution_scope_note 却明确声称「进入任一 theorem / 补域 / 挖奇点框架之后……
        必须一律使用同一个场」，并提及「补面 Σ₀ / 补线段、体域 V / 平面区域 D、挖洞后的剩余区域」。
        即：note 覆盖了挖奇点框架与空间补线，但 followup 无法路由到它们——内部不一致。
      consequence: >
        router 无法表达「A10 替换 → A5l/A5s/A4c」组合路线。学生只得放弃替换、
        改用原场 F 直接走 framework（合法，但损失 A10 的化简价值）。无漏解（A1 与各
        framework 可独立进入），无错误结论。
      blocker_classification: >
        不构成 B1（scope 内题目无漏解，A1 兜底）；不满足 B4 字面定义
        （无 action_ref 指向不存在 / 无 mandatory continuation 悬空 / 无旧语义残留 /
        无 provenance 升级）。判定为 reachability 完整性缺陷，归 non-blocking。
      note: lint R2 只校验「cell 清单 ↔ eligible_cells」双向一致，无法捕获
        「followup 分支 ↔ framework action 对应关系」这类缺边。本缺口即是一例。
    - id: NB-2
      severity: low（wording / 证据量）
      what: >
        A10 的 substitution_scope_note 声称 B7 的错误模式对 Green（A3g/A4l/A5l）与
        Stokes（A3s/A4c）「逐字成立」。机制层面**成立**：B7 的错误源自「替换只在载体上
        成立」，与用哪条定理无关；我的独立复核确认该论证对平面 Green 与空间 Stokes
        同样适用（替换后场 F̃ 在补线段/补面/剩余区域上 ≠ F，混用即错）。但「逐字成立」
        目前是分析性论断，B7 的 verified witness 只在曲面格构造，平面/空间格未逐字
        构造数字反例。
      blocker_classification: 不构成 blocker（数学正确，仅证据量问题），backlog 级。
    - id: NB-3
      severity: low（标签误导，wording 类）
      what: >
        complete_within_declared_universe 的二分在机制上站得住：11 项 completion_criteria
        是过程标准（扫描协议跑完），global_exhaustiveness: not_established 承载「不可能
        再有别的路线」这一实质主张，作者在 route_scan_status_note 与 completeness_reasoning
        中已明确定义，未用定义规避实质问题。但「complete」标签本身有过强暗示，且
        v3.4.0 / v3.5.0 连续两轮各扫出 5 条与 2+1 条新 route（surface 格还自认
        「扫描前覆盖判断失准」），该状态的历史可靠性低。
      blocker_classification: 不构成 blocker（wording 类）。建议在 HANDOFF / evidence
        中强化「最近两轮扫描均产出新 route」的醒目警示。
    - id: NB-4
      severity: low（搜索预算偏浅，backlog）
      what: >
        limit 的 A7a-∞^0 not_found 仅 1 个数值例子（x^(1/x)）。诚实但浅：幂指取对数在
        ∞^0 型上结构上无风险（底→∞ 的去心邻域恒正），not_found 合理；但未系统覆盖
        0^0 / 1^∞ 边界（如底不恒正的去心邻域）与 0·∞ 子型。A7a 的 applies_when
        「原式在去心邻域为正」已兜底，故非 blocker，仅搜索预算可扩充。
      blocker_classification: backlog（可加数值抽样覆盖），不构成 blocker。
      vector 侧：A3s 的支撑记为 theorem_instantiation（v3.3.0 已从 not_found 更正），
      证据类型正确。

  candidate_routes: []        # 三格独立枚举差集为空，见下方「独立 route universe 枚举」
  rejected_routes: []         # 未新增排除；空间「挖奇点」经独立分析确认 duplicate_mechanism
                              # 判定成立（理由见下方专项复核 ③）

counter_witnesses:
  verified: []                # 未发现击穿任何 guard / mechanism / boundary 的 direct counter-witness
  pending: []
  verification_summary: >
    对所有关键 witness 做了独立数值复核（脚本存于审查者工作区，41/42 项通过；
    唯一 FAIL 为容差设置问题，数学成立）。全部通过项见下方「witness 数值复核」。

guard_audit:
  limit:
    - { guard: "A1 乘除上下文定义域条件", 定性: necessary, 理由: "h 非零是 E=u·h 有定义的必然前提；「不需要 E 与 u 同阶」正确——约去 h 后只剩 v/u → 1，与 E、u 量级无关。这是等价无穷小定义的一部分，必要且充分的前提" }
    - { guard: "A1 加减上下文 u−v=o(E)",  定性: sufficient, 理由: "Ẽ−E = v−u = o(E) ⟹ Ẽ~E（E≠0 时）。不声称必要：更高精度替换或数值巧合仍可正确。定性正确" }
    - { guard: "A3 洛必达四条",            定性: necessary, 理由: "定理前提，逐条必要" }
    - { guard: "A3 不可直接用于数列",      定性: necessary, 理由: "n 不可导" }
    - { guard: "A5 递推数列单调有界+连续+选不动点", 定性: necessary, 理由: "递推取极限的定理前提" }
    - { guard: "A8 Riemann 和四条件",      定性: necessary, 理由: "L-adv4 已验证区间固定性；四条件是 Riemann 和收敛的实质前提" }
    - { guard: "A2 展开到第一个非零主项",  定性: supporting_heuristic, 理由: "效率指导，不是合法性条件" }
  vector:
    - { guard: "先完成一级分类",           定性: necessary, 理由: "对象分类是路由前提" }
    - { guard: "A3g/A3G 闭合、A3s 只 L 闭合", 定性: necessary, 理由: "三定理闭合要求不同，分写正确" }
    - { guard: "A4/A5 完整闭边界+同一诱导定向", 定性: necessary, 理由: "挖奇点题差负号的高发处；v2 的「统一取外侧」对有洞区域会误导，已分 Green（内洞顺时针）/Gauss（小球内法向）" }
    - { guard: "场光滑性无奇点",           定性: necessary, 理由: "B1（∮=2π vs ∬0=0）证明该 guard 非装饰" }
    - { guard: "A5 奇点可隔离四项 guard",  定性: necessary, 理由: "非点状 singular set 不自动套用挖洞结构" }
    - { guard: "A6 全局势函数",            定性: necessary, 理由: "B9 的场 rot=0 但无单值全局 φ，A6 不适用" }
    - { guard: "∂P/∂y=∂Q/∂x 且单连通是 A6 充分条件", 定性: sufficient, 理由: "v1 错标 necessary 已改；环域 F=(2x,2y) 反例证明非必要，定性正确" }
    - { guard: "A10 进入 theorem/补域后同一场", 定性: necessary, 理由: "B7 两种混用分别给 π/2 与 3π/2，验证必要" }
    - { guard: "A1q 逐项单值分片+逐片定号", 定性: necessary, 理由: "B8 缺分片给 2π/3（差一半），分片同号给 0" }
    - { guard: "A12 div F≡0 于夹区且无奇点", 定性: necessary, 理由: "区域有奇点换面不成立，正是 A5s 存在的理由" }
    - { guard: "A6p rot F=0 于夹区且无奇点", 定性: necessary, 理由: "B9 证明「两路径各自避开奇点」不蕴含「夹区无奇点」" }
    - { guard: "A6p 与 A6 并列不可互推",   定性: necessary, 理由: "去心平面 F 无全局 φ（A6 不适用）但夹区无奇点时 A6p 适用" }
    - { guard: "A4c 另加 A3s 五条准入",    定性: necessary, 理由: "补线只解决不闭合，不解决所张曲面可用性；两要求独立" }
    - { guard: "A11 ∇·F≡0 必要、可缩区域充分", 定性: necessary, 理由: "旋度场必要条件" }
    - { guard: "A13 非严格/严格不等号",    定性: necessary, 理由: "≥0 只给 ≥0；严格正需正测度子集" }
    - { guard: "A2 四步 pullback 核对",    定性: necessary, 理由: "B5 覆盖四项缺一即失效" }
    - { guard: "补面垂直坐标轴",           定性: supporting_heuristic, 理由: "效率偏好，非合法性" }
  extrema:
    - { guard: "A1 二阶偏导连续",          定性: necessary, 理由: "AC−B² 判别前提" }
    - { guard: "AC−B²=0 无结论",           定性: necessary, 理由: "B1 两例判别式同零但结论相反" }
    - { guard: "A2 正则点必要候选+按 F1 分类/比较", 定性: necessary, 理由: "E-adv6 证明全局值比较不能替代局部分类" }
    - { guard: "A2 ∇g≠0 正则性",          定性: necessary, 理由: "B3 反例 ∇f=(1,0)、∇g=(0,0) 无 λ 满足 ∇f=λ∇g" }
    - { guard: "A3 f 连续（Weierstrass）", 定性: necessary, 理由: "v1 漏掉的最重要 guard；B2c 有界闭但 f 不连续 → 无最值" }
    - { guard: "A3 有界闭",                定性: necessary, 理由: "B2a（失闭）/B2b（失界）两例" }
    - { guard: "A3 只路由 full_dimensional_region", 定性: necessary, 理由: "B7 反例：x²+y²=1 是一维约束流形，进 A3 是对象层级错误" }
    - { guard: "A3 完整搜索三部分",        定性: necessary, 理由: "B4 反例 f=x 在圆盘内部无驻点，跳过边界则错" }
    - { guard: "A4 保留取值范围",          定性: necessary, 理由: "B9 反例丢负支丢全局最小" }
    - { guard: "A6 验证取到",              定性: necessary, 理由: "估计不是最值" }
    - { guard: "F5 时 A4 通常更快",        定性: supporting_heuristic, 理由: "效率偏好" }
  结论: 三族全部 guard 定性未发现 necessary/sufficient/heuristic 串位。

source_evidence:
  - 全部 20 处 evidentiary_weight 均为 none；ocr_uncertain 题面库未被升为 witness。
  - vector B1 的 candidate_source_references（2020-16）为 possible_real_instance / pending / none，
    未越权。
  - extrema B4 的 candidate_source_references（2007-17 / 2018-16 / 2024-18）为 pending / none，
    未越权。
  - extrema B5a 的 verification_lineage 记录 v3.2 pending → GPT full-file audit 独立核验 → verified，
    provenance 透明。
  - scan_basis 中的 解法.md 均标 status: unverified_inference，未当答案权威。

recommended_changes:
  - id: RC-1
    target: vector A10 followup_actions
    priority: medium
    change: 补三条 action_ref 分支（带 when）：
      - { action_ref, action: A5s, when: "**曲面格**、singular set 可由所选小闭曲面隔离，且后续整条路线都使用替换后的场" }
      - { action_ref, action: A5l, when: "**平面曲线格**、奇异集可由所选小边界隔离，且后续整条路线都使用替换后的场" }
      - { action_ref, action: A4c, when: "**空间曲线格**、L 不闭合，且后续整条路线都使用替换后的场" }
      或：收窄 substitution_scope_note，把「挖奇点框架」从声称范围移除。
    reason: 消除 note 与 followup 的 reachability 不一致（NB-1）。
    note: 此变更不改变任何 state，不触发冻结族 reopen。
  - id: RC-2
    target: vector A10 substitution_scope_note 末句
    priority: low
    change: 把「B7 对 Green 与 Stokes 逐字成立」改为「机制层面成立（替换只在载体上成立），
      已论证适用于 Green/Stokes；未在曲线格逐字构造数字反例」或补一个平面版数字反例。
    reason: 使「逐字成立」的断言与证据量一致（NB-2）。
  - id: RC-3
    target: HANDOFF / evidence 的 route_scan_status_note
    priority: low
    change: 强化警示——「v3.4.0 与 v3.5.0 连续两轮 scan 各产出新 route，complete_within_
      declared_universe 仅表示协议过程完成，不表示覆盖判断曾经失准的风险已消失」。
    reason: 降低「complete」标签的过强暗示（NB-3）。
  - id: RC-4
    target: 分析/tests/lint_method_families.py
    priority: low
    change: 输出前 sys.stdout.reconfigure(encoding='utf-8')（或对 warn 行做 ASCII 降级），
      否则在 Windows cp1252 控制台下脚本因 ⚠/✘ 编码崩溃（本审查即遇到）。
    reason: 可移植性改进；非被审对象缺陷，不影响 lint 结论（error 0 · warning 4 已用
      PYTHONIOENCODING=utf-8 复现确认）。

status_recommendation:
  calc.limit.method-selection:          maintain partially_verified
  calc.vector-integral.route-selection: maintain candidate
  calc.extrema.constraint-selection:    maintain candidate
  challenged_recommendation: none       # 未发现 direct counter-witness
  rationale_limit_pv: >
    limit 的 partially_verified 由外部 reviewer（GPT v3.3.0 targeted revalidation）判定，
    本次独立复核支持该状态：scope 可定义、候选集多路线、核心乘除/加减 mechanism 数学上站得住
    （第四版 guard 经我独立验证正确，B1(a)/(c) 对照 verified）、关键 guard 定性无串位、
    至少一个 verified failure boundary（B1/B2）、且有明确列出的未闭合边界（中值定理转化差式
    route scan、F2b 多层嵌套判据、global_exhaustiveness not_established）。
    证据不支持降级或升级。
  rationale_vector: candidate 与「四格 complete_within_declared_universe / global_exhaustiveness
    not_established」一致；route scan 完成不构成自动升级理由。NB-1 不改变该判定。
  rationale_extrema: candidate 与 HANDOFF 一致；4 条 S3 warning 属冻结族 backlog。

# ── 独立 route universe 枚举（任务书 do 第 2 条）──

方法：先不看被审候选集，按「对被积对象做什么 × 对载体做什么」两轴独立枚举本格结构合法的
路线类型，再做差集。全部为单轮结构枚举；global_exhaustiveness 对审查者同样 not_established。

## planar_curve_second_kind
对象条件: L ∈ R² 分段光滑有向曲线（可闭可不闭）；F=(P,Q)；∫_L P dx + Q dy 或符号/是否为零。
独立枚举的路线类型（未排除项）:
  P1 参数化化定积分                      → 对应 A1
  P2 图形式（y=y(x) 或 x=x(y) 积分）      → A1 的 subroute（已并入）
  P3 载体方程代入（g(x,y)=0 改写被积）     → A10
  P4 第二类→第一类（方向余弦）单向         → A7
  P5 对称/奇偶性配对（含轮换）             → A2
  P6 补线凑闭 + Green 减补线              → A4l
  P7 挖奇点（孤立奇点/小圆；Green 剩余区域） → A5l
  P8 换路径（夹区 rot=0 且无奇点）         → A6p
  P9 势函数作差（全局单值 φ）             → A6
  P10 Green 直接（闭曲线）                → A3g
  P11 逐点定号（F·τ 不变号）             → A13
  被排除（与现有候选一致）:
  - 坐标平移/旋转/极坐标后重算            → A1 重参数化，duplicate_mechanism
  - ∮ xdy−ydx = 2·面积                   → A3g 后二重积分取常数值，duplicate_mechanism
  - 常向量场只与端点有关                  → ∇(Px+Qy)，属 A6，duplicate_mechanism
  - 分段求和 / 分片逐段                    → local_operation
  - 复变留数 / Cauchy 定理                → out_of_scope（超考纲）
  - 奇点落在 L 上的反常曲线积分           → out_of_scope（scope 未含反常积分）
  差集: 空

## spatial_curve_second_kind
对象条件: L ∈ R³ 分段光滑有向曲线（可闭可不闭）；F=(P,Q,R)；∫_L P dx+Q dy+R dz 或符号/是否为零。
独立枚举:
  S1 参数化（含图形式：x 参数化 y=y(x), z=z(x)） → A1
  S2 载体方程代入（曲面交线 g₁=0, g₂=0）        → A10
  S3 第二类→第一类单向                          → A7
  S4 对称/奇偶性                                → A2
  S5 Stokes（闭曲线 → admissible spanning surface） → A3s
  S6 补线 + Stokes（开曲线）                    → A4c
  S7 势函数作差（全局 φ）                       → A6
  S8 换路径（夹区 ∇×F=0 且无奇点）             → A6p
  S9 逐点定号（F·τ 不变号）                    → A13
  被排除:
  - 投影到坐标面逐项化为平面问题 → invalid（丢 dz 与耦合项，非效率问题）
  - 挖奇点（空间版）             → duplicate_mechanism（复核成立，见专项 ③）
  - 微分形式 / 广义 Stokes       → out_of_scope
  - 分段求和                     → local_operation
  差集: 空

## surface_second_kind
对象条件: S ∈ R³ 分片光滑可定向曲面（可闭可不闭），给一侧；F=(P,Q,R)；∬ P dydz+Q dzdx+R dxdy
或符号/是否为零。
独立枚举:
  SF1 参数化化二重积分                 → A1
  SF2 分项投影（逐项单值分片+定号）    → A1q
  SF3 合一投影（统一 dxdy）           → A8
  SF4 对称配对                        → A2
  SF5 Gauss（闭曲面）                 → A3G
  SF6 补面 + Gauss（不闭合）           → A4s
  SF7 挖奇点（小球面）                → A5s
  SF8 载体方程代入                    → A10
  SF9 第二类→第一类单向               → A7
  SF10 向量势 F=∇×G → 边界线积分      → A11
  SF11 同边界换面（div F≡0 于夹区）   → A12
  SF12 逐点定号（F·n 不变号）         → A13
  被排除:
  - 投影到不同坐标面的组合（y=y(x,z) 等作投影面）→ A1q/A1 的执行细节，duplicate_mechanism
  - 闭曲面部分 + 补面                  → A4s
  - 先转第一类再用对称性              → A7→A2 组合，duplicate_mechanism
  - 奇点在 S 上 / 反常积分             → out_of_scope
  - 数值积分 / 级数逼近                → out_of_scope
  - 微分形式统一处理                   → out_of_scope
  差集: 空

# ── 专项复核（任务书第 5 节七处）──

① B9 与 A6/A6p 的拆分
   - witness 数学：已独立数值验证（F=(−y/(x²+y²), x/(x²+y²))，上/下半圆 (1,0)→(−1,0) 得
     π / −π，差 2π；rot F≡0 于去心平面）。B9 成立。
   - 拆分是否过度：否。A6 要求「含 L 的区域上存在单值全局势函数」；A6p 只要求「两路径
     所夹区域内 rot=0 且无奇点」。两者 guard 不同（B9 的场 rot=0 但无全局 φ，A6 不适用而
     A6p 在夹区无奇点时适用）、产出不同（A6 直接给数值，A6p 只换载体仍须 A1 实算）、
     **互不蕴含**（A6 适用 ⟹ A6p 适用，但反向不成立，故非同一机制的两种写法）。拆分合理，
     不构成 B3 过度切分。open_items 已记「A6 与 A6p 之间无 preference_rule」属 backlog。
② A4c 的「非 B1 类漏解」判定
   - 判定正确。B1 的两个条件均不成立：a)「现有 router 无合法 action 接收」——A1 对任意
     可参数化曲线始终合法可用（空间分段光滑曲线必然可参数化，可核对定向）；b)「遗漏决定
     答案的合法分支」——A4c 不是唯一能得答案的分支。A4c 是效率更优的 new_route 而非 blocker。
   - 边界情形：若曲线本身无法参数化（如复杂隐式交线），A1 亦不适用，但此时 A4c/Stokes
     同样无法计算（需参数化补线后的闭曲线与曲面），属「现实可执行」限制而非结构漏洞，
     不影响判定。
③ 空间「挖奇点」被归为 duplicate_mechanism
   - 判定成立，独立佐证如下：
     · 闭曲线绕奇异线（linking number ≠ 0）：不存在避开奇异集的 admissible spanning
       surface（代数相交数 = 链接数 ≠ 0），A3s 失败；但 L 与同伦类相同的标准小圆 L′ 在
       R³∖奇异线 内同伦（同 linking number 的闭曲线同伦），两者夹的环带可避开奇异线，
       A6p 适用 → A1 在 L′ 上实算。A6p 接住。
     · 链接数 = 0：存在避开奇异集的 spanning surface，A3s 选面自由度接住。
     · rot F ≠ 0 且处处正则：A3s 总可用（任意 spanning surface admissible）。
     · 开曲线绕奇异线：A6p/A4c/A3s 均失败，但「挖奇点」本就不适用于开曲线（无围出区域
       可挖），只剩 A1 兜底——不构成漏解。
   - 结论：构造不出「A3s 选面 + A6p 同伦」两者都接不住的闭曲线情形；duplicate_mechanism
     判定成立，不是 B1。
④ A10 的 substitution_scope_note 声称 B7 对 Green 与 Stokes「逐字成立」
   - 推广成立。B7 的错误机制是「替换后的场 F̃ 只在载体上等于 F，进入补域/挖奇点框架后
     任一子积分用错场即错」，该事实与定理类型无关：平面 Green（补线段 + 区域 D）、空间
     Stokes（补线 + spanning surface）中 F̃ 同样只在 L 上等于 F。我的独立复核确认该论证对
     Green/Stokes 逐字适用。
   - 但「逐字成立」目前是分析性论断，B7 的 verified witness 仅在曲面格构造，平面/空间格
     未逐字给出数字反例。建议（RC-2）把断言级别与证据量对齐。不构成 blocker。
⑤ limit 等价无穷小的第四版
   - 第四版数学正确，独立验证：
     · 乘除 guard（necessary）：E=u·h / u/h，Ẽ/E = v/u → 1 成立，需要 h 非零、比值在去心
       邻域有定义；「不需要 E 与 u 同阶」正确（约去 h 后与 E 无关）。
     · 加减 guard（sufficient）：u−v = o(E) ⟹ Ẽ ~ E。数值验证 B1(c)：E = sin x − x + x²，
       Ẽ = x²，Ẽ/E → 1（x=1e-2/1e-3/1e-4 → 1.0017/1.00017/1.00002）。
     · B1(a)/(b)/(c) 三对照结构正确：B1(a) 替换给 0、真值 −1/6；B1(c) 相消但替换安全。
   - 第三版「E ≍ u」论证的假处：把「E ≍ u ⟹ 安全」（一个充分条件）反用为「E ≪ u（相消）
     ⟹ 失效」（必要性），B1(c) 反例证伪后者。第四版改为 u−v = o(E) 的显式充分条件 +
     F2b 独立判据，已修复。正文无旧语义残留（「相消⇒失效」仅作为标注为错误的引述存在）。
⑥ 三族 not_found 的搜索预算
   - limit A7a-∞^0：预算偏浅（仅 x^(1/x) 一例），但幂指取对数在 ∞^0 型上结构上无风险
     （底→∞ 去心邻域恒正），not_found 诚实。建议扩充（NB-4）。
   - vector A3s：theorem_instantiation（v3.3.0 已更正），非 not_found 冒充，诚实。
   - extrema：B2a/B2b 补 F4 后的 not_found 合理（B2a/B2b 已是定理级反例）。
   - 所有 not_found 均用词正确（未用 no_counterexample_exists / unique / exhaustive）。
⑦ complete_within_declared_universe 的二分
   - 站得住：11 项 completion_criteria 是过程标准，「不可能再有别的路线」由
     global_exhaustiveness: not_established 承载，两者分离是诚实做法，未用定义规避实质问题。
   - 残余风险：标签「complete」有过强暗示，且 v3.4.0/v3.5.0 连续扫出新 route 表明其历史
     可靠性低。属 wording 类（NB-3），不构成 blocker。

# ── witness 数值复核摘要 ──

独立脚本（基础数值积分，容差 1e-4~1e-3）逐条验证，41/42 通过；唯一 FAIL 为容差设置
（limit B2 x=100：sin(100)/100 ≈ −0.0051 收敛慢，x=1e8 已验证 →1，数学成立）。

limit:
  - B1(a) (sin x−x)/x³ = −1/6；naive 替换 sin x~x 得 0 ≠ −1/6 ✓
  - B1(c) E=sin x−x+x²，Ẽ=x²，Ẽ/E → 1 ✓
  - B2 (x+sin x)/x → 1；洛必达后 1+cos x 不存在 ✓
vector:
  - B1 ∮单位圆 F·dr = 2π（rot F ≡ 0 off origin）✓
  - B9 上/下半圆 π / −π ✓
  - B6 单位球面 ∬1 dS = 4π via F=(x,y,z) ✓
  - B8 单位球面 ∬x dydz = 4π/3（前片 2π/3，缺分片得 2π/3）✓
  - B4 F=(0,0,z) 单位圆盘下侧直接 = 0；A4s 路线 = 0 ✓
  - B7 抛物面真值 π；全 F / 全 F̃ 均 π；混用 π/2、3π/2 ✓（全部数值吻合）
extrema:
  - B1 x⁴+y⁴ 严格局部极小、x⁴−y⁴ 鞍点（A=B=C=0 判别法无信息）✓
  - B5a f=y³ 在单位圆：(1,0)/(−1,0) 为 Lagrange 候选但 sin³t 在 t=0 变号，非极值 ✓
  - B9 约束 x²+y²=1, f=y：正支 min 0 vs 真全局 min −1 ✓
  - E-adv6 f=1.9y−1.2y³ 恒等式 sin t+0.3sin3t 成立；f''(π/2)=+1.7（局部最小 f=0.7）✓

confidence_limits:
  - 未读 solutions/（遵守红线）。未读 papers/ 原文（route 合法性不依赖真题）。
  - 独立 route 枚举为单轮结构枚举，预算受限；global_exhaustiveness 对审查者同样
    not_established。
  - 未做第二轮独立重扫；未系统比对外部教材路线清单。
  - 数值验证用基础数值积分；B8 球面分片用 600×600 网格，误差 ~1e-4。
  - lint 需 PYTHONIOENCODING=utf-8 才能在本机 cp1252 控制台运行（见 RC-4）。

files_changed:
  - 分析/审查/DeepSeek-audit-batch1-69d5df1.md   # 本报告（新文件）
被审对象 分析/方法族-高数-第一批.md 无改动（diff 为空）。
```
