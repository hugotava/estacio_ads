import os
print("Renomeando arquivo...")
try:
    os.rename("teste_alfa.txt", "teste_beta.txt")
    print("Arquivo renomeado!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição:", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição:", erro)
except FileExistsError as erro:
    print("O arquivo de destino já existe!")
    print("Descrição:", erro)

print("Término do programa")

# Para a função rename (os.rename) são usadas as exceçções:
# - FileNotFoundError (Ocorre quando a origem não existe)
# - PermissionError (Ocorre quando não temos permissão para alterar o arquivo de origem ou para escrita do destino)
# - FileExistsError (Ocorre quando o arquivo de destino já existe)