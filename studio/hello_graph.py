import random 
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    agentName: str


def capitalizeName(state: State):
    return {"agentName": state["agentName"].capitalize()}
    
builder = StateGraph(State)

builder.add_node("capitalizeName", capitalizeName)

builder.add_edge(START,"capitalizeName")
builder.add_edge("capitalizeName", END)

# Compile graph
graph = builder.compile()

