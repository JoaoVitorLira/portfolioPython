#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar
# quantos jogos serão gerados e vai sortear 6 números entre 1 a 60 para cada jogo,
# cadastrando tudo em uma lista composta

import random

jogo = []
joguinho = []

try:
    numero = int(input('Digite quantos jogos deseja gerar: '))

    for ele in range(numero):
        #Geração de um jogo

        for x in range(6):
            aleatorio = random.randint(1, 60)
            while aleatorio in joguinho:
                aleatorio = random.randint(1, 60)

            joguinho.append(aleatorio)

        #Cópia da lista
        jogo.append(joguinho[:])
        joguinho.clear()

    for y in jogo:
        print(sorted(y))

except ValueError:
    print('Só aceitamos números')
