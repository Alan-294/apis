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
            FOREIGN KEY (turma_id) REFERENCES turmas (id)
        )
    ''')

    # Inserir valores na tabela professores
    professores = [
        ("João Silva", "Matemática"),
        ("Maria Oliveira", "História"),
        ("Carlos Souza", "Física"),
        ("Ana Lima", "Química"),
        ("Fernanda Costa", "Biologia")
    ]
    cursor.executemany("INSERT OR IGNORE INTO professores (nome, disciplina) VALUES (?, ?)", professores)

    # Buscar os IDs reais dos professores
    cursor.execute("SELECT id FROM professores ORDER BY id")
    professores_ids = [row[0] for row in cursor.fetchall()]

    # Inserir valores na tabela turmas usando os IDs reais dos professores
    turmas = [
        ("Turma A", "Manhã", professores_ids[0], True),
        ("Turma B", "Tarde", professores_ids[1], True),
        ("Turma C", "Noite", professores_ids[2], True),
        ("Turma D", "Manhã", professores_ids[3], True),
        ("Turma E", "Tarde", professores_ids[4], True)
    ]
    cursor.executemany("INSERT OR IGNORE INTO turmas (nome, turno, professor_id, ativo) VALUES (?, ?, ?, ?)", turmas)

    # Inserir valores na tabela alunos
    alunos = [
        ("Pedro Santos", 15, 1),
        ("Julia Almeida", 16, 2),
        ("Lucas Pereira", 14, 3),
        ("Mariana Rocha", 17, 4),
        ("Gabriel Nunes", 15, 5)
    ]
    cursor.executemany("INSERT OR IGNORE INTO alunos (nome, idade, turma_id) VALUES (?, ?, ?)", alunos)

    # Salvar alterações e fechar conexão
    conexao.commit()
    conexao.close()
    print("Banco de dados inicializado com sucesso!")