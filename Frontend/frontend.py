import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/task_plan"  # Update with actual FastAPI backend URL

st.title("Task Plan Generator")

st.write("Upload a Python file and provide a task description to generate a task plan.")

uploaded_file = st.file_uploader("Upload Python file", type=["py"])
task_description = st.text_area("Task Description", "Describe the task plan you need...")

if uploaded_file and task_description:
    if st.button("Generate Task Plan"):
        try:
            files = {"file": uploaded_file.getvalue()}
            data = {"task_description": task_description}
            response = requests.post(BACKEND_URL, files=files, data=data)

            if response.status_code == 200:
                task_plan = response.json().get("task_plan", "No task plan generated.")
                st.success("Task Plan Generated Successfully!")
                st.text_area("Generated Task Plan", task_plan['task_plan'].replace("\\n", "\n"), height=300)
            else:
                st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
        except Exception as e:
            st.error(f"Request failed: {e}")