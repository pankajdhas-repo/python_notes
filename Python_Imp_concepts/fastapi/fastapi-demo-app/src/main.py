from fastapi import FastAPI
from .routes.todo_routes import router as todo_router

app = FastAPI()

app.include_router(todo_router)

@app.get('/', tags=['main'])
def read_root():
    return {"message": "Welcome to the FastAPI ToDo application!"}