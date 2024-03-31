import sqlite3 as conector
from modelo import Pessoa
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./bancao.db")
cursor = conexao.cursor()

# Definição dos comandos
comando = '''SELECT * FROM Pessoa;'''
cursor.execute(comando)

# Recuperação dos registros
pessoas = []
reg_pessoas = cursor.fetchall()
for reg_pessoa in reg_pessoas:
    pessoa = Pessoa(*reg_pessoa)
    pessoa.veiculos

#Fechamento das conexões
cursor.close()
conexao.close()