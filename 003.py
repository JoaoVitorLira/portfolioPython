#Escreva um programa que leia o nome, e o sobrenome, CONCATENE em uma nova variável nome completo, e retorne para o usuário

try:
    nome = input('Qual o seu nome? ')
    sobrenome = input('Qual o seu sobrenome? ')

    nomeSobrenome = nome + ' ' + sobrenome

    print(f'Seu nome completo é: {nomeSobrenome}')

except ValueError :
    print('[ERRO] Não digite números!')