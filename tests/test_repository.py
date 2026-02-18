import pytest
import json

from task_cli.repository import load_tasks, _update_task


def test_load_tasks_no_file(tmp_path):
    assert load_tasks(tmp_path / "test_tasks.json") == []


def test_load_tasks_with_data(tmp_path):
    task_file = tmp_path / "test_tasks.json"
    tasks = [{"id": 1, "description": "Buy milk", "status": "todo"}]
    task_file.write_text(json.dumps(tasks))
    assert load_tasks(task_file) == tasks


def test_load_tasks_invalid_json(tmp_path):
    task_file = tmp_path / "test_tasks.json"
    task_file.write_text("not valid json{{{")
    with pytest.raises(json.JSONDecodeError):
        load_tasks(task_file)


def test_update_task_description(tmp_path):
    task_file = tmp_path / "test_tasks.json"
    tasks = [{"id": 1, "description": "Buy milk", "status": "todo"}]
    task_file.write_text(json.dumps(tasks))
    result = _update_task(1, description="Buy oat milk")
    assert result["description"] == "Buy oat milk"


def test_update_task_not_found(tmp_path):
    task_file = tmp_path / "test_tasks.json"
    task_file.write_text(json.dumps([]))
    with pytest.raises(KeyError):
        _update_task(999)
