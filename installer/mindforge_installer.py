# mindforge_gui_installer.py
# рџ“ќ MindForge GUI Installer
# Р§РёС‚Р°РµС‚ Markdown СЃРѕ СЃС‚СЂСѓРєС‚СѓСЂРѕР№ (tree-РіСЂР°С„РёРєР° в”њв”Ђв”Ђ, в””в”Ђв”Ђ, в”‚   ) Рё:
# 1) РёР·РІР»РµРєР°РµС‚ СЃРїРёСЃРѕРє РґРёСЂРµРєС‚РѕСЂРёР№,
# 2) СЃСЂР°РІРЅРёРІР°РµС‚ СЃ С†РµР»РµРІРѕР№ РїР°РїРєРѕР№ (РїРѕ СѓРјРѕР»С‡Р°РЅРёСЋ H:\MindForge),
# 3) РїРѕРєР°Р·С‹РІР°РµС‚ РѕС‚С‡С‘С‚ Рё СЃРѕР·РґР°С‘С‚ РЅРµРґРѕСЃС‚Р°СЋС‰РёРµ РґРёСЂРµРєС‚РѕСЂРёРё.

import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import List, Set

DEFAULT_TARGET = Path(r"H:\MindForge")  # в†ђ С‚РІРѕСЏ С†РµР»РµРІР°СЏ РґРёСЂРµРєС‚РѕСЂРёСЏ

# -------- РџР°СЂСЃРµСЂ РґРµСЂРµРІР° --------

CONNECTORS = ("в”њв”Ђв”Ђ", "в””в”Ђв”Ђ")

def _calc_depth(line: str) -> int:
    """
    РџСЂРёР±Р»РёР·РёС‚РµР»СЊРЅРѕ СЃС‡РёС‚Р°РµС‚ РіР»СѓР±РёРЅСѓ РїРѕ РїСЂРµС„РёРєСЃРЅС‹Рј РіСЂСѓРїРїР°Рј 'в”‚   ' РёР»Рё '    ' РґРѕ РїРµСЂРІРѕРіРѕ СЃРѕРµРґРёРЅРёС‚РµР»СЏ.
    """
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
    # Р±РµСЂС‘Рј РІСЃС‘ РїРѕСЃР»Рµ 'в”њв”Ђв”Ђ ' РёР»Рё 'в””в”Ђв”Ђ '
    for c in CONNECTORS:
        idx = line.find(c)
        if idx != -1:
            return line[idx + len(c):].strip().split("#")[0].strip()  # СѓР±РµСЂС‘Рј РєРѕРјРјРµРЅС‚Р°СЂРёРё РїРѕСЃР»Рµ '#'
    return line.strip()

def parse_tree_dirs(markdown: str) -> List[List[str]]:
    """
    Р’РѕР·РІСЂР°С‰Р°РµС‚ СЃРїРёСЃРѕРє РїСѓС‚РµР№ (РєР°Р¶РґС‹Р№ РїСѓС‚СЊ вЂ” СЃРїРёСЃРѕРє СЃРµРіРјРµРЅС‚РѕРІ) РўРћР›Р¬РљРћ РґР»СЏ РґРёСЂРµРєС‚РѕСЂРёР№.
    РљРѕСЂРЅРµРІСѓСЋ РґРёСЂРµРєС‚РѕСЂРёСЋ (mindforge/ РёР»Рё MindForge/) РѕСЃС‚Р°РІР»СЏРµРј РєР°Рє СЃРµРіРјРµРЅС‚ 0,
    РЅРѕ РїРѕР·Р¶Рµ РѕС‚Р±СЂРѕСЃРёРј РїСЂРё СЃР±РѕСЂРєРµ РѕС‚РЅРѕСЃРёС‚РµР»СЊРЅС‹С… РїСѓС‚РµР№.
    """
    dirs: List[List[str]] = []
    stack: List[str] = []

    lines = markdown.splitlines()

    # РРЅРѕРіРґР° РІ Р±Р»РѕРєРµ РјРѕРіСѓС‚ Р±С‹С‚СЊ plain-СЃС‚СЂРѕРєРё РІРёРґР° "mindforge/" Р±РµР· РІРµС‚РѕРє вЂ” РѕР±СЂР°Р±РѕС‚Р°РµРј РёС…
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue

        # РћС‚РґРµР»СЊРЅР°СЏ РѕР±СЂР°Р±РѕС‚РєР° "РіРѕР»С‹С…" РєРѕСЂРЅРµРІС‹С…: "mindforge/" РёР»Рё "MindForge/"
        if (line.strip().lower().endswith("mindforge/") and " " not in line.strip()) or \
           (line.strip().endswith("/") and line.strip().count("/") == 1 and ("в”њ" not in line and "в””" not in line)):
            # РЎР±СЂРѕСЃРёРј СЃС‚РµРє Рё РЅР°С‡РЅС‘Рј РѕС‚ РєРѕСЂРЅСЏ
            stack = [line.strip().rstrip("/")]
            continue

        if _is_tree_line(line):
            depth = _calc_depth(line)
            name = _extract_name(line)

            # РЅРѕСЂРјР°Р»РёР·СѓРµРј РёРјСЏ (Р±РµР· РєРѕРјРјРµРЅС‚Р°СЂРёСЏ РІ РєРѕРЅС†Рµ Рё Р±РµР· Р»РёС€РЅРёС… РїСЂРѕР±РµР»РѕРІ)
            name = name.strip()

            # РћР±СЂРµР¶РµРј СЃС‚РµРє РґРѕ С‚РµРєСѓС‰РµР№ РіР»СѓР±РёРЅС‹
            # (РґР»СЏ РїРµСЂРІРѕР№ Р·Р°РїРёСЃРё СЃС‚РµРє РјРѕР¶РµС‚ Р±С‹С‚СЊ РїСѓСЃС‚С‹Рј вЂ” С‚РѕРіРґР° РєРѕСЂРµРЅСЊ РѕРїСЂРµРґРµР»РёРј РєР°Рє РїРµСЂРІС‹Р№ РєР°С‚Р°Р»РѕРі РІРµСЂС…РЅРµРіРѕ СѓСЂРѕРІРЅСЏ)
            while len(stack) > depth:
                stack.pop()

            is_dir = name.endswith("/")
            seg = name.rstrip("/")

            if is_dir:
                # РєР°С‚Р°Р»РѕРі вЂ” РґРѕР±Р°РІР»СЏРµРј РІ СЃС‚РµРє Рё СЂРµРіРёСЃС‚СЂРёСЂСѓРµРј РїСѓС‚СЊ
                stack.append(seg)
                dirs.append(stack.copy())
            else:
                # С„Р°Р№Р» вЂ” РґРёСЂРµРєС‚РѕСЂРёСЋ РЅРµ РґРѕР±Р°РІР»СЏРµРј, РЅРѕ РїСѓС‚СЊ-СЂРѕРґРёС‚РµР»СЊ Р·Р°С„РёРєСЃРёСЂСѓРµРј (РЅР° СЃР»СѓС‡Р°Р№, РµСЃР»Рё РѕРЅР° РЅРµ РІСЃС‚СЂРµС‡Р°РµС‚СЃСЏ РѕС‚РґРµР»СЊРЅРѕ)
                parent = stack.copy()
                if parent:
                    dirs.append(parent.copy())

    # РЈРЅРёРєР°Р»РёР·РёСЂСѓРµРј (РєР°Рє РєРѕСЂС‚РµР¶Рё) Рё РІРµСЂРЅС‘Рј СЃРїРёСЃРєРё СЃРµРіРјРµРЅС‚РѕРІ
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
    РћС‚Р±СЂР°СЃС‹РІР°РµС‚ РїРµСЂРІС‹Р№ СЃРµРіРјРµРЅС‚ (РєРѕСЂРµРЅСЊ mindforge/MindForge), СЃРѕР±РёСЂР°РµС‚ РѕС‚РЅРѕСЃРёС‚РµР»СЊРЅС‹Рµ РїСѓС‚Рё.
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

        # Р’РІРѕРґ С†РµР»РµРІРѕР№ РґРёСЂРµРєС‚РѕСЂРёРё
        self.target_var = tk.StringVar(value=str(DEFAULT_TARGET))
        tk.Label(self, text="Target directory:").grid(row=0, column=0, sticky="w", padx=8, pady=8)
        tk.Entry(self, textvariable=self.target_var, width=70).grid(row=0, column=1, sticky="we", padx=4, pady=8)
        tk.Button(self, text="BrowseвЂ¦", command=self.browse_target).grid(row=0, column=2, padx=8, pady=8)

        # РљРЅРѕРїРєРё Р·Р°РіСЂСѓР·РєРё Markdown
        tk.Button(self, text="Open MarkdownвЂ¦", command=self.open_md).grid(row=1, column=0, padx=8, pady=4, sticky="w")
        tk.Button(self, text="Paste from Clipboard", command=self.paste_clipboard).grid(row=1, column=1, padx=4, pady=4, sticky="w")

        # РўРµРєСЃС‚РѕРІР°СЏ РѕР±Р»Р°СЃС‚СЊ РґР»СЏ Markdown
        tk.Label(self, text="Scaffold Markdown:").grid(row=2, column=0, sticky="w", padx=8)
        self.md_text = scrolledtext.ScrolledText(self, wrap="word", height=18)
        self.md_text.grid(row=3, column=0, columnspan=3, sticky="nsew", padx=8, pady=4)

        # РљРЅРѕРїРєРё Р°РЅР°Р»РёР·Р°/СЃРѕР·РґР°РЅРёСЏ
        self.btn_analyze = tk.Button(self, text="Analyze scaffold", command=self.analyze)
        self.btn_analyze.grid(row=4, column=0, padx=8, pady=8, sticky="w")

        self.btn_create = tk.Button(self, text="Create missing folders", command=self.create_missing, state="disabled")
        self.btn_create.grid(row=4, column=1, padx=4, pady=8, sticky="w")

        # РћС‚С‡С‘С‚
        tk.Label(self, text="Report:").grid(row=5, column=0, sticky="w", padx=8)
        self.report = scrolledtext.ScrolledText(self, wrap="word", height=12, state="disabled")
        self.report.grid(row=6, column=0, columnspan=3, sticky="nsew", padx=8, pady=4)

        # Grid weights
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Р”Р°РЅРЅС‹Рµ Р°РЅР°Р»РёР·Р°
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
            # Р°РЅР°Р»РёР· РѕС‚РЅРѕСЃРёС‚РµР»СЊРЅРѕ РЅРµСЃСѓС‰РµСЃС‚РІСѓСЋС‰РµР№ С†РµР»Рё: РІСЃРµ РґРёСЂРµРєС‚РѕСЂРёРё СЃС‡РёС‚Р°РµРј РѕС‚СЃСѓС‚СЃС‚РІСѓСЋС‰РёРјРё
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
            self.report.insert("end", "вњ” Existing:\n")
            for p in sorted(self.existing):
                self.report.insert("end", f"  - {p}\n")
            self.report.insert("end", "\n")

        if self.missing:
            self.report.insert("end", "вњљ To create:\n")
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

        # РџРµСЂРµРїСЂРѕРІРµСЂРёРј РїРѕСЃР»Рµ СЃРѕР·РґР°РЅРёСЏ
        self.analyze()


if __name__ == "__main__":
    app = MindForgeGUI()
    app.mainloop()
