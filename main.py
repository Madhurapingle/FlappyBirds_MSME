from graph.workflow import graph
from utils.pretty_print import print_final_state

initial_state = {
    "user_input": "...",
    "input_mode": "TEXT",   # or "FORM"
    "intent": None,
    "entities": {},
    "decision": None,
    "confidence": None,
    "execute_action": False,
    "action_result": None,
    "logs": []
}

final_state = graph.invoke(initial_state)

print_final_state(final_state)
