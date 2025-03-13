from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/exemplo', methods=['GET'])

def get_example():
    dados = {'message': 'Bem-vindo á minha primeira API'}
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)