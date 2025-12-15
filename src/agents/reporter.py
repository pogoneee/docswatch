from notion_client import Client
from datetime import datetime
from src.config.settings import NOTION_TOKEN, NOTION_PAGE_ID

notion = Client(auth=NOTION_TOKEN)

def report_node(state):
    """
    Notion Reporter Agent
    - 변경 요약을 지정된 Notion 페이지에 누적 기록
    """

    summary = state["summary"]
    repo = state["repo"]
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    

    blocks = [
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": f"📦 {repo} – Docs Update"}
                    }
                ]
            },
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": f"⏱ {now}"}
                    }
                ]
            },
        },
    ]

    # Notion block text limit 대응 (chunking)
    MAX_LEN = 1800
    for i in range(0, len(summary), MAX_LEN):
        chunk = summary[i:i + MAX_LEN]
        blocks.append(
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": chunk}
                        }
                    ]
                },
            }
        )

    notion.blocks.children.append(
        block_id=NOTION_PAGE_ID,
        children=blocks
    )

    return {"report": summary}

