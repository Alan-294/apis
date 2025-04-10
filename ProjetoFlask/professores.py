from flask import Flask,jsonify, request
from app import app
import models.model_professores as model



@app.route('/api/professores', methods=['GET'])
def consulta_professores():
    return model.professores()

@app.route('/api/professores/<int:id>', methods=['GET'])
def professorPorId(id):
    return model.professorPorId(id)


@app.route('/api/professores', methods=['POST'])
def cria_professor():

    return model.cria_professor()


@app.route('/api/professores/<int:id>', methods=['PUT'])
def atualiza_professor(id):
            return model.atualiza_professor(id)


@app.route('/api/professores/<int:id>', methods=['DELETE'])
def deleta_professor(id):

            return model.deleta_professor(id)
    
if __name__ == '__main__':
    app.run(debug=True)
