#!/usr/bin/env python3
"""抽取 PDF 元数据与正文节选，生成 .kb/seeds/*.md 与 seeds.json。
只依赖 pdftotext / pdfinfo。"""
import hashlib, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.dirname(ROOT)
CACHE = os.path.join(ROOT, ".kb")
TEXT = os.path.join(CACHE, "text")
SEEDS = os.path.join(CACHE, "seeds")
os.makedirs(TEXT, exist_ok=True)
os.makedirs(SEEDS, exist_ok=True)

THEMES = {
    "01_灵巧手抓取规划": ["grasp plan", "grasp pose", "grasp detection", "graspnet", "grasp synthesis",
                     "grasp quality", "grasp stability", "grasp prediction", "抓取规划", "抓取位姿", "抓取质量"],
    "02_触觉感知与传感": ["tactile sensor", "gelsight", "digit", "tactile sensing", "vision-based tactile",
                     "触觉传感器", "压阻", "视触觉", "光电"],
    "03_阻抗与柔顺控制": ["impedance", "compliance", "admittance", "force/position", "柔顺", "阻抗", "力位控制"],
    "04_绳驱机构与结构设计": ["underactuated", "tendon", "mechanism", "kinetostatic", "欠驱动", "绳驱", "腱驱动", "结构设计"],
    "05_抓取力优化与力封闭": ["force optimization", "force distribution", "force closure", "grasping force",
                       "linear complementarity", "力封闭", "抓取力", "力优化", "内力", "接触力分配"],
    "06_滑移检测与抓取稳定": ["slip detection", "incipient slip", "滑移", "打滑"],
    "07_装配与操作任务": ["peg-in-hole", "insertion", "assembly", "装配", "轴孔"],
    "08_学习与强化学习": ["reinforcement learning", "imitation learning", "policy", "sim-to-real",
                    "强化学习", "模仿学习", "神经网络"],
    "09_视触融合与VLA": ["vision-language", "vla", "multimodal", "tactile fusion", "视触融合", "多模态", "大模型"],
    "10_综述与展望": ["review", "survey", "overview", "综述", "发展现状", "outlook"],
}


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, errors="ignore").stdout


def pages(pdf):
    out = run(["pdfinfo", pdf])
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1)) if m else 0


def text(pdf, first, last):
    return run(["pdftotext", "-layout", "-f", str(first), "-l", str(last), pdf, "-"])


def jaccard_name(name):
    return re.sub(r"\s+", " ", name.replace(".pdf", "").replace("_", " ")).strip()


def main():
    files = sorted(f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf"))
    seen, uniq, dups = {}, [], []
    for f in files:
        p = os.path.join(PDF_DIR, f)
        h = hashlib.md5(open(p, "rb").read()).hexdigest()
        if h in seen:
            dups.append({"keep": seen[h], "drop": f})
        else:
            seen[h] = f
            uniq.append(f)

    records = []
    for i, f in enumerate(uniq, 1):
        pid = f"KB-{i:03d}"
        p = os.path.join(PDF_DIR, f)
        n = pages(p)
        head = text(p, 1, min(8, n))
        tail = text(p, max(1, n - 9), n)
        extra = text(p, 1, min(14, n)) if re.search(r"[\u4e00-\u9fff]", f) else ""
        # 中文学位论文：封面可能是扫描页，另抽 15-40 页找摘要
        if re.search(r"[\u4e00-\u9fff]", f) and len(re.sub(r"\s", "", head)) < 500:
            extra += text(p, 4, min(40, n))
        raw = "\n".join([head, "\n<<<TAIL>>>\n", tail, "\n<<<CN>>>\n", extra])
        with open(os.path.join(TEXT, f"{pid}.txt"), "w", encoding="utf-8") as fh:
            fh.write(raw)

        flat = re.sub(r"[ \t]+", " ", head)
        doi = re.search(r"\b(10\.\d{4,9}/[^\s\"'<>]+)", flat)
        arx = re.search(r"arXiv:(\d{4}\.\d{4,5})", raw)
        years = [int(y) for y in re.findall(r"\b(19[89]\d|20[0-2]\d)\b", head)]
        years = [y for y in years if 1985 <= y <= 2026]
        from collections import Counter
        year_cand = [y for y, _ in Counter(years).most_common(6)]

        low = raw.lower()
        key = (jaccard_name(f) + " " + head[:2500]).lower()
        score = {t: sum(key.count(w.lower()) * (3 if w.lower() in jaccard_name(f).lower() else 1)
                        for w in ws) for t, ws in THEMES.items()}
        best = max(score, key=score.get)

        needs_ocr = len(re.sub(r"\s", "", head)) < 200
        records.append({
            "id": pid, "file": f, "pages": n, "title_guess": jaccard_name(f),
            "year_candidates": year_cand,
            "doi": doi.group(1).rstrip(".,;)") if doi else None,
            "arxiv": arx.group(1) if arx else None,
            "theme_suggest": best if score[best] > 0 else "10_综述与展望",
            "theme_scores": score, "needs_ocr": needs_ocr,
            "text_path": f".kb/text/{pid}.txt",
        })

        # 摘要 / 引言 / 结论 节选
        def grab(pattern, blob, length):
            m = re.search(pattern, blob)
            if not m:
                return ""
            return re.sub(r"[ \t]+", " ", blob[m.end():m.end() + length]).lstrip(" —-—:：.:,，").strip()

        abs_en = grab(r"(?im)^\s*Abstract\b", head, 1600)
        abs_cn = grab(r"摘\s*要", (extra or head), 1400)
        intro = grab(r"(?im)^\s*(?:[IVX]+\.?|\d+\.?)?\s*Introduction\b", head, 2200) or \
                grab(r"(?im)^\s*(?:引\s*言|1\s*绪\s*论)", (extra or head), 2000)
        body_tail = re.split(r"(?im)^\s*(?:REFERENCES|References|参\s*考\s*文\s*献)\s*$", tail)[0]
        concl = ""
        for m in re.finditer(r"(?im)^\s*(?:[IVX]+\.?|\d+\.?)?\s*(?:Conclusions?|CONCLUSIONS?|结\s*论|总结与展望)", body_tail):
            concl = re.sub(r"[ \t]+", " ", body_tail[m.end():m.end() + 1600]).lstrip(" —-:：.:,，").strip()
        if not concl:
            concl = grab(r"(?im)\b(?:Conclusions?|结\s*论)\b", tail, 1300) or body_tail[-1400:]
        if not intro:
            m = re.search(r"(?im)^\s*Abstract\b", head)
            intro = grab(r"(?im)^\s*Abstract\b", head, 2600) if m else head[1200:3200]

        with open(os.path.join(SEEDS, f"{pid}.md"), "w", encoding="utf-8") as fh:
            fh.write(f"""# 种子 {pid}

- 原文件: {f}
- 页数: {n} | 建议主题: {best} | 需 OCR: {needs_ocr}
- 标题候选: {jaccard_name(f)}
- 年份候选: {year_cand}
- DOI: {records[-1]['doi']} | arXiv: {records[-1]['arxiv']}

## 摘要（英文）
{abs_en[:1600]}

## 摘要（中文）
{abs_cn[:1300]}

## 引言节选
{intro[:1900]}

## 结论节选
{concl[:1300]}

## 首页原文
{flat[:2600]}
""")

    with open(os.path.join(CACHE, "seeds.json"), "w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(CACHE, "dedupe.json"), "w", encoding="utf-8") as fh:
        json.dump({"total": len(files), "unique": len(uniq), "dups": dups}, fh, ensure_ascii=False, indent=1)

    ocr = [r["file"] for r in records if r["needs_ocr"]]
    print(f"total={len(files)} unique={len(uniq)} dups={len(dups)} ocr={len(ocr)}")
    for d in dups:
        print("DUP:", d["drop"], "==>", d["keep"])
    for o in ocr:
        print("OCR:", o)


if __name__ == "__main__":
    main()
