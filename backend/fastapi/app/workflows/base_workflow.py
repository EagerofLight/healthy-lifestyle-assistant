from typing import Dict, Any
from langgraph.graph import StateGraph
from abc import ABC, abstractmethod
from langgraph.checkpoint.memory import MemorySaver

class BaseWorkflow(ABC):
    def __init__(self):
        self.graph = None
        self.build_graph()
    
    @abstractmethod
    def build_graph(self) -> StateGraph:
        '''
        return a state graph
        '''
        pass

    def run(self, initial_state: Dict[str, Any]) -> Dict[str, Any]:
        if not self.graph:
            self.graph = self.build_graph()
        compiled = self.graph.compile(checkpointer=MemorySaver())
        final_state = compiled.invoke(initial_state)
        return final_state
    
    def get_workflow(self) -> StateGraph:
        if not self.graph:
            self.graph = self.build_graph()
        return self.graph