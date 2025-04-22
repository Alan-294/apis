from flask import Flask
from controllers.alunos_controller import alunos_bp
from controllers.professores_controller import professores_bp
from controllers.turmas_controller import turmas_bp
<<<<<<< HEAD

from models.BancoSQLite import inicializar_banco

playBD = True
if playBD == True:
    inicializar_banco()
playBD = False
=======
>>>>>>> 3a9ed188ab87db7ac3bb07925be1767065734163

app = Flask(__name__)

app.register_blueprint(alunos_bp)
app.register_blueprint(professores_bp)
app.register_blueprint(turmas_bp)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')