from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent / '.cache'
DATA_DIR = Path(__file__).parent / 'data'
REGISTRY_DIR = Path(__file__).parent / 'registry'
LOOKUPS_DIR = DATA_DIR / 'lookups'
EXPLORER_ROOT_DIR = Path(Path(__file__).parent.parent, 'explorer')
