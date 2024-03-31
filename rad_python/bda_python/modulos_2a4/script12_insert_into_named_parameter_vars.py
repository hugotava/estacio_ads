import sqlite3 as conector
from modelo import Pessoa

conexao = conector.connect('bancao.db')
cursor = conexao.cursor()

# Criação de um objeto do tipo Pessoa
pessoa = Pessoa(33300077722, 'Silva', '1990-03-30', True)

# Definição de um comando com named parameter
comando = '''INSERT INTO Pessoa VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);'''
cursor.execute(comando, vars(pessoa))
print(vars(pessoa))

conexao.commit()

cursor.close()
conexao.close()