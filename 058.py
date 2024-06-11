#Crie um programa onde serão informados diversos valores em uma lista. Caso o número já exista ele não será adicionado.
# No final, serão exibidos todos os valores únicos em ordem crescente

lista = []

while True:
    numero = input('Digite um número[N para sair]: ')
    if numero == 'N':
        break
    if int(numero) not in lista:
        lista.append(int(numero))

print(lista)
