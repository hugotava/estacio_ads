import os

arquivos = os.scandir(".")
for arquivo in arquivos:
    print(arquivo.name)