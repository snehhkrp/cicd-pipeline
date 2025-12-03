# import app


# def test_home_status_code():
#     client = app.app.test_client()
#     response = client.get("/")
#     assert response.status_code == 200


# def test_home_contains_ui_text():
#     client = app.app.test_client()
#     response = client.get("/")
#     body = response.data.decode("utf-8")
#     assert "CI/CD" in body or "Pipeline" in body or "Welcome" in body


# def test_health_endpoint():
#     client = app.app.test_client()
#     response = client.get("/health")
#     assert response.status_code == 200

#     data = response.get_json()
#     assert data["status"] == "ok"
#     assert "build_version" in data
# ====================================================
import sys
import os
import json

# Add project root to PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app


def test_home_status_code():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_ui_text():
    client = app.test_client()
    response = client.get("/")
    body = response.data.decode("utf-8")
    assert "CI/CD" in body or "Pipeline" in body or "Welcome" in body


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "ok"
