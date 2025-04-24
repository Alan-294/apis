import sqlite3
from flask import jsonify, request

# Função para conectar ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect("banco_de_dados.db")
    conexao.row_factory = sqlite3.Row  # Permite acessar os resultados como dicionários
    return conexao

# Adicionar um novo aluno
def adiciona_aluno():
    aluno = request.json

    if not aluno:
        return jsonify({"erro": "JSON inválido ou ausente"}), 400

    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Calcula a média final
    media_final = (aluno['nota_primeiro_semestre'] + aluno['nota_segundo_semestre']) / 2

    # Insere o aluno no banco de dados
    cursor.execute('''
        INSERT INTO alunos (nome, idade, turma_id)
        VALUES (?, ?, ?)
    ''', (aluno['nome'], aluno['idade'], aluno['turma_id']))

    conexao.commit()
    aluno_id = cursor.lastrowid  # Obtém o ID do aluno recém-inserido
    conexao.close()

    # Retorna o aluno com o ID e a média final
    aluno['id'] = aluno_id
    aluno['media_final'] = media_final
    return jsonify(aluno), 201

# Listar todos os alunos
def lista_alunos():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Consulta todos os alunos
    cursor.execute('SELECT * FROM alunos')
    alunos = [dict(row) for row in cursor.fetchall()]  # Converte os resultados em uma lista de dicionários
    conexao.close()

    return jsonify(alunos)

# Consultar um aluno por ID
def consulta_aluno(aluno_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM alunos WHERE id = ?', (aluno_id,))
    aluno = cursor.fetchone()
    conexao.close()

    if aluno:
        return jsonify(dict(aluno)), 200
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

# Atualizar um aluno
def update_aluno(id_aluno):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    novo_aluno = request.json

    cursor.execute('''
        UPDATE alunos
        SET nome = ?, idade = ?, turma_id = ?
        WHERE id = ?
    ''', (
        novo_aluno.get('nome'),
        novo_aluno.get('idade'),
        novo_aluno.get('turma_id'),
        id_aluno
    ))

    conexao.commit()
    conexao.close()

    if cursor.rowcount > 0:
        return jsonify({'mensagem': 'Aluno atualizado com sucesso'})
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404

# Deletar um aluno
def deletar_aluno(aluno_id):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('DELETE FROM alunos WHERE id = ?', (aluno_id,))
    conexao.commit()
    conexao.close()

    if cursor.rowcount > 0:
        return jsonify({'mensagem': 'Usuário removido com sucesso'})
    else:
        return jsonify({'mensagem': 'Usuário não encontrado'}), 404