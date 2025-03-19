def organizar_dados(professores_db, turma_db, alunos_db):
    # Cria um dicionário para armazenar os dados organizados
    dados_organizados = {}

    # Organiza os professores com suas turmas
    for professor in professores_db:
        professor['turmas'] = []  # Adiciona uma chave 'turmas' para cada professor
    
    # Organiza as turmas e relaciona com o professor
    for turma in turma_db:
        # Encontra o professor responsável pela turma
        professor = next((p for p in professores_db if p['id'] == turma['professor_id']), None)
        if professor:
            professor['turmas'].append(turma)  # Adiciona a turma à lista de turmas do professor
    
    # Organiza os alunos e relaciona com a turma
    for aluno in alunos_db:
        # Encontra a turma do aluno
        turma = next((t for t in turma_db if t['id'] == aluno['turma_id']), None)
        if turma:
            if 'alunos' not in turma:
                turma['alunos'] = []  # Adiciona uma chave 'alunos' se não existir
            turma['alunos'].append(aluno)  # Adiciona o aluno à lista de alunos da turma
    
    # Organiza tudo em dados_organizados
    dados_organizados['professores'] = professores_db
    dados_organizados['turmas'] = turma_db
    dados_organizados['alunos'] = alunos_db

    return dados_organizados

alunos_db = [
    {
        "id": 1009,
        "nome": "João Pedro",
        "data_nascimento": "2000-01-01",
        "nota_primeiro_semestre": 10.0,
        "nota_segundo_semestre": 8.0,
        "turma_id": 1,
        "mediaFinal": 9
    },
    {
        "id": 3029,
        "nome": "André Augusto",
        "data_nascimento": "1998-09-05",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 6.0,
        "turma_id": 2,
        "mediaFinal": 7
    }
]

turma_db = [
    {
    "id": 1,
    "nome": "ADS3",
    "turno": "manha",
    "professor_id": 1,
    "ativo": True
  }, 
    {
    "id": 2,
    "nome": "SI6",
    "turno": "Noturno",
    "professor_id": 2,
    "ativo": True
  }
]

professores_db = [
    {
        "id": 1,
        "nome": "Maria",
        "data_nascimento": "2003-02-03",
        "disciplina": "Math",
        "salario": 1500,
        "Observações": "None"
    },
    {
        "id": 2,
        "nome": "Joao",
        "data_nascimento": "2005-10-03",
        "disciplina": "Chemistry",
        "salario": 2500,
        "Observações": "None"
    },
    {
        "id": 3,
        "nome": "Pedro",
        "data_nascimento": "2005-10-03",
        "disciplina": "English",
        "salario": 1550,
        "Observações": "None"
    }
]

# Chama a função para organizar os dados
dados_organizados = organizar_dados(professores_db, turma_db, alunos_db)

# Exibe os dados organizados
print(dados_organizados)








"""
   {
    'professores': [
        {
            'id': 1,
            'nome': 'Maria',
            'data_nascimento': '2003-02-03',
            'disciplina': 'Math',
            'salario': 1500,
            'Observações': 'None',
            'turmas': [
                {
                    'id': 1,
                    'nome': 'ADS3',
                    'turno': 'manha',
                    'professor_id': 1,
                    'ativo': True,
                    'alunos': [
                        {
                            'id': 1009,
                            'nome': 'João Pedro',
                            'data_nascimento': '2000-01-01',
                            'nota_primeiro_semestre': 10.0,
                            'nota_segundo_semestre': 8.0,
                            'turma_id': 6,
                            'mediaFinal': 9
                        },
                        {
                            'id': 3029,
                            'nome': 'André Augusto',
                            'data_nascimento': '1998-09-05',
                            'nota_primeiro_semestre': 8.0,
                            'nota_segundo_semestre': 6.0,
                            'turma_id': 6,
                            'mediaFinal': 7
                        }
                    ]
                }
            ]
        },
        # ... Outros professores
    ],
    'turmas': [
        {
            'id': 1,
            'nome': 'ADS3',
            'turno': 'manha',
            'professor_id': 1,
            'ativo': True,
            'alunos': [
                {
                    'id': 1009,
                    'nome': 'João Pedro',
                    'data_nascimento': '2000-01-01',
                    'nota_primeiro_semestre': 10.0,
                    'nota_segundo_semestre': 8.0,
                    'turma_id': 6,
                    'mediaFinal': 9
                },
                {
                    'id': 3029,
                    'nome': 'André Augusto',
                    'data_nascimento': '1998-09-05',
                    'nota_primeiro_semestre': 8.0,
                    'nota_segundo_semestre': 6.0,
                    'turma_id': 6,
                    'mediaFinal': 7
                }
            ]
        }
    ],
    'alunos': [
        {
            'id': 1009,
            'nome': 'João Pedro',
            'data_nascimento': '2000-01-01',
            'nota_primeiro_semestre': 10.0,
            'nota_segundo_semestre': 8.0,
            'turma_id': 6,
            'mediaFinal': 9
        },
        # ... Outros alunos
    ]
} 
"""