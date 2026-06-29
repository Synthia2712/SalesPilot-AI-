from langgraph.graph import StateGraph, END

from app.graph.state import SalesState

from app.agents.planner import generate_plan


def planner_node(state: SalesState):

    plan = generate_plan(state["query"])

    return {

        "plan": plan

    }


workflow = StateGraph(SalesState)

workflow.add_node(

    "planner",

    planner_node

)

workflow.set_entry_point(

    "planner"

)

workflow.add_edge(

    "planner",

    END

)

graph = workflow.compile()