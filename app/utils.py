from pathlib import Path
import dotenv
import os

dotenv.load_dotenv()

# FOR THE LOVE OF GOKU, PLEASE UPDATE THIS IF YOU MOVE THIS FILE
def get_project_root() -> Path:
    return Path(__file__).parent.parent

def get_db_url(test=False) -> str:
    return os.getenv("DATABASE_URL", "") if not test else os.getenv("TEST_DATABASE_URL", "")