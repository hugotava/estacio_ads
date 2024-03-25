with open("dados1.txt", "r") as arquivo:
    print("Representação original da linha")
    for line in arquivo:
        print(repr(line.strip()))