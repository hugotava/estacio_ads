frase = "Eu amo comer amoras no café da manhã"

#Resultado obtido utilizando o método count diretamente
print("Contagem direta: ", frase.count('amo'))

#Resultado obtido utilizando a quebra da frase em palavras
contador = 0
lista_termos = frase.split()
for palavra in lista_termos:
    if palavra =='amo':
        contador += 1
print("Contagem correta com loop for e contador: ", contador)

#Resultado obtido utilizando a quebra da frase (split) mais a contagem do python (count)
lista_termos = frase.split()
contacao = lista_termos.count("amo")
print("Contagem correta com split+count: ", contacao)