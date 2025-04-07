from flask import Flask,jsonify, request
import random
import model_aluno as model
from app import app

def criar_id():
    novo_id = random.randint(1000, 9999)
    if not any(aluno["id"] == novo_id for aluno in alunos_db):  
        return novo_id  
   
alunos_db = [
     {
        "id": 1009,
        "nome": "João Pedro",
        "data_nascimento": "2000-01-01",
        "nota_primeiro_semestre": 10.0,
        "nota_segundo_semestre": 8.0,
        "turma_id": 6,
        "mediaFinal": 9
    },
     {
        "id": 3029,
        "nome": "André Augusto",
        "data_nascimento": "1998-09-05",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 6.0,
        "turma_id": 6,
        "mediaFinal": 7
    },
]



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
        
    return model.adiciona_aluno(aluno)
    

#Caminho do método GET para todos os alunos
#http://127.0.0.1:5000/api/alunos

@app.route('/api/alunos', methods=['GET'])
def consulta_alunos():
    return jsonify(alunos_db)



@app.route('/api/alunos/<int:aluno_id>', methods=['GET'])
#Exemplo de rota:
#http://127.0.0.1:5000/api/alunos/1009
def consulta_aluno(aluno_id):
    
    return model.consulta_aluno(aluno_id)


@app.route('/api/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):

    novo_aluno = request.json
            

    return model.update_aluno(aluno_id)


@app.route('/api/alunos/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    return model.deletar_aluno(aluno_id)
