from .swagger_init import api

def configure_swagger(app):
    from namespace.alunosnamespace import alunos_ns
    from namespace.professornamespace import professores_ns
    from namespace.turmanamespace import turmas_ns

    api.init_app(app)
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(professores_ns, path="/professores")
    api.add_namespace(turmas_ns, path="/turmas")
    api.mask_swagger = False
