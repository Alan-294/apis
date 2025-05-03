from flask import Flask,jsonify, request
import random
from .BD import dados
import mysql.connector

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '', #Alterar a senha aqui
    'database': 'banco_escolar',
    'port': 3306  
}
def criar_id():
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()

    while True:
        novo_id = random.randint(1000, 9999)
        cursor.execute("SELECT id FROM turmas WHERE id = %s", (novo_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            break 

    cursor.close()
    conexao.close()
    return novo_id
    
def apiTurma():
    metodo = request.method

    if metodo == "GET": # http://127.0.0.1:5000/api/turma 
        id_turma = request.args.get('id')
        if id_turma:
            try:
                conexao = mysql.connector.connect(**db_config)
                cursor = conexao.cursor(dictionary=True)

                sql = "SELECT * FROM turmas WHERE id = %s"
                cursor.execute(sql, (id_turma,))
                resultado = cursor.fetchone()
                if resultado:
                    return jsonify(resultado)

                else:
                    return jsonify({"mensagem": "Turma não encontrada"}), 404
                        
                    
            except mysql.connector.Error as erro:
                return jsonify({'erro': str(erro)}), 500

            finally:
                if 'conexao' in locals() and conexao.is_connected():
                    cursor.close()
                    conexao.close()
        try:
            conexao = mysql.connector.connect(**db_config)
            cursor = conexao.cursor(dictionary=True)

            cursor.execute("SELECT * FROM turmas")
            resultado = cursor.fetchall()

            return jsonify(resultado)
        
        except mysql.connector.Error as erro:
            return jsonify({'erro': str(erro)}), 500

        finally:
            if 'conexao' in locals() and conexao.is_connected():
                cursor.close()
                conexao.close()
    

    
    elif metodo == "POST": #http://127.0.0.1:5000/api/turma?nome=ads2&turno=tarde&professor_id=12345
        turma = request.get_json()
        turma['id'] = criar_id()
        conexao = None
        try:
            conexao = mysql.connector.connect(**db_config)
            cursor = conexao.cursor()

            sql = """
                INSERT INTO turmas (
                    id, nome, turno, professor_id, ativo
                    
                )
                VALUES (%s, %s, %s, %s, %s)
            """
            valores = (
                turma['id'],
                turma['nome'],
                turma['turno'],
                turma['professor_id'],
                turma['ativo']
            )

            cursor.execute(sql, valores)
            conexao.commit()

        except Exception as e:
            return jsonify({'erro': str(e)}), 500

        finally:
            if conexao and conexao.is_connected():
                cursor.close()
                conexao.close()

        return jsonify({
                "mensagem": "Turma adicionada com sucesso",
                "turma_adicionada": {
                    "id": turma['id'],
                    "nome": turma['nome'],
                    "turno": turma['turno'],
                    "professor_id": turma['professor_id'],
                    "ativo": turma['ativo']
                }
            })

    
    
    elif metodo == "DELETE": #http://127.0.0.1:5000/api/turma?id=1
        try:
            id_turma = request.args.get('id')
            conexao = mysql.connector.connect(**db_config)
            cursor = conexao.cursor()

            sql = "DELETE FROM turmas WHERE id = %s"
            cursor.execute(sql, (id_turma,))
            conexao.commit()

            if cursor.rowcount == 0:
                return jsonify({'mensagem': 'Turma não encontrada'}), 404

            return jsonify({'mensagem': 'Turma deletada com sucesso'})

        except mysql.connector.Error as erro:
            return jsonify({'erro': str(erro)}), 500

        finally:
            if 'conexao' in locals() and conexao.is_connected():
                cursor.close()
                conexao.close()
            
    
    elif metodo == "PUT": #http://127.0.0.1:5000/api/turma?id=1&nome=ads2&turno=Noite&professor_id=13
        try:
            id_turma = request.args.get('id')
            conexao = mysql.connector.connect(**db_config)
            cursor = conexao.cursor()
            dados = request.get_json()
            cursor.execute(
                    "UPDATE turmas SET nome = %s, turno = %s, professor_id = %s, ativo = %s WHERE id = %s",
                    (dados['nome'], dados['turno'], (dados['professor_id']), int(dados['ativo']), id_turma)
                    )
            conexao.commit()
            if cursor.rowcount == 0:
                # Ajuste: Retorna um código de erro no formato esperado
                return jsonify({"mensagem": "Turma não encontrada"}), 404
            return jsonify({"mensagem": "Turma atualizada com sucesso"}), 200
        except mysql.connector.Error as erro:
            return jsonify({'erro': str(erro)}), 500

        finally:
            if 'conexao' in locals() and conexao.is_connected():
                cursor.close()
                conexao.close()