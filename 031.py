#Escreva um programa que verifique se uma palavra é um palíndromo.

print('--- Bem vindo ao meu verificador de Palíndromos ---')
compatibilidade = 0

palavra = input('Digite uma palavra: ').strip().lower()

for ele in range(0, len(palavra)):
    if palavra[ele] == palavra[-1-ele]:
        compatibilidade += 1

if compatibilidade == len(palavra):
    print('É uma palíndromo')
else:
    print('Não é um palíndromo')
