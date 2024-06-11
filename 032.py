#Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.

print('--- Bem vindo ao meu localizador de números pares! ---')

n1 = int(input('Digite um número: ').strip())
n2 = int(input('Digite outro número: '.strip()))

for numeros in range(n1, n2 - 1, -1):
    if numeros % 2 == 0:
        print(numeros)

    else:
        for numeros in range(n1, n2 + 1):
            if (numeros % 2) == 0:
                print(numeros)