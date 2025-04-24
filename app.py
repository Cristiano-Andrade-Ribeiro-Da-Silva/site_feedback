from flask import Flask, render_template, request, redirect, jsonify
import random
#Importando a classe 'Conexao' do arquivo 'conexao.py' que está dentro da pasta 'DATA'
from DATA.conexao import Conexao
#Importando a classe 'Mensagem' do arquivo 'controler_mensagem.py' que está dentro da pasta 'model'
from model.controler_mensagem import Mensagem

from model.controler_usuario import Usuario

from flask import session



app = Flask(__name__)

app.secret_key = "senha"

lista = []

lista_gif = ['chat.gif','macaco.gif','aleatorio-01.gif','aleatorio-02.gif','aventura-01.gif','aventura-02.gif','berserk-01.gif','berserk-02.gif','dragon-01.gif','dragon-02.gif']


#Todas as rotas estarão aqui
@app.route("/")
def pagina_cadastro():

    return render_template("cadastro.html")


@app.route("/post/cadastro", methods = ["POST"])
def cadastro_usuario():

    #Pega informações dos input no html 
    login = request.form.get("login")
    nome = request.form.get("nome")
    senha = request.form.get("senha")


    Usuario.cadastrar_usuario(login, nome, senha)

    return redirect("/")


@app.route("/login/usuario")
def login_usuario():

    return render_template("login.html")


@app.route("/post/logar", methods = ["POST"])
def post_logar():

    #Pega informações dos input no html 
    login = request.form.get("login")
    senha = request.form.get("senha")

    # Existem duas formas de fazer esse if/else
    # Uma é de um modo mais profissional, sendo fazer direto como aqui abaixo, ou podemos usar um uma variavel para representar o "Usuario.verificar_usuario(login, senha)"
    # Algo como "esta_logado = Usuario.verificar_usuario(login, senha)".

    if Usuario.verificar_usuario(login, senha):
        return redirect("/comentario")
    
    else:
        return redirect("/login/usuario")


# Rota para deslogar do site
@app.route("/get/logoff")
def pos_logoff():

    Usuario.logoff()

    return redirect("/")


@app.route("/comentario")
def pagina_principal():

    #  Se ouver algun usuario logado na session, a pagina será carregada.
    if "usuario" in session:

        gif = random.choice(lista_gif)

        #Mostrando as mensagens em um container usando a classe 'Mensagem com o método 'recuperar_mensagens' 
        mensagens = Mensagem.recuperar_mensagens()

        return render_template("pagina-principal.html", mensagem_html = mensagens, gif_html = gif)

    else:

        return redirect("/login/usuario")


@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    
    #Pega informações dos input no html 
    nome_usuario = session["nome_usuario"]
    mensagem = request.form.get("mensagem")

    #Cadastrando a mensagem usando a classe 'Mensagem' com o método 'Cadastrar_mensagem'
    Mensagem.cadastrar_mensagem(nome_usuario, mensagem)

    return redirect("/comentario")


@app.route("/api/get/mensagens")
def api_get_mensagens():
    mensagens = Mensagem.recuperar_mensagens()

    return jsonify(mensagens)


@app.route("/api/get/ultimamenasgem/<usuario>")
def api_ultima_mensagem(usuario):

    mensagem = Mensagem.ultima_mensagem(usuario)

    return jsonify(mensagem)


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

#Apenas quando o site estiver ligado a internet 
#app.run(host = "0.0.0.0", port = 8080)

# Apenas quando for para testes em local
app.run(debug = True)