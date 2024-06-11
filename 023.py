#Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.

print('--- Bem vindo ao meu comparador de vogais e consoantes! ---')

palavra = input('Digite uma palavra: ').strip()

if palavra[0] in 'aeiou':
    print('A palavra começa com uma vogal')

else:
    print('A palavra começa com uma consoante')