from flask import Flask,jsonify, request

app = Flask(__name__)

alunos_db = [
    {
        "nome": "João Pedro",
        "data_nascimento": "2000-01-01",
        "nota_primeiro_semestre": 7.5,
        "nota_segundo_semestre": 8.0,
        "turma_id": 6
    }
    
]


@app.route('/api/alunos', methods=['GET','POST'])
#Caminho do método POST provisoriamente
#http://127.0.0.1:5000/api/alunos?nome=Alan&data=2019-01-01&nota_primeiro_semestre=9&nota_segundo_semestre=10

#Caminho do método GET
#http://127.0.0.1:5000/api/alunos

def cria_aluno():
    if request.method == 'POST':
        aluno = request.get_json()
        mediaFinal = (aluno['nota_primeiro_semestre'] + aluno['nota_segundo_semestre']) / 2
        aluno['media_final'] = mediaFinal
        alunos_db.append(aluno)
        return jsonify(aluno)
    
    elif request.method == 'GET':
        return jsonify(alunos_db)


if __name__ == '__main__':
    app.run(debug=True)