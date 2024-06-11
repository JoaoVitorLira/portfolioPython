#Escreva um programa que leia o Nome, idade e sexo de 4 pessoas. No final mostre:

#1 - A média de idade do grupo
#2 - Qual é o homem mais velho
#3 - Quantas mulheres têm menos de 20 anos

print('--- Bem vindo ao meu analisador de grupo de pessoas! ---')

soma = 0
maisVelho = None
qtdMulher = 0

for pessoa in range(1, 5):
    nome = input('Digite seu nome: ').strip().lower()
    idade = int(input('Digite sua idade: ').strip().lower())
    sexo = input('Digite o seu sexo(m/f): ').strip().lower()

    soma += idade

    if maisVelho == None and sexo == 'm':
                maisVelho = idade

    if idade > maisVelho and sexo == 'm':
        maisVelho = idade
        nomeVelho = nome

    if sexo == 'f' and idade < 20:
        qtdMulher = +1



print(f'A média de idade é {soma/4} anos.')
print(f'O homem mais velho é o {nomeVelho}.')
print(f'{qtdMulher} mulher(es) tem menos de 20 anos.')