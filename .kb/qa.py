#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""知识库质量检查：板块完整性、frontmatter、断链、文件名、主题归属、重复标题。
用法：python3 .kb/qa.py [--strict]   报告写入 .kb/qa_report.md"""
import os, re, sys, json
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "02_文献库")
TERMS = os.path.join(LIB, "00_专业名词库")
OUT = os.path.join(ROOT, ".kb", "qa_report.md")

REQUIRED_FM = ["title", "year", "key", "theme", "tags", "pdf", "confidence", "source"]
SECTIONS = ["📌 年份", "🔑 论文识别码", "👥 作者与所属院校", "📖 研究背景",
            "❓ 需要解决的问题", "📥📤 输入与输出", "✅ 论文最终达到的效果", "🏷️ 标签"]
OPTIONAL = ["🔗 关联"]
ILLEGAL = re.compile(r'[:/\\?*"<>|]')
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]


def main():
    term_files = {}
    if os.path.isdir(TERMS):
        for f in os.listdir(TERMS):
            if f.endswith(".md"):
                term_files[f[:-3]] = os.path.join(TERMS, f)

    notes = []
    for dirpath, dirnames, filenames in os.walk(LIB):
        if os.path.abspath(dirpath) == os.path.abspath(TERMS):
            continue
        for f in filenames:
            if f.endswith(".md"):
                notes.append(os.path.join(dirpath, f))

    titles = {}
    errors, warns = [], []
    per_theme = Counter()
    conf = Counter()
    term_links = Counter()
    pending = Counter()

    # 术语别名 -> 主名
    alias_map = {}
    for name, p in term_files.items():
        t = open(p, encoding="utf-8").read()
        m = re.search(r"^aliases:\s*\[(.*?)\]\s*$", t, re.M)
        if m:
            for a in m.group(1).split(","):
                a = a.strip()
                if a:
                    alias_map.setdefault(a, name)

    for p in notes:
        rel = os.path.relpath(p, ROOT)
        stem = os.path.basename(p)[:-3]
        text = open(p, encoding="utf-8").read()
        fm, body = frontmatter(text)
        if fm is None:
            errors.append(f"{rel}: 缺少 frontmatter")
            fm = {}
        for k in REQUIRED_FM:
            if k not in fm:
                errors.append(f"{rel}: frontmatter 缺字段 {k}")
        if "title" in fm:
            titles.setdefault(fm["title"], []).append(rel)
        if ILLEGAL.search(stem):
            errors.append(f"{rel}: 文件名含非法字符")
        theme = os.path.basename(os.path.dirname(p))
        if theme not in (fm.get("theme") or ""):
            warns.append(f"{rel}: theme 字段({fm.get('theme')}) 与所在目录({theme}) 不一致")
        if not re.fullmatch(r"\d{4}", fm.get("year", "")):
            warns.append(f"{rel}: year 非四位年份 ({fm.get('year')})")
        if fm.get("confidence") not in ("high", "medium", "low"):
            warns.append(f"{rel}: confidence 取值异常 ({fm.get('confidence')})")
        conf[fm.get("confidence", "?")] += 1
        pdf = fm.get("pdf", "")
        if pdf:
            target = os.path.normpath(os.path.join(os.path.dirname(p), pdf))
            if not os.path.exists(target):
                errors.append(f"{rel}: pdf 路径不存在 -> {pdf}")

        for s in SECTIONS:
            if not re.search(rf"^##\s*{re.escape(s)}\s*$", body, re.M):
                errors.append(f"{rel}: 缺少板块 {s}")

        # 待建名词
        for m in re.finditer(r"【待建名词：([^】]+)】", body):
            pending[m.group(1).strip()] += 1
        for m in re.finditer(r"【待建名词[^】]*】", body):
            if "：" not in m.group(0):
                warns.append(f"{rel}: 待建名词格式应为 【待建名词：xxx】")

        # 链接解析
        for m in LINK.finditer(body):
            tgt = m.group(1).strip()
            base = tgt.split("/")[-1]
            ok = base in term_files or base in alias_map
            if not ok:
                ok = any(os.path.basename(n)[:-3] == base for n in notes) or base in titles
            if ok:
                term_links[alias_map.get(base, base)] += 1
            else:
                errors.append(f"{rel}: 断链 [[{tgt}]]")
        per_theme[theme] += 1

    # 术语卡片内部链接校验
    for name, tp in term_files.items():
        body = open(tp, encoding="utf-8").read()
        for m in LINK.finditer(body):
            tgt = m.group(1).strip().split("/")[-1]
            if tgt not in term_files and tgt not in alias_map:
                ok = any(os.path.basename(n)[:-3] == tgt for n in notes)
                if not ok:
                    errors.append(f"{os.path.relpath(tp, ROOT)}: 断链 [[{tgt}]]")

    for t, paths in titles.items():
        if len(paths) > 1:
            errors.append(f"重复标题「{t}」: {paths}")

    total = len(notes)
    lines = ["# 质量检查报告", "",
             f"- 笔记总数：**{total}**", f"- 术语卡片：**{len(term_files)}**", ""]
    lines += ["## 主题分布", ""]
    for k in sorted(per_theme):
        lines.append(f"- {k}: {per_theme[k]}")
    lines += ["", "## 置信度", ""] + [f"- {k}: {v}" for k, v in conf.most_common()]
    lines += ["", f"## 错误（{len(errors)}）", ""] + [f"- {e}" for e in errors[:300]]
    lines += ["", f"## 警告（{len(warns)}）", ""] + [f"- {w}" for w in warns[:200]]
    lines += ["", f"## 待建名词（{len(pending)} 个，共 {sum(pending.values())} 次）", ""]
    for k, v in pending.most_common(60):
        lines.append(f"- {k}: {v}")
    lines += ["", "## 被链接最多的术语 Top 20", ""]
    for k, v in term_links.most_common(20):
        lines.append(f"- [[{k}]]: {v}")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"notes={total} terms={len(term_files)} errors={len(errors)} warnings={len(warns)}")
    print(f"report -> {OUT}")
    for e in errors[:10]:
        print("ERR:", e)
    if "--strict" in sys.argv and errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
