from fastapi import File, Form, HTTPException, UploadFile
from app.controllers.task_controller import extract_python_structure_from_code, generate_task_plan
from app.models.task_model import TaskPlanRequest
from app import app
from datetime import datetime
import pytz


@app.get("/server-check")
def health_check():
    try:
        # Get current time in IST
        ist = pytz.timezone('Asia/Kolkata')
        current_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
         
        # Format the response
        response = {
            "status_code": 200,
            "message": "Server check successful.",
            "data": {
                "timestamp": current_time
            }
        }
        return response

    except Exception as e:
        # Log the exceptio
        
        # Return error response
        response = {
            "status_code": 500,
            "message": "Server check failed.",
            "data": {
                "error": str(e)
            }
        }
        return response
    

@app.post("/task_plan")
async def create_task_plan(
    file: UploadFile = File(...),
    task_description: str = Form(...)
):
    try:
        file_content = await file.read()  # Read the file content as bytes
        file_text = file_content.decode("utf-8")  # Convert bytes to string (assuming UTF-8 encoding)

        code_structure = extract_python_structure_from_code(file_text)

        if "error" in code_structure:
            raise HTTPException(status_code=400, detail=code_structure["error"])

        task_plan = generate_task_plan(task_description, code_structure)
        return {"task_plan": task_plan}

    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File must be a valid UTF-8 text file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")