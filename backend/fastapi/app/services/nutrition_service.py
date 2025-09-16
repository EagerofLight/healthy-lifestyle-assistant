# CalorieNinjas + USDA API
import httpx
import json
from typing import Dict, List, Any, Optional
from config import settings

class NutritionService:
    def __init__(self):
        self.calorieninjas_api_key = settings.CALORIENINJAS_API_KEY
        self.usda_api_key = settings.USDA_API_KEY

    def get_nutrition_info(self, food_name: str) -> Dict[str, Any]:
        if self.usda_api_key:
            result = self.get_nutrition_from_usda(food_name)
            if result.get("success"):
                return result
        
        # if result not match
        return self.get_nutrition_in_database(food_name)
    
    def get_nutrition_from_usda(self, food_name: str) -> Dict[str, Any]:
        # TODO:
        # Step1: search food
        # Step2: get nutrition data
        # Step3: parse nutrition data
        pass

    def get_nutrition_in_database(self, food_name: str) -> Dict[str, Any];
        # TODO:
        # Return data from db