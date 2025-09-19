from fastapi.testclient import TestClient

def test_get_all_animes_empty(client: TestClient):
    """
    Testa a rota /animes quando o banco de dados de teste está vazio.
    """
    response = client.get("/animes")
    assert response.status_code == 200
    assert response.json() == []

def test_read_root(client: TestClient):
    """
    Testa a rota raiz /.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à API de Animes!"}