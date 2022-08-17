# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")

# Rota Raiz
@app.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome="Henrique Poyatos"
    produtos = [
    {"nome": "Ração", "preco": 199.99},
    {"nome": "Playstation", "preco": 1999.99}]

    return render_template("alo.html", n=nome, aProdutos=produtos), 200

# Nova Rota Teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):
    return "Nova rota teste<br>Variável: {}".format(variavel), 200

app.run()

