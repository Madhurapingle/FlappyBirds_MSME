from agents.base import BaseAgent
from graph.state import AgentState
from models.llm import get_llm


class PerceptionAgent(BaseAgent):
    name = "perception"

    def __init__(self):
        super().__init__()
        self.llm = get_llm(model="llama-3.3-70b-versatile")

    def run(self, state: AgentState) -> AgentState:

        if state.get("input_mode") == "FORM":
            state["logs"].append(
                "[Perception] FORM mode detected – skipping perception"
            )
            return state

        # Ensure entities dict exists
        if state.get("entities") is None:
            state["entities"] = {}

        # TEXT mode 
        text = state["user_input"].lower().strip()

        if any(word in text for word in ["cancel", "abort", "stop order"]):
            intent = "CANCEL_ORDER"

        elif any(word in text for word in ["status", "track", "tracking"]):
            intent = "CHECK_STATUS"

        elif any(word in text for word in ["order", "buy", "purchase"]):
            intent = "NEW_ORDER"

        else:
            intent = "OTHER"

        #  Save intent into state
        state["intent"] = intent

        # Flags
        needs_inventory = False
        needs_staff = False

        if intent == "NEW_ORDER":
            needs_inventory = True
            needs_staff = True

        state["entities"]["needs_inventory"] = needs_inventory
        state["entities"]["needs_staff"] = needs_staff

        state["logs"].append(f"[Perception] intent={intent}")

        return state
