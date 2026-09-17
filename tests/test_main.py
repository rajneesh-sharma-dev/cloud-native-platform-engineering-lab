from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Platform engineering lab available now"}

def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "All Good Bro"}

def test_version():
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"app current version": "0.1.0"}
