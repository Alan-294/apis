import sqlite3
from flask import jsonify, request

# Função para conectar ao banco de dados
def conectar_banco():
    conexao = sqlite3.connect("banco_de_dados.db")
    conexao.row_factory = sqlite3.Row  # Permite acessar os resultados como dicionários
    return conexao

# Adicionar um novo aluno

def adiciona_aluno(aluno):
    # Validate JSON payload
    if not aluno:
        return jsonify({"erro": "JSON inválido ou ausente"}), 400

    campos_obrigatorios = ['nome', 'idade', 'turma_id', 'nota_primeiro_semestre', 'nota_segundo_semestre']
    for campo in campos_obrigatorios:
        if campo not in aluno:
            return jsonify({"erro": f"Campo obrigatório ausente: {campo}"}), 400

    try:
        idade = int(aluno['idade'])
        turma_id = int(aluno['turma_id'])
        nota1 = float(aluno['nota_primeiro_semestre'])
        nota2 = float(aluno['nota_segundo_semestre'])
        media_final = (nota1 + nota2) / 2
    except ValueError:
        return jsonify({"erro": "Idade, turma_id e notas devem ser números válidos"}), 400

    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute('''
            INSERT INTO alunos (nome, idade, turma_id, nota_primeiro_semestre, nota_segundo_semestre, media_final)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (aluno['nome'], idade, turma_id, nota1, nota2, media_final))

        conexao.commit()
        aluno_id = cursor.lastrowid

    except sqlite3.Error as e:
        conexao.rollback()
        return jsonify({"erro": f"Erro ao inserir no banco de dados: {str(e)}"}), 500

    finally:
        conexao.close()

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
def update_aluno(id_aluno, novo_aluno):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE alunos
        SET nome = ?, idade = ?, turma_id = ?, nota_primeiro_semestre = ?, nota_segundo_semestre = ?, media_final = ?
        WHERE id = ?
    ''', (
        novo_aluno.get('nome'),
        novo_aluno.get('idade'),
        novo_aluno.get('turma_id'),
        novo_aluno.get('nota_primeiro_semestre'),
        novo_aluno.get('nota_segundo_semestre'),
        (novo_aluno.get('nota_primeiro_semestre') + novo_aluno.get('nota_segundo_semestre')) / 2,
        id_aluno
    ))

    conexao.commit()
    conexao.close()

    if cursor.rowcount > 0:
        return jsonify({'mensagem': 'Aluno atualizado com sucesso'}), 200
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