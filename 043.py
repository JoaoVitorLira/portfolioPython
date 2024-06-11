'''Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar 0000.
No final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag)
'''

print('--- Bem vindo ao meu programa leitor de números inteiros ---')

soma = 0
contador = 0

while True:

    numero = (input('Digite um número[0000 para sair]: '))

    if numero == '0000':
        print(f'A quantidade de números digitados foi {contador} e soma entre eles é {soma}')
        break

    else:
        soma += int(numero)
        contador += 1



