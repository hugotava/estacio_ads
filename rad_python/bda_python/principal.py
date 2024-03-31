import sqlite3 as conector
from modelos import Municipio, Dengue

conexao = None
cursor = None

try:
    conexao = conector.connect("meu_banco.db")
    conexao.execute("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    with open("dengue_ce.csv") as arquivo:
        arquivo.readline() # descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, casos_2018, casos_2019 = linha.strip().split(',')
            print(codigo, nome, casos_2018, casos_2019)

            municipio = Municipio(codigo, nome)
            comando = '''INSERT INTO Municipio VALUES (:codigo, :nome);''' # parâmetros nomeados
            cursor.execute(comando, vars(municipio))

            dengue_2018 = Dengue(codigo, 2018, int(casos_2018))
            dengue_2019 = Dengue(codigo, 2019, int(casos_2019))
            comando = '''INSERT INTO Dengue VALUES (:codigo,:ano,:casos);''' # parâmetros nomeados
            cursor.execute(comando, vars(dengue_2018))
            cursor.execute(comando, vars(dengue_2019))
    
    with open("populacao.csv") as arquivo:
        arquivo.readline() # descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, pop_2018, pop_2019 = linha.strip().split(',')
            print(codigo, nome, pop_2018, pop_2019)

            comando = '''INSERT INTO Populacao VALUES (?, ?, ?);''' # delimitador ?
            cursor.execute(comando, (codigo, 2018, pop_2018))
            cursor.execute(comando, (codigo, 2019, pop_2018))

# Criação das tabelas
    # comando = '''CREATE TABLE Municipio (
    #                 codigo INTEGER NOT NULL,
    #                 nome VARCHAR(32) NOT NULL,
    #                 PRIMARY KEY (codigo)
    #                 );'''
    # cursor.execute(comando)

    # comando = '''CREATE TABLE Populacao (
    #                 codigo INTEGER NOT NULL,
    #                 ano INTEGER NOT NULL,
    #                 PRIMARY KEY (codigo, ano),
    #                 FOREIGN KEY (codigo) REFERENCES Municipio(codigo)
    #                 );'''
    # cursor.execute(comando)

    # comando = '''CREATE TABLE Dengue (
    #                 codigo INTEGER NOT NULL,
    #                 ano INTEGER NOT NULL,
    #                 casos INTEGER NOT NULL,
    #                 PRIMARY KEY (codigo, ano),
    #                 FOREIGN KEY (codigo) REFERENCES Municipio(codigo)
    #                 );'''
    # cursor.execute(comando)

# Alteração de tabela
    # comando = '''ALTER TABLE Populacao
    #                 ADD populacao INTEGER NOT NULL;'''
    # cursor.execute(comando)

    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)

finally:
    # Fechamento das conexões e cursores
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()