from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class FoodItem(Base):
    __tablename__ = 'food_items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    confidence = Column(Float)
    estimate_weight = Column(Float)
    calories_g = Column(Float)
    total_calories = Column(Float)

    nutrition = relationship("NutritionData", back_populates="food_item", uselist=False, cascade="all, delete-orphan")
    task = relationship("Task", back_populates="food_items")

class NutritionData(Base):
    __tablename__ = 'nutrition_data'
    
    id = Column(Integer, primary_key=True, index=True)
    food_item_id = Column(Integer, ForeignKey("food_items.id"), nullable=False, unique=True)

    protein_g = Column(Float)
    carbs_g = Column(Float)
    fat_g = Column(Float)
    fiber_g = Column(Float)
    sugar_g = Column(Float)
    sodium_mg = Column(Float)

    food_item = relationship("FoodItem", back_populates="nutrition")