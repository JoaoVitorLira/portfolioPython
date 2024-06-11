#Escreva um programa que calcule a soma de todos os números múltiplos de 4 que são encontrados entre 1 até 500

print('--- Essa é a soma de todos os números múltiplos de 4 encontrados de 1 até 500')

soma = 0

for numeros in range(0, 501):
    if (numeros % 4) == 0:
        soma += numeros
        print(soma)