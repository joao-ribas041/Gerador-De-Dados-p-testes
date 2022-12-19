from unicodedata import name
from flask import Flask, render_template
from dados import gerarNomes, gerarEmails, gerarTelefones, gerarCidades, gerarEstados

app = Flask(__name__)

@app.route("/")
def index():
    dados = {}
    return render_template('index.html', name=name)

@app.route("/dados")
def gerarDados():
    dados = resgatarDados()
    return render_template('index.html', dados)

def resgatarDados():
    dados = {}
    dados['nome'] = gerarNomes()
    dados['email'] = gerarEmails()
    dados['telefone'] = gerarTelefones()
    dados['cidade'] = gerarCidades()
    dados['estado'] = gerarEstados()
    return dados

if __name__ == "__main__":
    app.run(port=5000, host='localhost', debug=True)