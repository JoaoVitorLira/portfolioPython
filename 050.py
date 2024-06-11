'''Escreva um programa que leia uma frase, e mostre uma formatação adaptável
de acordo com o tamanho da frase, coordenado por uma função

Exemplo:
       ----------------------------
            Senai Show de bola
       ---------------------------- '''
def mostrarFrase(msg) :
        print('---' *   len(msg))
        print(f' ' * len(msg) + msg)
        print('---' * len(msg))

try:
        frase = input('Digite uma frase: ').strip()
        mostrarFrase(frase)

except:
        print('ERRO')