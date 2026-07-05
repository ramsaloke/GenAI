from fastapi import FastAPI

from app.routers.todo import router

app = FastAPI()

app.include_router(router)