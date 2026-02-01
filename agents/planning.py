from agents.base import BaseAgent
from graph.state import AgentState
from models.llm import get_llm


class PlanningAgent(BaseAgent):
    name = "planning"

    def __init__(self):
        super().__init__()
        self.llm = get_llm()

    def run(self, state: AgentState) -> AgentState:
        action_result = state.get("action_result", {})
        reasoning_summary = state.get("reasoning_summary", "")

        if action_result.get("status") != "blocked":
            state["plan"] = "No planning required. The request was handled successfully."
            state["logs"].append(
                "[Planning] skipped (no blockage)"
            )
            return state

        context = {
            "reason": reasoning_summary,
            "details": action_result
        }

        prompt = f"""
You are an operations planning assistant for a small business.

The system could not execute an action due to the following reason:
{context}

Your task:
- Propose a clear, step-by-step plan to resolve the issue
- Do NOT execute anything
- Do NOT assume external systems
- Keep steps practical and realistic for an MSME

Return the plan as a numbered list.
"""

        plan_text = self.llm.invoke(prompt).content.strip()

        state["plan"] = plan_text

        state["logs"].append(
            f"[Planning DEBUG] plan_length={len(state['plan']) if state.get('plan') else 0}"
)


        state["logs"].append(
            "[Planning] recovery plan generated"
        )

        return state
