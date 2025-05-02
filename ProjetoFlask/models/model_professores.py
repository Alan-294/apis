from flask import Flask,jsonify, request
import mysql.connector
import random

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
        cursor.execute("SELECT id FROM professores WHERE id = %s", (novo_id,))
        resultado = cursor.fetchone()

        if resultado is None:
            break 

    cursor.close()
    conexao.close()
    return novo_id
    
def professores():
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM professores")
        resultado = cursor.fetchall()
        return jsonify(resultado)
    
    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

def professorPorId(professor_id):
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM professores WHERE id = %s"
        cursor.execute(sql, (professor_id,))
        resultado = cursor.fetchone()

        if resultado:
            return jsonify(resultado)
        else:
            return jsonify({"mensagem": "Professor não encontrado"}), 404
         
    
    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

def cria_professor():
    professor = request.get_json()
    professor['id'] = criar_id()
    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()
        sql = """
            INSERT INTO professores (
                id, nome, data_nascimento,
                disciplina, salario, observacoes
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            professor['id'],
            professor['nome'],
            professor['data_nascimento'],
            professor['disciplina'],
            professor['salario'],
            professor['observacoes']
        )

        cursor.execute(sql, valores)
        conexao.commit()

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()
    return jsonify(professor)

def atualiza_professor(id_professor):
    try:
        professor = request.get_json()
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = """
            UPDATE professores
            SET nome = %s,
                data_nascimento = %s,
                disciplina = %s,
                salario = %s,
                observacoes = %s
            WHERE id = %s
        """
        valores = (
            professor['nome'],
            professor['data_nascimento'],
            professor['disciplina'],
            professor['salario'],
            professor['observacoes'],
            id_professor
        )

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount == 0:
            return jsonify({'mensagem': 'professor não encontrado'}), 404

        return jsonify({'mensagem': 'professor atualizado com sucesso'})

    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

        
def deleta_professor(id):
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = "DELETE FROM professores WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()

        if cursor.rowcount == 0:
            return jsonify({'mensagem': 'Professor não encontrado'}), 404

        return jsonify({'mensagem': 'Professor deletado com sucesso'})

    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

