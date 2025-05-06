from langchain_core.messages import HumanMessage, SystemMessage, RemoveMessage
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END

# We will use this model for both the conversation and the summarization
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4o", temperature=0) 

    
# Define the logic to call the model
def call_model(state: MessagesState):
    messages = state["messages"]
    response = model.invoke(messages)
    return {"messages": response}


# Define a new graph
workflow = StateGraph(MessagesState)

workflow.add_edge(START, "conversation")
workflow.add_node("conversation", call_model)
workflow.add_edge("conversation", END)

# Compile
graph = workflow.compile()