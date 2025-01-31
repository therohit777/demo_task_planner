# Task Planner Application

## Description
Task Planner is a tool that generates an action plan to modify or refactor changes in a codebase. Currently, it supports Python codebases but can be extended to support additional languages in the future.

---
![Task Planner Application](https://drive.google.com/file/d/1KSRJFMprAB5wInxAWg7cbqG76VNifzJf/view?usp=sharing)

## Setup and Running Instructions

### Running the Backend
1. Navigate to the backend directory:
   ```sh
   cd Backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install all dependencies from the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the backend server:
   ```sh
   python run.py
   ```

### Running the Frontend
1. Navigate to the frontend directory:
   ```sh
   cd frontend
   ```
2. Run the Streamlit application:
   ```sh
   streamlit run frontend.py
   ```

---

## Environment Variables
To test the application, ensure you have an `.env` file in the root directory with the following key:
```
OPEN_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

---

## Future Enhancements
- Support for additional programming languages.
- Improved action plan generation with AI-powered suggestions.
- Integration with various IDEs and code repositories.

---

Enjoy using Task Planner! 🚀
