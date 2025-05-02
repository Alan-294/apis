from flask import Flask,jsonify, request
from .BD import dados 
import mysql.connector

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '', #Alterar a senha aqui
    'database': 'banco_escolar',
    'port': 3306  
}

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

        return jsonify(resultado)
    
    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

def cria_professor():
    professor = request.get_json()
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = """
            INSERT INTO professores (
                id, nome, data_nascimento,
                disciplina, salario, observações
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (
            professor['id'],
            professor['nome'],
            professor['data_nascimento'],
            professor['disciplina'],
            professor['salario'],
            professor['observções']
        )

        cursor.execute(sql, valores)
        conexao.commit()

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()


def atualiza_professor(id):
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
                media_final = %s,
                observações = %s
            WHERE id = %s
        """
        valores = (
            professor['id'],
            professor['nome'],
            professor['data_nascimento'],
            professor['disciplina'],
            professor['salario'],
            professor['observções'],
            id
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

