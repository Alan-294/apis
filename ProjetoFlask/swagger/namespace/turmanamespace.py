from flask import Namespace, Resource, fields
from models.model_turmas import *

turmas_ns = Namespace("Turmas", description="Operações relacionadas as turmas")

turmas_model = turmas_ns.model("Turmas", {
    "id": fields.Integer(required=True, description="Id da turma"),
    "nome": fields.String(required=True, description="Nome da turma)"),
    "turno": fields.Float(required=True, description="Turno da turma, manhã, tarde ou noite"),
    "professor_id": fields.Integer(required=True, description="Id do professor associado"),
    "ativo":fields.String(required=True, description="Status atual da turma relacionada"),
})

turmas_output_model = turmas_ns.model("TurmasOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "disciplina": fields.Float(description="Disciplina que o professor atua"),
    "salario": fields.Float(description="Salário do professor"),
    "observacao":fields.String(description="Observações do histórico do professor"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})

@turmas_ns.route("/")
class ProfessoresResource(Resource):
    @turmas_ns.marshal_list_with(turmas_output_model)
    def get(self):
        """Lista todas as turmas"""
        return turmas()

    @turmas_ns.expect(turmas_model)
    def post(self):
        """Cria um novo professor"""
        data = turmas_ns.payload
        response, status_code = cria_professor(data)
        return response, status_code

@turmas_ns.route("/<int:id_turmas>")
class ProfessorIdResource(Resource):
    @turmas_ns.marshal_with(turmas_output_model)
    def get(self, id_professor):
        """Obtém uma turma pelo ID"""
        return professorPorId(id_professor)

    @turmas_ns.expect(turmas_model)
    def put(self, id_professor):
        """Atualiza uma turma pelo ID"""
        data = turmas_ns.payload
        atualiza_professor(id_professor, data)
        return data, 200

    def delete(self, id_professores):
        """Exclui uma turma pelo ID"""
        deleta_professor(id_professores)
        return {"message": "Professor excluído com sucesso"}, 200