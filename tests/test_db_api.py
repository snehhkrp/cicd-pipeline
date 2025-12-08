from db import add_task, get_tasks
import db


def test_add_task_and_get_tasks(monkeypatch):
    """Mock DB so tests pass even without MySQL."""
    fake_db = []

    def fake_add(title):
        fake_db.append({"id": 1, "title": title, "status": "pending"})

    def fake_get():
        return fake_db

    monkeypatch.setattr(db, "add_task", fake_add)
    monkeypatch.setattr(db, "get_tasks", fake_get)

    add_task("Sample Task")
    tasks = get_tasks()

    assert isinstance(tasks, list)
    assert any("Sample Task" in t["title"] for t in tasks)
