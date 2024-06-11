#Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

try:
    raio = float(input('Qual o raio da esfera? '))

    volume = (4/3) * 3.1415 * raio ** 3

    area = 4 * 3.1415 * raio ** 2

    print(f'O volume da esfera é: {volume:.2f}')
    print(f'A área da esfera é: {area:.2f}')

except ValueError :
    print('[ERRO] Não digite letras!')

