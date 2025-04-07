from flask import Flask,jsonify, request
import random
from app import app
import models.model_turmas as model


@app.route('/test')
def home():
    return "Hello, World!"

turma_db = [
     {
    "id": 1,
    "nome": "ADS3",
    "turno": "manha",
    "professor_id": 1,
    "ativo": True
  }
]

def gerar_id():

    return model.gerar_id()
    
@app.route('/api/turma', methods=['GET', 'POST', 'DELETE','PUT'])
def apiTurma():

        return model.apiTurma()
