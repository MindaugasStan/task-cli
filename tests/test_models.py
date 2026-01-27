from datetime import datetime
from task_cli.models import Task, TaskStatus

def test_task_to_dict_and_from_dict():
    now = datetime.now()
    task = Task(
        id=1,
        description="Test task",
        status=TaskStatus.TODO,
        created_at=now,
        updated_at=now,
    )

    data = task.to_dict()

    assert data["id"] == 1
    assert data["description"] == "Test task"
    assert data["status"] == "todo"
    assert data["created_at"] == now.isoformat()
    assert data["updated_at"] == now.isoformat()

    new_task = Task.from_dict(data)
    assert new_task.id == 1
    assert new_task.description == "Test task"
    assert new_task.status == TaskStatus.TODO
    assert new_task.created_at == now
    assert new_task.updated_at == now


def test_task_update():
    task = Task(
        id=1,
        description="Old desc",
        status=TaskStatus.TODO,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

    old_updated = task.updated_at

    task.update(description="New desc", status=TaskStatus.IN_PROGRESS)

    assert task.description == "New desc"
    assert task.status == TaskStatus.IN_PROGRESS
    assert task.updated_at > old_updated


def test_task_str():
    task = Task(
        id=1,
        description="Task string",
        status=TaskStatus.DONE,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    s = str(task)
    assert s == f"[1] Task string (done)"

