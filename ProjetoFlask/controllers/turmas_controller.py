from flask import Blueprint, request
from models import model_turmas

turmas_bp = Blueprint('turma', __name__)

@turmas_bp.route('/api/turma', methods=['GET'])
def consulta_turmas():
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turma/<int:turma_id>', methods=['GET'])
def consulta_turma(turma_id):
    request.args = {'id': turma_id}  
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turma', methods=['POST'])
def cria_turma():
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turma', methods=['PUT'])
def atualiza_turma():
    return model_turmas.apiTurma()

@turmas_bp.route('/api/turma', methods=['DELETE'])
def deleta_turma():  
    return model_turmas.apiTurma()