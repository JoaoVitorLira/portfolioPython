#Faça um programa que leia um número e retorne o fatorial !

#4! = 4 x 3 x 2 x 1

print('--- Bem vindo a minha calculadora de fatorial! ---')

numero = int(input('Digite um número: '))
fatorial = 1

while numero > 1:
   fatorial *= numero
   numero -= 1

print(f'O fatorial desse número é {fatorial}')