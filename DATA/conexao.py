import mysql.connector


class Conexao:

    def criar_conexao():
        #criando conexão

        if False:
            # Conexão na Nuvem
                conexao = mysql.connector.connect(host = "bdgodofredo-alexstocco-93db.b.aivencloud.com", 
                                                    port = 27974, 
                                                    user = "3ds", 
                                                    password = "banana", 
                                                    database = "db_feedback")
                return conexao

        
        else:
            # Conexão no Local do computador
                    #criando conexão
                    conexao = mysql.connector.connect(host = "localhost", 
                                                    port = 3306, 
                                                    user = "root", 
                                                    password = "root", 
                                                    database = "db_feedback")
                    return conexao




# class Conexao:
#     #  Conexão no PC do professor
#     conexao = mysql.connector.connect(host = "10.110.134.2", 
#                                     port = 3306, 
#                                     user = "3ds", 
#                                     password = "banana", 
#                                     database = "db_feedback")
#     return conexao