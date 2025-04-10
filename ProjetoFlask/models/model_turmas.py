from flask import Flask,jsonify, request
import random
from BD import dados

def gerar_id():
    ids_existentes = {turma['id'] for turma in dados['turmas']}
    
    num = 0
    while num in ids_existentes:
        num += 1
    
    return num 

def apiTurma():
    metodo = request.method

    if metodo == "GET": # http://127.0.0.1:5000/api/turma 
        id_turma = request.args.get('id')
        if id_turma:
            for turma in dados['turmas']:
                if turma['id'] == int(id_turma):
                    return {"turma": turma,
                            "code": 200}
            return {"message": "Turma não encontrada",
                 'code': 404}
        return {"turmas": dados['turmas'],
            "code": 200}
    

    
    elif metodo == "POST": #http://127.0.0.1:5000/api/turma?nome=ads2&turno=tarde&professor_id=12345

        nome = request.args.get('nome')  
        turno = request.args.get('turno')  
        professor_id = request.args.get('professor_id')


        dados['turmas'].append(
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
                "id": dados['turmas'][len(dados['turmas'])-1],           
            } }
    
    
    elif metodo == "DELETE": #http://127.0.0.1:5000/api/turma?id=1
        id_turma = request.args.get('id')
        for turma in dados['turmas']:
            if turma['id'] == int(id_turma):
                dados['turmas'].remove(turma)
                return {"message": "Turma excluída com sucesso",
                        "code": 200}
            
    
    elif metodo == "PUT": #http://127.0.0.1:5000/api/turma?id=1&nome=ads2&turno=Noite&professor_id=13
        id_turma = request.args.get('id')
        nome = request.args.get('nome')  
        turno = request.args.get('turno')  
        professor_id = request.args.get('professor_id')
        posicao = -1
        for turma in dados['turmas']:
            posicao += 1
            if turma['id'] == int(id_turma):
                break               
        dados['turmas'][posicao] = {
            "id": int(id_turma),
            "nome": nome,
            "turno": turno,
            "professor_id": professor_id,
            "ativo": True
        }
        return {"message" : "Turma atualizada com sucesso",
                "code": 200,
               }
