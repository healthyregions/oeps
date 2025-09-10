from pathlib import Path

TEMP_DIR = Path(__file__).parent.parent / ".temp"
DATA_DIR = Path(__file__).parent / "data"
REGISTRY_DIR = Path(__file__).parent / "registry"
EXPLORER_ROOT_DIR = Path(__file__).parent.parent.parent / "explorer"

THEME_ORDER = [
    "Geography",
    "Social",
    "Environment",
    "Economic",
    "Policy",
    "Outcome",
    "Composite",
]