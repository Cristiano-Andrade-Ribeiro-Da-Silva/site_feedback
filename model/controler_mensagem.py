#Importando a classe Conexao
from DATA.conexao import Conexao
import datetime


class Mensagem:

    def cadastrar_mensagem(usuario, mensagem):

        data_hora = datetime.datetime.today()

        #A primeira 'conexao' é uma variavel e a segunda 'Conexao' é uma classe
        conexao = Conexao.criar_conexao()

        # O  cursor é responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        tamanho_mensagem = len(mensagem)


        if tamanho_mensagem > 100:
            
            #Fecha a conexão com o banco de dados
            cursor.close()
            conexao.close()

        if tamanho_mensagem <= 100:

            #Criando SQL para ser executado
            # As tres aspas adcionais são para poder dar quebra de linha
            sql = """INSERT INTO tb_comentarios(usuario, comentario, data_comentario)
                            VALUES(%s, %s, %s)"""

            valores = (usuario, mensagem, data_hora)

            #Executa o comendo mysql
            cursor.execute(sql, valores)

            #Confirma a alteração
            conexao.commit()

            #Fecha a conexão com o banco de dados
            cursor.close()
            conexao.close()
            

    def recuperar_mensagens():

        #A primeira 'conexao' é uma variavel e a segunda 'Conexao' é uma classe
        conexao = Conexao.criar_conexao()

        # O  cursor é responsavel por manipular o banco de dados, o 'dictionary = True' serve para
        cursor = conexao.cursor(dictionary = True)

        #Criando SQL para ser executado
        # As tres aspas adcionais são para poder dar quebra de linha
        sql = """SELECT usuario,
                        comentario,
                        data_comentario
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
