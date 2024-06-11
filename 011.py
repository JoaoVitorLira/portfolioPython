#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
#Quantas letras ao todo (sem considerar os espaços)
#Quantas letras tem o primeiro nome


nome = input('Digite o seu nome: ').strip()

contagemEspacos = nome.count(' ')
tamanhoNome = len(nome)

nomeSeparado = nome.split()
primeiroNome = nomeSeparado[0]


print(f'o seu nome maiusculo é {nome.upper()},'
      f' o seu nome minúsculo é {nome.lower()},'
      f' o seu nome tem {tamanhoNome - contagemEspacos} letras,'
      f' o seu primeiro nome possuí {len(primeiroNome)} letras')
