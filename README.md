# 📚 考研数学一真题库 (1987-2026)

[![License](https://img.shields.io/badge/License-CC--BY--NC--SA%204.0-green.svg)](LICENSE) [![Years](https://img.shields.io/badge/年份-1987--2026-blue.svg)](papers/) [![Papers](https://img.shields.io/badge/真题-39年-orange.svg)](papers/)

**考研数学一真题 Markdown 版**，收录 1987-2026 年共 **39 个年份**的真题（1994 年缺失；2024 年有三份来源并存，故题面文件为 41 个），支持 LaTeX 公式渲染。

> ⚠️ **声明**：本项目仅供学习交流使用，真题版权归原出题单位所有。

---

## 📖 内容

| 年份范围 | 套数 | 卷型 | 说明 |
|---------|------|------|------|
| 1987-1993 | 7 套 | 分节式 | 章节标题为「一、」…「十五、」，无全卷连续题号 |
| 1995-2003 | 9 套 | 分节式 | 1994 年缺失 |
| 2004-2020 | 17 套 | 三段式 | 选择 8 + 填空 6 + 解答 9 = 23 题（2007 年为 24 题） |
| 2021-2026 | 6 套 | 新三段式 | 选择 10 + 填空 6 + 解答 6 = 22 题，**现行卷型** |

另有 `papers/数学二/` 收录数学二真题 1 套（2024，扫描件，无文字层）。

---

## 🚀 特性

- ✅ **LaTeX 公式** - 数学公式完整保留，支持渲染
- ✅ **答案解析** - 包含详细解题步骤
- ✅ **Markdown 格式** - 可在 Obsidian、Typora、VS Code 等编辑器中阅读
- ✅ **结构清晰** - 选择题、填空题、解答题分类整理

---

## 📁 目录结构

```
Kaoyan-Math1-Papers/
├── papers/                    # 真题文件
│   ├── 1987年考研数学(一)真题.md
│   ├── 1988年考研数学(一)真题.md
│   ├── ...
│   ├── 2025年数学一真题.md
│   ├── 2026年考研数学一真题.md
│   ├── 数学二/                # 数学二真题
│   └── images/               # 配图（可选）
├── 分析/                      # 考点标注与统计分析（详见 分析/交接说明-教学AI.md）
├── solutions/                 # PDF 转换的官方解析稿
├── CLAUDE.md                  # 本仓库的分析规则
├── README.md
└── LICENSE
```

---

## 🔧 使用方式

### Obsidian

1. 将 `papers/` 文件夹复制到你的 Obsidian Vault
2. 启用 LaTeX 公式渲染（默认支持）

### VS Code

安装 **Markdown+Math** 或 **Markdown All in One** 插件

### Typora

直接打开 `.md` 文件，原生支持 LaTeX

---

## 📝 格式示例

```markdown
## 一、选择题

1．已知函数 $f(x) = \int_0^x e^{t^2} \sin t \, dt$，则

A．$x = 0$ 是 $f(x)$ 的极值点  
B．$(0, 0)$ 是拐点  
C．...

【答案】B

【解析】

$$
f'(x) = e^{x^2} \sin x, \quad f''(x) = 2xe^{x^2}\sin x + e^{x^2}\cos x
$$
```

---

## 🔗 相关项目

- [MinerU-Skill](https://github.com/Nebutra/MinerU-Skill) - PDF 转 Markdown 工具

---

## 📜 License

本项目采用 **CC BY-NC-SA 4.0** 许可证：

- ✅ 可分享、复制、传播
- ✅ 可修改、 remix
- ❌ 不得商用
- 🔄 衍生作品需相同许可

真题内容版权归原作者所有。

---

## 🙏 致谢

- 真题来源：网络整理
- PDF 解析：[MinerU](https://mineru.net/)

---

<div align="center">

**祝考研顺利！🎓**

</div>
