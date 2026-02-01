from typing import TypedDict, Optional, Dict, Any, List


class OrderEntities(TypedDict, total=False):
    """
    Structured business data extracted from user input
    or provided directly by a form / API.
    """
    product: Optional[str]
    quantity: Optional[int]
    order_id: Optional[str]
    raw_text: Optional[str]


class AgentState(TypedDict):
    """
    Global state shared across all agents.
    This is the ADK contract.
    """

    user_input: str                      # original user message (always present)
    input_mode: str                      # "TEXT" or "FORM"

    intent: Optional[str]                # NEW_ORDER, CANCEL_ORDER, CHECK_STATUS, OTHER
    entities: OrderEntities              # structured entities

    decision: Optional[str]              # CREATE_ORDER, CANCEL_ORDER, FETCH_STATUS, HUMAN_REVIEW
    confidence: Optional[float]          # confidence in decision (0.0 – 1.0)
    execute_action: bool                 

    action_result: Optional[Dict[str, Any]]  
    logs: List[str]                      

    inventory_status: Optional[Dict[str, int]]   # e.g. {"Laptop": 12}
    staff_status: Optional[Dict[str, bool]]

    reasoning_summary: str
    plan : str