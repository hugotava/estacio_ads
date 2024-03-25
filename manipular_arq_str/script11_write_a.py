arquivo_escrita = open("dados1.txt", "a")
# "a" significa que ao escrever ele vai apenas incluir o texto no final do arquivo.
# Não vai sobreescrever o conteúdo do arquivo.

arquivo_escrita.write("\nTeste de inclusao de texto")

arquivo_escrita.close()