from flask import jsonify, request
import mysql.connector

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '', #Alterar a senha aqui
    'database': 'banco_escolar',
    'port': 3306  
}
# Função principal para gerenciar turmas
def apiTurma():
    metodo = request.method
    conexao = mysql.connector.connect(**db_config)
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