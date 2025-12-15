from agents.diff_agent import diff_node

state = {
    "repo": "fastapi/fastapi",
    "raw_docs": {
        "README.md": "# Title\nOld content"
    }
}

result = diff_node(state)

print("Diff keys:", result["diffs"].keys())
print(result["diffs"]["README.md"])

