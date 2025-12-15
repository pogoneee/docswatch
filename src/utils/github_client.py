# src/utils/github_client.py
from github import Github
from src.config.settings import GITHUB_TOKEN

class GitHubClient:
    def __init__(self):
        self.client = Github(GITHUB_TOKEN)

    def fetch_markdown_files(self, repo_full_name: str):
        repo = self.client.get_repo(repo_full_name)
        contents = repo.get_contents("")
        docs = {}

        while contents:
            file = contents.pop(0)
            if file.type == "dir":
                contents.extend(repo.get_contents(file.path))
            elif file.name.endswith(".md"):
                docs[file.path] = file.decoded_content.decode("utf-8")

        return docs

