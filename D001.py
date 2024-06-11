#Escreva um programa que execute o cálculo da Função horária da posição no MRUV, e retorne de acordo com o tempo informado pelo usuário

posicaoInicial = float(input('Digite a posição inicial: '))
velocidadeInicial = float(input('Digite a velocidade inicial: '))
tempo = float(input('Digite o tempo: '))
aceleracao = float(input('Digite a aceleração: '))

S = posicaoInicial + velocidadeInicial * tempo + (aceleracao * (tempo**2))/2

print(f'A posição do objeto é {S}')