# paths.py
#mf_core/common/paths.py
# [WIP] paths (в разработке)
from pathlib import Path
# .../MindForge/mf_core/common/paths.py -> parents[2] = MindForge (корень проекта)
PROJECT_ROOT = Path(__file__).resolve().parents[2]