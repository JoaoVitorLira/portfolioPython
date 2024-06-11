#Crie um programa para jogar par ou ímpar com o usuário, e só pare quando perder. Ao final deve mostrar a quantidade de vitórias

import random

maquina = None
vitorias = 0

while True:

    escolha = input('Escolha par ou impar: ').upper().strip()

    if escolha == 'PAR':
        maquina = 'IMPAR'

    elif escolha == 'IMPAR':
        maquina = 'PAR'

    numero = int(input('Escolha um número de 0 a 10: '))
    aleatorio = random.randint(0,10)
    soma = numero + aleatorio

    if escolha == 'PAR' and soma % 2 == 0:
        vitorias += 1
        print('\nVocê venceu!'
              f'\nA escolha da máquina foi {aleatorio}')


    elif escolha == 'IMPAR' and soma % 2 > 0:
        vitorias += 1
        print('\nVocê venceu!'
              f'\nA escolha da máquina foi {aleatorio}')


    else:
        print(f'\nVocê perdeu! a escolha da máquina foi {aleatorio}'
              f'\nQuantidade de vitórias: {vitorias}')

        break

