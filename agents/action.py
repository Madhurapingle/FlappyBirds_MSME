from agents.base import BaseAgent
from graph.state import AgentState

from tools.order_tools import (
    create_order,
    cancel_order,
    fetch_status
)

from tools.ops_tools import (
    check_inventory,
    check_staff
)


class ActionAgent(BaseAgent):
    name = "action"

    def run(self, state: AgentState) -> AgentState:

        state["action_result"] = {
            "status": "not_executed",
            "message": "No action taken yet"
        }

        if not state.get("execute_action", False):
            state["logs"].append(
                "[Action] skipped execution (not authorized)"
            )
            state["action_result"] = {
                "status": "skipped",
                "message": "Action not executed – requires human review"
            }
            return state

        decision = state.get("decision")
        entities = state.get("entities", {})

        if decision == "CREATE_ORDER":
            product = entities.get("product")
            quantity = entities.get("quantity")

            if not product or not quantity:
                state["logs"].append(
                    "[Action] missing product or quantity"
                )
                state["action_result"] = {
                    "status": "error",
                    "message": "Missing product or quantity"
                }
                return state

            # -------- Inventory check --------
            inventory_result = check_inventory(product, quantity)
            state["logs"].append(
                f"[Action] inventory check: {inventory_result}"
            )

            if not inventory_result["sufficient"]:
                state["action_result"] = {
                    "status": "blocked",
                    "message": "Insufficient inventory",
                    "inventory": inventory_result
                }
                state["logs"].append(
                    "[Action] order blocked due to insufficient inventory"
                )
                return state

            # -------- Staff check --------
            staff_result = check_staff(role="packer")
            state["logs"].append(
                f"[Action] staff check: {staff_result}"
            )

            if not staff_result["available"]:
                state["action_result"] = {
                    "status": "blocked",
                    "message": "Required staff not available",
                    "staff": staff_result
                }
                state["logs"].append(
                    "[Action] order blocked due to staff unavailability"
                )
                return state

            result = create_order(entities)

        elif decision == "CANCEL_ORDER":
            result = cancel_order(entities)

        elif decision == "FETCH_STATUS":
            result = fetch_status(entities)

        else:
            result = {
                "status": "error",
                "message": f"Unknown decision '{decision}'"
            }

        state["action_result"] = result

        state["logs"].append(
            f"[Action] decision={decision}, executed=True"
        )

        return state
