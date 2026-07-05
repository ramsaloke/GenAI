from fastapi import APIRouter, HTTPException, status

from app.fake_db import todos
from app.schemas import TodoCreate, TodoUpdate

router = APIRouter()

#create todo
@router.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreate):

    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": todo.completed
    }

    todos.append(new_todo)

    return new_todo

#read all todos
@router.get("/todos")
def get_todos():
    return todos

#read one todo 

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):

    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

#update 
@router.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: TodoUpdate):

    for todo in todos:

        if todo["id"] == todo_id:

            if updated.title is not None:
                todo["title"] = updated.title

            if updated.completed is not None:
                todo["completed"] = updated.completed

            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

#delete todo 

@router.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):

    for index, todo in enumerate(todos):

        if todo["id"] == todo_id:
            todos.pop(index)
            return

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )