'''Escreva um programa que peça ao usuário 5 notas, de 0 a 10 e imprima se a média,
é insuficiente (menor que 6), suficiente (entre 6 e 7), bom (entre 7 e 9) ou excelente (9 ou maior).
'''

print('--- Bem vindo ao meu calculador de média escolar! ---')

nota1 = float(input('Digite uma nota: ').strip())
nota2 = float(input('Digite sua segunda nota: ').strip())
nota3 = float(input('Digite sua terceira nota: ').strip())
nota4 = float(input('Digite sua quarta nota: ').strip())
nota5 = float(input('Digite sua quinta nota: ').strip())

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

if media < 6:
    print(f'A sua média é {media}, ela foi insuficiente')

elif media >= 6 and media <= 7:
    print(f' a sua média é {media}, ela foi suficiente')

elif media > 7 and media < 9:
    print(f'a sua média é {media}, ela foi boa')

elif media > 9 and media <= 10:
    print(f'A sua média é {media}, ela foi excelente')

else:
    print('ERRO')