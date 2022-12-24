from unicodedata import name
from flask import Flask, render_template
from dados import gerarNomes, gerarEmails, gerarTelefones, gerarCidades, gerarEstados

app = Flask(__name__)

dados = {}


@app.route("/")
def index():
    dados = testeBotao()
    return render_template('index.html', dados=dados)


@app.route("/#")
def testeBotao():
    dados = {
        'nome': '',
        'email': '',
        'telefone': '',
        'cidade': '',
        'estado': ''
    }
    if bool(dados):
        dados = resgatarDados()
    return dados


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
