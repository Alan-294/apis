from flask import Flask,jsonify, request

app = Flask(__name__)

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
    for professor in professores_db:
        if professor["id"] == id:
            return professor
    
    return jsonify({'mensagem': 'Professor não encontrado'}), 404


@app.route('/api/professores', methods=['POST'])
def cria_professor():
    professor = request.get_json()
    professor['id'] = len(professores_db) + 1
    professores_db.append(professor)
    return jsonify(professor)


@app.route('/api/professores/<int:id>', methods=['PUT'])
def atualiza_professor(id):
    professor = request.get_json()
    for i in range(len(professores_db)):
        if professores_db[i]['id'] == id:
            professores_db[i].update(professor)
            return jsonify(professores_db[i])


@app.route('/api/professores/<int:id>', methods=['DELETE'])
def deleta_professor(id):
    for i in range(len(professores_db)):
        if professores_db[i]['id'] == id:
            professores_db.pop(i)
            return jsonify(professores_db)
    
if __name__ == '__main__':
    app.run(debug=True)

