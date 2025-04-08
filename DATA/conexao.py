import mysql.connector
# Local do computador

# class Conexao:
#     def criar_conexao():
#         #criando conexão
#         conexao = mysql.connector.connect(host = "localhost", 
#                                         port = 3306, 
#                                         user = "root", 
#                                         password = "root", 
#                                         database = "db_feedback")
#         return conexao

#  PC do professor

# class Conexao:
#     def criar_conexao():
#         #criando conexão
#         conexao = mysql.connector.connect(host = "10.110.134.2", 
#                                         port = 3306, 
#                                         user = "3ds", 
#                                         password = "banana", 
#                                         database = "db_feedback")
#         return conexao
    

class Conexao:
    def criar_conexao():
        #criando conexão
        conexao = mysql.connector.connect(host = "bdgodofredo-alexstocco-93db.b.aivencloud.com", 
                                        port = 27974, 
                                        user = "3ds", 
                                        password = "banana", 
                                        database = "db_feedback")
        return conexao