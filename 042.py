'''Simulação de um Caixa Eletrônico Este programa simula um caixa eletrônico,
permitindo que o usuário faça depósitos, saques e consulte o saldo da conta, e sair'''

saldo = 0
resposta = 0

print('--- Bem vindo ao meu programa de Caixa Eletrônico ---')

while resposta != 4:
    resposta = int(input('1 - Saque'
      '\n2 - Depósito'
      '\n3 - Saldo'
      '\n4 - sair\n'
        '\nO que deseja fazer? '))

    if resposta == 1:
        saque = int(input('Qual o valor do saque? '))
        saldo = saldo - saque
        print(f'\nVocê sacou {saque} reais! O seu saldo é de {saldo} reais.\n')

    elif resposta == 2:
        deposito = int(input('Qual o valor do depósito? '))
        saldo = saldo + deposito
        print(f'\nO seu depósito foi de {deposito} reais! O seu saldo é de {saldo} reais.\n')

    elif resposta == 3:
        print(f'\nO seu saldo é de {saldo} reais!\n')

    else:
        print('\nVocê saiu do Caixa Eletrônico!\n')
