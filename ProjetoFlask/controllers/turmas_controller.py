from flask import Blueprint, request
from models import model_turmas

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/api/turmas', methods=['GET'])
def consulta_turmas():
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turmas/<int:turma_id>', methods=['GET'])
def consulta_turma(turma_id):
    request.args = {'id': turma_id}  # Simula o parâmetro de consulta
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turmas', methods=['POST'])
def cria_turma():
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turmas/<int:turma_id>', methods=['PUT'])
def atualiza_turma(turma_id):
    request.args = {'id': turma_id}  # Simula o parâmetro de consulta
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turmas/<int:turma_id>', methods=['DELETE'])
def deleta_turma(turma_id):
    request.args = {'id': turma_id}  # Simula o parâmetro de consulta
    return model_turmas.apiTurma()