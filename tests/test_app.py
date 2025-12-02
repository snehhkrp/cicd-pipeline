import app


def test_home_status_code():
    client = app.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200


def test_home_contains_text():
    client = app.app.test_client()
    resp = client.get("/")
    body = resp.data.decode("utf-8")
    assert "CI/CD" in body or "Pipeline" in body


def test_health_endpoint():
    client = app.app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200

    data = resp.get_json()
    assert data["status"] == "ok"
    assert "build_version" in data
# from flask import Flask, render_template