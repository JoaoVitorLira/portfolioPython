#Crie um programa para jogar JOKEMPO, usando a função random.randint

import random

print('Bem vindo ao seu jogo de JOKEMPO, essas são as regras:'
      '\n1 = Pedra,'
      '\n2 = Papel,'
      '\n3 = Tesoura.')

escolhaJogador = int(input('Digite sua escolha: '))
aleatorio = random.randint(1,3)
print(f'A escolha da máquina foi {aleatorio}.')

if escolhaJogador == 1 and aleatorio == 1:
    print('O jogo empatou! Pedra x Pedra')

elif escolhaJogador == 1 and aleatorio == 2:
    print('a máquina venceu! Pedra X Papel')

elif escolhaJogador == 1 and aleatorio == 3:
    print('Você venceu! Pedra X Tesoura')

elif escolhaJogador == 2 and aleatorio == 1:
    print('Você venceu! Papel X Pedra')

elif escolhaJogador == 2 and aleatorio == 2:
    print('O jogo empatou! Papel X Papel')

elif escolhaJogador == 2 and aleatorio == 3:
    print('A máquina venceu! Papel X Tesoura')

elif escolhaJogador == 3 and aleatorio == 1:
    print('A máquina venceu! Tesoura X Pedra')

elif escolhaJogador == 3 and aleatorio == 2:
    print('Você venceu! Tesoura X Papel')

elif escolhaJogador == 3 and aleatorio == 3:
    print('O jogo empatou! Tesoura X Tesoura')

else:
    print('[ERRO] Escolha um número segundo as regras!')


# 1 - Pedra
# 2 - Papel
# 3 - Tesoura

# Ler uma escolha do jogador e comparar com o PC aleatório
'''
usuario = 1

aleatorio = 2


print(aleatorio)

contador = 1
while contador:
    contador = contador + 1
    print('OI')

    if contador > 10:
        break'''