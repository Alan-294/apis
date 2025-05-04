from flask_restx import Api

api = Api(
    title="API de Gestão Escolar",
    version="1.0",
    description="Documentação da API para Alunos, Professores e Turmas",
    doc="/docs",              # Caminho para acessar a interface Swagger
    prefix="/api",            # Prefixo base da API
)