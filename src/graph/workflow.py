from langgraph.graph import StateGraph, END
from typing import TypedDict

from src.agents.collector import collector_node
from src.agents.diff_agent import diff_node
from src.agents.analyzer import analyze_node
from src.agents.reporter import report_node


class State(TypedDict):
    repo: str
    raw_docs: dict
    diffs: dict
    summary: str
    report: str

graph = StateGraph(State)

graph.add_node("collector", collector_node)
graph.add_node("diff", diff_node)
graph.add_node("analyze", analyze_node)
graph.add_node("report", report_node)

graph.set_entry_point("collector")
graph.add_edge("collector", "diff")
graph.add_edge("diff", "analyze")
graph.add_edge("analyze", "report")
graph.add_edge("report", END)

workflow = graph.compile()

