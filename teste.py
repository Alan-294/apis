import requests

url = "http://127.0.0.1:5000/api/turma"
response = requests.get(url)

if response.status_code == 200:
    print("Resposta:", response.json())
else:
    print("Erro:", response.status_code)