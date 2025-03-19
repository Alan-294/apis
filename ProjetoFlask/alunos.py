from flask import Flask,jsonify, request
import random
from app import app
from BD import alunos_db, turma_db

def criar_id():
    novo_id = random.randint(1000, 9999)
    if not any(aluno["id"] == novo_id for aluno in alunos_db):  
        return novo_id  
   

def turma_existe(turma_id):
    #Verifica se o ID da turma existe na base de dados.
    for turma in turma_db:
        if (turma["id"] == turma_id):
            return True
    return False

@app.route('/api/alunos', methods=['POST'])
#Caminho do método POST 
#http://127.0.0.1:5000/api/alunos
#Enviar dados pelo Postman em formato Json como no campo abaixo:
#"aluno":{
#"nome": "Jonas Padro",
#"data_nascimento": "2008-01-01",
#"nota_primeiro_semestre": 9.5,
#"nota_segundo_semestre": 8.0,
#"turma_id": 6
#}
#NÃO INSERIR O ID DO ALUNO JUNTO DO JSON

    
def cria_aluno():

    aluno = request.get_json()
    
    mediaFinal = (aluno['nota_primeiro_semestre'] + aluno['nota_segundo_semestre']) / 2
    id_turma = aluno['turma_id']
    if turma_existe(id_turma):
        aluno['media_final'] = mediaFinal
        aluno['id'] = criar_id()
        
        alunos_db.append(aluno)
        return jsonify(aluno)
    return jsonify({"Erro": f"A turma {id_turma} não existe"})
    

#Caminho do método GET para todos os alunos
#http://127.0.0.1:5000/api/alunos

@app.route('/api/alunos', methods=['GET'])
def consulta_alunos():
    return jsonify(alunos_db)



@app.route('/api/alunos/<int:aluno_id>', methods=['GET'])
#Exemplo de rota:
#http://127.0.0.1:5000/api/alunos/1009
def consulta_aluno(aluno_id):
    for aluno in alunos_db:
        if aluno["id"] == aluno_id:
            return aluno
    
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404


@app.route('/api/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    for aluno in alunos_db:
        if aluno['id'] == aluno_id:
            novo_aluno = request.json
        
        
            aluno['nome'] = novo_aluno.get('nome', aluno['nome'])
            aluno['data_nascimento'] = novo_aluno.get('data_nascimento', aluno['data_nascimento'])
            aluno['nota_primeiro_semestre'] = novo_aluno.get('nota_primeiro_semestre', aluno['nota_primeiro_semestre'])
            aluno['nota_segundo_semestre'] = novo_aluno.get('nota_segundo_semestre', aluno['nota_segundo_semestre'])
            aluno['turma_id'] = novo_aluno.get('turma_id', aluno['turma_id'])
            aluno['media_final'] = novo_aluno.get('media_final', aluno['media_final'])
            
            return jsonify(aluno)
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404


@app.route('/api/alunos/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    for aluno in alunos_db:
        if aluno['id'] == aluno_id:
            alunos_db.remove(aluno)
            return jsonify({'mensagem': 'Usuário removido'})
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404



