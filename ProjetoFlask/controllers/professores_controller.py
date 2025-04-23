from flask import Blueprint, request
from models import model_professores 

professores_bp = Blueprint('professores', __name__)

# GET /api/professores - Lista todos os professores
@professores_bp.route('/api/professores', methods=['GET'])
def consulta_professores():
    return model_professores.professores()

# GET /api/professores/<int:professor_id> - Consulta um professor específico
@professores_bp.route('/api/professores/<int:professor_id>', methods=['GET'])
def consulta_professor(professor_id):
    return model_professores.professorPorId(professor_id)

# POST /api/professores - Cria um novo professor
@professores_bp.route('/api/professores', methods=['POST'])
def cria_professor():
    return model_professores.cria_professor()

# PUT /api/professores/<int:professor_id> - Atualiza um professor existente
@professores_bp.route('/api/professores/<int:professor_id>', methods=['PUT'])
def atualiza_professor(professor_id):
    return model_professores.atualiza_professor(professor_id)

# DELETE /api/professores/<int:professor_id> - Remove um professor
@professores_bp.route('/api/professores/<int:professor_id>', methods=['DELETE'])
def deleta_professor(professor_id):
    return model_professores.deleta_professor(professor_id)