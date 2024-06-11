#Crie um programa que retorne a tabuada de um número, e só pare quando o número digitado for 0000

print('--- Bem vindo ao meu programa de tabuada! ---')
tabuada = 0

while True:
    numero = input('Digite um número: ')

    if numero == '0000':
        break

    for tabuada in range(0, 11):
        resultado = int(numero) * tabuada
        print(f'{numero} X {tabuada} = {resultado}')