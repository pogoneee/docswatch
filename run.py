from src.graph.workflow import workflow

if __name__ == "__main__":
    workflow.invoke({
        "repo": "fastapi/fastapi"
    })

print("FINAL RESULT:", result)
