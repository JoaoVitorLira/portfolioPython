#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:

#Qual é o total gasto na compra
#Quantos produtos custam mais de R$1000,00
#Qual é o produto mais barato

print('--- Bem vindo ao meu leitor de produtos! ---')

total = 0
produtosCaros = 0
maisBarato = 0
nomeBarato = ''

while True:
    nome = input('Digite o nome do produto: ')
    preco = int(input('Digite o preço do produto: '))
    total += preco

    if maisBarato == 0:
        maisBarato = preco


    if preco > 1000:
        produtosCaros += 1


    if preco < maisBarato:
        maisBarato = preco
        nomeBarato = nome

    resposta = input('Deseja continuar? [S/N] ').upper().strip()


    if resposta == 'N':
        print(f'O total gasto foi: R${total}'
              f'\n{produtosCaros} produtos custam mais de R$1000,00'
              f'\nO produto mais barato é {nomeBarato} que custa R${maisBarato}')
        break
