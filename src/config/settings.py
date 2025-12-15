import os

# Notion
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
NOTION_PAGE_ID = os.getenv("NOTION_PAGE_ID")

# GitHub
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Local storage
DATA_DIR = os.getenv("DATA_DIR", "./data")

