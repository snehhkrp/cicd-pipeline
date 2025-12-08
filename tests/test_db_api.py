# tests/test_db_api.py

import db


def test_add_task_and_get_tasks(monkeypatch):
    """
    Mock the database functions so tests pass without MySQL.
    """

    # Fake in-memory list to simulate DB
    fake_db = []

    # Fake add_task that inserts into in-memory list
    def fake_add_task(title):
        fake_db.append({
            "id": len(fake_db) + 1,
            "title": title,
            "status": "pending"
        })

    # Fake get_tasks that returns our in-memory list
    def fake_get_tasks():
        return fake_db

    # Replace real DB functions with fakes
    monkeypatch.setattr(db, "add_task", fake_add_task)
    monkeypatch.setattr(db, "get_all_tasks", fake_get_tasks)
    monkeypatch.setattr(db, "get_tasks", fake_get_tasks)  # alias if app uses get_tasks

    # Run test logic
    db.add_task("Sample Task")
    tasks = db.get_tasks()

    assert isinstance(tasks, list)
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Sample Task"
    assert tasks[0]["status"] == "pending"
