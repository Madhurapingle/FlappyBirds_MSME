from agents.base import BaseAgent
from graph.state import AgentState
from models.llm import get_llm
from agents.learning import get_failure_rate


class ReasoningAgent(BaseAgent):
    name = "reasoning"

    def __init__(self):
        super().__init__()
        self.llm = get_llm()

    def run(self, state: AgentState) -> AgentState:
        intent = state.get("intent")
        input_mode = state.get("input_mode")

        failure_rate = get_failure_rate(intent)
        high_risk = failure_rate >= 0.6
        extreme_risk = failure_rate >= 0.8

        if input_mode == "FORM":
            if intent == "NEW_ORDER":
                decision = "CREATE_ORDER"
            elif intent == "CANCEL_ORDER":
                decision = "CANCEL_ORDER"
            elif intent == "CHECK_STATUS":
                decision = "FETCH_STATUS"
            else:
                decision = "HUMAN_REVIEW"

            # Execution policy
            execute = decision != "HUMAN_REVIEW" and not extreme_risk

            # Confidence adapts
            confidence = 1.0 if not high_risk else max(0.4, 1.0 - failure_rate)

            state["decision"] = decision
            state["execute_action"] = execute
            state["confidence"] = confidence

            state["logs"].append(
                f"[Reasoning] FORM mode: intent={intent}, failure_rate={failure_rate:.0%}, decision={decision}"
            )

            return state

        if intent == "NEW_ORDER":
            decision = "CREATE_ORDER"
        elif intent == "CANCEL_ORDER":
            decision = "CANCEL_ORDER"
        elif intent == "CHECK_STATUS":
            decision = "FETCH_STATUS"
        else:
            decision = "HUMAN_REVIEW"

        execute = decision != "HUMAN_REVIEW" and not high_risk
        confidence = 0.9 if not high_risk else max(0.3, 0.9 - failure_rate)

        state["decision"] = decision
        state["execute_action"] = execute
        state["confidence"] = confidence

        state["logs"].append(
            f"[Reasoning] TEXT mode: intent={intent}, failure_rate={failure_rate:.0%}, decision={decision}"
        )

        return state
