from flask import Flask
from controllers.alunos_controller import alunos_bp
from controllers.professores_controller import professores_bp
from controllers.turmas_controller import turmas_bp
import os
import mysql.connector

conexao = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    port=int(os.getenv('DB_PORT', 3306)),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', ''),
    database=os.getenv('DB_NAME', 'banco_escolar')
)

app = Flask(__name__)

app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

if __name__ == '__main__':
    app.run(debug=True)