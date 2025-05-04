from flask_restx import Namespace, Resource, fields
from models.model_professores import *

professores_ns = Namespace("professores", description="Operações relacionadas aos professores")

professores_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "data_nascimento": fields.String(required=True, description="Data de nascimento (YYYY-MM-DD)"),
    "disciplina": fields.Float(required=True, description="Disciplina que o professor atua"),
    "salario": fields.Float(required=True, description="Salário do professor"),
    "observacao":fields.String(required=True, description="Observações do histórico do professor"),
    "turma_id": fields.Integer(required=True, description="ID da turma associada"),

})

professores_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "data_nascimento": fields.String(description="Data de nascimento (YYYY-MM-DD)"),
    "disciplina": fields.Float(description="Disciplina que o professor atua"),
    "salario": fields.Float(description="Salário do professor"),
    "observacao":fields.String(description="Observações do histórico do professor"),
    "turma_id": fields.Integer(description="ID da turma associada"),
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professores_output_model)
    def get(self):
        """Lista todos os professores"""
        return professores()

    @professores_ns.expect(professores_model)
    def post(self):
        """Cria um novo professor"""
        data = professores_ns.payload
        response, status_code = cria_professor(data)
        return response, status_code

@professores_ns.route("/<int:id_professor>")
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professores_output_model)
    def get(self, id_professor):
        """Obtém um professor pelo ID"""
        return professorPorId(id_professor)

    @professores_ns.expect(professores_model)
    def put(self, id_professor):
        """Atualiza um professor pelo ID"""
        data = professores_ns.payload
        atualiza_professor(id_professor, data)
        return data, 200

    def delete(self, id_professores):
        """Exclui um professor pelo ID"""
        deleta_professor(id_professores)
        return {"message": "Professor excluído com sucesso"}, 200