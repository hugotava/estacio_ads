with open("dados1.txt", "r") as arquivo:
    print("Representação da linha após strip")
    for line in arquivo:
        clean_line = line.strip()
        print(repr(clean_line))