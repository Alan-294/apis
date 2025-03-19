from flask import Flask,jsonify, request

app = Flask(__name__)
from professores import *
from alunos import *
from Turma import *


if __name__ == '__main__':
    
    app.run(debug=True)