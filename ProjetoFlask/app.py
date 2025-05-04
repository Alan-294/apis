import sys
import os
from controllers.alunos_controller import alunos_bp
from controllers.professores_controller import professores_bp
from controllers.turmas_controller import turmas_bp

# Adiciona o diretório pai ao caminho do sistema para permitir imports relativos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa a instância do aplicativo e inicializador do banco de dados
from config import app
from models.BancoSQLite import inicializar_banco

# Inicializa o banco de dados
inicializar_banco()

# Registra os blueprints
app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

# Configura o Swagger
from swagger import swagger_init
from swagger.swaggerconfig import configure_swagger
configure_swagger(app)

# Executa o aplicativo
if __name__ == '__main__':
    app.run(
        host=app.config.get('HOST'),  
        port=app.config.get('PORT'),         
        debug=app.config.get('DEBUG')        
    )