from datetime import datetime

from task_cli.models import TaskStatus, Task
from task_cli.repository import load_tasks, save_task_to_file


def add_task(task: str) -> Task:
    tasks = load_tasks()
    task_id = 1
    if tasks:
        task_id = len(tasks) + 1
    task = Task(id=task_id, description=task, status=TaskStatus.TODO, created_at=datetime.now(), updated_at=datetime.now())
    save_task_to_file(task)
    return task


def update_task(task_id: int) -> int:
    pass


def delete_task(task_id: int) -> int:
    pass


def mark_task_in_progress(task_id: int) -> int:
    pass


def mark_task_done(task_id: int) -> int:
    pass


def list_tasks(status: TaskStatus) -> int:
    pass

