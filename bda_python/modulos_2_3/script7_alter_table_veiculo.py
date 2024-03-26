import sqlite3 as conector

try:
    # Abertura de conexao e aquisição de cursor
    conexao = conector.connect('bancao.db')
    cursor = conexao.cursor()
    
    # Execução de um comando: SELECT... CREATE...
    comando = '''ALTER TABLE Veiculo
                    ADD motor REAL;'''
    
    cursor.execute(comando)

    # Efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("Erro de banco de dados.", err)

finally:
    # Fechamento das conexões

    if conexao:
        cursor.close()
        conexao.close()





