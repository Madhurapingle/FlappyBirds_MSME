from agents.base import BaseAgent
from graph.state import AgentState


class ExplanationAgent(BaseAgent):
    name = "explanation"

    def run(self, state: AgentState) -> AgentState:
        decision = state.get("decision")
        action_result = state.get("action_result", {})

        summary = ""

        if action_result.get("status") == "success":
            summary = (
                "The requested action was successfully executed. "
                "All required conditions such as inventory and staff availability "
                "were satisfied."
            )

        elif action_result.get("status") == "skipped":
            summary = (
                "The system did not execute any action because the request "
                "requires human review or explicit confirmation."
            )

        elif action_result.get("status") == "blocked":
            reasons = []

            if "inventory" in action_result:
                inv = action_result["inventory"]
                reasons.append(
                    f"only {inv['available']} units were available while "
                    f"{inv['requested']} were requested"
                )

            if "staff" in action_result:
                staff = action_result["staff"]
                reasons.append(
                    f"required staff role '{staff['role']}' is currently unavailable"
                )

            reason_text = " and ".join(reasons)

            summary = (
                "The requested action could not be completed because "
                + reason_text
                + "."
            )

        else:
            summary = (
                "The system could not complete the request due to an "
                "unexpected condition. Manual review is recommended."
            )

        state["reasoning_summary"] = summary

        state["logs"].append(
            f"[Explanation] summary generated"
        )

        return state
