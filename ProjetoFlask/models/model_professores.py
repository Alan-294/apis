from flask import Flask, jsonify, request
import sqlite3
from .BancoSQLite import BancoSQLite


# Retorna todos os professores
def professores():
    BD = BancoSQLite()
    BD.conectar_banco()
    cursor = BD.conexao.cursor()
    cursor.execute("SELECT * FROM professores")
    resultados = cursor.fetchall()
    BD.conexao.close()

    # Converte os resultados para um formato JSON
    professores = [
        {"id": row[0], "nome": row[1], "disciplina": row[2]} for row in resultados
    ]
    return jsonify(professores)

# Retorna um professor por ID
def professorPorId(id):
    BD = BancoSQLite()
    BD.conectar_banco()
    cursor = BD.conexao.cursor()
    cursor.execute("SELECT * FROM professores WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    BD.conexao.close()

    if resultado:
        professor = {"id": resultado[0], "nome": resultado[1], "disciplina": resultado[2]}
        return jsonify(professor)
    else:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404

# Cria um novo professor
def cria_professor():
    dados = request.get_json()
    BD = BancoSQLite()
    BD.conectar_banco()
    cursor = BD.conexao.cursor()
    cursor.execute(
        "INSERT INTO professores (nome, disciplina) VALUES (?, ?)",
        (dados["nome"], dados["disciplina"]),
    )
    BD.conexao.commit()
    novo_id = cursor.lastrowid
    BD.conexao.close()

    return jsonify({"id": novo_id, "nome": dados["nome"], "disciplina": dados["disciplina"]})

# Atualiza um professor existente
def atualiza_professor(id):
    dados = request.get_json()
    BD = BancoSQLite()
    BD.conectar_banco()
    cursor = BD.conexao.cursor()
    cursor.execute(
        "UPDATE professores SET nome = ?, disciplina = ? WHERE id = ?",
        (dados["nome"], dados["disciplina"], id),
    )
    BD.conexao.commit()
    BD.conexao.close()

    return jsonify({"id": id, "nome": dados["nome"], "disciplina": dados["disciplina"]})

# Deleta um professor
def deleta_professor(id):
    BD = BancoSQLite()
    BD.conectar_banco()
    cursor = BD.conexao.cursor()
    cursor.execute("DELETE FROM professores WHERE id = ?", (id,))
    BD.conexao.commit()
    BD.conexao.close()

    return jsonify({'mensagem': 'Professor deletado com sucesso'})
