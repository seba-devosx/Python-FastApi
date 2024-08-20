from fastapi.testclient import TestClient
from app.main import app


client= TestClient(app)

#test de ejemplo
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_protected_route_without_token():
    response = client.get("v1/users/me")
    assert response.status_code == 404

def test_create_user_invalid_email():
    response = client.post("/v1/user/create_user", json={"name": "pruebausuario", "lastname": "testprueba","email":"test.prueba@gmail.com","address":"calle falsa123","paswrd":"test2024"})
    assert response.status_code == 201