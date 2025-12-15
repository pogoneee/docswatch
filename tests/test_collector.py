from agents.collector import collector_node

state = {
    "repo": "fastapi/fastapi"
}

result = collector_node(state)

print("Fetched files:", len(result["raw_docs"]))
print(list(result["raw_docs"].keys())[:5])

