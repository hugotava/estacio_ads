import os.path

# Para abrir dados1.txt
arquivo1 = open("dados1.txt") # caminho relativo
arquivo2 = open("/estacio_ead/manipular_arq_str/dados1.txt") # caminho absoluto

# Para abrir dados1.txt
arquivo3 = open("dados2.txt") # caminho relativo
arquivo4 = open("/estacio_ead/manipular_arq_str/dados2.txt") # caminho absoluto

print(os.path.relpath(arquivo1.name))
print(os.path.abspath(arquivo1.name))

print(arquivo1)