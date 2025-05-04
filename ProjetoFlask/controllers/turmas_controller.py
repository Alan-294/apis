from flask import Blueprint, request
from models import model_turmas

turmas_bp = Blueprint('turma', __name__)

# GET /api/turma - Lista todas as turmas
@turmas_bp.route('/api/turma', methods=['GET'])
def consulta_turmas():
    return model_turmas.apiTurma()

# GET /api/turma/<int:turma_id> - Consulta uma turma específica
@turmas_bp.route('/api/turma/<int:turma_id>', methods=['GET'])
def consulta_turma(turma_id):
    request.args = {'id': turma_id}  
    return model_turmas.apiTurma()

# POST /api/turma - Cria uma nova turma
@turmas_bp.route('/api/turma', methods=['POST'])
def cria_turma():
    return model_turmas.apiTurma()

# PUT /api/turma - Atualiza uma turma existente
@turmas_bp.route('/api/turma', methods=['PUT'])
def atualiza_turma():
    return model_turmas.apiTurma()

# DELETE /api/turma - Deleta uma turma existente
@turmas_bp.route('/api/turma', methods=['DELETE'])
def deleta_turma():  
    return model_turmas.apiTurma()