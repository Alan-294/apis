from flask import Flask,jsonify, request
import random
from app import app


@app.route('/test')
def home():
    return "Hello, World!"

turma_db = [
     {
    "id": 1,
    "nome": "ADS3",
    "turno": "manha",
    "professor_id": 1,
    "ativo": True
  }
]

def gerar_id():
    # Obtém todos os IDs existentes em um conjunto para busca rápida
    ids_existentes = {turma['id'] for turma in turma_db}
    
    # Começa do zero e encontra o primeiro ID disponível
    num = 0
    while num in ids_existentes:
        num += 1
    
    return num 
    
@app.route('/api/turma', methods=['GET', 'POST', 'DELETE','PUT'])
def apiTurma():
    metodo = request.method


    if metodo == "GET": # http://127.0.0.1:5000/api/turma 
        id_turma = request.args.get('id')
        if id_turma:
            for turma in turma_db:
                if turma['id'] == int(id_turma):
                    return {"turma": turma,
                            "code": 200}
            return {"message": "Turma não encontrada",
                 'code': 404}
        return {"turmas": turma_db,
            "code": 200}
    

    
    elif metodo == "POST": #http://127.0.0.1:5000/api/turma?nome=ads2&turno=tarde&professor_id=12345

        nome = request.args.get('nome')  
        turno = request.args.get('turno')  
        professor_id = request.args.get('professor_id')


        turma_db.append(
            {
                "id": gerar_id(),
                "nome": nome,
                "turno": turno,
                "professor_id": professor_id,
                "ativo": True
            }
        )
        return {"message": "Turma adicionada com sucesso",
                'code': 200,
                'turma_adicionada':  {
                "id": turma_db[len(turma_db)-1],           
            } }
    
    
    elif metodo == "DELETE": #http://127.0.0.1:5000/api/turma?id=1
        id_turma = request.args.get('id')
        for turma in turma_db:
            if turma['id'] == int(id_turma):
                turma_db.remove(turma)
                return {"message": "Turma excluída com sucesso",
                        "code": 200}
            
    
    elif metodo == "PUT": #http://127.0.0.1:5000/api/turma?id=1&nome=ads2 (alterado)&turno=Noite&professor_id=13
        id_turma = request.args.get('id')
        nome = request.args.get('nome')  
        turno = request.args.get('turno')  
        professor_id = request.args.get('professor_id')
        posicao = -1
        for turma in turma_db:
            posicao += 1
            if turma['id'] == int(id_turma):
                break               
        turma_db[posicao] = {
            "id": int(id_turma),
            "nome": nome,
            "turno": turno,
            "professor_id": professor_id,
            "ativo": True
        }
        return {"message" : "Turma atualizada com sucesso",
                "code": 200,
               }
        
