lista_linhas = ["Aqui esta a primeira linha do arquivo.",
                "\nOlha aqui a segunda, papito."]

arquivo_escrita = open("dados2.txt", "w")
arquivo_escrita.writelines(lista_linhas)
arquivo_escrita.close()