# Crie um programa que leia o nome, sexo e idade de vários Alunos,
# guardando os dados de cada aluno em um dicionário e todos os dicionários em uma lista. No final mostre:
#
# Quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idade acima da média

alunos = []

while True:
    nome = input('Digite o nome [sair para parar]: ')
    if nome == 'sair':
        break
    sexo = input('Sexo [F/M]: ').strip().upper()
    idade = int(input('Digite sua idade: '))
    alunos.append({'nome': nome, 'sexo': sexo, 'idade': idade})


numerosCadastros = len(alunos)
somaIdade = sum(aluno['idade'] for aluno in alunos)
mediaIdade = (somaIdade / numerosCadastros)


mulheres = [aluno['nome'] for aluno in alunos if aluno['sexo'] == 'F']

acimaMedia = [aluno['nome'] for aluno in alunos if aluno['idade'] > mediaIdade]

print(f'\nNúmero de cadastros: {numerosCadastros}',
      f'\nMédia de idade: {mediaIdade:.2f}',
      f'\nLista com apenas mulheres: {mulheres}',
      f'\nPessoas com idade acima da média: {acimaMedia}'),