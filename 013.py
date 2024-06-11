#Crie um programa que leia uma frase e mostre:
# 1.Quantas vezes aparece a letra “a”
# 2.Em que posição ela aparece a primeira vez
# 3.Em que posição ela aparece na última vez


frase = input('Digite uma frase: ').strip()

contagemA = frase.count('a')
primeiraLetra = frase.find('a')
ultimaLetra = frase.rfind('a')

print(f'A frase possuí {contagemA} letras "a", a primeira aparece na posição {primeiraLetra} e a última aparece na posição {ultimaLetra}')
