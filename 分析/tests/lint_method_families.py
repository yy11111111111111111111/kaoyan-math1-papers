# -*- coding: utf-8 -*-
"""method-family schema lint（CALC-METHOD-FAMILY-v1.3.1）。

无第三方依赖以外只需 pyyaml。检查项与 schema 条款一一对应：
  S1  terminal_when 必须存在（执行顺序里第 3 步要有东西可求值）
  S2  optional_any_of 必须带 on_skip（堵「静默漏解」）
  S3  followup 项必须标 kind: action_ref | local_operation（未标 = 待迁移）
  T1  terminal_policy: never_terminal 的 action 不得有非空 terminal_when
      （防止「局部子任务完成」在 S1 的 terminal 语义下被误读成「整题完成」）
  R1  followup 的 action_ref 必须指向本 family 内真实存在的 action（B4 类）
  R2  action 的 eligible_cells 必须与 level_2_candidates 的 cell 清单双向一致（B4 类）
  U1  family_id 不得在多个文件中重复定义（多文件加载会静默覆盖）
  D1  同一 YAML 映射内不得有重复键（pyyaml 会静默取最后一个，是沉默失效的错误源）
  C1  frontmatter status_summary 必须与各族正文 status 一致
  C2  freeze_status 标 frozen 的族，其正文必须有 frozen: true（反之亦然）
  V   废弃字段 invokes / requires_followup 不得残留
  E   evidence 索引与正文 witness 一致；不得有 pending witness
  P   三族 pedagogical_validation 必须 untested
另检查 GPT 点名的语义残留（正文陈述位置，排除 status_history 的引述）。
"""
import re, sys, os, yaml


class DupKeyLoader(yaml.SafeLoader):
    """D1：把同一映射内的重复键从「静默取最后一个」改为报错。"""


def _no_dup(loader, node, deep=False):
    seen, out = set(), {}
    for k, v in node.value:
        key = loader.construct_object(k, deep=deep)
        if key in seen:
            raise yaml.constructor.ConstructorError(
                None, None, f"重复键 {key!r}（D1）", k.start_mark)
        seen.add(key)
        out[key] = loader.construct_object(v, deep=deep)
    return out


DupKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dup)

DOCS = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 '方法族-高数-第一批.md'),
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                 '方法族-高数-微分方程.md'),
]
SCHEMA = 'CALC-METHOD-FAMILY-v1.3.1'

# level_2_candidates 用中文 cell 名，route_scan_by_cell 用英文 cell_id
CELL_ALIAS = {
    '平面 · 曲线 · 第二类': 'planar_curve_second_kind',
    '空间 · 曲线 · 第二类': 'spatial_curve_second_kind',
    '曲面 · 第二类':        'surface_second_kind',
    '曲线或曲面 · 第一类':  'first_kind',
}

# GPT v3.2 full-file audit 点名的措辞；只允许出现在 status_history 的引述里
RESIDUE = [
    (r'合法性只要求闭合与定向',        'V1 补域合法性被写窄'),
    (r'任一以[^，。]*为边界的曲面',     'V2 Stokes spanning surface 过强'),
    (r'全部退出候选集',                'V3 第一类被绝对排除'),
    (r'从不参与变为外层框架',           'E3 A3 进入条件漏了 F6'),
    (r'合法性只要求闭合与定向一致。$', 'V1 断言式残留'),
]

def load():
    fams = {}
    fm_index = {}    # family_id -> 所在文件的 frontmatter（C1/C2 按文件就近）
    texts = []       # 每个文件的全文（语义残留扫描逐文件跑）
    for DOC in DOCS:
        s = open(DOC, encoding='utf-8').read()
        texts.append(s)
        fm = yaml.load(s.split('---')[1], Loader=DupKeyLoader)
        for b in re.findall(r'```yaml\n(.*?)\n```', s, re.S):
            d = yaml.load(b, Loader=DupKeyLoader)
            if isinstance(d, dict) and 'method_family_rule' in d:
                r = d['method_family_rule']
                fid = r['family_id']
                if fid in fams:      # U1：跨文件重名会被静默覆盖，与 D1 同类
                    raise ValueError(f"family_id {fid!r} 在多个文件中重复定义（U1）")
                fams[fid] = r
                fm_index[fid] = fm
    return texts, fams, fm_index

def main():
    # Windows 控制台默认 cp1252，⚠/✘ 会让脚本崩在输出上（外部 reviewer 实测遇到）
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
    try:
        texts, fams, fm_index = load()
    except yaml.constructor.ConstructorError as e:
        print(f"✘ YAML 结构错误：{e.problem} @ {e.problem_mark}")
        print("\nFAIL：error 1 · warning 0")
        return 1
    except ValueError as e:
        print(f"✘ {e}")
        print("\nFAIL：error 1 · warning 0")
        return 1
    err, warn = [], []

    # 每个文件的 frontmatter 都要声明 schema 版本
    checked_fms = set()
    for _fm in fm_index.values():
        if id(_fm) in checked_fms:
            continue
        checked_fms.add(id(_fm))
        if _fm['schema_version'] != SCHEMA:
            err.append(f"frontmatter schema_version={_fm['schema_version']}，应为 {SCHEMA}")

    for fid, r in fams.items():
        if r.get('schema_version') != SCHEMA:
            err.append(f"{fid}: schema_version={r.get('schema_version')}")
        if r['pedagogical_validation']['status'] != 'untested':
            err.append(f"{fid}: pedagogical_validation 非 untested")
        if r['status'] == 'challenged' and r.get('teaching_use') != 'quarantine':
            err.append(f"{fid}: challenged 但未 quarantine")
        # C1/C2: 用该族所在文件的 frontmatter
        fm = fm_index[fid]
        declared = (fm.get('status_summary') or {}).get(fid)
        if declared != r['status']:
            err.append(f"{fid}: frontmatter status_summary={declared!r}，正文 status={r['status']!r}（C1）")
        # C2: 冻结标记双向一致
        frozen_fm = (fm.get('freeze_status') or {}).get(fid) == 'frozen'
        if frozen_fm != bool(r.get('frozen')):
            err.append(f"{fid}: freeze_status 与正文 frozen 不一致（C2）")

        for a in r['candidate_actions']:
            aid = f"{fid}/{a['action_id']}"
            if 'produces' not in a:      err.append(f"{aid}: 缺 produces")
            if 'terminal_when' not in a: err.append(f"{aid}: 缺 terminal_when（S1）")
            for dead in ('invokes', 'requires_followup'):
                if dead in a: err.append(f"{aid}: 残留 v1.3 已废弃字段 {dead}")
            # T1: terminal_policy: never_terminal 的 action 不得有非空 terminal_when
            if a.get('terminal_policy') == 'never_terminal' and a.get('terminal_when'):
                err.append(f"{aid}: terminal_policy=never_terminal 却有非空 terminal_when（T1）")
            f = a.get('followup_actions')
            if isinstance(f, dict):
                if f.get('mode') == 'optional_any_of' and 'on_skip' not in f:
                    err.append(f"{aid}: optional_any_of 缺 on_skip（S2）")
                for it in f.get('actions', []):
                    if not (isinstance(it, dict) and 'kind' in it):
                        warn.append(f"{aid}: followup 项未标 kind，待迁移（S3）")

        # R1: action_ref 可解析
        ids = {a['action_id'] for a in r['candidate_actions']}
        for a in r['candidate_actions']:
            f = a.get('followup_actions')
            if not isinstance(f, dict):
                continue
            for it in f.get('actions', []):
                if isinstance(it, dict) and it.get('kind') == 'action_ref':
                    tgt = it.get('action')
                    if tgt not in ids:
                        err.append(f"{fid}/{a['action_id']}: action_ref 指向不存在的 {tgt!r}（R1）")

        # R2: eligible_cells 与 level_2_candidates 清单双向一致
        cells = {}
        for c in r.get('level_2_candidates') or []:
            key = c.get('cell_id') or CELL_ALIAS.get(c.get('cell'))
            if key:
                cells[key] = set(c['actions'])
        if cells:
            for a in r['candidate_actions']:
                ec = a.get('eligible_cells')
                if ec is None:
                    continue          # 未声明者豁免（已知限制，记 backlog）
                aid = a['action_id']
                unknown = [c for c in ec if c not in cells]
                if unknown:
                    err.append(f"{fid}/{aid}: eligible_cells 含未知 cell {unknown}（R2）")
                # 已声明者必须**完全**等于实际列出它的 cell 集合，不允许只声明一部分
                actual = {c for c, acts in cells.items() if aid in acts}
                if set(ec) - set(unknown) != actual:
                    err.append(f"{fid}/{aid}: eligible_cells={sorted(ec)} 与清单实际 {sorted(actual)} 不一致（R2）")

        fb = r['failure_boundaries']
        pend = [x['boundary_id'] for x in fb
                if x.get('witness', {}).get('verification') == 'pending']
        if pend: err.append(f"{fid}: 存在 pending witness {pend}")
        have = {x['boundary_id'] for x in fb
                if x.get('witness', {}).get('kind') == 'constructed_counterexample'}
        idx = set(r['evidence'].get('constructed_counterexamples', []))
        if have - idx: err.append(f"{fid}: evidence 索引缺 {sorted(have - idx)}")
        if idx - have: err.append(f"{fid}: evidence 索引多 {sorted(idx - have)}")

    # 语义残留：只抓「把旧规则当作现行规则来主张」的行。
    # 引述旧措辞并指出它错（更正段、status_history 的 reason、对抗复验的 target）
    # 是必须保留的 lineage，不算残留。
    CITATION = re.compile(
        r'过强|更正|不得写成|被推翻|被证伪|v3\.2 写|v3\.2 的|v3\.2 中|表述|'
        r'reason:|target:|- "|误判|是错的|缺口')
    for _s in texts:
        for i, ln in enumerate(_s.split('\n'), 1):
            for pat, why in RESIDUE:
                if re.search(pat, ln) and not CITATION.search(ln):
                    err.append(f"L{i}: 语义残留「{why}」→ {ln.strip()[:60]}")

    for e in err:  print("✘", e)
    for w in sorted(set(warn)): print("⚠", w)
    print(f"\n{'FAIL' if err else 'PASS'}：error {len(err)} · warning {len(set(warn))}")
    return 1 if err else 0

if __name__ == '__main__':
    sys.exit(main())
