import json
from pathlib import Path

from task_cli.models import Task, TaskStatus


TASK_FILE = Path("tasks.json")


def _update_task(task_id: int, description: str = None, status: TaskStatus = None) -> dict:
    tasks = load_tasks()

    for i, task_dict in enumerate(tasks):
        if task_dict["id"] == task_id:
            task = Task.from_dict(task_dict)
            task.update(description=description, status=status)

            tasks[i] = task.to_dict()
            save_tasks(tasks)

            return tasks[i]

    raise KeyError(f"No such task with id {task_id}")


def load_tasks() -> list[dict]:
    """Read tasks from the JSON file."""
    if TASK_FILE.exists():
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks: list[dict]) -> None:
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def save_task_to_file(task: Task) -> None:
    """Save tasks list to the JSON file."""
    tasks = load_tasks()
    tasks.append(task.to_dict())
    save_tasks(tasks)
