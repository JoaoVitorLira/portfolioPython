'''Crie um programa que pede ao usuário para digitar dois números e,
em seguida, divida o primeiro número pelo segundo número. No entanto,
o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido,
como uma string ou o número zero.
'''


while True:
    try:
        numerador = int(input('Digite um numerador: '))
        denominador = int(input('Digite um denominador: '))

        print(f'O resultado da sua divisão é {numerador / denominador}')

    except ZeroDivisionError :
        print('[ERRO] Não faça divisões por zero!')

    except ValueError :
        print(f'[ERRO] Não digite letras no programa!')

    except:
        print('ERRO')