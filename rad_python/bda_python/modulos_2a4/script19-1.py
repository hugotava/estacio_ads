import sqlite3 as conector
from modelo import Pessoa
# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./bancao.db")
cursor = conexao.cursor()

# Definição dos registros
comando = '''SELECT * FROM Veiculo;'''
cursor.execute(comando)

# Recuperação dos registros
reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Pessoa(*reg_veiculo)
    print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)

#Fechamento das conexões
cursor.close()
conexao.close()