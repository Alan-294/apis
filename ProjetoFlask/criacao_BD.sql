CREATE TABLE alunos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    data_nascimento DATE,
    nota_primeiro_semestre FLOAT,
    nota_segundo_semestre FLOAT,
    media_final FLOAT,
    turma_id INT
);
