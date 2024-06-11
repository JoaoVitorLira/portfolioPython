#Crie uma função para verificar se um número é par ou ímpar
def ParImpar(num):
    if (num % 2) == 0:
        return 1

    else:
        return 0


try:
    numero = int(input('Digite um número: '))
    ParImpar(numero)
except ValueError:
    print('[ERRO] Não digite letras!')
