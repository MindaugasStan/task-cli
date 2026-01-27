import argparse
import task_cli.cli as task_cli


def test_run_add(monkeypatch):
    called = {}
    def fake_handle(args):
        called["task"] = args.task
        return 0

    monkeypatch.setattr(task_cli, "handle_add", fake_handle)

    result = task_cli.run(["add", "Buy milk"])

    assert result == 0
    assert called["task"] == "Buy milk"


# fake task object to return from add_task
class FakeTask:
    def __init__(self, task_id):
        self.id = task_id

def test_handle_add_print(monkeypatch, capsys):
    def fake_add_task(text):
        return FakeTask(42)

    monkeypatch.setattr(task_cli, "add_task", fake_add_task)

    args = argparse.Namespace(task="Buy milk")
    result = task_cli.handle_add(args)

    captured = capsys.readouterr()

    assert result == 0
    assert "Task added successfully (ID: 42)" in captured.out


def test_handle_add_failure(monkeypatch, capsys):
    monkeypatch.setattr(task_cli, "add_task", lambda x: None)

    args = argparse.Namespace(task="Buy milk")
    result = task_cli.handle_add(args)

    captured = capsys.readouterr()

    assert result == 1
    assert captured.out == ""


def test_handle_delete_calls_delete_task(monkeypatch):
    called = {}

    def fake_delete_task(task_id):
        called["id"] = task_id

    monkeypatch.setattr(task_cli, "delete_task", fake_delete_task)

    args = argparse.Namespace(task_id=5)
    result = task_cli.handle_delete(args)

    assert result == 0
    assert called["id"] == 5


def test_handle_in_progress_success(monkeypatch):
    def fake_mark(task_id):
        pass

    monkeypatch.setattr(task_cli, "mark_task_in_progress", fake_mark)

    args = argparse.Namespace(task_id=2)
    result = task_cli.handle_in_progress(args)

    assert result == 0

def test_handle_in_progress_failure(monkeypatch, capsys):
    def fake_mark(task_id):
        raise KeyError("Not found")

    monkeypatch.setattr(task_cli, "mark_task_in_progress", fake_mark)

    args = argparse.Namespace(task_id=2)
    result = task_cli.handle_in_progress(args)

    captured = capsys.readouterr()
    assert result == 1
    assert "Not found" in captured.out


def test_handle_done_success(monkeypatch):
    def fake_mark(task_id):
        pass

    monkeypatch.setattr(task_cli, "mark_task_done", fake_mark)

    args = argparse.Namespace(task_id=3)
    result = task_cli.handle_done(args)
    assert result == 0

def test_handle_done_failure(monkeypatch, capsys):
    def fake_mark(task_id):
        raise KeyError("Not found")

    monkeypatch.setattr(task_cli, "mark_task_done", fake_mark)

    args = argparse.Namespace(task_id=3)
    result = task_cli.handle_done(args)

    captured = capsys.readouterr()
    assert result == 1
    assert "Not found" in captured.out


def test_handle_list_empty(monkeypatch, capsys):
    monkeypatch.setattr(task_cli, "list_tasks", lambda status: [])

    args = argparse.Namespace(status=None)
    result = task_cli.handle_list(args)

    captured = capsys.readouterr()
    assert result == 0
    assert "No tasks found" in captured.out

