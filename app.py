from flask import Flask, render_template, request, redirect
import random
#Importando a classe 'Conexao' do arquivo 'conexao.py' que está dentro da pasta 'DATA'
from DATA.conexao import Conexao
#Importando a classe 'Mensagem' do arquivo 'controler_mensagem.py' que está dentro da pasta 'model'
from model.controler_mensagem import Mensagem



app = Flask(__name__)

lista = []

lista_gif = ['chat.gif','aleatorio-01.gif','aleatorio-02.gif','aventura-01.gif','aventura-02.gif','berserk-01.gif','berserk-02.gif','dragon-01.gif','dragon-02.gif']


#Todas as rotas estarão aqui

@app.route("/")
def pagina_principal():

    gif = random.choice(lista_gif)

    #Mostrando as mensagens em um container usando a classe 'Mensagem com o método 'recuperar_mensagens' 
    mensagens = Mensagem.recuperar_mensagens()

    return render_template("index.html", mensagem_html = mensagens, gif_html = gif)



@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    
    #Pega informações dos input no html 
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    #Cadastrando a mensagem usando a classe 'Mensagem' com o método 'Cadastrar_mensagem'
    Mensagem.cadastrar_mensagem(usuario, mensagem)

    return redirect("/")



app.run(debug = True)