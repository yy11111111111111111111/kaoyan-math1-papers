"""检验脚本的公共加载层。所有检验共用同一份读入逻辑，避免各自解析 TSV 时口径漂移。"""
import csv, hashlib, math, collections, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TSV  = os.path.join(ROOT, '考点标注.tsv')
TYPES = ['选择', '填空', '解答']

def input_sha():
    return hashlib.sha256(open(TSV, 'rb').read()).hexdigest()[:16]

def load():
    """返回逐题记录。TSV 列数不定（次考点数量可变），末四列固定：
    题型内序号 / 解答位序号 / 高数解答位序号 / 功能位类型。"""
    rows = []
    for f in csv.reader(open(TSV), delimiter='\t'):
        tail = f[-4:]
        rows.append(dict(
            yr=int(f[0]), q=f[1], tx=f[2],
            kps=[x for x in f[3:len(f) - 4] if x.strip()],
            tx_idx=tail[0].strip(), slot=tail[1].strip(),
            gslot=tail[2].strip(), demand=tail[3].strip(),
        ))
    return rows

def subject_map(rows):
    """考点 → 科目。依据三份考法统计文件的标签集合，非 TSV 字段。"""
    S = {}
    for subj, fn in [('高数', '高数考法统计.md'), ('线代', '线性代数考法统计.md'), ('概率', '概率考法统计.md')]:
        S[subj] = open(os.path.join(ROOT, fn)).read()
    out = {}
    for r in rows:
        for k in r['kps']:
            if k in out: continue
            out[k] = next((s for s in ('高数', '线代', '概率') if k in S[s]), '高数')
    return out

def norm_entropy(counts):
    n = sum(counts)
    if n == 0: return None
    H = -sum((c / n) * math.log(c / n) for c in counts if c > 0)
    return H / math.log(len(counts))

def cramers_v(pairs):
    n = len(pairs)
    rt = collections.Counter(a for a, _ in pairs)
    ct = collections.Counter(b for _, b in pairs)
    tab = collections.Counter(pairs)
    chi = sum((tab[(r, c)] - rt[r] * ct[c] / n) ** 2 / (rt[r] * ct[c] / n)
              for r in rt for c in ct if rt[r] * ct[c] > 0)
    k = min(len(rt), len(ct))
    return math.sqrt(chi / (n * (k - 1))) if k > 1 else 0.0

def record(**kw):
    """按约定的元数据格式打印检验记录，便于逐字复核。"""
    order = ['test_id','input_sha','inclusion_rule','estimand','statistic','null_model',
             'randomization_unit','iterations','seed','observed','null_summary',
             'p_value','interpretation','known_contamination','generated_at']
    print('```yaml')
    for k in order:
        if k in kw:
            v = kw[k]
            if isinstance(v, str) and '\n' in v:
                print(f'{k}: |')
                for ln in v.strip().split('\n'): print('  ' + ln)
            else:
                print(f'{k}: {v}')
    print('```')
