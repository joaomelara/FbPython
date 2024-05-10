import pymysql
import os
def limpatela():
    os.system('cls')

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password='fbradesco',
    database='agenda',
)



cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuario")

resultados = cursor.fetchall()

print(resultados)


#inserir dados
dados = ("Gustavo","gustavo@gmail.com","11 9888-8888","paia")

cursor.execute("INSERT INTO usuario (nome,email,telefone,mensagem) values(%s,%s,%s,%s)",dados)

conexao.commit

cursor.execute("SELECT * FROM usuario")

resultados = cursor.fetchall()

print(resultados)


#fechamento da conexao
conexao.close()