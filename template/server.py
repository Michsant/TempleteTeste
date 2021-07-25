
#Importa bibliotecas
from flask import Flask, session, redirect, request, render_template
import sys
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

# Pode escolher o nome que quiser
app = Flask('nome_aplicacao')

# Define conteudo pagina inicial
@app.route('/', methods=['GET', 'POST'])
def inicio():
    if request.method == 'POST':
        # Redireciona para outra pagina ao submeter
        return redirect('/pagina2')
    # Aqui é onde fica o conteudo da pagina, no arquivo "pagina1.html": ele fica na pasta templates (obrigatoriamente)
    return render_template('pagina1.html')


# Define caminho como "pagina2" pode ser qualquer nome ou sem nada
@app.route('/pagina2', methods=['GET', 'POST'])
def segunda_pagina():
    if request.method == 'POST':
        # Volta pra pagina inicial, mas poderia ser qualquer coisa
        return redirect('/')
    # Aqui é onde fica o conteudo da pagina, no arquivo "pagina2.html": ele fica na pasta templates (obrigatoriamente)
    return render_template('pagina2.html')


if __name__ == '__main__':
    app.run()