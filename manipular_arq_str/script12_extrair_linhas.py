print("Iterando sobre o arquivo")

# Extrair linha por linha de um arquivo grande
with open("dados1.txt") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo", arquivo.name)