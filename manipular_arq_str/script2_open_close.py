arquivo = open("dados1.txt")

print("Nome do arquivo: ", arquivo.name)
print("Modo do arquivo: ", arquivo.mode)
print("Arquivo fechado? ", arquivo.closed)

arquivo.close()

print("Arquivo fechado? ", arquivo.closed)
