import os
import sys

# Add project root to module path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app  # noqa: E402


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
    
