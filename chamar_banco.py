# importa a biblioteca de conexão com mysql
import mysql.connector


# cria conexão com o banco de dados
def conectar():

    return mysql.connector.connect(

        # endereço do servidor mysql
        host="localhost",

        # usuário do banco
        user="root",

        # senha do banco
        password="271008",

        # nome do banco utilizado
        database="suporte_ti"
    )