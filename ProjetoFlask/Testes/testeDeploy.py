import requests

BASE_URL = "https://new-api-flask2.onrender.com"  # URL de produção

def test_smoke():
    endpoints = [
        "/api/alunos",
        "/api/professores",
        "/api/turma",
        "/docs"  # Swagger
    ]
    for endpoint in endpoints:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url)
        assert response.status_code == 200, f"Erro no endpoint {url}: {response.status_code}"

if __name__ == "__main__":
    test_smoke()
    print("Todos os endpoints principais estão funcionando corretamente.")