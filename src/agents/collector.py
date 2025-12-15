from src.utils.github_client import GitHubClient

def collector_node(state):
    repo = state["repo"]
    client = GitHubClient()
    docs = client.fetch_markdown_files(repo)
    return {"raw_docs": docs}

