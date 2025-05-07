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
                    # Buscar turma por ID
                    if request.args.get('id'):
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
                            return jsonify({"turma": turma_dict}), 200
                        else:
                            return jsonify({"code": 404, "mensagem": "Turma não encontrada"}), 404
                                     
                    # Listar todas as turmas
                    else:
                        comando = "SELECT * FROM turmas"
                        todasAsTurmas = cursor.execute(comando).fetchall()
                        turmas_list = [
                            {"id": turma[0], "nome": turma[1], "turno": turma[2], "professor_id": turma[3], "ativo": turma[4]}
                            for turma in todasAsTurmas
                        ]
                        return jsonify(turmas_list), 200
                    
                    
        # Adicionar uma nova turma      
        elif metodo == "POST":
            dados = request.get_json()
            cursor.execute(
                "INSERT INTO turmas (nome, turno, professor_id, ativo) VALUES (?, ?, ?, ?)",
                (dados['nome'], dados['turno'], dados['professor_id'], True)
            )
            conexao.commit()
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

        # Atualizar uma turma existente
        elif metodo == "PUT":  
            id_turma = request.args.get('id') 
            dados = request.get_json()
            cursor.execute(
                "UPDATE turmas SET nome = ?, turno = ?, professor_id = ?, ativo = ? WHERE id = ?",
                (dados['nome'], dados['turno'], int(dados['professor_id']), dados['ativo'], int(id_turma))
            )
            conexao.commit()
            if cursor.rowcount == 0:
                return jsonify({"mensagem": "Turma não encontrada"}), 404
            return jsonify({"mensagem": "Turma atualizada com sucesso"}), 200

        # Deletar uma turma
        elif metodo == "DELETE":  
            id_turma = request.args.get('id')
            cursor.execute("DELETE FROM turmas WHERE id = ?", (id_turma,))
            conexao.commit()
            if cursor.rowcount == 0:
                return jsonify({"mensagem": "Turma não encontrada"}), 404
            return jsonify({"mensagem": "Turma excluída com sucesso"}), 200

        else:
            return jsonify({"mensagem": "Método não permitido"}), 405
    finally:
        cursor.close()
        conexao.close()
