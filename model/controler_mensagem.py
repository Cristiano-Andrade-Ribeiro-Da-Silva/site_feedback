#Importando a classe Conexao
from DATA.conexao import Conexao
import datetime


class Mensagem:

    def cadastrar_mensagem(nome, mensagem):

        data_hora = datetime.datetime.today()

        #A primeira 'conexao' é uma variavel e a segunda 'Conexao' é uma classe
        conexao = Conexao.criar_conexao()

        # O  cursor é responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        tamanho_mensagem = len(mensagem)


        if tamanho_mensagem > 1000:
            
            #Fecha a conexão com o banco de dados
            cursor.close()
            conexao.close()

        if tamanho_mensagem <= 1000:

            #Criando SQL para ser executado
            # As tres aspas adcionais são para poder dar quebra de linha
            sql = """INSERT INTO tb_comentarios(nome, comentario, data_hora)
                            VALUES(%s, %s, %s);"""

            valores = (nome, mensagem, data_hora)

            #Executa o comando mysql
            cursor.execute(sql, valores)

            #Confirma a alteração
            conexao.commit()

            #Fecha a conexão com o banco de dados
            cursor.close()
            conexao.close()


    def recuperar_mensagens():

        #A primeira 'conexao' é uma variavel e a segunda 'Conexao' é uma classe
        conexao = Conexao.criar_conexao()

        # O  cursor é responsavel por manipular o banco de dados, o 'dictionary = True' serve para criar um dicionário
        cursor = conexao.cursor(dictionary = True)

        #Criando SQL para ser executado
        # As tres aspas adcionais são para poder dar quebra de linha
        sql = """SELECT cod_comentario,
                        nome,
                        comentario,
                        data_hora,
                        curtidas
                        FROM tb_comentarios"""

        #Executa o comendo mysql
        cursor.execute(sql)

        #Recupera os dados e guarda na variavel
        dados = cursor.fetchall()

        #O 'conexao.commit()' apenas confirma uma alteração, como um 'INSERT INTO'

        #Fecha a conexão com o banco de dados, o 'cursor' faz parte da 'conexao' então não é necessário fechar ele também
        cursor.close()
        conexao.close()

        return dados
    
    # def recuperar_ultima_mensagem(usuario):

    #     conexao = Conexao.criar_conexao()

    #     cursor = conexao.cursor()

    #     sql = """"""


    def deletar_mensagem(codigo):

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """DELETE FROM tb_comentarios WHERE cod_comentario = %s;"""

        # Virgula colocada no final para reconhecer como tupla
        valores = (codigo,)

        cursor.execute(sql,valores)

        #Confirma a alteração
        conexao.commit()

        #Fecha a conexão com o banco de dados
        cursor.close()
        conexao.close()
    
    
    def curtir_mensagem(codigo):

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql  = """UPDATE tb_comentarios SET curtidas = curtidas +1 WHERE cod_comentario = %s;"""

        valores = (codigo,)

        #Executa o comando mysql
        cursor.execute(sql, valores)

        #Confirma a alteração
        conexao.commit()

        #Fecha a conexão com o banco de dados
        cursor.close()
        conexao.close()
    

    def descurtir_mensagem(codigo):

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql  = """UPDATE tb_comentarios SET curtidas = curtidas -1 WHERE cod_comentario = %s;"""

        valores = (codigo,)

        #Executa o comando mysql
        cursor.execute(sql, valores)

        #Confirma a alteração
        conexao.commit()

        #Fecha a conexão com o banco de dados
        cursor.close()
        conexao.close()