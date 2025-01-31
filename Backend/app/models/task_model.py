from pydantic import BaseModel

class TaskPlanRequest(BaseModel):
    file_content: str
    task_description: str