#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""修复 frontmatter 中未加引号却含 ": " 等 YAML 敏感字符的值（Obsidian 会显示"无效属性"）。
可反复运行；只改需要加引号的行。"""
import os, re, sys
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ponytail: 只处理本项目常见形态（单行 key: value），不做通用 YAML 回写
SPECIAL = set('-?:,[]{}#&*!|>\'"%@`')


def needs_quote(v):
    if not v or v.startswith('[') or (v[0] in '"\'' and v[-1] == v[0]):
        return False
    return (': ' in v or ' #' in v or v.endswith(':') or v[0] in SPECIAL)


def quote(v):
    return '"' + v.replace('\\', '\\\\').replace('"', '\\"') + '"'


def fix(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return text, False
    fm, body = m.group(1), text[m.end():]
    out, changed = [], False
    for line in fm.splitlines():
        mm = re.match(r'^([A-Za-z_][\w-]*):[ \t]?(.*)$', line)
        if mm:
            k, v = mm.group(1), mm.group(2).strip()
            if needs_quote(v):
                line = f'{k}: {quote(v)}'
                changed = True
        out.append(line)
    if not changed:
        return text, False
    new_fm = "\n".join(out)
    try:
        yaml.safe_load(new_fm)
    except Exception as e:
        print(f"  !! 修复后仍不合法: {e}")
        return text, False
    return f"---\n{new_fm}\n---\n{body}", True


def main():
    targets = []
    for base in ('00_模板', '02_文献库', '01_索引主页'):
        d = os.path.join(ROOT, base)
        if not os.path.isdir(d):
            continue
        for dp, _, fs in os.walk(d):
            for f in fs:
                if f.endswith('.md'):
                    targets.append(os.path.join(dp, f))
    n = 0
    for p in sorted(targets):
        text = open(p, encoding='utf-8').read()
        new, changed = fix(text)
        if changed:
            open(p, 'w', encoding='utf-8').write(new)
            n += 1
            print("fixed:", os.path.relpath(p, ROOT))
    print(f"共修复 {n} 个文件")

    # 复核
    bad = 0
    for p in sorted(targets):
        t = open(p, encoding='utf-8').read()
        m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
        if not m:
            continue
        try:
            yaml.safe_load(m.group(1))
        except Exception:
            bad += 1
            print("仍不合法:", os.path.relpath(p, ROOT))
    print(f"复核: {bad} 个文件 frontmatter 仍不合法")
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
