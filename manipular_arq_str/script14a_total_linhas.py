with open("dados1.txt", "r") as file:
    print("Total de linhas no arquivo")
    contacao = 0
    for line in file:
        if line:
            contacao += 1
        print("Total = ", contacao)