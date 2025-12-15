from agents.analyzer import analyze_node

state = {
    "diffs": {
        "README.md": """
        - Old sentence
        + New important sentence
        """
    }
}

result = analyze_node(state)

print(result["summary"])

