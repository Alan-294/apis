from controllers.alunos_controller import alunos_bp
from controllers.professores_controller import professores_bp
from controllers.turmas_controller import turmas_bp
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import app # Importa o arquivo config.py
from models.BancoSQLite import inicializar_banco # Importa o arquivo BancoSQLite.py
inicializar_banco()

# Registra os blueprints
app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])