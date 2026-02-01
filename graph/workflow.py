from langgraph.graph import StateGraph
from graph.state import AgentState

from agents.perception import PerceptionAgent
from agents.reasoning import ReasoningAgent
from agents.action import ActionAgent
from agents.explanation import ExplanationAgent
from agents.planning import PlanningAgent
from agents.learning import LearningAgent


perception = PerceptionAgent()
reasoning = ReasoningAgent()
action = ActionAgent()
explanation = ExplanationAgent()
planning = PlanningAgent()
learning = LearningAgent()


builder = StateGraph(AgentState)

builder.add_node("perception", perception.safe_run)
builder.add_node("reasoning", reasoning.safe_run)
builder.add_node("action", action.safe_run)
builder.add_node("explanation", explanation.safe_run)
builder.add_node("planning", planning.safe_run)
builder.add_node("learning", learning.safe_run)


builder.set_entry_point("perception")

builder.add_edge("perception", "reasoning")
builder.add_edge("reasoning", "action")
builder.add_edge("action", "explanation")
builder.add_edge("explanation", "planning")
builder.add_edge("planning", "learning")


builder.set_finish_point("planning")
builder.set_finish_point("learning")

graph = builder.compile()
