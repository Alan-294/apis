from flask import Blueprint, request
from models import model_aluno

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/api/alunos', methods=['GET'])
def consulta_alunos():
    return model_aluno.lista_alunos()

@alunos_bp.route('/api/alunos/<int:aluno_id>', methods=['GET'])
def consulta_aluno(aluno_id):
    return model_aluno.consulta_aluno(aluno_id)

@alunos_bp.route('/api/alunos', methods=['POST'])
def cria_aluno():
    aluno = request.get_json()
    return model_aluno.adiciona_aluno(aluno)

@alunos_bp.route('/api/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    
    return model_aluno.update_aluno(aluno_id)

@alunos_bp.route('/api/alunos/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    return model_aluno.deletar_aluno(aluno_id)