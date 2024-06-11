#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

numero = float(input('Digite um número: ').strip)

if (numero % 2) == 0:
    print('O número é par')
else:
    print('O número é impar')