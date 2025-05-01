from DATA.conexao import Conexao
from hashlib import sha256
from flask import session


class Usuario:

    def cadastrar_usuario(login, nome, senha):
        
        # Criptografa a senha
        senha = sha256(senha.encode()).hexdigest()

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        #Criando SQL para ser executado
        # As tres aspas adcionais são para poder dar quebra de linha
        sql = """INSERT INTO tb_usuarios(login, nome, senha)
                        VALUES(%s, %s, %s);"""

        valores = (login, nome, senha)

        #Executa o comando mysql
        cursor.execute(sql, valores)

        #Confirma a alteração
        conexao.commit()

        #Fecha a conexão com o banco de dados
        cursor.close()
        conexao.close()
    

    def verificar_usuario(login, senha):

        # Criptografa a senha
        senha = sha256(senha.encode()).hexdigest()


        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary= True)

        #Criando SQL para ser executado
        # As tres aspas adcionais são para poder dar quebra de linha
        sql = """SELECT login, nome FROM tb_usuarios WHERE login = %s AND binary senha = %s;"""

        valores = (login, senha)

        #Executa o comando mysql
        cursor.execute(sql, valores)

        resultado = cursor.fetchone()


        #Fecha a conexão com o banco de dados
        cursor.close()
        conexao.close()


        if resultado:
            
            session['usuario'] = resultado['login']
            session['nome_usuario'] = resultado['nome']

            return True
        
        else:
            
            return False
    
    def logout():

        session.clear()