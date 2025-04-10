# alunos_routes.py

from flask import Blueprint, request, jsonify
from ..models.model_aluno import adiciona_aluno, lista_alunos, aluno_por_id, update_aluno, deletar_aluno, consulta_aluno

alunos_blueprint = Blueprint('alunos',__name__)


@alunos_blueprint.route('/api/alunos', methods=['POST'])
def cria_aluno():
    aluno = request.get_json()
    return jsonify(adiciona_aluno(aluno))


@alunos_blueprint.route('/api/alunos', methods=['GET'])
def consulta_alunos():
    return jsonify(lista_alunos())


@alunos_blueprint.route('/api/alunos/<int:aluno_id>', methods=['GET'])
def consulta_aluno(aluno_id):
    return jsonify(consulta_aluno(aluno_id))


@alunos_blueprint.route('/api/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    novo_aluno = request.json        
    return jsonify(update_aluno(aluno_id))


@alunos_blueprint.route('/api/alunos/<int:aluno_id>', methods=['DELETE'])
def deletar_aluno(aluno_id):
    return jsonify(deletar_aluno(aluno_id))
