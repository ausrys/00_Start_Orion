from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_search_success(monkeypatch):
    def mock_grab_text(url: str):
        return "This is an example page with some content. example text here."
    monkeypatch.setattr("app.grab_text_from_url", mock_grab_text)

    response = client.post(
        "/search", json={"url": "https://example.com", "search": "example"})
    assert response.status_code == 200
    assert "matches" in response.json()
    assert any("example" in m.lower() for m in response.json()["matches"])


def test_search_not_found(monkeypatch):
    def mock_grab_text(url: str):
        return "No relevant content here."
    monkeypatch.setattr("app.grab_text_from_url", mock_grab_text)

    response = client.post(
        "/search", json={"url": "https://example.com", "search": "notfound"})
    assert response.status_code == 404


def test_invalid_input():
    response = client.post(
        "/search", json={"search": "example"})  # missing URL
    assert response.status_code == 422
