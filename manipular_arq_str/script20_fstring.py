nome = "Hugo"
lista = [4, 5, 6]

minha_string = "Olá, " + nome + "."
minha_fstring1 = f"Olá, {nome}."
minha_fstring2 = f"Olá, {nome.upper()}."
minha_fstring3 = f"Quantos anos você tem? {30 + 9}."
minha_fstring4 = f"O número 2 é maior que o número 1? {2 > 1}"
minha_fstring5 = f"O número 2 está contido na lista {lista}? {2 in lista}"

print()
print("Exemplo de string formatada sem o fstring")
print(minha_string)
print()
print("Exemplo de fstring")
print(minha_fstring1)
print()
print("Exemplo de fstring e o método upper")
print(minha_fstring2)
print()
print("Exemplo de fstring com uma soma de números")
print(minha_fstring3)
print()
print("Exemplo de fstring com uma verificação de condição")
print(minha_fstring4)
print()
print("Exemplo de fstring com uma verificação de condição com método IN")
print(minha_fstring5)
