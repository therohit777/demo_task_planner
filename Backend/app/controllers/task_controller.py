
import os
import ast
import json
from fastapi import HTTPException
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def extract_python_structure_from_code(code: str):
    """
    Extracts functions and classes from the provided Python code.
    Returns a dictionary with lists of function and class names.
    """
    try:
        tree = ast.parse(code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        return {"functions": functions, "classes": classes}
    except Exception as e:
        return {"error": f"Could not parse code: {e}"}


def generate_task_plan(task_description: str, code_structure: dict):
    """
    Uses OpenAI GPT-4 to generate a step-by-step task plan based on the provided code structure
    and saves the plan in the 'scripts' folder within the backend application.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not found in environment variables.")

    prompt = f"""
    You are an AI assistant that helps developers modify a codebase.
    The following is the structure of the code (from the provided file):
    {json.dumps(code_structure, indent=2)}

    The user wants to accomplish the following task:
    "{task_description}"

    Provide a structured step-by-step task plan on how to achieve this, identifying relevant modifications required and also provide example with the code snippets.
    """

    client = openai.OpenAI(api_key=OPENAI_API_KEY)  # Ensure you set your OpenAI API key

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        task_plan = response.choices[0].message.content.strip()

        # Define the scripts directory explicitly
        base_folder = os.path.join("app", "scripts")
        os.makedirs(base_folder, exist_ok=True)

        # Generate a unique filename based on task description
        sanitized_task_name = task_description.replace(" ", "_").replace("/", "_")[:50]  # Limit filename length
        file_path = os.path.join(base_folder, f"{sanitized_task_name}.txt")

        # Save the task plan to a file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(task_plan)

        return {"task_plan": task_plan, "file_path": file_path}

    except openai.error.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating task plan: {str(e)}")

