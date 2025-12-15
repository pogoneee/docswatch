from agents.reporter import report_node

state = {
    "repo": "test/repo",
    "summary": "이건 Notion Reporter 단독 테스트입니다.\n- 정상 동작 확인\n- 여러 줄 테스트"
}

report_node(state)
print("DONE")

