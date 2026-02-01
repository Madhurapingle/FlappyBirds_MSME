from agents.learning import LEARNING_MEMORY
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel
from typing import Optional, Dict, Any

from graph.workflow import graph
from graph.state import AgentState

app = FastAPI(title="MSME Agent System")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_PATH = BASE_DIR / "frontend" / "index.html"


@app.get("/")
def serve_ui():
    return FileResponse(FRONTEND_PATH)


@app.get("/favicon.ico")
def favicon():
    return ""


# -------------------------
# Request model
# -------------------------
class ProcessRequest(BaseModel):
    input_mode: str                      # "FORM" or "TEXT"
    user_input: str
    intent: Optional[str] = None
    entities: Optional[Dict[str, Any]] = None


# -------------------------
# Core API
# -------------------------
@app.post("/process")
def process_message(req: ProcessRequest):

    # ---------- INITIAL STATE ----------
    state: AgentState = {
        "user_input": req.user_input,
        "input_mode": req.input_mode,

        "intent": None,
        "entities": {},

        "decision": None,
        "confidence": None,
        "execute_action": False,

        "action_result": None,

        "inventory_status": None,
        "staff_status": None,

        "reasoning_summary": "",
        "plan": "",

        "logs": []
    }

    # ---------- FORM MODE ----------
    if req.input_mode == "FORM":
        state["intent"] = req.intent
        state["entities"] = req.entities or {}

        state["logs"].append(
            "[API] FORM mode detected – skipping perception"
        )

    # ---------- TEXT MODE ----------
    else:
        state["logs"].append(
            "[API] TEXT mode detected – full pipeline"
        )

    # ---------- RUN GRAPH ----------
    # LangGraph may return PARTIAL state → must merge
    result_state = graph.invoke(state)

    # CRITICAL: force full merge
    final_state = {**state, **result_state}

    print("API DEBUG — final_state keys:", final_state.keys())
    print("API DEBUG — plan length:", len(final_state.get("plan", "")))

    # ---------- RESPONSE ----------
    return {
        "intent": final_state.get("intent"),
        "decision": final_state.get("decision"),
        "action_result": final_state.get("action_result"),
        "reasoning_summary": final_state.get("reasoning_summary"),
        "plan": final_state.get("plan"),
        "logs": final_state.get("logs"),
    }
@app.get("/learning/stats")
def get_learning_stats():
    return LEARNING_MEMORY
