from fastapi import FastAPI
from pydantic import BaseModel

# declaring our model class using pydantic

class Todo(BaseModel):
    id : int
    item: str