#Faça um programa que leia o nome e o QI de várias pessoas, guardando tudo em uma lista.
# No final mostre:

#1 - Quantas pessoas foram cadastradas
#2 - Uma listagem com as pessoas com o maior QI
#3 - Uma listagem com as pessoas de menor QI

lista = []
nomes = []
medidaQI = []

print('---Bem vindo ao meu medidor de QI---')


while True:
    nome = input('Digite o seu nome [sair para parar]: ')
    if nome == 'sair':
        break
    nomes.append(nome[:])
    medidaQI.append(int(input('Digite o seu qi: ')))

lista.append(nomes[:])
lista.append(medidaQI[:])



print('Programa finalizado!\n'
    f'O total de pessoas cadastradas é {len(lista[0])}\n'
    f'\nPessoas com maiores QI:\n'
    f'{sorted(lista[1], reverse=True)[:3]}\n'
    f'\n Pessoas com menores QI:\n'
    f'\n{sorted(medidaQI[(len(medidaQI)-3):len(medidaQI)])}')



