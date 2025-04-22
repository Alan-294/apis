from flask import Flask
from controllers.alunos_controller import alunos_bp
from controllers.professores_controller import professores_bp
from controllers.turmas_controller import turmas_bp


# Importa a função de inicialização do banco de dados
from models.BancoSQLite import inicializar_banco

# Inicializa o banco de dados (executado apenas uma vez ao iniciar o app)
inicializar_banco()

app = Flask(__name__)

app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    