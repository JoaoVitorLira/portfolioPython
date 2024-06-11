#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).

idade = int(input('Digite sua idade: ').strip())

if idade >= 18:
    print('É maior de idade')
else:
    print('É menor de idade')