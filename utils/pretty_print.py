def print_final_state(state: dict):
    line = "━" * 44

    print(f"\n{line}")
    print(" MSME AGENT EXECUTION SUMMARY")
    print(f"{line}\n")

    # User Input
    print(" User Input:")
    print(state.get("user_input", ""))
    print()

    # Perception
    print(" Perception:")
    print(f"• Intent detected: {state.get('intent')}")
    print()

    # Reasoning
    print(" Reasoning:")
    print(f"• Decision taken: {state.get('decision')}")
    print(f"• Confidence: {state.get('confidence')}")
    print()

    # Action Result
    print(" Action Result:")
    action = state.get("action_result") or {}
    for k, v in action.items():
        print(f"• {k.replace('_', ' ').title()}: {v}")
    print()

    # Logs
    print(" Execution Logs:")
    for log in state.get("logs", []):
        print(f"• {log}")

    print(f"\n{line}\n")
