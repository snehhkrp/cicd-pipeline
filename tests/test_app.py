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

import app

def test_home():
    c = app.app.test_client()
    r = c.get("/")
    assert r.status_code == 200
