import sqlite3 as conector
from modelo import Marca, Pessoa

conexao = conector.connect('bancao.db')
# O comando PRAGMA é uma extensão do SQL específica para o SQLite. Ela é utilizada para modificar alguns comportamentos internos do banco de dados. O SQLite, por padrão, não força a checagem das restrições de chave estrangeira. Isso ocorre por motivos históricos, visto que versões mais antigas do SQLite não tinham suporte à chave estrangeira.
conexao.execute("PRAGMA foreign_keys = on")
cursor = conexao.cursor()

# Inserção de dados na tabela Marca
comando1 = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''

marca1 = Marca("Marca A", "MA")
cursor.execute(comando1, vars(marca1))
marca1.id = cursor.lastrowid

marca2 = Marca("Marca B", "MB")
cursor.execute(comando1, vars(marca2))
marca2.id = cursor.lastrowid

# Inserção de dados na tabela Veiculo
comando2 = '''INSERT INTO Veiculo
                VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''

veiculo1 = Pessoa("AAA0001", 2001, "Prata", 1.0, 10020030040, 1)
veiculo2 = Pessoa("BBB0002", 2002, "Preto", 1.4, 10020050040, 1)
veiculo3 = Pessoa("CCC0003", 2003, "Branco", 2.0, 10020630040, 2)
veiculo4 = Pessoa("DDD0004", 2004, "Azul", 1.8, 10020070040, 2)
cursor.execute(comando2, vars(veiculo1))
cursor.execute(comando2, vars(veiculo2))
cursor.execute(comando2, vars(veiculo3))
cursor.execute(comando2, vars(veiculo4))

conexao.commit()

cursor.close()
conexao.close()