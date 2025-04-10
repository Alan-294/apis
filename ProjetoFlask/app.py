from flask import Flask,jsonify, request
from Controllers.alunos_routes import alunos_blueprint
from Controllers.professores_routes import professores_blueprint

app.register_blueprint(alunos_blueprint)
app.register_blueprint(professores_blueprint)

app = Flask(__name__)
from professores import *
from alunos import *
from Turma import *


if __name__ == '__main__':
    
    app.run(debug=True)