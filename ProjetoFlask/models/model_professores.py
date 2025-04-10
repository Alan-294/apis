from flask import Flask,jsonify, request
from BD import dados 


def professores():
    return jsonify(dados["professores"])

def professorPorId(id):
    for professor in dados["professores"]:
        if professor["id"] == id:
            return professor
    
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

def cria_professor():
    professor = request.get_json()
    professor['id'] = len(dados["professores"]) + 1
    dados["professores"].append(professor)
    return jsonify(professor)

def atualiza_professor(id):
    professor = request.get_json()
    for i in range(len(dados["professores"])):
        if dados["professores"][i]['id'] == id:
            dados["professores"][i].update(professor)
            return jsonify(dados["professores"][i])
        
def deleta_professor(id):
    for i in range(len(dados["professores"])):
        if dados["professores"][i]['id'] == id:
            dados["professores"].pop(i)
            return jsonify(dados["professores"])

