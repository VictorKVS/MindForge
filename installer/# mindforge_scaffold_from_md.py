# mindforge_scaffold_from_md.py
# 📝 Создать алфавитно отсортированную структуру папок MindForge из Markdown-схемы
# Использование:
#   python mindforge_scaffold_from_md.py "MindForge — Flat Layout Scaffold (mf_core) v0.2.md"
#   python mindforge_scaffold_from_md.py scaffold.md --target "H:/MindForge" --dry-run

from __future__ import annotations
import argparse
from pathlib import Path
from typing import List, Set

CONNECTORS = ("├──", "└──")

def _calc_depth(line: str) -> int:
    """Примерно считает глубину по группам '│   ' / '|   ' / '    ' до первого соединителя."""
    depth = 0
    i = 0
    while i < len(line):
        if line.startswith("│   ", i) or line.startswith("|   ", i) or line.startswith("    ", i):
            depth += 1
            i += 4
        elif line[i] in ("├", "└"):
            break
        else:
            i += 1
    return depth

def _is_tree_line(line: str) -> bool:
    return any(c in line for c in CONNECTORS)

def _extract_name(line: str) -> str:
    """Берём всё после '├── ' или '└── ', отрезаем комментарии после '#'."""
    for c in CONNECTORS:
        idx = line.find(c)
        if idx != -1:
            return line[idx + len(c):].strip().split("#")[0].strip()
    return line.strip()

def parse_tree_dirs(markdown: str) -> List[List[str]]:
    """
    Возвращает список путей (каждый — список сегментов) ТОЛЬКО для директорий.
    Первый сегмент — корень (mindforge/ или MindForge/), позже отбросим.
    """
    dirs: List[List[str]] = []
    stack: List[str] = []
    lines = markdown.splitlines()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue

        # Поддержка «голых» корней вроде "MindForge/" без веток.
        if (line.strip().lower().endswith("mindforge/") and " " not in line.strip()) or \
           (line.strip().endswith("/") and line.strip().count("/") == 1 and ("├" not in line and "└" not in line)):
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
                # файл — запоминаем родителя, если он ещё не попадался
                parent = stack.copy()
                if parent:
                    dirs.append(parent.copy())

    # Уникализация
    uniq: List[List[str]] = []
    seen: Set[tuple[str, ...]] = set()
    for p in dirs:
        t = tuple(p)
        if t not in seen and p:
            seen.add(t)
            uniq.append(p)
    return uniq

def to_relative_dirs(paths: List[List[str]]) -> Set[Path]:
    """Отбрасываем корень (первый сегмент) → получаем относительные пути."""
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
    # Алфавитная сортировка, как в Windows Explorer
    missing = sorted([p for p in rel_dirs if not (target / p).is_dir()], key=lambda p: str(p).lower())
    existing = sorted([p for p in rel_dirs if (target / p).is_dir()], key=lambda p: str(p).lower())

    print(f"Target: {target}")
    print(f"Total dirs in scaffold: {len(rel_dirs)}")
    print(f"Existing: {len(existing)}")
    print(f"Missing:  {len(missing)}\n")

    if existing:
        print("✔ Existing:")
        for p in existing:
            print(f"  - {p}")
        print()

    if missing:
        print("✚ To create (alphabetical):")
        for p in missing:
            print(f"  + {p}")
    else:
        print("Nothing to create. All good!")

    if args.dry_run or not missing:
        return

    # Создание недостающих папок
    for p in missing:
        (target / p).mkdir(parents=True, exist_ok=True)
        print(f"📂 Created: {target / p}")

    print("\n✅ Done.")

if __name__ == "__main__":
    main()
