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

def aluno():
    if request.method == 'POST':
      
        nome = request.args.get('nome', type=str)
        data = request.args.get('data', type=str)
        nota_primeiro_semestre = request.args.get('nota_primeiro_semestre', type=int)
        nota_segundo_semestre = request.args.get('nota_segundo_semestre', type=int)
        media_final = (nota_primeiro_semestre + nota_segundo_semestre) /2

        aluno = {
            "turma_id": 6,
            "nome": nome,
            "data_nascimento": data,
            "nota_primeiro_semestre": nota_primeiro_semestre,
            "nota_segundo_semestre": nota_segundo_semestre,
            "media_final": media_final
            }
        alunos_db.append(aluno)

        return jsonify(aluno)

    elif request.method == 'GET':
        return jsonify(alunos_db)
        

if __name__ == '__main__':
    app.run(debug=True)