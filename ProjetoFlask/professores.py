from flask import Flask,jsonify, request
from app import app
from BD import professores_db, turma_db


def acharTurmas(professor_id):
    turmas = []

    for turma in turma_db:
        if (turma["professor_id"] == professor_id):
            turmas.append(turma)
            
    return turmas
@app.route('/api/professores', methods=['GET'])
def professores():
    return jsonify(professores_db)


@app.route('/api/professores/<int:id>', methods=['GET'])
def professorPorId(id):
    for professor in professores_db:
        if professor["id"] == id:
            turmas = acharTurmas(professor['id'])
     
            return jsonify({
                "Professor": professor,
                "turmas ministradas": turmas,
                "code": 200})
                    
            return  jsonify(professor)
    
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

