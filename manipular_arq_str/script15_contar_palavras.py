with open("dados1.txt", "r") as daduu:
    msg = daduu.read()
    cont = msg.count("un")
    print("Total de vezes que a palavra aparece no arquivo", daduu.name,":", cont, "vezes!")
