<<<<<<< HEAD
from flask import jsonify, request
import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect("banco_de_dados.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

# Função principal para gerenciar turmas
def apiTurma():
    metodo = request.method
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        if metodo == "GET":
                    if request.args.get('id'):
                        # Buscar turma por ID
                        id_turma = request.args.get('id')
                        comando = "SELECT * FROM turmas WHERE id = ?"
                        turma = cursor.execute(comando, (id_turma,)).fetchone()
                        if turma:
                            turma_dict = {
                                "id": turma[0],
                                "nome": turma[1],
                                "turno": turma[2],
                                "professor_id": turma[3],
                                "ativo": turma[4]
                            }
                            # Retorna a turma dentro de uma chave "turma"
                            return jsonify({"turma": turma_dict}), 200
                        else:
                            # Retorna um código de erro no formato esperado
                            return jsonify({"code": 404, "mensagem": "Turma não encontrada"}), 404
                    else:
                        # Listar todas as turmas
                        comando = "SELECT * FROM turmas"
                        todasAsTurmas = cursor.execute(comando).fetchall()
                        turmas_list = [
                            {"id": turma[0], "nome": turma[1], "turno": turma[2], "professor_id": turma[3], "ativo": turma[4]}
                            for turma in todasAsTurmas
                        ]
                        return jsonify(turmas_list), 200
        elif metodo == "POST":
            # Adicionar uma nova turma
            dados = request.get_json()
            cursor.execute(
                "INSERT INTO turmas (nome, turno, professor_id, ativo) VALUES (?, ?, ?, ?)",
                (dados['nome'], dados['turno'], dados['professor_id'], True)
            )
            conexao.commit()
            # Ajuste: Retorna a turma adicionada no formato esperado
            return jsonify({
                "mensagem": "Turma adicionada com sucesso",
                "turma_adicionada": {
                    "id": cursor.lastrowid,
                    "nome": dados['nome'],
                    "turno": dados['turno'],
                    "professor_id": dados['professor_id'],
                    "ativo": True
                }
            })


        elif metodo == "PUT":  # Atualizar uma turma existente
            id_turma = request.args.get('id')
            dados = request.get_json()
            cursor.execute(
                "UPDATE turmas SET nome = ?, turno = ?, professor_id = ?, ativo = ? WHERE id = ?",
                (dados['nome'], dados['turno'], int(dados['professor_id']), dados['ativo'], int(id_turma))
            )
            conexao.commit()
            if cursor.rowcount == 0:
                # Ajuste: Retorna um código de erro no formato esperado
                return jsonify({"mensagem": "Turma não encontrada"}), 404
            return jsonify({"mensagem": "Turma atualizada com sucesso"}), 200

        elif metodo == "DELETE":  # Deletar uma turma
            id_turma = request.args.get('id')
            cursor.execute("DELETE FROM turmas WHERE id = ?", (id_turma,))
            conexao.commit()
            if cursor.rowcount == 0:
                # Ajuste: Retorna um código de erro no formato esperado
                return jsonify({"mensagem": "Turma não encontrada"}), 404
            return jsonify({"mensagem": "Turma excluída com sucesso"}), 200

        else:
            return jsonify({"mensagem": "Método não permitido"}), 405

    finally:
        cursor.close()
        conexao.close()
=======
from flask import Flask,jsonify, request
import random
from .BD import dados

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
>>>>>>> 3a9ed188ab87db7ac3bb07925be1767065734163
