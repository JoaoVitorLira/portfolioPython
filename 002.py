#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

try:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    cidadeNascimento = input('Digite sua cidade de nascimento: ')
    print(f'Meu nome é {nome}, tenho {idade} anos e nasci em {cidadeNascimento}')

except ValueError:
    print('[ERRO] Não digite letras na idade!')