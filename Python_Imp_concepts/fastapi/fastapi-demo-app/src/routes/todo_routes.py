from fastapi import APIRouter, HTTPException, status
from typing import List
from ..models.todo import ToDo

router = APIRouter()

todos = []

@router.post('/todo', response_model=ToDo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDo):
    todos.append(todo)
    return todo

@router.get('/todo', response_model=List[ToDo], status_code=status.HTTP_200_OK)
def get_todos():
    return todos

@router.get('/todo/{todo_id}', response_model=ToDo, status_code=status.HTTP_200_OK)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

@router.put('/todo/{todo_id}', response_model=ToDo, status_code=status.HTTP_200_OK)
def update_todo(todo_id: int, updated_todo: ToDo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

@router.delete('/todo/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")