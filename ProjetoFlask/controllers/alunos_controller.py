from flask import Blueprint, request
from models import model_aluno

# Define o blueprint com um prefixo de rota
alunos_bp = Blueprint('alunos', __name__, url_prefix='/api/alunos')

# GET /api/alunos - Lista todos os alunos
@alunos_bp.route('/', methods=['GET'])
def listar_alunos():
    return model_aluno.lista_alunos()

# GET /api/alunos/<id> - Consulta aluno específico
@alunos_bp.route('/<int:aluno_id>', methods=['GET'])
def obter_aluno(aluno_id):
    return model_aluno.consulta_aluno(aluno_id)

# POST /api/alunos - Cria um novo aluno
@alunos_bp.route('/', methods=['POST'])
def criar_aluno():
    aluno = request.get_json()
    return model_aluno.adiciona_aluno(aluno)

# PUT /api/alunos/<id> - Atualiza dados de um aluno
@alunos_bp.route('/<int:aluno_id>', methods=['PUT'])
def atualizar_aluno(aluno_id):
    dados = request.get_json()
    return model_aluno.update_aluno(aluno_id, dados)

# DELETE /api/alunos/<id> - Remove um aluno
@alunos_bp.route('/<int:aluno_id>', methods=['DELETE'])
def remover_aluno(aluno_id):
    return model_aluno.deletar_aluno(aluno_id)
