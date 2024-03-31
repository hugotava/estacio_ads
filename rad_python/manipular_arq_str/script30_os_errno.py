import os
import errno
print("Removendo diretório...")
try:
    os.rmdir("meu_diretorio")
    print("Diretório removido!")
except OSError as erro:
    print(erro.errno)
    if erro.errno == errno.ENOTEMPTY:
        print("O diretório não está vazio.")
    else:
        print("Erro inesperado!")
    print("Descrição:", erro)

print("Término do programa.")