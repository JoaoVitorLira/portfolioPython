#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

try:
    n1 = int(input('Digite sua primeira nota: '))
    n2 = int(input('Digite sua segunda nota: '))
    n3 = int(input('Digite sua terceira nota: '))
    n4 = int(input('Digite sua quarta nota: '))
    n5 = int(input('Digite sua quinta nota: '))
    n6 = int(input('Digite sua sexta nota: '))

    media = (n1 + n2 + n3 + n4 + n5 + n6) / 6

    print(f'A sua média final é: {media}')

except ValueError:
    print('[ERRO] Não digite letras!')