from flask import Flask


app = Flask(__name__)
app.config['HOST'] = '127.0.0.1'
#app.config['HOST'] = 'localhost'
app.config['PORT']=5000
app.config['DEBUG'] = True

# URL base para o ambiente local
BASE_URL = "http://" + app.config['HOST'] + ':' + str(app.config['PORT'])


# Para o Render, use o seguinte URL
# BASE_URL =  "https://focused-goldberg.onrender.com"