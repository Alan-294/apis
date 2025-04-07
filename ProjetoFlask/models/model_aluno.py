import random
from flask import jsonify, request
dados = {"alunos":[
        {"id": 1009,
        "nome": "João Pedro",
        "data_nascimento": "2000-01-01",
        "nota_primeiro_semestre": 10.0,
        "nota_segundo_semestre": 8.0,
        "turma_id": 6,
        "mediaFinal": 9},{
            "id": 3029,
        "nome": "André Augusto",
        "data_nascimento": "1998-09-05",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 6.0,
        "turma_id": 6,
        "mediaFinal": 7
        }
                  ], 
        "professores":[]}


def criar_id():
    novo_id = random.randint(1000, 9999)
    if not any(aluno["id"] == novo_id for aluno in dados["alunos"]):  
        return novo_id  
    
def adiciona_aluno(aluno):
    mediaFinal = (aluno['nota_primeiro_semestre'] + aluno['nota_segundo_semestre']) / 2

    aluno['media_final'] = mediaFinal
    aluno['id'] = criar_id()
    dados['alunos'].append(aluno)
    return jsonify(aluno)

def lista_alunos():
    return jsonify(dados['alunos'])


class AlunoNaoEncontrado(Exception):
    pass 

def aluno_por_id(aluno_id):
    lista = dados["alunos"]
    for aluno in lista:
        if aluno["id"] == aluno_id:
            return jsonify(aluno)

    return jsonify({'mensagem': 'Usuário não encontrado'}), 404
        

def update_aluno(id_aluno):
     
     for aluno in dados['alunos']:
        if aluno['id'] == id_aluno:
            novo_aluno = request.json
        
        
            aluno['nome'] = novo_aluno.get('nome', aluno['nome'])
            aluno['data_nascimento'] = novo_aluno.get('data_nascimento', aluno['data_nascimento'])
            aluno['nota_primeiro_semestre'] = novo_aluno.get('nota_primeiro_semestre', aluno['nota_primeiro_semestre'])
            aluno['nota_segundo_semestre'] = novo_aluno.get('nota_segundo_semestre', aluno['nota_segundo_semestre'])
            aluno['turma_id'] = novo_aluno.get('turma_id', aluno['turma_id'])
            aluno['media_final'] = novo_aluno.get('media_final', aluno['media_final'])
            
            return jsonify(aluno)
    
     return jsonify({'mensagem': 'Usuário não encontrado'}), 404

def deletar_aluno(aluno_id):
    for aluno in dados['alunos']:
        if aluno['id'] == aluno_id:
            dados['alunos'].remove(aluno)
            return jsonify({'mensagem': 'Usuário removido'})
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404

def consulta_aluno(aluno_id):
    for aluno in dados['alunos']:
        if aluno["id"] == aluno_id:
            return aluno
    
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404
