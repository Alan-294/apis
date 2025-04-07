from flask import Flask,jsonify, request

from app import app

dados_professores = [
    {
        "id": 1,
        "nome": "Maria",
        "data_nascimento": "2003-02-03",
        "disciplina": "Math",
        "salario": 1500,
        "Observações": "None"
    },
    {
        "id": 2,
        "nome": "Joao",
        "data_nascimento": "2005-10-03",
        "disciplina": "Chemistry",
        "salario": 2500,
        "Observações": "None"
    },
    {
        "id": 3,
        "nome": "Pedro",
        "data_nascimento": "2005-10-03",
        "disciplina": "English",
        "salario": 1550,
        "Observações": "None"
    }
    
]

def professores():
    return jsonify(dados_professores)

def professorPorId(id):
    for professor in dados_professores:
        if professor["id"] == id:
            return professor
    
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

def cria_professor():
    professor = request.get_json()
    professor['id'] = len(dados_professores) + 1
    dados_professores.append(professor)
    return jsonify(professor)

def atualiza_professor(id):
    professor = request.get_json()
    for i in range(len(dados_professores)):
        if dados_professores[i]['id'] == id:
            dados_professores[i].update(professor)
            return jsonify(dados_professores[i])
        
def deleta_professor(id):
    for i in range(len(dados_professores)):
        if dados_professores[i]['id'] == id:
            dados_professores.pop(i)
            return jsonify(dados_professores)

