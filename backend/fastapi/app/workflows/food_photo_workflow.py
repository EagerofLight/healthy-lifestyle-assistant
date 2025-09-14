from typing import TypedDict, Any, Dict, List
from langgraph.graph import StateGraph
from workflows.base_workflow import BaseWorkflow

class FoodPhotoWorkflowState(TypedDict):
    image_path: str
    detected_foods: List[Dict[str, Any]]
    weight_estimates: List[Dict[str, Any]]
    nutrition: List[Dict[str, Any]]
    final_result: Dict[str, Any]
    err: str
    success: bool

class FoodPhotoWorkflow(BaseWorkflow):
    def build_graph(self) -> StateGraph[Any, None, Any, Any]:
        self.graph = StateGraph(FoodPhotoWorkflowState)

        # detect food from photo
        def detect_foods(state: FoodPhotoWorkflowState) -> FoodPhotoWorkflowState:
            '''
            detected_foods --
            '''
            return state
        
        def estimate_weight(state: FoodPhotoWorkflowState) -> FoodPhotoWorkflowState:
            '''
            weight_estimates --
            '''
            return state
        
        def analyze_nutrition(state: FoodPhotoWorkflowState) -> FoodPhotoWorkflowState:
            '''
            nutrition --
            '''
            return state
        
        def compile_result(state: FoodPhotoWorkflowState) -> FoodPhotoWorkflowState:
            if not state["success"]:
                return state
            # combine result
            result = {
                "foods": state["detected_foods"],
                "nutrition": state["nutrition"],
                "weights": state["weight_estimates"],
            }
            state["final_result"] = result
            return state

        # add nodes
        self.graph.add_node("detect_foods", detect_foods)
        self.graph.add_node("analyze_nutrition", analyze_nutrition)
        self.graph.add_node("estimate_weight", estimate_weight)
        self.graph.add_node("compile_result", compile_result)

        # add edges
        self.graph.add_edge("detect_foods", "analyze_nutrition")
        self.graph.add_edge("analyze_nutrition", "estimate_weight")
        self.graph.add_edge("estimate_weight", "compile_result")

        return self.graph