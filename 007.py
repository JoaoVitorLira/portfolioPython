#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

try:
    numero = float(input('Digite um número: '))

    dobro = numero * 2
    triplo = numero * 3
    raizQuadrada = numero ** 0.5

    print(f'O dobro de {numero} é: {dobro}')
    print(f'O triplo de {numero} é: {triplo}')
    print(f'A raiz quadrada de {numero} é: {raizQuadrada}')

except ValueError:
    print('[ERRO] Não digite letras!')