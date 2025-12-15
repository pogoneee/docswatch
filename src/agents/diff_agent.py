import difflib
from src.utils.memory import load_doc, save_doc

def diff_node(state):
    repo = state["repo"]
    diffs = {}

    for path, content in state["raw_docs"].items():
        old = load_doc(repo, path)
        if old:
            diff = difflib.unified_diff(
                old.splitlines(),
                content.splitlines(),
                lineterm=""
            )
            diffs[path] = "\n".join(diff)

        save_doc(repo, path, content)

    return {"diffs": diffs}

