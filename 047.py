#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

valor = int(input('Digite o valor do saque: '))

quant50 = valor // 50
valor = valor - quant50 * 50

quant20 = valor // 20
valor = valor - quant20 * 20

quant10 = valor // 10
valor = valor - quant10 * 10

quant1 = valor

print(f'A quantidade de notas de:'
      f'\n 50: {quant50}'
      f'\n20: {quant20}'
      f'\n10: {quant10}'
      f'\n1: {quant1}')