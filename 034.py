#Escreva um programa que leia 10 números, se for ímpar deve ser descartado, se não, deve ser agregado a uma soma

print('--- Bem vindo ao meu programa de somar números pares ---')

soma = 0
inicio = int(input('Digite o primeiro número dos 10: ').strip())
final = inicio + 11

for numeros in range(inicio, final):
    if (numeros % 2) == 0:
        soma += numeros
        print(f'A soma dos pares é {soma}')

