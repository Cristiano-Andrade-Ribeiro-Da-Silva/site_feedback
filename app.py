from flask import Flask, render_template, request
import mysql.connector
import datetime


app = Flask(__name__)

#Todas as rotas estarão aqui

@app.route("/")
def pagina_principal():


    return render_template("index.html")



@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    
    #Pega informações dos input no html 
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")
    data_hora = datetime.datetime.today()

    #criando conexão
    conexao = mysql.connector.connect(host = "localhost", 
                                      port = 3306, 
                                      user = "root", 
                                      password = "root", 
                                      database = "db_feedback")

    # O  cursor é responsavel por manipular o banco de dados
    cursor = conexao.cursor()

    #Criando SQL para ser executado

    # As tres aspas adcionais são para poder dar Enter
    sql = """INSERT INTO tb_comentarios(usuario, comentario, data_hora)
                    VALUES(%s, %s, %s)"""

    valores = (usuario, mensagem, data_hora)

    #Executa o comendo mysql
    cursor.execute(sql, valores)

    #Confirma a alteração
    conexao.commit()

    #Fecha a conexão com o banco de dados
    cursor.close()
    conexao.close()


    return render_template("index.html")



app.run(debug = True)