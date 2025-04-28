from flask import Flask
''' Exemplo rápido de aplicação WEB com Flask '''

app = Flask(__name__)

# Definição de Rotas
@app.route("/")
def hello_world():
    # Retorno de HTML
    return "<p>Hello World!</p>"

@app.route("/home")
def home():
    return "<h1>Bem-vindo à minha página!</h1>"