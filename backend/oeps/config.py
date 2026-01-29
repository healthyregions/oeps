from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    load_dotenv(env_path)

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