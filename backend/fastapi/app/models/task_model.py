from sqlalchemy import Column, Integer, String, Text, JSON, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String(255), unique=True, index=True, nullable=False)
    type = Column(String(50), default='general')
    status = Column(String(50), default='Pending')
    params = Column(JSON)
    input_path = Column(String(500))
    output_path = Column(String(500))
    error_message = Column(Text)
    extra = Column(JSON) 
    create_at = Column(DateTime, server_default=func.now())
    complete_at = Column(DateTime, nullable=True)

    food_items = relationship("FoodItem", back_populates="task", cascade="all, delete-orphan", lazy="dynamic")

class WorkflowLog(Base):
    __tablename__ = "workflow_logs"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(String(255), index=True)
    node_name = Column(String(100))
    status = Column(String(50))
    input_data = Column(Text)
    output_data = Column(Text)
    error_message = Column(Text)
    execution_time = Column(Integer)
    created_at = Column(DateTime, server_default=func.now())