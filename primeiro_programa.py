print('Vamos calcular o seu IMC')
peso = eval(input('Digite aqui o seu peso em kg: '))
altura = eval(input('Digite aqui a sua altura em cm: '))
imc = peso / ((altura/100) 
              ** 2)

print(f'Seu IMC é igual a {imc}')
