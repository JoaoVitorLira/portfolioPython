#Escreva um programa que converta real para o Franco Congolês

try:
    real = float(input('Digite os reais: '))

    francoCongoles = 554.65 * real

    print(f'{real} reais, equivalem a {francoCongoles} Francos Congoleses')

except ValueError:
    print('[ERRO] Nâo digite letras!')