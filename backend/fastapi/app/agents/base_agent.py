from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, name: str = 'BaseAgent'):
        self.name = name

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

    def log(self, message, level, **kwargs):
        print(f"[{self.name}] -- [{level}] -- {message} | info: {kwargs}")