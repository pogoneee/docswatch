from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1-mini")

def analyze_node(state):
    summaries = []
    
    for path, diff in state["diffs"].items():
        if not diff.strip():
            continue

        prompt = f"""
        다음은 문서 변경 diff입니다.
        중요 변경점만 요약하고 중요도를 high/medium/low로 분류하세요.
        
        {diff}
        """
        res = llm.invoke(prompt)
        summaries.append(f"## {path}\n{res.content}")

    return {"summary": "\n\n".join(summaries)}

