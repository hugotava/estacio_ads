import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect('bancao.db')
cursor = conexao.cursor()

pessoa = Pessoa(55566677788, 'Hugo', '1984-01-01', False)

comando = '''INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);'''
cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

conexao.commit()

cursor.close()
conexao.close()