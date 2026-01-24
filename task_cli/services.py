from datetime import datetime

from task_cli.models import TaskStatus, Task
from task_cli.repository import load_tasks, save_task_to_file, save_tasks, _update_task


def add_task(task: str) -> Task:
    tasks = load_tasks()
    task_id = 1
    if tasks:
        task_id = len(tasks) + 1
    task = Task(id=task_id, description=task, status=TaskStatus.TODO, created_at=datetime.now(), updated_at=datetime.now())
    save_task_to_file(task)
    return task


def update_task(task_id: int, description: str) -> dict:
    return _update_task(task_id, description=description)


def delete_task(task_id: int) -> int:
    tasks = load_tasks()

    for i, task_dict in enumerate(tasks):
        if task_dict["id"] == task_id:
            tasks.remove(task_dict)

            save_tasks(tasks)
            return 0

    raise KeyError(f"No such task with id {task_id}")


def mark_task_in_progress(task_id: int) -> dict:
    return _update_task(task_id, status=TaskStatus.IN_PROGRESS)


def mark_task_done(task_id: int) -> dict:
    return _update_task(task_id, status=TaskStatus.DONE)


def list_tasks(status: TaskStatus) -> list[dict]:
    tasks = load_tasks()
    return list(filter(lambda task_dict: task_dict["status"] == status, tasks))

