from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from backend.fastapi.app.api.v1.routers import tasks_management
from backend.fastapi.app.api.v1.routers import food_analysis
from backend.fastapi.app.database import engine, Base

PORT = 8000

@asynccontextmanager
async def lifespan(app: FastAPI):
    # initialization steps

    print("Initialization completed")

    yield # seperate start and close

    print("Shutting down")

# create a singleton
app = FastAPI(lifespan=lifespan)

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# routers
app.include_router(tasks_management.router)
app.include_router(food_analysis.router)