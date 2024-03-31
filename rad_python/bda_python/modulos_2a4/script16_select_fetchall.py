import sqlite3 as conector

# Abertura de conexão e aquisição de cursor
conexao = conector.connect("./bancao.db")
cursor = conexao.cursor()

# Definição dos registros
comando = '''SELECT nome, oculos FROM Pessoa;'''
cursor.execute(comando)

# Recuperação dos dados
registros = cursor.fetchall()
print("Tipo retornando pelo fetchall():", type(registros))

for registro in registros:
    print("Tipo:", type(registro), "- Conteúdo:", registro)

#Fechamento das conexões
cursor.close()
conexao.close()