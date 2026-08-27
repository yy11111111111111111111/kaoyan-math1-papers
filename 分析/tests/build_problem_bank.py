# -*- coding: utf-8 -*-
"""题面库第一阶段抽取器。
仅从 papers/ 的 OCR 转换稿抽取题面，**不接触** solutions/、不写入任何考点/方法/答案。
source_status 上限为 ocr_uncertain —— 仓库没有 PDF/扫描件，无法做对原卷的视觉核验。
"""
import re, os, sys, csv, json, collections, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAPERS = os.path.join(ROOT, 'papers')
TSV = os.path.join(ROOT, '分析', '考点标注.tsv')
YEARS = [y for y in range(2004, 2024) if y != 2022]        # 2022 全文乱码；2024–2026 留作模考，不入库
UNUSABLE = {'2023-9'}                                       # 待确认.md §一：四个选项全空
# 自动抽取会产出被污染的正文，按「不得据数学常识静默修复」的原则不入库，留待人工转写：
NEEDS_MANUAL = {
    '2023-7': '题号 `7.` 出现在行中而非行首，且与第 6 题的选项块（矩阵 OCR 已错乱）交织在一起；'
              '自动切分只能产出被污染的正文。待确认.md §2.1 已登记 2023-5/6/7。',
}

SEC = re.compile(r'^#+\s*([一二三四五六七八九十]+)、\s*(.+)$')
# 题号标记：(1) / （1） / 1. / 1、  行首
ITEM = re.compile(r'^\s*(?:[（(]?\s*(\d{1,2})\s*[)）]|(\d{1,2})\s*[.、])\s*')

def sec_type(title):
    if '填空' in title: return '填空'
    if '选择' in title: return '选择'
    return '解答'

def tsv_index():
    idx = collections.defaultdict(dict)
    for f in csv.reader(open(TSV), delimiter='\t'):
        idx[int(f[0])][f[1]] = f[2]
    return idx

def parse(year, expect_by_type):
    """按「该节的期望题号集合」驱动切分，而不是见到 (n) 就切。
    这样能同时解决两类问题：解答题里的 (1)(2) 小问被误判为新题；
    以及 OCR 吃掉题号首位（2020/2021 出现 `4）` 实为 (14)）。"""
    path = os.path.join(PAPERS, f'{year}年考研数学(一)真题.md')
    lines = open(path, encoding='utf-8').read().split('\n')
    out, cur_type, buf, cur_no, cur_flags = [], None, [], None, []
    pending, sec_recovered = [], False
    order = [t for t in ('选择', '填空', '解答') if t in expect_by_type]
    def flush():
        if cur_no is not None:
            out.append((cur_no, cur_type, '\n'.join(buf).strip(), list(cur_flags)))
    for ln in lines:
        m = SEC.match(ln)
        if m:
            flush(); buf, cur_no, cur_flags = [], None, []
            cur_type = sec_type(m.group(2))
            pending = list(expect_by_type.get(cur_type, []))
            if cur_type in order: order.remove(cur_type)
            continue
        if cur_type is None: continue
        mi = ITEM.match(ln)
        hit, flag = None, None
        if mi and not pending and order:
            cur_type = order.pop(0)
            pending = list(expect_by_type.get(cur_type, []))
            sec_recovered = True
        if mi and pending:
            raw = mi.group(1) or mi.group(2)
            nxt = pending[0]
            if raw == nxt:
                hit = nxt
            elif nxt.endswith(raw) and len(raw) < len(nxt):
                hit, flag = nxt, dict(span=ln.strip()[:24],
                                      reason='item_number_reconstructed_from_position')
            elif raw in pending:                      # 允许跳号（残缺题被剔除时）
                hit = raw
        if hit:
            flush(); cur_no, buf, cur_flags = hit, [ln[mi.end():]], ([flag] if flag else [])
            while pending and pending[0] != hit: pending.pop(0)
            if pending: pending.pop(0)
        elif cur_no is not None:
            buf.append(ln)
    flush()
    return out

def flags_for(text):
    out = []
    if '![' in text: out.append(dict(span='<figure>', reason='figure_present_in_source'))
    for bad in ['□', '\ufffd', '〓']:
        if bad in text: out.append(dict(span=bad, reason='symbol_ambiguous'))
    if re.search(r'\$[^$]*\$\$[^$]*\$', text): out.append(dict(span='$$', reason='latex_delimiter_suspect'))
    if len(text.strip()) < 25: out.append(dict(span=text.strip()[:30], reason='body_suspiciously_short'))
    return out

def main():
    idx = tsv_index()
    report, banks = [], collections.defaultdict(list)
    for y in YEARS:
        exp = collections.defaultdict(list)
        for no, tp in sorted(idx[y].items(), key=lambda kv: int(kv[0])):
            exp[tp].append(no)
        items = parse(y, exp)
        got = {no for no, _, _, _ in items}
        want = set(idx[y])
        report.append((y, len(items), len(want), sorted(want - got, key=lambda x: int(x)),
                       sorted(got - want, key=lambda x: int(x))))
        for no, tp, body, pf in items:
            pid = f'{y}-{no}'
            if pid in UNUSABLE or pid in NEEDS_MANUAL: continue
            if no not in idx[y]: continue          # 抽到但 TSV 没有的，先不入库，进报告
            banks[y].append(dict(problem_id=pid, year=y, number=int(no),
                                 question_type=idx[y][no], body=body,
                                 uncertainty_flags=flags_for(body)))
    print(f"{'年':<6}{'抽到':>5}{'TSV':>5}   缺失(TSV有/未抽到)                多出(抽到/TSV无)")
    for y, g, w, miss, extra in report:
        mark = '  ' if not miss and not extra else ' ⚠'
        print(f'{y:<6}{g:>5}{w:>5}{mark} {",".join(miss) or "-":<32} {",".join(extra) or "-"}')
    json.dump({str(k): v for k, v in banks.items()},
              open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '_bank.json'), 'w'),
              ensure_ascii=False)
    tot = sum(len(v) for v in banks.values())
    print(f'\n可入库题数 {tot}；带 uncertainty_flags 的 {sum(1 for v in banks.values() for x in v if x["uncertainty_flags"])} 题')
    emit(banks)

RANGES = [(2004, 2010), (2011, 2016), (2017, 2020), (2021, 2023)]
HEAD = '''---
doc_id: calc.problem-bank.{a}-{b}
doc_version: 1.0.0
scope: {a}–{b} 年数学一真题**题面**（第一阶段：仅来自 papers/ 的 OCR 转换稿）
source_status_ceiling: ocr_uncertain
generated_at: 2026-08-27
generator: 分析/tests/build_problem_bank.py
---

# 数学一真题题面　{a}–{b}

> **本文件只有题面。**没有考点、没有方法、没有切入点、没有易错处、没有答案。
> 这是刻意的：取题面时不应同时读到决定性提示。考点查 `考点标注.tsv`，方法查 `*方法速查.md`，
> 缺陷查 `待确认.md`，推断路线查 `解法.md`（未核验）。
>
> ## ⚠️ 第一阶段的效力边界
>
> 本仓库**只有 `papers/` 的 OCR 转换稿，没有 PDF 原件或扫描图**，因此无法做「对原卷的视觉核验」。
> 全部记录的 `source_status` 上限为 **`ocr_uncertain`**，不因「读起来正常」或「数学上讲得通」而升级。
>
> ```
> 对 OCR 的核对  ≠  对原卷的核对
> ```
>
> `transcription_check: matched_against_ocr_source` 只能证明**二次整理没有新增错误**，
> 不能证明原 OCR 无误。
>
> **使用限制**：可用于检索、候选选择、历史结构分析；
> **若要据此严格判定作答对错、做精细条件辨析、或作为正式真题投放，应先完成原卷核验。**
>
> 用户补入 PDF/扫描件后，第二阶段做 `ocr_uncertain → 视觉比对 → verified_from_paper`。
>
> ## 排除项
>
> - **2022 年整年**：题面文件全文乱码。
> - **2024–2026 三套**：留作模考，2026-11-29 前不入库。
> - **2023-9**：四个选项全空，题面无法复原（`待确认.md` §一）。
>
> 排除项**保留 tombstone 记录**（`source_status: unusable`，正文为 `[UNAVAILABLE: …]`），
> 以区分「库里根本没有这题」与「库知道这题存在、但当前来源无法恢复可靠题面」。
> 拿到原卷后直接替换为 `verified_from_paper`。
{manual}
---

'''

def emit(banks):
    outdir = os.path.join(ROOT, '分析')
    for a, b in RANGES:
        ys = [y for y in YEARS if a <= y <= b]
        man = [f'> - **{k}**：{v}' for k, v in sorted(NEEDS_MANUAL.items())
               if a <= int(k.split('-')[0]) <= b]
        body = [HEAD.format(a=a, b=b, manual=('\n'.join(man) + '\n') if man else '')]
        n = 0
        idx = tsv_index()
        tomb = {}
        for pid, why in list(NEEDS_MANUAL.items()) + [(k, '四个选项全部为空，题面无法复原（待确认.md §一）。') for k in UNUSABLE]:
            yy, nn = pid.split('-')
            if a <= int(yy) <= b: tomb[(int(yy), int(nn))] = why
        for y in ys:
            for nn, why in sorted([(k[1], v) for k, v in tomb.items() if k[0] == y]):
                pid = f'{y}-{nn}'
                qt = idx[y].get(str(nn), '未知')
                body.append(f'''## {pid}

```yaml
problem_id: {pid}
year: {y}
number: {nn}
question_type: {qt}
source_status: unusable
source_basis: ocr_conversion_only
transcription_mode: none
transcription_check: impossible_from_current_source
uncertainty_flags:
    - span: "<whole_item>"
      reason: source_structure_corrupted
figure_status: none
figure_ref: null
source_page: null
```

### 题面

[UNAVAILABLE: {why}]

<!-- END_PROBLEM:{pid} -->

---

''')
                n += 1
            for it in sorted(banks[y], key=lambda x: x['number']):
                fl = it['uncertainty_flags']
                fls = '[]' if not fl else '\n' + '\n'.join(
                    f"    - span: {json.dumps(f['span'], ensure_ascii=False)}\n      reason: {f['reason']}" for f in fl)
                has_fig = 'linked_verified' if '![' in it['body'] else 'none'
                body.append(f'''## {it["problem_id"]}

```yaml
problem_id: {it["problem_id"]}
year: {it["year"]}
number: {it["number"]}
question_type: {it["question_type"]}
source_status: ocr_uncertain
source_basis: ocr_conversion_only
transcription_mode: normalized_from_ocr
transcription_check: matched_against_ocr_source
uncertainty_flags: {fls}
figure_status: {has_fig}
figure_ref: {"见正文内嵌 ![] 引用" if has_fig != "none" else "null"}
source_page: null
```

### 题面

{it["body"]}

<!-- END_PROBLEM:{it["problem_id"]} -->

---

''')
                n += 1
        fn = os.path.join(outdir, f'高数真题题面_{a}-{b}.md')
        open(fn, 'w').write(''.join(body))
        print(f'  写出 {os.path.basename(fn)}  {n} 题')

if __name__ == '__main__':
    main()
