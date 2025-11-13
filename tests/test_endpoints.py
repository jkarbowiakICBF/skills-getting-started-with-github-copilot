import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test the root endpoint
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # The root redirects to /static/index.html, so check for HTML content
    assert "<html" in response.text.lower()

# Test the activities endpoint
def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test registering a participant
def test_register_participant():
    payload = {"email": "test@mergington.edu"}
    response = client.post("/activities/Chess%20Club/signup", params=payload)
    assert response.status_code == 200 or response.status_code == 201
    assert "message" in response.json()

# Test unregistering a participant
def test_unregister_participant():
    payload = {"email": "test@mergington.edu"}
    response = client.post("/activities/Chess%20Club/unregister", params=payload)
    assert response.status_code == 200 or response.status_code == 204