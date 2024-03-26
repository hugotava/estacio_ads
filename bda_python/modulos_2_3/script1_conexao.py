import sqlite3
conexao = sqlite3.connect('bancao.db')
# Se quisermos criar um banco de dados em memória, que será criado para toda execução do programa, basta utilizar o comando
# conexao = sqlite3.connect(':memory:')