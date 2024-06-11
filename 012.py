#Crie um programa que leia um nome, e mostre o primeiro e o último nome

nome = input('Digite o seu nome completo: ').strip()

nomeSeparado = nome.split()
contagemNome = len(nome)
ultimoEspaco = nome.rfind(' ')

ultimoNome = nome[ultimoEspaco:contagemNome]


print(f'o seu nome é {nome}. Primeiro nome: {nomeSeparado[0]}. Último nome: {ultimoNome}.')


