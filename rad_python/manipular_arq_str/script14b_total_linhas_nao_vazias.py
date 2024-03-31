with open("dados1.txt", "r") as file:
    print("Total REAL de linhas não vazias no arquivo")
    contacao = 0
    for line in file:
        if line.strip():
            contacao += 1
        print("Total não vazio= ", contacao)