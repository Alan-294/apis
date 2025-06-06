import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect("banco_de_dados.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    cursor = conexao.cursor()

    # Criação das tabelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            disciplina TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            turno TEXT NOT NULL,
            professor_id INTEGER NOT NULL,
            ativo BOOLEAN NOT NULL,
            FOREIGN KEY (professor_id) REFERENCES professores (id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            turma_id INTEGER NOT NULL,
            nota_primeiro_semestre REAL,
            nota_segundo_semestre REAL,
            media_final REAL,
            FOREIGN KEY (turma_id) REFERENCES turmas (id)
        )
    ''')

    # Verificar se a tabela professores já possui registros
    cursor.execute("SELECT COUNT(*) FROM professores")
    if cursor.fetchone()[0] == 0:
        professores = [
            ("João Silva", "Matemática"),
            ("Maria Oliveira", "História"),
            ("Carlos Souza", "Física"),
            ("Ana Lima", "Química"),
            ("Fernanda Costa", "Biologia")
        ]
        cursor.executemany("INSERT INTO professores (nome, disciplina) VALUES (?, ?)", professores)

    # Buscar IDs reais dos professores
    cursor.execute("SELECT id FROM professores ORDER BY id")
    professores_ids = [row[0] for row in cursor.fetchall()]

    # Inserir turmas (se não existirem)
    cursor.execute("SELECT COUNT(*) FROM turmas")
    if cursor.fetchone()[0] == 0:
        turmas = [
            ("Turma A", "Manhã", professores_ids[0], True),
            ("Turma B", "Tarde", professores_ids[1], True),
            ("Turma C", "Noite", professores_ids[2], True),
            ("Turma D", "Manhã", professores_ids[3], True),
            ("Turma E", "Tarde", professores_ids[4], True)
        ]
        cursor.executemany("INSERT INTO turmas (nome, turno, professor_id, ativo) VALUES (?, ?, ?, ?)", turmas)

    # Inserir alunos iniciais (sem notas, se não existirem)
    cursor.execute("SELECT COUNT(*) FROM alunos")
    if cursor.fetchone()[0] == 0:
        alunos = [
            ("Pedro Santos", 15, 1),
            ("Julia Almeida", 16, 2),
            ("Lucas Pereira", 14, 3),
            ("Mariana Rocha", 17, 4),
            ("Gabriel Nunes", 15, 5)
        ]
        cursor.executemany("INSERT INTO alunos (nome, idade, turma_id) VALUES (?, ?, ?)", alunos)

    # Atualizar alunos existentes com notas iniciais
    cursor.execute("SELECT COUNT(*) FROM alunos WHERE nota_primeiro_semestre IS NOT NULL AND nota_segundo_semestre IS NOT NULL and media_final IS NOT NULL")
    if cursor.fetchone()[0] == 0:
        # Definindo notas iniciais
        notas_iniciais = [
            (8.0, 7.5, 1),
            (9.0, 8.5, 2),
            (7.0, 6.5, 3),
            (10.0, 9.5, 4),
            (6.0, 5.5, 5)
        ]
        # Atualizando as notas dos alunos
        for nota_primeiro_semestre, nota_segundo_semestre, aluno_id in notas_iniciais:
            cursor.execute('''
                UPDATE alunos
                SET nota_primeiro_semestre = ?, nota_segundo_semestre = ?, media_final = (nota_primeiro_semestre + nota_segundo_semestre) / 2
                WHERE id = ?
            ''', (nota_primeiro_semestre, nota_segundo_semestre, aluno_id))
            conexao.commit()

    conexao.commit()
    conexao.close()
    print("Banco de dados inicializado com sucesso!")
