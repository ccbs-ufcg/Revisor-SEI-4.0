from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_revisao():
    response = client.post("/api/v1/revisar", json={
        "texto": "Prezados, venho por meio deste solicitar o envio das documentação.",
        "tipo_documento": "oficio",
        "perfil": "ufcg",
        "unidade": "CCBS"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["total_problemas"] >= 1
    assert data["nota"] < 100
