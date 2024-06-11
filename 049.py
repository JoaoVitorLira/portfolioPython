'''Crie um programa que tenha a função área(), que receba as dimensões de um muro retangular e mostra a área do terreno'''

def area(a, b):
    return a * b

try:
    altura = int(input('Digite a altura: '))
    largura = int(input('Digite a largura: '))

    print(f'a área do terreno é {area(altura, largura)} metros!')

except ValueError :
    print('[ERRO] Não utilize letras!')