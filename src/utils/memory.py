import os
from src.config.settings import DATA_DIR

def save_doc(repo, path, content):
    dir_path = f"{DATA_DIR}/{repo}/{path}"
    os.makedirs(os.path.dirname(dir_path), exist_ok=True)
    with open(dir_path, "w") as f:
        f.write(content)

def load_doc(repo, path):
    try:
        with open(f"{DATA_DIR}/{repo}/{path}") as f:
            return f.read()
    except FileNotFoundError:
        return None

