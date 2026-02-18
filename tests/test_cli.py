from types import SimpleNamespace

import task_cli.cli as cli
import task_cli.services as services


def test_add_task(monkeypatch, capsys):
    monkeypatch.setattr(services, "add_task", lambda text: SimpleNamespace(id=42))

    result = cli.run(["add", "Buy milk"])

    assert result == 0
    assert "Task added successfully (ID: 42)" in capsys.readouterr().out


def test_add_task_failure(monkeypatch):
    monkeypatch.setattr(services, "add_task", lambda text: None)

    assert cli.run(["add", "Buy milk"]) == 1


def test_delete_task(monkeypatch):
    monkeypatch.setattr(services, "delete_task", lambda task_id: None)

    assert cli.run(["delete", "1"]) == 0


def test_delete_task_not_found(monkeypatch, capsys):
    monkeypatch.setattr(services, "delete_task", lambda task_id: (_ for _ in ()).throw(KeyError("Not found")))

    result = cli.run(["delete", "999"])

    assert result == 1
    assert "Not found" in capsys.readouterr().out


def test_mark_in_progress(monkeypatch):
    monkeypatch.setattr(services, "mark_task_in_progress", lambda task_id: None)

    assert cli.run(["mark-in-progress", "1"]) == 0


def test_mark_done(monkeypatch):
    monkeypatch.setattr(services, "mark_task_done", lambda task_id: None)

    assert cli.run(["mark-done", "1"]) == 0


def test_list_empty(monkeypatch, capsys):
    monkeypatch.setattr(services, "list_tasks", lambda status: [])

    result = cli.run(["list"])

    assert result == 0
    assert "No tasks found" in capsys.readouterr().out
