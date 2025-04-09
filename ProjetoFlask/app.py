from flask import Flask
from controllers.alunos_controller import alunos_bp
# from controllers.professores_controller import professores_bp
# from controllers.turmas_controller import turmas_bp

app = Flask(__name__)

# Registrar os Blueprints
app.register_blueprint(alunos_bp)
# app.register_blueprint(professores_bp)
# app.register_blueprint(turmas_bp)

if __name__ == '__main__':
    app.run(debug=True)