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
    #Validate single mtcars instance against mtcar model 
    mtcar.model_validate(response.json())

def test_output_model(): 
    response = client.get("/api/dataset")
    assert response.status_code == 200
    #Validate that full dataset is a list and each list item is mtcar
    mtcars = response.json()
    assert isinstance (mtcars, list)
    for mtcar_data in mtcars: 
        mtcar(**mtcar_data)
