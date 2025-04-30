import random
from flask import jsonify, request
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
    novo_id = random.randint(1000, 9999)
    if not any(aluno["id"] == novo_id for aluno in dados["alunos"]):  
        return novo_id  
    
def adiciona_aluno(aluno):
    mediaFinal = (aluno['nota_primeiro_semestre'] + aluno['nota_segundo_semestre']) / 2

    aluno['media_final'] = mediaFinal
    aluno['id'] = criar_id()
    conexao = None
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = """
            INSERT INTO alunos (
                id, nome, data_nascimento,
                nota_primeiro_semestre, nota_segundo_semestre,
                media_final, turma_id
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        valores = (
            aluno['id'],
            aluno['nome'],
            aluno['data_nascimento'],
            aluno['nota_primeiro_semestre'],
            aluno['nota_segundo_semestre'],
            aluno['media_final'],
            aluno['turma_id']
        )

        cursor.execute(sql, valores)
        conexao.commit()

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

    finally:
        if conexao and conexao.is_connected():
            cursor.close()
            conexao.close()

    return jsonify(aluno)


def lista_alunos():
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor(dictionary=True)

        cursor.execute("SELECT * FROM alunos")
        resultado = cursor.fetchall()

        return jsonify(resultado)
    
    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

class AlunoNaoEncontrado(Exception):
    pass 

def update_aluno(id_aluno):

    try:
        dados = request.get_json()
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = """
            UPDATE alunos
            SET nome = %s,
                data_nascimento = %s,
                nota_primeiro_semestre = %s,
                nota_segundo_semestre = %s,
                media_final = %s,
                turma_id = %s
            WHERE id = %s
        """
        media_final = (dados['nota_primeiro_semestre'] + dados['nota_segundo_semestre']) / 2

        valores = (
            dados['nome'],
            dados['data_nascimento'],
            dados['nota_primeiro_semestre'],
            dados['nota_segundo_semestre'],
            media_final,
            dados['turma_id'],
            id_aluno
        )

        cursor.execute(sql, valores)
        conexao.commit()

        if cursor.rowcount == 0:
            return jsonify({'mensagem': 'Aluno não encontrado'}), 404

        return jsonify({'mensagem': 'Aluno atualizado com sucesso'})

    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()


def deletar_aluno(aluno_id):
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor()

        sql = "DELETE FROM alunos WHERE id = %s"
        cursor.execute(sql, (aluno_id,))
        conexao.commit()

        if cursor.rowcount == 0:
            return jsonify({'mensagem': 'Aluno não encontrado'}), 404

        return jsonify({'mensagem': 'Aluno deletado com sucesso'})

    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()

def consulta_aluno(aluno_id):
    try:
        conexao = mysql.connector.connect(**db_config)
        cursor = conexao.cursor(dictionary=True)

        sql = "SELECT * FROM alunos WHERE id = %s"
        cursor.execute(sql, (aluno_id,))
        resultado = cursor.fetchall()

        return jsonify(resultado)
    
    except mysql.connector.Error as erro:
        return jsonify({'erro': str(erro)}), 500

    finally:
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
