from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message":"Hello"}


def test_post_empty():
    r = client.post("/salary")
    assert r.status_code == 422
    assert r.json() ==  {'detail': [{'loc': ['body'], 'msg': 'field required', 'type': 'value_error.missing'}]}


def test_post_below_50():
    r = client.post(
        "/salary",
        json={
            "age": 53,
            "workclass": "Private",
            "fnlgt": 234721,
            "education": "11th",
            "education_num": 7,
            "marital_status": "Married-civ-spouse",
            "occupation": "Handlers-cleaners",
            "relationship": "Husband",
            "race": "Black",
            "sex": "Male",
            "capital_gain": 0,
            "capital_loss": 0,
            "hours_per_week": 40,
            "native_country": "United-States"
            }
        )
    assert r.status_code == 200
    assert r.json() == False

def test_post_above_50():
    r = client.post(
        "/salary",
        json={
            "age": 31,
            "workclass": "Private",
            "fnlgt": 45781,
            "education": "Masters",
            "education_num": 14,
            "marital_status": "Never-married",
            "occupation": "Prof-specialty",
            "relationship": "Not-in-family",
            "race": "White",
            "sex": "Female",
            "capital_gain": 14084,
            "capital_loss": 0,
            "hours_per_week": 50,
            "native_country": "United-States"
            }
        )
    assert r.status_code == 200
    assert r.json() ==  True


def test_post_below_50():
    r = client.post(
        "/salary",
        json={
            "age": 53,
            "workclass": "Private",
            "fnlgt": 234721,
            "education": "11th",
            "education_num": 7,
            "marital_status": "Married-civ-spouse",
            "occupation": "Handlers-cleaners",
            "relationship": "Husband",
            "race": "Black",
            "sex": "Male",
            "capital_gain": 0,
            "capital_loss": 0,
            "hours_per_week": 40,
            "native_country": "United-States"
            }
        )
    assert r.status_code == 200
    assert r.json() == False
