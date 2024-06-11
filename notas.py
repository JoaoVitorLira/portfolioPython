'''
print('Oi, bem vindo ao curso')

a = 10 + 5
b = 5 - 10
c = 1000000000 / 8
d = 5 * 8
e = 50 % 2
f = 5 ** 2

print(e)
print(f'Sua idade é {c}')
'''

#Concatenação de String
'''Senai = 'Senai' + ' Luis Eulalio'
print(Senai)'''

nome = input('digite seu nome: ')
print(nome)

a = int(input('Digite um número: '))
b = a + 10
print(f'Seu novo número é {b}')

nome = 'João Vitor Lira'
print(nome[0])
print(nome[0:7])

nomeMaiuscula = nome.upper()
print(nomeMaiuscula)
nomeMinusculo = nome.lower()
print(nomeMinusculo)

nome = input('Digite seu nome: ').strip().capitalize()
print(nome)

nomeSeparado = nome.split()
print(nomeSeparado)

contagem = nome.count(' ')

nomeContagem = len(nome) - nome.count(' ')

print(nomeContagem)

nomeSemEspaco = nome.replace(__old=" ", __new=" ")
frase = input('Escreva uma frase: ').strip().lower()
frase = frase[::-1]


#IF

idade = int(input('Digite sua idade: '))

if idade > 18:
    print('Você já é maior de idade')
else:
    print('Pode Voltar pra casa')

#exemplo de if e elif

altura = float(input('Digite a sua altura: '))
if altura > 3:
    print('Você não pode andar no brinquedo')

elif altura < 1.2:
    print('Você não pode andar no brinquedo')

else:
    print('Divirta-se :)')


#Positivo
for ele in range(1, 10):
    print(ele)


#Negativo
for ele in range(10, 1, -1):
    print(ele)

#Variaável auxiliar

soma = 0
for ele in range(0, 10):
    numero = int(input('Digite um número: '))
    soma = numero + soma

    print(f'a soma é {soma}')

#Numero

contador = 0

while contador < 5:
    print('Oi')
    contador += 1


#String

resposta = ''

while resposta != 'N':
    print('Bem vindo ao senai')
    resposta = input('Deseja continuar? [S/N] --->')

while True:
    numero = int(input('Digite um número[0 para sair] -->>  '))
    if numero == 0:
        break

#funções

def quebraLinha() :
    print('-----'* 30)

def titulo(msg) :
    quebraLinha()
    print(msg)
    quebraLinha()

def raizQuadrada(n):
    return n ** (1/2)

quebraLinha()
titulo('Olá')
x = raizQuadrada(8)
print(x)
print(raizQuadrada(10))

#tuplas

carro = ('Ferrari', 'Vermelha', '2024')
print (carro)

for ele in carro:
    print(ele)

for ele in range(0, len(carro)):
    print(carro[ele])

idade = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
idade2 = (11, 12, 13)

idade3 = idade + idade2

print(idade3)
print(sum(idade3))
print(len(idade3))
print(max(idade3))
print(min(idade3))
print(sorted(idade3))

#listas

lista = [1, 2, 3, 4, 5, 6, 7]
print(sum(lista))
print(min(lista))

alunos = ['José', 'Gustavo', 'Ana']
alunos[1] = 'Felipe'

for ele in range(5):
    alunos.append(input('Digite algo: '))

print(alunos)
alunos.pop(0)
alunos.remove('Felipe')
print(alunos)

#listas aninhadas

#1
Aluno = [] #Principal
dados = [] #Secundaria

for ele in range(3):
    dados.append(input('Digite o nome: '))
    dados.append(int(input('Digite a idade: ')))
    Aluno.append(dados[:]) #cópia da lista secundária
    dados.clear()

print(Aluno)

#2
Aluno = []
nomes = []
idades = []

for ele in range(3):
    nomes.append(input('Digite o nome: '))
    idades.append(int(input('Digite a idade')))

Aluno.append(nomes[:]) #Cópia da lista secundária
Aluno.append(idades[:])

print(Aluno)

# Dicionários

dados = {'nome': 'Luis', 'idade': 23}

print(dados['nome'])
print(dados.values())
print(dados.keys())

for chave in dados:
    print(dados[chave])

#2
Alunos = {'nomes': ['a','b','c','d'],
          'idades': [1, 2, 3, 4]}

print(Alunos['nomes'])

nome = []
idade = []
Banco_Dados = {}

for x in range(5):
    nome.append(input('Digite um nome: '))
    idade.append(int(input('Digite a sua idade: ')))

Banco_Dados['Nomes'] = nome[:]
Banco_Dados['Idades'] = idade[:]

print(Banco_Dados)
print(sum(Banco_Dados['Idades']))




#Escrita
arquivo = open('registro.txt', 'w')
arquivo.write('Olá, mundo!')
arquivo.close()

#Escrita Combinada
arquivo = open('registro.txt', 'a')
arquivo.write('\nOlá, mundo!')
arquivo.close()

#leitura
arquivo = open('registro.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

nomes = ['Luis', 'Gustavo', 'Ana', 'Aline']

arquivo = open('registro.txt', 'a')

for nome in nomes:
    arquivo.write(nome)
    arquivo.write('\n')

arquivo.close()

