import os
print("Removendo arquivo...")
try:
    os.remove("teste.txt")
    print("Arquivo removido!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição:", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição:", erro)
except IsADirectoryError as erro:
    print("'Remove' serve apenas para arquivo")
    print("Descrição:", erro)

print("Término do programa")

# Para a função remove (os.remove) são usadas as exceçções:
# - FileNotFoundError (Ocorre quando o arquivo não existe)
# - PermissionError (Ocorre quando não temos permissão para alterar o arquivo)
# - IsADirectoryError (Ocorre quando tentamos remover um diretório usando a função 'remove' em vez de 'rmdir')