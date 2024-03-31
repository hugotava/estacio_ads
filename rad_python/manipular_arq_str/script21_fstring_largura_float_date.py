from datetime import datetime

frutas = ['Jabuticaba', 'Laranja', 'Uva', 'Banana']
for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número de letras: {len(fruta):3}"
    #Dentro das chaves, após a variável, ":12" siginifica que do início da palavra até o próximo
    # trecho da fstring deverá conter 12 espaços (com letras e espaços). Ou seja, é a largura!
    print(minha_fruta)

print()

pi = 3.1415
meu_numero = f'O número PI é: {pi:.1f}'
# Utilizamos a expressão {pi:.1f}, ou seja, queremos que seja exibido o valor da variável pi com uma casa decimal apenas.
# Como não especificamos a largura, ela será calculada de forma a acomodar toda a parte inteira do float.

meu_numero_deslocado = f'O número PI deslocado é: {pi:6.1f}'
# Utilizamos a expressão {pi:6.1f}, que indica que o número deve ocupar seis espaços "6.",
# sendo que, necessariamente, deve ter uma casa decimal ".1".

meu_numero_preciso = f'O número PI mais preciso é: {pi:.4f}'
# Utilizamos a expressão {pi:.4f}, para que seja exibido o número com quatro casas decimais ".4".

print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)
print()

data = datetime.now()
minha_data = f'A data de hoje é {data}'
# Criamos uma f-string para exibir o valor da variável data sem informar ao Python qual formatação ele deve utilizar ({data}).
# Com isso, a data foi impressa no formato padrão: 2020-08-13 10:50:32.262037.

minha_data_formatada = f'A data de hoje formatada é {data:%d/%m/%Y}'
# Utilizamos a expressão {data:%d/%m/%Y}, que indica que desejamos exibir a data no formato “dia/mês/ano” (13/08/2020).

print(minha_data)
print(minha_data_formatada)