from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent / '.cache'
DATA_DIR = Path(__file__).parent / 'data'
RESOURCES_DIR = DATA_DIR / 'resources'
LOOKUPS_DIR = DATA_DIR / 'lookups'
EXPLORER_ROOT_DIR = Path(Path(__file__).parent.parent, 'explorer')
