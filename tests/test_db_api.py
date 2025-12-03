import json

import app


def test_api_get_tasks(monkeypatch):
    fake = [{"id": 2, "title": "t2", "status": "pending"}]

    def fake_get():
        return fake

    monkeypatch.setattr("db.get_all_tasks", fake_get)
    client = app.app.test_client()
    r = client.get("/tasks")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, list)
    assert data[0]["title"] == "t2"


def test_api_post_task(monkeypatch):
    called = {}

    def fake_add(title):
        called["t"] = title

    monkeypatch.setattr("db.add_task", fake_add)
    client = app.app.test_client()
    r = client.post(
        "/tasks",
        data=json.dumps({"title": "hello"}),
        content_type="application/json",
    )
    assert r.status_code == 201
    assert called["t"] == "hello"
