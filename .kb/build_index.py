#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""汇总生成：01_索引主页/文献总览.md、01_索引主页/名词索引.md，并回填
术语卡片的"关联文献"与笔记的"🔗 关联"。可反复运行。"""
import os, re, json
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "02_文献库")
TERMS = os.path.join(LIB, "00_专业名词库")
INDEX = os.path.join(ROOT, "01_索引主页")
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
SKIP = {"00_专业名词库"}


def parse(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    fm, body = {}, text
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
        body = m.group(2)
    return fm, body


def section(body, title):
    m = re.search(rf"^##\s*{re.escape(title)}\s*$", body, re.M)
    if not m:
        return None
    nxt = re.search(r"^##\s", body[m.end():], re.M)
    return body[m.end():m.end() + nxt.start()] if nxt else body[m.end():]


def replace_section(body, title, new_content):
    m = re.search(rf"^##\s*{re.escape(title)}\s*$", body, re.M)
    if not m:
        return body.rstrip() + f"\n\n## {title}\n{new_content}\n"
    nxt = re.search(r"^##\s", body[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(body)
    return body[:m.end()] + "\n" + new_content.strip() + "\n\n" + body[end:].lstrip("\n")


def main():
    os.makedirs(INDEX, exist_ok=True)
    term_names, alias_map = {}, {}
    for f in sorted(os.listdir(TERMS)):
        if not f.endswith(".md"):
            continue
        name = f[:-3]
        fm, body = parse(os.path.join(TERMS, f))
        term_names[name] = {"fm": fm, "body": body, "path": os.path.join(TERMS, f)}
        for a in fm.get("aliases", "").strip("[]").split(","):
            a = a.strip()
            if a:
                alias_map[a] = name

    notes = []
    for dirpath, dirnames, filenames in os.walk(LIB):
        if os.path.basename(dirpath) in SKIP:
            continue
        for f in sorted(filenames):
            if f.endswith(".md"):
                p = os.path.join(dirpath, f)
                fm, body = parse(p)
                notes.append({"path": p, "file": f, "title": f[:-3], "theme": os.path.basename(dirpath),
                              "fm": fm, "body": body})

    # ---------- 回填笔记 🔗 关联（同主题最近/相邻 3 篇） ----------
    by_theme = defaultdict(list)
    for n in notes:
        by_theme[n["theme"]].append(n)
    for n in notes:
        sec = section(n["body"], "🔗 关联") or ""
        existing = [m.group(1).strip() for m in LINK.finditer(sec)]
        existing = [e for e in existing if e != n["title"]]
        cands = [x["title"] for x in sorted(by_theme[n["theme"]], key=lambda z: z["title"])
                 if x["title"] != n["title"] and x["title"] not in existing]
        final = (existing + cands)[:3]
        content = "\n".join(f"- [[{t}]]" for t in final) if final else "- 同主题暂无可关联笔记"
        new_body = replace_section(n["body"], "🔗 关联", content)
        if new_body != n["body"]:
            fm_text = "".join(f"{k}: {v}\n" for k, v in n["fm"].items())
            with open(n["path"], "w", encoding="utf-8") as fh:
                fh.write(f"---\n{fm_text}---\n{new_body}")
            n["body"] = new_body

    # ---------- 术语 -> 引用它的笔记 ----------
    term_refs = defaultdict(list)
    for n in notes:
        seen = set()
        for m in LINK.finditer(n["body"]):
            base = m.group(1).strip().split("/")[-1]
            name = alias_map.get(base, base)
            if name in term_names and name not in seen:
                term_refs[name].append(n["title"])
                seen.add(name)

    for name, info in term_names.items():
        refs = sorted(term_refs.get(name, []))
        content = "\n".join(f"- [[{t}]]" for t in refs[:12]) if refs else "- （暂无引用文献）"
        if len(refs) > 12:
            content += f"\n- …等共 {len(refs)} 篇"
        new_body = replace_section(info["body"], "关联文献", content)
        if new_body != info["body"]:
            fm_text = "".join(f"{k}: {v}\n" for k, v in info["fm"].items())
            with open(info["path"], "w", encoding="utf-8") as fh:
                fh.write(f"---\n{fm_text}---\n{new_body}")
            info["body"] = new_body

    # ---------- 文献总览 ----------
    yrs = Counter(n["fm"].get("year", "?") for n in notes)
    theme_cnt = Counter(n["theme"] for n in notes)
    dedupe = json.load(open(os.path.join(ROOT, ".kb", "dedupe.json"))) if \
        os.path.exists(os.path.join(ROOT, ".kb", "dedupe.json")) else {"total": len(notes), "unique": len(notes), "dups": []}

    merged = len([d for d in dedupe.get("dups", []) if d.get("reason")])
    L = ["# 文献总览", "",
         f"本库共收录 **{len(notes)}** 篇文献笔记（原始 PDF {dedupe['total']} 个，按内容去重后 {dedupe['unique']} 篇，"
         f"其中 {merged} 对为同一工作的预印本/重复件，已合并建 1 篇笔记），"
         f"覆盖专业术语 **{len(term_names)}** 个。由 `.kb/build_index.py` 自动生成，勿手工编辑。", "",
         "## 一、主题分布", "", "| 主题 | 篇数 |", "|---|---|"]
    for k in sorted(theme_cnt, key=lambda x: x):
        L.append(f"| {k} | {theme_cnt[k]} |")
    L += ["", "## 二、年份分布", "", "| 年份 | 篇数 |", "|---|---|"]
    for y, c in sorted(yrs.items()):
        L.append(f"| {y} | {c} |")
    L += ["", "## 三、按主题浏览", ""]
    for theme in sorted(by_theme):
        L += [f"### {theme}（{len(by_theme[theme])} 篇）", "",
              "| 文献 | 年份 | 识别码 | 关键词 |", "|---|---|---|---|"]
        for n in sorted(by_theme[theme], key=lambda z: z["title"]):
            key = n["fm"].get("doi") or n["fm"].get("arxiv") or n["fm"].get("key", "")
            tags = n["fm"].get("tags", "").strip("[]")
            L.append(f"| [[{n['title']}]] | {n['fm'].get('year','')} | {key} | {tags} |")
        L.append("")

    L += ["", "## 四、附录", "", "### 4.1 重复/重复版本 PDF（只建 1 篇笔记）", ""]
    for d in dedupe.get("dups", []):
        reason = f"（{d['reason']}）" if d.get("reason") else "（md5 完全相同）"
        L.append(f"- `{d['drop']}` 与 `{d['keep']}` 重复{reason}")
    low = [n["title"] for n in notes if n["fm"].get("confidence") in ("low", "medium")]
    nodoi = [n["title"] for n in notes if not n["fm"].get("doi") and not n["fm"].get("arxiv")]
    L += ["", "### 4.2 扫描件 / 置信度中低（建议人工复核）", ""]
    L += [f"- [[{t}]]" for t in low] or ["- （无）"]
    L += ["", "### 4.3 无 DOI 与 arXiv（识别码退化为 KB 编号）", ""]
    L += [f"- [[{t}]]" for t in nodoi] or ["- （无）"]
    L += ["", "### 4.4 结构说明", "",
          "- readme 示例中的「05_仿真与动力学建模」按语料实际并入：动力学建模类归 `03_阻抗与柔顺控制`，"
          "仿真/Sim2Real 类归 `08_学习与强化学习`；新增 05/06/07/09/10 五个语料驱动主题。",
          "- 每篇文献只归入一个主主题，次级主题体现在 🏷️ 标签与 🔗 关联中。"]
    with open(os.path.join(INDEX, "文献总览.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")

    # ---------- 名词索引 ----------
    groups = defaultdict(list)
    for name, info in term_names.items():
        tag = info["fm"].get("tags", "").strip("[]").split(",")
        grp = tag[-1].strip() if len(tag) > 1 else "其他"
        groups[grp].append(name)
    M = ["# 名词索引", "",
         f"共 **{len(term_names)}** 个专业术语，按类别分组；括号内为引用该术语的文献数。"
         "所有术语卡片位于 `02_文献库/00_专业名词库/`。由 `.kb/build_index.py` 自动生成。", ""]
    for grp in sorted(groups):
        M += [f"## {grp}", ""]
        for name in sorted(groups[grp]):
            body = term_names[name]["body"]
            d = section(body, "定义") or ""
            d = re.sub(r"\s+", " ", d).strip()
            d = re.split(r"(?<=。)", d)[0] if d else ""
            M.append(f"- [[{name}]]（{len(term_refs.get(name, []))}）— {d[:90]}")
        M.append("")
    pending = Counter(m.group(1).strip() for n in notes for m in re.finditer(r"【待建名词：([^】]+)】", n["body"]))
    M += ["## 附录：待建名词", "",
          "以下术语在文献中被提及但尚未建卡（出现次数 ≥2 的优先建卡）：", ""]
    M += [f"- {k}: {v} 次" for k, v in pending.most_common(80)] or ["- （无）"]
    with open(os.path.join(INDEX, "名词索引.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(M) + "\n")

    print(f"notes={len(notes)} terms={len(term_names)} pending={len(pending)}")
    print("->", os.path.join(INDEX, "文献总览.md"))
    print("->", os.path.join(INDEX, "名词索引.md"))


if __name__ == "__main__":
    main()
