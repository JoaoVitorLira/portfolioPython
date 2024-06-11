#Escreva um programa que peça ao usuário um número de 1 a 7 e imprima o dia da semana correspondente (1 é segunda-feira, 2 é terça-feira, etc.).

print('--- Bem vindo ao meu comparador de dias da semana! ---')

numero = int(input('Digite um número: ').strip())

if numero == 1:
    print('1 é equivalante ao primeiro dia da semana, no caso é segunda-feira')

elif numero == 2:
    print('2 é equivalante ao segundo dia da semana, no caso é terça-feira')

elif numero == 3:
    print('3 é equivalante ao terceiro dia da semana, no caso é quarta-feira')

elif numero == 4:
    print('4 é equivalante ao quarto dia da semana, no caso é quinta-feira')

elif numero == 5:
    print('5 é equivalante ao quinto dia da semana, no caso é sexta-feira')

elif numero == 6:
    print('6 é equivalante ao sexto dia da semana, no caso é sábado')

elif numero == 7:
    print('7 é equivalante ao sétimo dia da semana, no caso é domingo')

else:
    print('Não corresponde a nenhum dia da semana')