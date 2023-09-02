from fastapi import FastAPI
from models import Todo


app = FastAPI()

# Using fastapi, create a todo list

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos" : todos}

# add authentication
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


# Get a single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message" : "Todo not found"}

# Create a todo
@app.post("/todos")
async def create_todo(todo: Todo):
    todos.append(todo)
    return {"message" : "todo has been added"}


# Update a todo
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo" : todo}
    return {"message" : "Todo not found"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message" : "Todo has been deleted"}
    return {"message" : "Todo not found"}

