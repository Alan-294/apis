from flask import Namespace, Resource, fields
from models.model_turmas import *

turma_ns = Namespace("Turmas", description="Operações relacionadas as turmas")

turma_model = turma_ns.model("Turmas", {
    "turma_id": fields.Integer(required=True, description="Id da turma"),
    "nome": fields.String(required=True, description="Nome da turma)"),
    "turno": fields.Float(required=True, description="Turno da turma, manhã, tarde ou noite"),
    "professor_id": fields.Integer(required=True, description="Id do professor associado"),
    "ativo":fields.String(required=True, description="Status atual da turma relacionada"),
})

turma_output_model = turma_ns.model("TurmasOutput", {
    "turma_id": fields.Integer(description="ID da turma"),
    "nome": fields.String(description="Nome da turma"),
    "data_nascimento": fields.String(description="Turno da turma, manhã, tarde ou noite"),
    "disciplina": fields.Float(description="Id do professor associado"),
    "ativo": fields.Float(description="Status atual da turma relacionada"),
})

@turma_ns.route("/")
class TurmasResource(Resource):
    @turma_ns.marshal_list_with(turma_output_model)
    def get(self):
        """Lista todas as turmas"""
        return consulta_turmas()

    @turmas_ns.expect(turmas_model)
    def post(self):
        """Cria uma nova turma"""
        data = turmas_ns.payload
        response, status_code = cria_turma()
        return response, status_code

@turmas_ns.route("/<int:id_turmas>")
class TurmasIdResource(Resource):
    @turmas_ns.marshal_with(turmas_output_model)
    def get(self, id_professor):
        """Consulta uma turma pelo ID"""
        return consulta_turma(turma_id)

    @turmas_ns.expect(turmas_model)
    def put(self, id_professor):
        """Atualiza uma turma"""
        data = turmas_ns.payload
        atualiza_turma()
        return data, 200

    def delete(self, id_professores):
        """Exclui uma turma pelo ID"""
        deleta_turma()
        return {"message": "Turma excluída com sucesso"}, 200