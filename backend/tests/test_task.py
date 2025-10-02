import pytest
from fastapi.testclient import TestClient
from main import app
from app.core.rate_limiter import limiter

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_rate_limits():
    """Reset rate limits before each test."""
    limiter.reset()
    yield
    limiter.reset()

@pytest.fixture
def auth_token():
    """Register a test user and return JWT token."""
    email = "taskuser@example.com"
    password = "password123"
    # Register user (ignore if already exists)
    client.post("/api/v1/users/register", json={
        "name": "Task User",
        "email": email,
        "password": password
    })
    # Login
    res = client.post(
        "/api/v1/users/login",
        data={"username": email, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return res.json()["access_token"]

@pytest.fixture
def auth_header(auth_token):
    return {"Authorization": f"Bearer {auth_token}"}

task_id = None  # store created task id for later tests

def test_create_task(auth_header):
    global task_id
    response = client.post("/api/v1/tasks/", json={
        "title": "Test Task",
        "description": "This is a test task"
    }, headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data
    task_id = data["id"]

def test_get_task(auth_header):
    response = client.get(f"/api/v1/tasks/{task_id}", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Test Task"

def test_update_task(auth_header):
    response = client.put(f"/api/v1/tasks/{task_id}", json={
        "title": "Updated Task",
        "description": "Updated description"
    }, headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"

def test_list_tasks(auth_header):
    response = client.get("/api/v1/tasks/", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(t["id"] == task_id for t in data)

def test_delete_task(auth_header):
    response = client.delete(f"/api/v1/tasks/{task_id}", headers=auth_header)
    assert response.status_code == 200
    data = response.json()
    assert data.get("message") == "Task deleted successfully"


def test_task_rate_limit(auth_header):
    """
    Test rate limiting on task creation endpoint
    """
    # First 100 requests should succeed (rate limit is 100/hour)
    for i in range(5):
        response = client.post("/api/v1/tasks/", json={
            "title": f"RateTask{i}",
            "description": "Rate limit test"
        }, headers=auth_header)
        assert response.status_code == 200
        
    # Clean up - delete the test tasks we just created
    tasks = client.get("/api/v1/tasks/", headers=auth_header).json()
    for task in tasks:
        if task["title"].startswith("RateTask"):
            client.delete(f"/api/v1/tasks/{task['id']}", headers=auth_header)
