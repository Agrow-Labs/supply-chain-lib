import sys
from pathlib import Path

# Ensure repository root is importable in tests (so `import tools...` works)
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))
