# mindforge_scaffold_from_md.py
# рџ“ќ РЎРѕР·РґР°С‚СЊ Р°Р»С„Р°РІРёС‚РЅРѕ РѕС‚СЃРѕСЂС‚РёСЂРѕРІР°РЅРЅСѓСЋ СЃС‚СЂСѓРєС‚СѓСЂСѓ РїР°РїРѕРє MindForge РёР· Markdown-СЃС…РµРјС‹
# РСЃРїРѕР»СЊР·РѕРІР°РЅРёРµ:
#   python mindforge_scaffold_from_md.py "MindForge вЂ” Flat Layout Scaffold (mf_core) v0.2.md"
#   python mindforge_scaffold_from_md.py scaffold.md --target "H:/MindForge" --dry-run

from __future__ import annotations
import argparse
from pathlib import Path
from typing import List, Set

CONNECTORS = ("в”њв”Ђв”Ђ", "в””в”Ђв”Ђ")

def _calc_depth(line: str) -> int:
    """РџСЂРёРјРµСЂРЅРѕ СЃС‡РёС‚Р°РµС‚ РіР»СѓР±РёРЅСѓ РїРѕ РіСЂСѓРїРїР°Рј 'в”‚   ' / '|   ' / '    ' РґРѕ РїРµСЂРІРѕРіРѕ СЃРѕРµРґРёРЅРёС‚РµР»СЏ."""
    depth = 0
    i = 0
    while i < len(line):
        if line.startswith("в”‚   ", i) or line.startswith("|   ", i) or line.startswith("    ", i):
            depth += 1
            i += 4
        elif line[i] in ("в”њ", "в””"):
            break
        else:
            i += 1
    return depth

def _is_tree_line(line: str) -> bool:
    return any(c in line for c in CONNECTORS)

def _extract_name(line: str) -> str:
    """Р‘РµСЂС‘Рј РІСЃС‘ РїРѕСЃР»Рµ 'в”њв”Ђв”Ђ ' РёР»Рё 'в””в”Ђв”Ђ ', РѕС‚СЂРµР·Р°РµРј РєРѕРјРјРµРЅС‚Р°СЂРёРё РїРѕСЃР»Рµ '#'."""
    for c in CONNECTORS:
        idx = line.find(c)
        if idx != -1:
            return line[idx + len(c):].strip().split("#")[0].strip()
    return line.strip()

def parse_tree_dirs(markdown: str) -> List[List[str]]:
    """
    Р’РѕР·РІСЂР°С‰Р°РµС‚ СЃРїРёСЃРѕРє РїСѓС‚РµР№ (РєР°Р¶РґС‹Р№ вЂ” СЃРїРёСЃРѕРє СЃРµРіРјРµРЅС‚РѕРІ) РўРћР›Р¬РљРћ РґР»СЏ РґРёСЂРµРєС‚РѕСЂРёР№.
    РџРµСЂРІС‹Р№ СЃРµРіРјРµРЅС‚ вЂ” РєРѕСЂРµРЅСЊ (mindforge/ РёР»Рё MindForge/), РїРѕР·Р¶Рµ РѕС‚Р±СЂРѕСЃРёРј.
    """
    dirs: List[List[str]] = []
    stack: List[str] = []
    lines = markdown.splitlines()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue

        # РџРѕРґРґРµСЂР¶РєР° В«РіРѕР»С‹С…В» РєРѕСЂРЅРµР№ РІСЂРѕРґРµ "MindForge/" Р±РµР· РІРµС‚РѕРє.
        if (line.strip().lower().endswith("mindforge/") and " " not in line.strip()) or \
           (line.strip().endswith("/") and line.strip().count("/") == 1 and ("в”њ" not in line and "в””" not in line)):
            stack = [line.strip().rstrip("/")]
            continue

        if _is_tree_line(line):
            depth = _calc_depth(line)
            name = _extract_name(line).strip()
            while len(stack) > depth:
                stack.pop()

            is_dir = name.endswith("/")
            seg = name.rstrip("/")

            if is_dir:
                stack.append(seg)
                dirs.append(stack.copy())
            else:
                # С„Р°Р№Р» вЂ” Р·Р°РїРѕРјРёРЅР°РµРј СЂРѕРґРёС‚РµР»СЏ, РµСЃР»Рё РѕРЅ РµС‰С‘ РЅРµ РїРѕРїР°РґР°Р»СЃСЏ
                parent = stack.copy()
                if parent:
                    dirs.append(parent.copy())

    # РЈРЅРёРєР°Р»РёР·Р°С†РёСЏ
    uniq: List[List[str]] = []
    seen: Set[tuple[str, ...]] = set()
    for p in dirs:
        t = tuple(p)
        if t not in seen and p:
            seen.add(t)
            uniq.append(p)
    return uniq

def to_relative_dirs(paths: List[List[str]]) -> Set[Path]:
    """РћС‚Р±СЂР°СЃС‹РІР°РµРј РєРѕСЂРµРЅСЊ (РїРµСЂРІС‹Р№ СЃРµРіРјРµРЅС‚) в†’ РїРѕР»СѓС‡Р°РµРј РѕС‚РЅРѕСЃРёС‚РµР»СЊРЅС‹Рµ РїСѓС‚Рё."""
    rel: Set[Path] = set()
    for segs in paths:
        if len(segs) <= 1:
            continue
        rel.add(Path(*segs[1:]))
    return rel

def main():
    parser = argparse.ArgumentParser(description="Create MindForge folder structure from Markdown scaffold.")
    parser.add_argument("markdown", help="Path to Markdown file with tree scaffold.")
    parser.add_argument("--target", default=r"H:\MindForge", help="Target root directory (default: H:\\MindForge).")
    parser.add_argument("--dry-run", action="store_true", help="Only show what would be created.")
    args = parser.parse_args()

    md_path = Path(args.markdown)
    if not md_path.is_file():
        raise SystemExit(f"Markdown file not found: {md_path}")

    markdown = md_path.read_text(encoding="utf-8")
    all_paths = parse_tree_dirs(markdown)
    rel_dirs = to_relative_dirs(all_paths)

    target = Path(args.target)
    # РђР»С„Р°РІРёС‚РЅР°СЏ СЃРѕСЂС‚РёСЂРѕРІРєР°, РєР°Рє РІ Windows Explorer
    missing = sorted([p for p in rel_dirs if not (target / p).is_dir()], key=lambda p: str(p).lower())
    existing = sorted([p for p in rel_dirs if (target / p).is_dir()], key=lambda p: str(p).lower())

    print(f"Target: {target}")
    print(f"Total dirs in scaffold: {len(rel_dirs)}")
    print(f"Existing: {len(existing)}")
    print(f"Missing:  {len(missing)}\n")

    if existing:
        print("вњ” Existing:")
        for p in existing:
            print(f"  - {p}")
        print()

    if missing:
        print("вњљ To create (alphabetical):")
        for p in missing:
            print(f"  + {p}")
    else:
        print("Nothing to create. All good!")

    if args.dry_run or not missing:
        return

    # РЎРѕР·РґР°РЅРёРµ РЅРµРґРѕСЃС‚Р°СЋС‰РёС… РїР°РїРѕРє
    for p in missing:
        (target / p).mkdir(parents=True, exist_ok=True)
        print(f"рџ“‚ Created: {target / p}")

    print("\nвњ… Done.")

if __name__ == "__main__":
    main()
