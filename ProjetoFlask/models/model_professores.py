<<<<<<< HEAD
from flask import Flask, jsonify, request
import sqlite3

# Função para conectar ao banco de dados
def conectar_banco():
    return sqlite3.connect("banco_de_dados.db")

# Retorna todos os professores
def professores():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM professores")
    resultados = cursor.fetchall()
    conexao.close()

    # Converte os resultados para um formato JSON
    professores = [
        {"id": row[0], "nome": row[1], "disciplina": row[2]} for row in resultados
    ]
    return jsonify(professores)

# Retorna um professor por ID
def professorPorId(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM professores WHERE id = ?", (id,))
    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        professor = {"id": resultado[0], "nome": resultado[1], "disciplina": resultado[2]}
        return jsonify(professor)
    else:
        return jsonify({'mensagem': 'Professor não encontrado'}), 404

# Cria um novo professor
def cria_professor():
    dados = request.get_json()
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO professores (nome, disciplina) VALUES (?, ?)",
        (dados["nome"], dados["disciplina"]),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()

    return jsonify({"id": novo_id, "nome": dados["nome"], "disciplina": dados["disciplina"]})

# Atualiza um professor existente
def atualiza_professor(id):
    dados = request.get_json()
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        "UPDATE professores SET nome = ?, disciplina = ? WHERE id = ?",
        (dados["nome"], dados["disciplina"], id),
    )
    conexao.commit()
    conexao.close()

    return jsonify({"id": id, "nome": dados["nome"], "disciplina": dados["disciplina"]})

# Deleta um professor
def deleta_professor(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM professores WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

    return jsonify({'mensagem': 'Professor deletado com sucesso'})
=======
from flask import Flask,jsonify, request
from .BD import dados 


def professores():
    return jsonify(dados["professores"])

def professorPorId(id):
    for professor in dados["professores"]:
        if professor["id"] == id:
            return professor
    
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

def cria_professor():
    professor = request.get_json()
    professor['id'] = len(dados["professores"]) + 1
    dados["professores"].append(professor)
    return jsonify(professor)

def atualiza_professor(id):
    professor = request.get_json()
    for i in range(len(dados["professores"])):
        if dados["professores"][i]['id'] == id:
            dados["professores"][i].update(professor)
            return jsonify(dados["professores"][i])
        
def deleta_professor(id):
    for i in range(len(dados["professores"])):
        if dados["professores"][i]['id'] == id:
            dados["professores"].pop(i)
            return jsonify(dados["professores"])

>>>>>>> 3a9ed188ab87db7ac3bb07925be1767065734163
