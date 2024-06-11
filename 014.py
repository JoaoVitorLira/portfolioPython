#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

numero = float(input('Digite um número: ').strip())

if numero > 0:
    print('É um número positivo')

elif numero == 0:
    print('O número é igual a 0')

else:
    print('É um número negativo')