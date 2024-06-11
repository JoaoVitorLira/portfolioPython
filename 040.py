#Escreva um programa que leia um número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

quant = int(input('Digite a quantidade de elementos a serem mostrados em sequência: '))
ciclos = 1
ant = 0
atual = 1


while quant + 1 > ciclos:
    if ciclos == 1:
        print('0')
    elif ciclos == 2:
        print('1')
    else:
        proximo = ant + atual
        ant = atual
        atual = proximo
        print(proximo)

    ciclos += 1