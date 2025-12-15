from src.graph.workflow import workflow

def pretty_print_state(state: dict):
    print("\n=== FINAL STATE ===")
    for k, v in state.items():
        if isinstance(v, str):
            print(f"\n[{k}] ({len(v)} chars)")
            print(v[:500])
        else:
            print(f"\n[{k}]")
            print(v)


if __name__ == "__main__":
    print("🚀 Starting Docswatch workflow...\n")

    # --- Stream mode: node별 실행 로그 ---
    final_state = None
    for event in workflow.stream({
        "repo": "pogoneee/docswatch"
    }):
        print("\n--- LANGGRAPH EVENT ---")
        for node, output in event.items():
            print(f"[{node}]")
            for k, v in output.items():
                preview = str(v)
                if isinstance(v, str):
                    preview = preview[:300]
                print(f"  {k}: {preview}")

        # 마지막 state 기억
        final_state = output

    # --- Final Result ---
    if final_state:
        pretty_print_state(final_state)

