import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    # Register a user
    response = client.post("/api/v1/users/register", json={
        "name": "Test User",
        "email": "testuser@example.com",
        "password": "password123"
    })
    assert response.status_code in [200, 400]  # 200 if new, 400 if already exists
    if response.status_code == 200:
        data = response.json()
        assert "id" in data
        assert data["email"] == "testuser@example.com"
        assert data["role"] == "user"

def test_login_user():
    # Login with valid credentials
    response = client.post(
        "/api/v1/users/login",
        data={"username": "testuser@example.com", "password": "password123"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_user():
    # Wrong password
    response = client.post(
        "/api/v1/users/login",
        data={"username": "testuser@example.com", "password": "wrongpass"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid email or password"

def test_register_rate_limit():
    """
    Exceed rate limit on register endpoint
    """
    for i in range(6):  # more than 5 requests/minute
        response = client.post("/api/v1/users/register", json={
            "name": f"Test{i}",
            "email": f"ratelimit{i}@example.com",
            "password": "password123"
        })

    # The last request should trigger rate limit
    assert response.status_code == 429  # Too Many Requests
    assert "rate limit exceeded" in response.text.lower()

def test_login_rate_limit():
    """
    Exceed rate limit on login endpoint
    """
    for i in range(6):  # more than 5 requests/minute
        response = client.post(
            "/api/v1/users/login",
            data={"username": "nonexistent@example.com", "password": "wrongpass"},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

    # The last request should be blocked
    assert response.status_code == 429
    assert "rate limit exceeded" in response.text.lower()