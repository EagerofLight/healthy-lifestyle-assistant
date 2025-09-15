from base_agent import BaseAgent

class FoodPhotoDetectionAgent(BaseAgent):
    def __init__(self, vision_service):
        super().__init__('FoodPhotoDetectionAgent')
        self.vision_service = vision_service

    def run(self, image_path: str):
        self.log('start food photo detection', 'INFO', image=image_path)
        # TODO


class NutritionSearchAgent(BaseAgent):
    def __init__(self, nutrition_api_client):
        super().__init__("NutritionsearchAgent")
        self.nutrition_api = nutrition_api_client

    def run(self, food_name):
        self.log("start searching nutrition from food", 'INFO', food=food_name) 
        # TODO


class WeightEstimationAgent(BaseAgent):
    def __init__(self, api):
        super().__init__("WeightEstimationAgent")
        self.llm = api

    def run(self, food_name, context={}):
        self.log("start weight estimaation", 'INFO', food=food_name)
        # TODO