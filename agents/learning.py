from agents.base import BaseAgent
from graph.state import AgentState
from typing import Dict, Any


LEARNING_MEMORY: Dict[str, Any] = {
    "events": [],
    "stats": {
        "total_requests": 0,
        "successful_actions": 0,
        "blocked_actions": 0,
        "skipped_actions": 0,
    }
}


class LearningAgent(BaseAgent):
    """
    Passive observer.
    Records outcomes for future optimization.
    """
    name = "learning"

    def run(self, state: AgentState) -> AgentState:
        action_result = state.get("action_result") or {}
        status = action_result.get("status")

        #Update global stats 
        LEARNING_MEMORY["stats"]["total_requests"] += 1

        if status == "success":
            LEARNING_MEMORY["stats"]["successful_actions"] += 1
        elif status == "blocked":
            LEARNING_MEMORY["stats"]["blocked_actions"] += 1
        elif status == "skipped":
            LEARNING_MEMORY["stats"]["skipped_actions"] += 1

        # Record event
        event = {
            "intent": state.get("intent"),
            "decision": state.get("decision"),
            "status": status,
            "reason": action_result.get("reason"),
            "had_plan": bool(state.get("plan")),
            "input_mode": state.get("input_mode"),
        }

        LEARNING_MEMORY["events"].append(event)

        state["logs"].append("[Learning] outcome recorded")

        return state

def get_failure_rate(intent: str) -> float:
    """
    Returns failure rate (0.0 – 1.0) for a given intent
    based on historical outcomes.
    """
    if not intent:
        return 0.0

    events = [
        e for e in LEARNING_MEMORY["events"]
        if e.get("intent") == intent
    ]

    if not events:
        return 0.0

    failures = [
        e for e in events
        if e.get("status") == "blocked"
    ]

    return len(failures) / len(events)
