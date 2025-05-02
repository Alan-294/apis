CREATE TABLE professores(
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    data_nascimento DATE,
    disciplina VARCHAR(40),
    salario FLOAT,
    observações VARCHAR(150)
);

CREATE TABLE turmas(
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    turno VARCHAR(10),
    professor_id int,
    ativo BOOLEAN,
    FOREIGN KEY (professor_id) REFERENCES professores(id)
);


CREATE TABLE alunos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    data_nascimento DATE,
    nota_primeiro_semestre FLOAT,
    nota_segundo_semestre FLOAT,
    media_final FLOAT,
    turma_id INT,
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);

INSERT INTO professores (
    id,
    nome,
    data_nascimento,
    disciplina,
    salario,
    observações
) VALUES (
    1,
    'Carlos Silva',
    '1980-09-15',
    'Matemática',
    4500.00,
    'Professor titular do ensino médio'
);
INSERT INTO turmas (
    id,
    nome,
    turno,
    professor_id,
    ativo
) VALUES (
    1,
    '3º Ano A',
    'Manhã',
    5001,
    TRUE
);





INSERT INTO alunos (
    id,
    nome,
    data_nascimento,
    nota_primeiro_semestre,
    nota_segundo_semestre,
    media_final,
    turma_id
) VALUES (
    1009,
    'Maria Fernandes',
    '2005-04-22',
    8.5,
    9.0,
    (8.5 + 9.0) / 2,
    1
);