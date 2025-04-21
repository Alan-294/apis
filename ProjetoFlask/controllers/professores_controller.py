from flask import Blueprint, request
from models import model_professores 

professores_bp = Blueprint('professores', __name__)

@professores_bp.route('/api/professores', methods=['GET'])
def consulta_professores():
    return model_professores.professores()

@professores_bp.route('/api/professores/<int:professor_id>', methods=['GET'])
def consulta_professor(professor_id):
    return model_professores.professorPorId(professor_id)

@professores_bp.route('/api/professores', methods=['POST'])
def cria_professor():
    return model_professores.cria_professor()

@professores_bp.route('/api/professores/<int:professor_id>', methods=['PUT'])
def atualiza_professor(professor_id):
    return model_professores.atualiza_professor(professor_id)

@professores_bp.route('/api/professores/<int:professor_id>', methods=['DELETE'])
def deleta_professor(professor_id):
    return model_professores.deleta_professor(professor_id)