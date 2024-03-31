arquivo = open("dados1.txt", "r")
conteudo1 = arquivo.read()
print()
print("Tipo do documento 1: ", type(conteudo1))
print("Conteúdo retornado pelo read: ")
print(repr(conteudo1))
print()
arquivo.closed

arquivo = open("dados1.txt", "r")
conteudo2 = arquivo.readline()
print()
print("Tipo do documento 2: ", type(conteudo2))
print("Conteúdo retornado pelo readline: ")
print(repr(conteudo2))
proximo_conteudo = arquivo.readline()
print("Próximo conteúdo retornando: ")
print(repr(proximo_conteudo))
print()
arquivo.closed

arquivo = open("dados1.txt", "r")
conteudo3 = arquivo.readlines()
print()
print("Tipo do documento 3: ", type(conteudo3))
print("Conteúdo retornado pelo readlines: ")
print(repr(conteudo3))
print()
arquivo.closed