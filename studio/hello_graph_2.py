import random 
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END

# State
class State(TypedDict):
    agentName: str


def seeName(state: State):
    pass

def longNameFunc(state: State):
    return {"agentName": state["agentName"] + "is long"}

def shortNameFunc(state: State):
    return {"agentName": state["agentName"] + "is short"}


builder = StateGraph(State)
builder.add_node("seeName", seeName)
builder.add_edge(START, "seeName")

builder.add_node("longNameFunc", longNameFunc)
builder.add_node("shortNameFunc", shortNameFunc)


def router(state: State):
    if len(state["agentName"]) > 10:
        return "longNameFunc"
    else:
        return "shortNameFunc"


builder.add_conditional_edges("seeName",router)
builder.add_edge("longNameFunc", END) 
builder.add_edge("shortNameFunc", END) 

# Compile graph
graph = builder.compile()

