from pydantic import BaseModel

class TodoCreate(BaseModel):
    title : str 
    completed : bool

class TodoUpdate(BaseModel):
    title : str | None = None 
    completed : bool | None = None


class TodoResponse(BaseModel):
    id: int
    title : str
    completed: bool
