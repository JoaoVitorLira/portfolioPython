#Escreva um programa que leia o peso de 7 pessoas, e no final, mostre qual foi o maior e o menor peso lidos

menor = None
maior = None

for ele in range (0, 7):
    peso = float(input('Digite o seu peso: '))

    if ele == 0:
        menor = peso
        maior = peso

    if peso > maior:
        maior = peso

    if peso < menor:
        menor = peso



print(f'O maior peso é {maior} quilos')
print(f'O menor peso é {menor} quilos')