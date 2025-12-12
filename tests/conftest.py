"""Конфіг для pytest."""

import sys
from pathlib import Path

# Додайте папку src до sys.path
root = Path(__file__).parent.parent
sys.path.insert(0, str(root / "src"))
