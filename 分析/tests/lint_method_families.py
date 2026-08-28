# -*- coding: utf-8 -*-
"""method-family schema lint（CALC-METHOD-FAMILY-v1.3.1）。

无第三方依赖以外只需 pyyaml。检查项与 schema 条款一一对应：
  S1  terminal_when 必须存在（执行顺序里第 3 步要有东西可求值）
  S2  optional_any_of 必须带 on_skip（堵「静默漏解」）
  S3  followup 项必须标 kind: action_ref | local_operation（未标 = 待迁移）
  V   废弃字段 invokes / requires_followup 不得残留
  E   evidence 索引与正文 witness 一致；不得有 pending witness
  P   三族 pedagogical_validation 必须 untested
另检查 GPT 点名的语义残留（正文陈述位置，排除 status_history 的引述）。
"""
import re, sys, os, yaml

DOC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   '方法族-高数-第一批.md')
SCHEMA = 'CALC-METHOD-FAMILY-v1.3.1'

# GPT v3.2 full-file audit 点名的措辞；只允许出现在 status_history 的引述里
RESIDUE = [
    (r'合法性只要求闭合与定向',        'V1 补域合法性被写窄'),
    (r'任一以[^，。]*为边界的曲面',     'V2 Stokes spanning surface 过强'),
    (r'全部退出候选集',                'V3 第一类被绝对排除'),
    (r'从不参与变为外层框架',           'E3 A3 进入条件漏了 F6'),
    (r'合法性只要求闭合与定向一致。$', 'V1 断言式残留'),
]

def load():
    s = open(DOC, encoding='utf-8').read()
    fm = yaml.safe_load(s.split('---')[1])
    fams = {}
    for b in re.findall(r'```yaml\n(.*?)\n```', s, re.S):
        d = yaml.safe_load(b)
        if isinstance(d, dict) and 'method_family_rule' in d:
            r = d['method_family_rule']
            fams[r['family_id']] = r
    return s, fm, fams

def main():
    s, fm, fams = load()
    err, warn = [], []

    if fm['schema_version'] != SCHEMA:
        err.append(f"frontmatter schema_version={fm['schema_version']}，应为 {SCHEMA}")

    for fid, r in fams.items():
        if r.get('schema_version') != SCHEMA:
            err.append(f"{fid}: schema_version={r.get('schema_version')}")
        if r['pedagogical_validation']['status'] != 'untested':
            err.append(f"{fid}: pedagogical_validation 非 untested")
        if r['status'] == 'challenged' and r.get('teaching_use') != 'quarantine':
            err.append(f"{fid}: challenged 但未 quarantine")

        for a in r['candidate_actions']:
            aid = f"{fid}/{a['action_id']}"
            if 'produces' not in a:      err.append(f"{aid}: 缺 produces")
            if 'terminal_when' not in a: err.append(f"{aid}: 缺 terminal_when（S1）")
            for dead in ('invokes', 'requires_followup'):
                if dead in a: err.append(f"{aid}: 残留 v1.3 已废弃字段 {dead}")
            f = a.get('followup_actions')
            if isinstance(f, dict):
                if f.get('mode') == 'optional_any_of' and 'on_skip' not in f:
                    err.append(f"{aid}: optional_any_of 缺 on_skip（S2）")
                for it in f.get('actions', []):
                    if not (isinstance(it, dict) and 'kind' in it):
                        warn.append(f"{aid}: followup 项未标 kind，待迁移（S3）")

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
    for i, ln in enumerate(s.split('\n'), 1):
        for pat, why in RESIDUE:
            if re.search(pat, ln) and not CITATION.search(ln):
                err.append(f"L{i}: 语义残留「{why}」→ {ln.strip()[:60]}")

    for e in err:  print("✘", e)
    for w in sorted(set(warn)): print("⚠", w)
    print(f"\n{'FAIL' if err else 'PASS'}：error {len(err)} · warning {len(set(warn))}")
    return 1 if err else 0

if __name__ == '__main__':
    sys.exit(main())
