from unittest.mock import patch

import pytest

from task_cli.models import TaskStatus
from task_cli.services import add_task, update_task, delete_task, mark_task_in_progress, mark_task_done, list_tasks


@patch('task_cli.services.save_task_to_file')
@patch('task_cli.services.load_tasks')
def test_add_task_when_no_existing_tasks(mock_load_tasks, mock_save):
    mock_load_tasks.return_value = []

    result = add_task("Test task")

    assert result.id == 1
    assert result.description == "Test task"
    assert result.status == TaskStatus.TODO

    mock_save.assert_called_once()
    mock_load_tasks.assert_called()


@patch('task_cli.services.save_task_to_file')
@patch('task_cli.services.load_tasks')
def test_add_task_when_tasks_are_there(mock_load_tasks, mock_save):
    mock_load_tasks.return_value = [
      {
        "id": 1,
        "description": "Test task",
        "status": "todo",
        "created_at": "2026-02-02T20:21:18.689908",
        "updated_at": "2026-02-02T20:21:18.689910"
      }
]

    result = add_task("Another test task")

    assert result.id == 2
    assert result.description == "Another test task"
    assert result.status == TaskStatus.TODO

    mock_save.assert_called_once()
    mock_load_tasks.assert_called()


@patch('task_cli.repository.save_tasks')
@patch('task_cli.repository.load_tasks')
def test_update_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    result = update_task(1, description="New description")

    assert result["id"] == 1
    assert result["description"] == "New description"

    mock_save_tasks.assert_called_once()


@patch('task_cli.repository.save_tasks')
@patch('task_cli.repository.load_tasks')
def test_update_not_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]


    with pytest.raises(KeyError):
        update_task(3, description="New description")
    mock_save_tasks.assert_not_called()


@patch('task_cli.services.save_tasks')
@patch('task_cli.services.load_tasks')
def test_delete_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    result = delete_task(1)

    assert result == 0
    assert mock_load_tasks.return_value == []

    mock_save_tasks.assert_called_once()


@patch('task_cli.services.save_tasks')
@patch('task_cli.services.load_tasks')
def test_delete_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    with pytest.raises(KeyError):
        delete_task(2)


@patch('task_cli.repository.save_tasks')
@patch('task_cli.repository.load_tasks')
def test_mark_in_progress_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    result = mark_task_in_progress(1)

    assert result["id"] == 1
    assert result["description"] == "Test task"
    assert result["status"] == TaskStatus.IN_PROGRESS

    mock_save_tasks.assert_called_once()


@patch('task_cli.repository.save_tasks')
@patch('task_cli.repository.load_tasks')
def test_mark_in_progress_not_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    with pytest.raises(KeyError):
        mark_task_in_progress(2)


@patch('task_cli.repository.save_tasks')
@patch('task_cli.repository.load_tasks')
def test_mark_task_done_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    result = mark_task_done(1)

    assert result["id"] == 1
    assert result["description"] == "Test task"
    assert result["status"] == TaskStatus.DONE

    mock_save_tasks.assert_called_once()


@patch('task_cli.repository.save_tasks')
@patch('task_cli.repository.load_tasks')
def test_mark_task_done_not_existing_task(mock_load_tasks, mock_save_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    with pytest.raises(KeyError):
        mark_task_done(2)



@patch('task_cli.services.load_tasks')
def test_list_tasks_without_status(mock_load_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        },
        {
            "id": 2,
            "description": "Another Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    result = list_tasks()
    assert result == mock_load_tasks.return_value


@patch('task_cli.services.load_tasks')
def test_list_tasks_todo_status(mock_load_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        },
        {
            "id": 2,
            "description": "Another Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    result = list_tasks(TaskStatus.TODO)
    assert result == mock_load_tasks.return_value


@patch('task_cli.services.load_tasks')
def test_list_tasks_in_progress_status(mock_load_tasks):
    mock_load_tasks.return_value = [
        {
            "id": 1,
            "description": "Test task",
            "status": "in_progress",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        },
        {
            "id": 2,
            "description": "Another Test task",
            "status": "todo",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

    result = list_tasks(TaskStatus.IN_PROGRESS)
    assert result ==  [
        {
            "id": 1,
            "description": "Test task",
            "status": "in_progress",
            "created_at": "2026-02-02T20:21:18.689908",
            "updated_at": "2026-02-02T20:21:18.689910"
        }
    ]

