import os
print("Criando um diretório...")
try:
    os.mkdir("meu_diretorio")
    print("Diretório criado!")
except PermissionError as erro:
    print("Sem permissão para criar diretório")
    print("Descrição:", erro)
except FileExistsError as erro:
    print("Diretório já existe!")
    print("Descrição:", erro)

print("Término do programa")
