'''Escreva um programa que peça ao usuário para adivinhar um número entre 1 e 10 e continue pedindo até
que o usuário acerte o número. E no final, retorne também a quantidade de tentativas necessárias.'''

import random

print('--- Bem vindo ao meu programa de advinhação de números ---')

aleatorio = random.randint(1,10)
tentativas = 0
resposta = 0

while resposta != aleatorio:
    resposta = int(input('Digite um número: '))
    tentativas += 1
    print(f'Essa foi sua {tentativas}° tentativa...')


if resposta == aleatorio:
    print(f'Você acertou! quantidade de tentativas: {tentativas}')