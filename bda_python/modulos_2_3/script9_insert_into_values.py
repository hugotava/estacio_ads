import sqlite3 as conector

try:
    # Abertura de conexao e aquisição de cursor
    conexao = conector.connect('bancao.db')
    cursor = conexao.cursor()
    
    # Execução do comando: INSERT INTO... VALUES (...)
    comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
              VALUES (11122233344, 'João', '2000-01-31', 1);'''
    cursor.execute(comando)    

    # Execução do comando: INSERT INTO com os VALUE ? e valores separados
    # comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    #           VALUES (?, ?, ?, ?);'''
    # valores = (11122233344, 'João', '2000-01-31', 1)
    # cursor.execute(comando, valores)
    
    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados.", err)

finally:
    # Fechamento das conexões

    if conexao:
        cursor.close()
        conexao.close()




