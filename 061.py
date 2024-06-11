#Escreva um programa que crie uma lista vazia e permita que o usuário insira números nessa lista até que ele digite um número negativo.
# Em seguida, exiba a lista na tela.


lista = []
while True:
    numeros = int(input('Digite um número: '))
    if numeros < 0:
        break
    lista.append(int(numeros))

print(lista)
