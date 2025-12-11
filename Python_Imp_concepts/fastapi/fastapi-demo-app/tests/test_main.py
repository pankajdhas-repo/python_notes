from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI ToDo application!"}

def test_create_todo():
    todo = {"id": 1, "name": "Test", "description": "Test ToDo"}
    response = client.post("/todo", json=todo)
    assert response.status_code == 201
    assert response.json() == todo

def test_get_todos():
    response = client.get("/todo")
    assert response.status_code == 200
    assert isinstance(response.json(), list)