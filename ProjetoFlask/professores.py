from flask import Flask,jsonify, request
from app import app
import model_professores as model

professores_db = [
    {
        "id": 1,
        "nome": "Maria",
        "data_nascimento": "2003-02-03",
        "disciplina": "Math",
        "salario": 1500,
        "Observações": "None"
    },
    {
        "id": 2,
        "nome": "Joao",
        "data_nascimento": "2005-10-03",
        "disciplina": "Chemistry",
        "salario": 2500,
        "Observações": "None"
    },
    {
        "id": 3,
        "nome": "Pedro",
        "data_nascimento": "2005-10-03",
        "disciplina": "English",
        "salario": 1550,
        "Observações": "None"
    }
    
]

@app.route('/api/professores', methods=['GET'])
def professores():
    return jsonify(professores_db)


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
