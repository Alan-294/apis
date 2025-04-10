# alunos_routes.py

from flask import Blueprint, request, jsonify
from ..models.model_professores import professores, professorPorId, cria_professor, atualiza_professor, deleta_professor

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/api/professores', methods=['GET'])
def professores():
    return jsonify(professores())

@professores_blueprint.route('/api/professores/<int:id>', methods=['GET'])
def professorPorId(id):
    return jsonify(professorPorId(id))


@professores_blueprint.route('/api/professores', methods=['POST'])
def cria_professor():
    return jsonify(cria_professor())


@professores_blueprint.route('/api/professores/<int:id>', methods=['PUT'])
def atualiza_professor(id):
            return jsonify(atualiza_professor(id))


@professores_blueprint.route('/api/professores/<int:id>', methods=['DELETE'])
def deleta_professor(id):
            return jsonify(deleta_professor(id))
    

