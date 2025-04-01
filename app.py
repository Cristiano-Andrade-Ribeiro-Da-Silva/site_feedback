from flask import Flask, render_template, request, redirect
import random
#Importando a classe 'Conexao' do arquivo 'conexao.py' que está dentro da pasta 'DATA'
from DATA.conexao import Conexao
#Importando a classe 'Mensagem' do arquivo 'controler_mensagem.py' que está dentro da pasta 'model'
from model.controler_mensagem import Mensagem

from model.controler_usuario import Usuario



app = Flask(__name__)

lista = []

lista_gif = ['chat.gif','macaco.gif','aleatorio-01.gif','aleatorio-02.gif','aventura-01.gif','aventura-02.gif','berserk-01.gif','berserk-02.gif','dragon-01.gif','dragon-02.gif']


#Todas as rotas estarão aqui
@app.route("/")
def pagina_login():


    return render_template("cadastro.html")


@app.route("/post/usuario", methods = ["POST"])
def cadastro_usuario():

    #Pega informações dos input no html 
    login = request.form.get("login")
    nome = request.form.get("nome")
    senha = request.form.get("senha")


    Usuario.cadastrar_usuario(login, nome, senha)

    return redirect("/")

@app.route("/login/usuario")
def login_usuario():

    #Pega informações dos input no html 
    login = request.form.get("login")
    senha = request.form.get("senha")

    Usuario.verificar_usuario(login, senha)

    return redirect("/comentario")


@app.route("/comentario")
def pagina_principal():

    gif = random.choice(lista_gif)

    #Mostrando as mensagens em um container usando a classe 'Mensagem com o método 'recuperar_mensagens' 
    mensagens = Mensagem.recuperar_mensagens()

    return render_template("pagina-principal.html", mensagem_html = mensagens, gif_html = gif)


@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    
    #Pega informações dos input no html 
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    #Cadastrando a mensagem usando a classe 'Mensagem' com o método 'Cadastrar_mensagem'
    Mensagem.cadastrar_mensagem(usuario, mensagem)

    return redirect("/comentario")


# o "<codigo>" esta em constante mudança
@app.route("/del/mensagem/<codigo>")
def del_mensagem(codigo):

    Mensagem.deletar_mensagem(codigo)

    return redirect("/comentario")


# "put" se refere para alterar algo no banco de dados
@app.route("/put/adicionar/curtidas/mensagem/<codigo>")
def adicionar_curtida(codigo):

    Mensagem.curtir_mensagem(codigo)

    return redirect("/comentario")


@app.route("/remover/curtidas/mensagem/<codigo>")
def remover_curtida(codigo):

    Mensagem.descurtir_mensagem(codigo)

    return redirect("/comentario")

app.run(debug = True)