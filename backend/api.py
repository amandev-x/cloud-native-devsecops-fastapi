from fastapi import APIRouter, HTTPException, status
from models import Task, TaskResponse
from typing import List
router = APIRouter()

task_db = {
   1: {"task_id": 1, "title": "Deploy Docker containers", "status": "completed"},
   2: {"task_id": 2, "title": "Scan images for vulnerabilities", "status": "in-progress"},
   3: {"task_id": 3, "title": "Update Kubernetes manifests", "status": "pending"},
   4: {"task_id": 4, "title": "Run security tests", "status": "pending"},
   5: {"task_id": 5, "title": "Deploy to staging", "status": "pending"}
}
@router.get("/tasks")
async def get_tasks():
    return list(task_db.values())

@router.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
  if task_id not in task_db:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Task with ID {task_id} not found"
    )
  return task_db[task_id]

@router.post("/tasks", response_model=TaskResponse)
async def create_task(task: Task):
   if task.id in task_db:
      raise HTTPException(
         status_code=status.HTTP_400_BAD_REQUEST,
         detail=f"Task with ID {task.id} already exists"
      )
   task_db[task.id] = task
   return task