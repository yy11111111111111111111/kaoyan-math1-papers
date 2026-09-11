# Opus 验收报告：线代「空间到方程」10题 v1

## 0. 元信息与本报告的效力

- 受审对象：`练习/线代空间到方程_10题_v1/01_题目.md` v1，题号1—10；基础提交 681c86f，分支 `claude/postgraduate-math-exam-szkbdo`。
- 执行顺序按 `00_Opus交接.md`：先只读 `01_题目.md` 与 `02_StageA说明.md`，逐题独立求解并封存；再读 `03_StageB_生成侧参考推导.md` 对照；结构审查结束后才读 `04_教学衔接_含学习状态.md`。本报告按此顺序产生。
- 协议依据：本次取得用户教学工作包中的《数学题_Validation_Protocol.md》1.1.0 与《数学出题_共享声明集.md》1.0.0（registry `MATH-ITEM-DECL-v1.0.0`），按其 Core 五项逐条执行。`00` 允许的「文件不可访问则降级」不适用，文件已取得。
- **本报告不是完整协议验收。** 降级原因不是文件缺失，而是本包 Stage A 不满足协议 §2.1 的 packet 接口，且 Full 等级所需的 Extended 检查在本轮不具备执行条件（见 §4、§5）。本报告是「Core 完整 ＋ 部分 Extended」的独立审题。
- 数学结论：**10题的题面条件、参数分支与 Stage B 参考答案，我独立求解后全部一致，未发现算错或漏解。**唯一的结构性缺陷在第3题末问（见 §3 必要修改 R1）。
- 独立性：Stage A 求解在读取 03、04 之前完成，隔离依据是本次会话的读取顺序，不是第三方 validator invocation。记 `rationale_blind_two_stage_check: executed`，并保留该限定。
- 群体校准 `uncalibrated`。本报告不预测分数、不判定掌握、不更新任何学习者记录。

## 1. Core 五项

```yaml
core:
  independent_solve:
    execution: executed
    result: 10/10 完成；另用有理数精确运算（秩、RREF、核基、通解、矩阵乘积）逐题复核
    agreement_with_stage_B: 10/10 一致
    evidence_strength: proved（第1、3、6、7、9题的唯一性/否定结论为证明；其余为可核验计算）
  condition_sufficiency:
    execution: executed
    result: 发现 1 个 counter-witness（第3题末问，b=0 时答案相反）；其余9题的对象、数域、量词、参数分支完整，未发现第二种自洽解释
    secondary_gaps: 第8题表示矩阵的行/列约定未声明；第9题所需的对称矩阵核—列空间正交互补未列入前置
  prerequisite_scope_P:
    execution: executed
    result: 逐题列出真实调用项；第9题必需项「A^T=A ⇒ ker A = Col(A)^⊥」在 02 前置表中 absent（表中只有「实对称矩阵不同特征子空间正交」）；其余题的调用项都落在 02 的声明范围内
  answer_response_requirement_consistency:
    execution: executed
    result: 01 的公共作答要求与 02 的公开评价准则一致，未出现「只收结论却按方法给分」或「允许多解却只认一个答案」
    open_items: 第2题末问「说明…关系」的可接受响应边界未定；第8题在缺列约定时无法判定转置答案是否可接受
  undecidable_reporting:
    execution: executed
    result: 无 undecidable。claim 名称均已在 MATH-ITEM-DECL-v1.0.0 注册；Stage A 字段缺失属执行不足，按 not_established 处理，不记 undecidable
```

## 2. 逐题结论

「独立解答」列指我在未读 03 时得到的结果与 03 的比对。状态列按协议 §10 的五态。

| 题 | 独立解答 vs Stage B | 结构问题 | 生成侧 claim | L_min | L_risk 触发 | 本轮状态 |
|---|---|---|---|---|---|---|
| 1 | 一致 | 无 | K-EXEC | Light | 否定主张（不可对角化） | not_established |
| 2 | 一致 | 末问检验力弱（R4） | K-COND | Light | 否定主张（两核不同）、方法名在前置表出现 | not_established |
| 3 | 一致 | **b=0 使末问答案相反（R1）** | K-REP | Full | 唯一性主张＋Core 发现边界反例 | **contradicted**（限末问；前两问 not_established） |
| 4 | 一致 | 无 | K-EXEC | Light | 否定主张（其余 t 无解） | not_established |
| 5 | 一致 | 无 | K-COND | Light | 否定主张（分支穷尽） | not_established |
| 6 | 一致 | 无 | K-REP | Full | 否定主张（非子空间） | not_established |
| 7 | 一致 | 无 | K-COND | Light | 否定主张（无公共解） | not_established |
| 8 | 一致 | 表示矩阵约定未登记（R2） | K-REP | Full | 未登记的局部约定 | not_established |
| 9 | 一致 | 前置项 absent（R3）；与第3题同构 | K-REP | Full | 唯一性主张、方法名在前置表出现 | not_established |
| 10 | 一致 | 无 | K-REP | Full | 否定主张（其余 t 无解） | not_established |

结论一句话：**数学上没有错题（第3题末问除外），但本轮没有任何一题可以记为 `supported`。**卡点在协议执行，不在数学。所有「唯一/不存在/其余无解」类结论我已给出证明级依据，满足 §5 的 negative-claim 下限；缺的是 Full 等级要求的 Extended 证据链。

第3题的 counter-witness 具体为：题面给定 `b∈Col(A)` 未排除 `b=0`。`b=0` 时任何补空间中的 `w` 都只能是 0，末问答案是「一定不变」；`b≠0` 时 `w≠0`，取核中非零向量 `n` 与 `W` 上满足 `f(w)=1` 的线性泛函，令 `W'={u+f(u)n:u∈W}`，它仍是核的补空间而其代表为 `w+n≠w`，末问答案是「一定可以改变」。两种答案都正确，取决于题面未固定的 `b`。03 的示例本身没问题（该例取 `b=e1≠0`），问题在题面的量词。

## 3. 必要修改

| 编号 | 题 | 问题 | 最小修订 |
|---|---|---|---|
| R1 | 3 | 末问在 `b=0` 与 `b≠0` 下答案相反，题面未排除 `b=0` | 题面改为「给定 `b∈Col(A)` 且 `b≠0`」。若想保留 `b=0`，改为把末问的量词写全：「是否对所有满足条件的 A、b、W、W′ 都不变」，并在评分中承认 `b=0` 为特例 |
| R2 | 8 | 表示矩阵的行/列约定未在题面或约定绑定中声明，转置答案无从裁定 | 题面加一句「表示矩阵以 T(u)、T(v) 在基 B 下的坐标为列」，或在包内登记该约定并在 `convention_bindings` 引用 |
| R3 | 9 | 决定性前置「A^T=A ⇒ ker A = Col(A)^⊥」未列入 02 的前置范围（表中只有特征子空间正交） | 二选一：把该结论补进前置表；或保留不列，并在本题证据边界写明「该一行推导本身属于被测内容」 |
| R4 | 2 | 末问 `Ac` 与 `(AQ)d` 恰好都为零，「相等」可以不理解机制就写出，检验力弱 | 追加一个 `Ac≠0` 的向量，或把末问改为「说明对任意 d 都有 (AQ)d=A(Qd)，并据此说明 ker(AQ) 与 ker A 的关系」 |

R1、R2 属于投放前必改；R3、R4 可与投放并行处理。按 `00` 第4条，修改题面须升版并保留变更记录；本报告未改动 `01_题目.md`，v1 仍是 v1，修订后需按新版本重跑受影响的检查，不得把修订后的结论回写成 v1 已通过。

## 4. 包装层缺口（这是本轮无法给 supported 的直接原因）

`02_StageA说明.md` 是整组共用的散文说明，不是协议 §2.1 的 Stage A packet。缺失字段：

- 每题的 `item_package`（`item_id`、`package_version`、无答案键的 `scoring_rule`、`source_refs`）；
- `prerequisite_profile` 的已登记 ID；
- 每题的 `required_prerequisites` 及精确来源（现为整组共用的能力范围列举，协议明确禁止用课程目录代替）；
- `convention_bindings`（直接导致 R2 无法裁定）；
- `declaration_set_version` 只出现在 Stage B，未出现在 Stage A；
- feature 声明（没有 `FTR-` 对象，feature witness audit 无可审计目标）。

`03` 的呈现信息以散文给出（同会话已展示过像/核/补空间、特征重数、正交性、`有解 iff b∈Col(A)`、特解＋核、`n-r` 等公式与完整解答，近期还展示过纠错解答），但没有 §2.2 的 `presentation_evidence` 结构字段（`presentation_version`、`visible_item_order`、`prior_items_or_solutions_visible`），`coverage` 记 `incomplete`。

## 5. Extended 执行状态

```yaml
extended:
  rationale_blind_two_stage_check: executed  # 限定：隔离依据为本次会话读取顺序，非独立 validator invocation
  route_family_search: skipped(reason: 未在解封前声明 family；解封后的路线枚举只登记为追加检查，不充当盲搜索)
  feature_witness_audit: skipped(reason: 本包未声明任何 feature，无可审计对象)
  leakage_search:
    execution: executed
    result: witnessed
    detail: 02 的前置范围直接点名第1题的「特征值及几何/代数重数」与第9题的「实对称矩阵…正交」；03 另记同会话已展示决定性公式与完整解答
    search_scope: 01 全文（标题、题面、公共作答要求）＋02 全文＋同目录文件名与标题
    budget_used: 10题逐题人工比对
    note: 只能记 witnessed 与 not_found，不写「无泄露」
  diagnostic_model_simulation: skipped(reason: not_applicable_to_claim，本组无 K-DIAG)
  task_fingerprint_full_profile: skipped(reason: 缺 item_package_ref 等字段)
population_calibration: {status: uncalibrated}
```

泄露的后果要按 claim 分别看，不是一律作废：第1、4题声明 K-EXEC，方法本就允许给定，前置表点名不削弱该 claim；但**本组10题都不能支持 K-SELECT（无提示方法选择）**，因为整组的决定性工具已在 02 与本会话中公开。03 自己也写了这一点，与我的检查一致。

## 6. 投放建议

1. **定位**：本组可以按复习、修复与衔接材料投放，作答结果用于定位当前断点。本轮不能用于任何 measurement claim 的取证，也不能记为节点通过；原因是 §4、§5 的执行缺口，与作答质量无关。
2. **先修后投**：R1、R2 改完再投第3、8题。其余8题可先投。
3. **顺序**：`04` 的 1—2 / 3—4 / 5—6 / 7—8 / 9—10 与题目结构一致，我复核后同意，补两条：
   - 第3题与第9题是同一结构论证的一般情形与正交特例（补空间中恰有一个代表）。两题相邻或同场完成时，后做的第9题证明部分不构成独立证据，只按执行证据记录。建议分到不同场次。
   - 第2、7题是右乘与左乘的对照对，放在一起做有比较价值；同场时后做的一题同样不计独立证据。
4. **不重开已撤回的诊断**：内积与外积混淆、「维数相同就不用证明」、A²=A 补空间证明的目标误读，这三项已撤回，本组不作为观察目标，也不作为讲解切入点。第1题按 `04` 的写法只做具体执行核对，本报告不新增任何能力结论。
5. **作答约定**：`01` 没有给用时预算，也没有「暂时不会时如何标注」的约定。建议补一句按题的粗略用时与标注方式（未学过／忘记入口／知道方法但未算完／时间不足），便于按真实断点回收证据，而不是只回收对错。
6. **补齐后可关闭的项**：生成侧按 §4 补齐 Stage A packet 与 feature 声明、并由未接触 Stage B 的一方在解封前声明 route family 后，第1、4题（K-EXEC）与第2、5、7题（K-COND）可较快走完 Light；第3、6、8、9、10题（K-REP）仍需 Full 的 feature witness、leakage audit 与 route search 全套。

## 7. 状态

```yaml
status: generation_complete / independent_review_done / revisions_applied_v2 / protocol_validation_incomplete / assignment_fit_pending
item_stems_changed: true    # 见 §8；§1—§7 是对 v1 的审查记录，未因修订改写
claims_supported: []        # v1 本轮无；v2 未重验，同样没有
next_actions:
  - 按 §4 补齐 Stage A packet 与 feature 声明
  - 由未接触 Stage B 的一方在解封前声明 route family 后，对 v2 重跑 Core 与 Extended
  - 第2题 v2 的新增小问与第3题 v2 的 b≠0 结论需第三方独立复核
```

审查者：Claude（Opus 会话），2026-09-11。§1—§7 只覆盖 681c86f 的 v1 题面并保持原样；v2 须按新版本重验，不继承本报告结论。

## 8. 变更执行记录（v1 → v2，2026-09-11）

用户指示后，R1—R4 已全部应用。改动如下，均在同一提交内：

| 编号 | 文件 | 改动 | 答案是否变化 |
|---|---|---|---|
| R1 | 01 第3题 | 题面加「且 b≠0」 | 不变。v1 的示例本就取 b≠0；排除 b=0 后末问只剩一个正确答案，且强于「不一定」：总能改变 |
| R2 | 01 第8题 | 题面写明表示矩阵的第一、第二列分别是 T(u)、T(v) 在基 B 下的坐标 | 不变，只是转置答案现在可裁定 |
| R4 | 01 第2题 | 拆成三小问；新增 e=(0,1,0)^T；末问改为要求 (AQ)d 与 A(Qd) 的一般关系及其对两个核的含义 | 新增内容。c 与 e 一个被 A 杀死、一个被 AQ 杀死，「相等」不再能不理解机制就写出 |
| R3 | 02 前置范围 | 补入「实对称矩阵的核与列空间互为正交补（也可由 A^T=A 现场推出）」 | 不变，补的是第9题的前置声明缺口 |

同步更新：`01` 标题与说明升为 v2；`02` 的适用题面改为 v2；`03` 中第2、3、8题条目由审查方同步并标注「v2 同步」，其余7题条目保持 v1 原文；`00` 补一行状态。

效力限制，按 `00` 第4条：**不得把 v2 的修订读成 v1 原本已通过。**§2 的逐题状态是对 v1 的判定，其中第3题 v1 为 contradicted；v2 修掉了该缺口，但 v2 本身尚未重验，所以 v2 的全部 10 题仍是 `not_established`，没有任何一题可用于取证。第2题 v2 新增的小问与第3题 v2 的强化结论由审查方给出并自行核验（精确有理数运算），尚无第三方独立复核。
