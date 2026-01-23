from pathlib import Path
import json
import os
from dotenv import load_dotenv

from task_cli.models import Task

load_dotenv()
TASK_FILE = Path(os.getenv("TASK_FILE", "tasks.json"))

def load_tasks() -> list[dict]:
    """Read tasks from the JSON file."""
    if TASK_FILE.exists():
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_task_to_file(task: Task) -> None:
    """Save tasks list to the JSON file."""
    tasks = load_tasks()
    tasks.append(task.to_dict())
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
