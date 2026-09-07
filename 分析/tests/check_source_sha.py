# -*- coding: utf-8 -*-
"""source_tsv_sha256 一致性断言。

`考点标注.tsv` 是全库唯一的人工标注层。`分析/` 下多份文件在 frontmatter 里写着
`source_tsv_sha256`，声明自己基于哪一版 TSV。TSV 一旦重建，这些声明全部过期——
而在此脚本出现之前，没有任何机制会报错，失配是静默的。

`common.input_sha()` 早就能算这个哈希，但只把它写进检验报告的 `input_sha` 字段供人看，
不做断言。本脚本补上断言：失配即非零退出。

用法：
    python3 分析/tests/check_source_sha.py

退出码：0 全部一致；1 存在失配（或没扫到任何声明——那本身就说明约定失效了）。
"""
import os, re, sys
from common import ROOT, TSV, input_sha

FIELD = re.compile(r'^source_tsv_sha256:\s*([0-9a-f]+)\s*$', re.M)
SKIP_DIRS = {'__pycache__'}


def declarations():
    """扫描 分析/ 下所有 .md 的 frontmatter，返回 [(相对路径, 声明值)]。"""
    found = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in sorted(filenames):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(dirpath, fn)
            with open(path, encoding='utf-8') as fh:
                head = fh.read(2048)          # frontmatter 只可能在开头
            m = FIELD.search(head)
            if m:
                found.append((os.path.relpath(path, ROOT), m.group(1)))
    return found


def main():
    actual = input_sha()
    decls = declarations()

    print(f'考点标注.tsv  实际 sha256[:16] = {actual}')
    print(f'路径          {os.path.relpath(TSV, ROOT)}')
    print(f'扫到声明      {len(decls)} 份\n')

    if not decls:
        print('✗ 一份 source_tsv_sha256 声明都没扫到。')
        print('  要么 frontmatter 约定已被改掉，要么扫描范围错了——两种都需要人来看。')
        return 1

    stale = [(p, v) for p, v in decls if v != actual]
    if not stale:
        print(f'PASS：{len(decls)} 份声明全部与当前 TSV 一致。')
        return 0

    print(f'✗ FAIL：{len(stale)} 份声明已过期（TSV 变了，这些文件的上层结论未同步）：\n')
    for p, v in stale:
        print(f'  {p}\n      声明 {v} ≠ 实际 {actual}')
    print('\n处理方式见 CLAUDE.md §4.0.1：逐份确认结论是否仍成立，再更新声明。')
    print('不要为了让本脚本变绿而批量改哈希——那正好抹掉了它要暴露的问题。')
    return 1


if __name__ == '__main__':
    sys.exit(main())
