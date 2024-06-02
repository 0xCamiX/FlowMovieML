from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_null_prediction():
    response = client.post('predict', json={
        "domestic_gross": 0,
        "production_budget": 0,
        "title_year": 0,
        "aspect_ratio": 0,
        "duration": 0,
        "cast_total_facebook_likes": 0,
        "budget": 0,
        "imdb_score": 0,
        "opening_gross": 0,
        "screens": 0
    })
    assert response.status_code == 200
    assert response.json()["prediction"] >= 0


def test_random_prediction():
    response = client.post('predict', json={
        "domestic_gross": 10000000,
        "production_budget": 10000000,
        "title_year": 2010,
        "aspect_ratio": 2.35,
        "duration": 120,
        "cast_total_facebook_likes": 10000,
        "budget": 10000000,
        "imdb_score": 7,
        "opening_gross": 10000000,
        "screens": 1000
    })
    assert response.status_code == 200
    assert response.json()["prediction"] > 0
