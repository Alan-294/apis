from flask import Flask


app = Flask(__name__)
#app.config['HOST'] = '127.0.0.1'
#app.config['HOST'] = 'localhost']
app.config['HOST'] ='0.0.0.0'
app.config['PORT']=5000
app.config['DEBUG'] =True

# URL base para o ambiente local (DOCKER ou local)
if app.config['HOST'] == '0.0.0.0':
    BASE_URL = "http://127.0.0.1:" + str(app.config['PORT'])
else:
    BASE_URL = "http://" + app.config['HOST'] + ':' + str(app.config['PORT'])

# Para o Render, use o seguinte URL
#BASE_URL =  "https://new-api-flask2.onrender.com"
