# mindforge_gui_installer.py
# 📝 MindForge GUI Installer
# Читает Markdown со структурой (tree-графика ├──, └──, │   ) и:
# 1) извлекает список директорий,
# 2) сравнивает с целевой папкой (по умолчанию H:\MindForge),
# 3) показывает отчёт и создаёт недостающие директории.

import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import List, Set

DEFAULT_TARGET = Path(r"H:\MindForge")  # ← твоя целевая директория

# -------- Парсер дерева --------

CONNECTORS = ("├──", "└──")

def _calc_depth(line: str) -> int:
    """
    Приблизительно считает глубину по префиксным группам '│   ' или '    ' до первого соединителя.
    """
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
    # берём всё после '├── ' или '└── '
    for c in CONNECTORS:
        idx = line.find(c)
        if idx != -1:
            return line[idx + len(c):].strip().split("#")[0].strip()  # уберём комментарии после '#'
    return line.strip()

def parse_tree_dirs(markdown: str) -> List[List[str]]:
    """
    Возвращает список путей (каждый путь — список сегментов) ТОЛЬКО для директорий.
    Корневую директорию (mindforge/ или MindForge/) оставляем как сегмент 0,
    но позже отбросим при сборке относительных путей.
    """
    dirs: List[List[str]] = []
    stack: List[str] = []

    lines = markdown.splitlines()

    # Иногда в блоке могут быть plain-строки вида "mindforge/" без веток — обработаем их
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue

        # Отдельная обработка "голых" корневых: "mindforge/" или "MindForge/"
        if (line.strip().lower().endswith("mindforge/") and " " not in line.strip()) or \
           (line.strip().endswith("/") and line.strip().count("/") == 1 and ("├" not in line and "└" not in line)):
            # Сбросим стек и начнём от корня
            stack = [line.strip().rstrip("/")]
            continue

        if _is_tree_line(line):
            depth = _calc_depth(line)
            name = _extract_name(line)

            # нормализуем имя (без комментария в конце и без лишних пробелов)
            name = name.strip()

            # Обрежем стек до текущей глубины
            # (для первой записи стек может быть пустым — тогда корень определим как первый каталог верхнего уровня)
            while len(stack) > depth:
                stack.pop()

            is_dir = name.endswith("/")
            seg = name.rstrip("/")

            if is_dir:
                # каталог — добавляем в стек и регистрируем путь
                stack.append(seg)
                dirs.append(stack.copy())
            else:
                # файл — директорию не добавляем, но путь-родитель зафиксируем (на случай, если она не встречается отдельно)
                parent = stack.copy()
                if parent:
                    dirs.append(parent.copy())

    # Уникализируем (как кортежи) и вернём списки сегментов
    uniq = []
    seen = set()
    for p in dirs:
        t = tuple(p)
        if t not in seen and len(p) > 0:
            seen.add(t)
            uniq.append(p)
    return uniq

def to_relative_dirs(paths: List[List[str]]) -> Set[Path]:
    """
    Отбрасывает первый сегмент (корень mindforge/MindForge), собирает относительные пути.
    """
    rel: Set[Path] = set()
    for segs in paths:
        if len(segs) <= 1:
            continue
        rel.add(Path(*segs[1:]))
    return rel

# -------- GUI --------

class MindForgeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MindForge GUI Installer")
        self.geometry("900x620")

        # Ввод целевой директории
        self.target_var = tk.StringVar(value=str(DEFAULT_TARGET))
        tk.Label(self, text="Target directory:").grid(row=0, column=0, sticky="w", padx=8, pady=8)
        tk.Entry(self, textvariable=self.target_var, width=70).grid(row=0, column=1, sticky="we", padx=4, pady=8)
        tk.Button(self, text="Browse…", command=self.browse_target).grid(row=0, column=2, padx=8, pady=8)

        # Кнопки загрузки Markdown
        tk.Button(self, text="Open Markdown…", command=self.open_md).grid(row=1, column=0, padx=8, pady=4, sticky="w")
        tk.Button(self, text="Paste from Clipboard", command=self.paste_clipboard).grid(row=1, column=1, padx=4, pady=4, sticky="w")

        # Текстовая область для Markdown
        tk.Label(self, text="Scaffold Markdown:").grid(row=2, column=0, sticky="w", padx=8)
        self.md_text = scrolledtext.ScrolledText(self, wrap="word", height=18)
        self.md_text.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=8, pady=4)

        # Кнопки анализа/создания
        self.btn_analyze = tk.Button(self, text="Analyze scaffold", command=self.analyze)
        self.btn_analyze.grid(row=4, column=0, padx=8, pady=8, sticky="w")

        self.btn_create = tk.Button(self, text="Create missing folders", command=self.create_missing, state="disabled")
        self.btn_create.grid(row=4, column=1, padx=4, pady=8, sticky="w")

        # Отчёт
        tk.Label(self, text="Report:").grid(row=5, column=0, sticky="w", padx=8)
        self.report = scrolledtext.ScrolledText(self, wrap="word", height=12, state="disabled")
        self.report.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=8, pady=4)

        # Grid weights
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Данные анализа
        self.rel_dirs: Set[Path] = set()
        self.missing: Set[Path] = set()
        self.existing: Set[Path] = set()

    def browse_target(self):
        d = filedialog.askdirectory(title="Select target directory")
        if d:
            self.target_var.set(d)

    def open_md(self):
        path = filedialog.askopenfilename(
            title="Open Scaffold Markdown",
            filetypes=[("Markdown", "*.md;*.markdown;*.txt"), ("All files", "*.*")]
        )
        if not path:
            return
        with open(path, "r", encoding="utf-8") as f:
            self.md_text.delete("1.0", "end")
            self.md_text.insert("1.0", f.read())

    def paste_clipboard(self):
        try:
            text = self.clipboard_get()
        except tk.TclError:
            text = ""
        if text:
            self.md_text.delete("1.0", "end")
            self.md_text.insert("1.0", text)

    def analyze(self):
        md = self.md_text.get("1.0", "end")
        if not md.strip():
            messagebox.showwarning("No data", "Paste or open the scaffold Markdown first.")
            return

        try:
            tree_paths = parse_tree_dirs(md)
            self.rel_dirs = to_relative_dirs(tree_paths)
        except Exception as e:
            messagebox.showerror("Parse error", f"Failed to parse scaffold:\n{e}")
            return

        target = Path(self.target_var.get()).expanduser()
        if not target.exists():
            # анализ относительно несуществующей цели: все директории считаем отсутствующими
            self.missing = set(self.rel_dirs)
            self.existing = set()
        else:
            self.missing = set()
            self.existing = set()
            for rel in sorted(self.rel_dirs):
                if (target / rel).is_dir():
                    self.existing.add(rel)
                else:
                    self.missing.add(rel)

        self.btn_create.config(state="normal" if self.missing else "disabled")
        self._write_report(target)

    def _write_report(self, target: Path):
        self.report.config(state="normal")
        self.report.delete("1.0", "end")
        total = len(self.rel_dirs)
        self.report.insert("end", f"Target: {target}\n")
        self.report.insert("end", f"Total directories in scaffold: {total}\n")
        self.report.insert("end", f"Existing: {len(self.existing)}\n")
        self.report.insert("end", f"Missing:  {len(self.missing)}\n\n")

        if self.existing:
            self.report.insert("end", "✔ Existing:\n")
            for p in sorted(self.existing):
                self.report.insert("end", f"  - {p}\n")
            self.report.insert("end", "\n")

        if self.missing:
            self.report.insert("end", "✚ To create:\n")
            for p in sorted(self.missing):
                self.report.insert("end", f"  + {p}\n")
        else:
            self.report.insert("end", "Nothing to create. All good!\n")

        self.report.config(state="disabled")

    def create_missing(self):
        target = Path(self.target_var.get()).expanduser()
        try:
            for rel in sorted(self.missing):
                (target / rel).mkdir(parents=True, exist_ok=True)
            messagebox.showinfo("Done", f"Created {len(self.missing)} folders in:\n{target}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create folders:\n{e}")
            return

        # Перепроверим после создания
        self.analyze()


if __name__ == "__main__":
    app = MindForgeGUI()
    app.mainloop()
