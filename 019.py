#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

numero = int(input('Digite um número: ').strip())

if numero > 20:
    print('O número é maior que 20')

elif numero > 10 and numero < 20:
    print('O número está entre 10 e 20')

elif numero < 0:
    print('O número é negativo, não se encaixa')

else:
    print('O número está entre 0 e 10')
