dados = {"alunos":[
        {"id": 1009,
        "nome": "João Pedro",
        "data_nascimento": "2000-01-01",
        "nota_primeiro_semestre": 10.0,
        "nota_segundo_semestre": 8.0,
        "turma_id": 6,
        "mediaFinal": 9},{
            "id": 3029,
        "nome": "André Augusto",
        "data_nascimento": "1998-09-05",
        "nota_primeiro_semestre": 8.0,
        "nota_segundo_semestre": 6.0,
        "turma_id": 6,
        "mediaFinal": 7
        }
                  ], 
        "professores":[
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
],"turmas":[
     {
    "id": 1,
    "nome": "ADS3",
    "turno": "manha",
    "professor_id": 1,
    "ativo": True
  }
]}
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

