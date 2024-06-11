#Faça um programa com uma função maior e menor,
#que leia uma lista com 5 valores informados pelo usuário e retorne esses valores e a posição deles

def maior(n):
    print(f'O maior é {max(n)}, está em {n.index(max(n))}')
def menor(n):
    print(f'O maior é {min(n)}, está em {n.index(min(n))}')


Numeros = []
try:
    for ele in range(5):
        Numeros.append(int(input('Digite algo: ')))
except:
    print('[ERRO]')

maior(Numeros)
menor(Numeros)