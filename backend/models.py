from pydantic import BaseModel

class Task(BaseModel):
    id: int 
    title: str 
    completed: bool = False

class TaskResponse(Task):
    pass 