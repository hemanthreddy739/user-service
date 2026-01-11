import os
import sys

# ensure project root is on sys.path so tests can import main
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "user-service up"}


def test_get_user():
    resp = client.get("/users/42")
    assert resp.status_code == 200
    assert resp.json() == {"id": 42, "name": "Demo User"}
