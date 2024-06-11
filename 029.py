#Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

print('--- Bem vindo a minha tabuada automatizada! ---')

numero = int(input('Digite um número: '))

for tabuada in range(1, 11):
    resultado = numero * tabuada
    print(f'{numero} X {tabuada} = {resultado}')
