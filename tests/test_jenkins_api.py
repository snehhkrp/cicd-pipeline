import app

def test_jenkins_api_endpoint():
    c = app.app.test_client()
    r = c.get("/api/jenkins/builds")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, (list, dict))
