#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

numero = int(input('Digite um número: ').strip())
segundoNumero = int(input('Digite outro número: ').strip())

if numero == segundoNumero:
    print('Eles são números iguais')
else:
    print('São números diferentes')