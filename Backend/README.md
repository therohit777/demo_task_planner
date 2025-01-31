# Task Planner CLI

## Overview
This is a CLI tool that scans a codebase, identifies key components, and generates a structured plan based on a user-defined task using AI.

## Requirements
- Python 3.x
- OpenAI API key

## Installation
1. Clone or download this repository.
2. Install required dependencies:

   ```sh
   pip install openai
   ```

3. Set your OpenAI API key in the script (`OPENAI_API_KEY`).

## Usage
Run the CLI tool by executing:

```sh
python task_planner.py
```

Then, follow the on-screen prompts to analyze a codebase and generate a task plan.

## Output
The task plan will be displayed in the terminal and saved to `task_plan.txt`.
