from fastapi.testclient import TestClient
from main import app
from models.outputs import mtcar, mtcarlist

client = TestClient(app)


def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}

def test_output_model(): 
    response = client.get("/api/HondaCivic")
    assert response.status_code == 200
    mtcar.model_validate(response.json())

'''def test_output_model(): 
    response = client.get("/api/dataset")
    assert response.status_code == 200
    mtcarlist.model_validate(response.json())'''