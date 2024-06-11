'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

print('--- Bem vindo ao meu calculador de média! ---')

maior = 0
menor = 0
soma = 0
contador = 0
resposta = 's'

while resposta == 's':

    numero = int(input("Digite um número inteiro: "))
    soma += numero

    if contador == 0:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero

    contador += 1

    resposta = input("Deseja continuar (s/n)? ").strip().lower()

    media = soma / contador

# Exibe os resultados
print(f"A média dos numeros é: {media}")
print(f"O maior valor foi {maior}")
print(f"O menor valor foi {menor}")
