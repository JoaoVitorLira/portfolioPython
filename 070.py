# Escreva um programa que leia diversos alunos, crie um dicionário com as notas de dele em três disciplinas: matemática, 
# português e história. Em seguida, exiba a média das notas do aluno.

alunos = {
  'Joao': {'matematica': 8, 'portugues': 8, 'historia': 9},
  'Matheus': {'matematica': 7, 'portugues': 8, 'historia': 7},
  'Alana':{'matematica': 9, 'portugues': 10, 'historia': 6},
  'Julia':{'matematica': 10, 'portugues': 7, 'historia': 9}
}

for chave, notas in alunos.items():
  media = sum(notas.values()) / len(notas)
  print(f' a media do {chave} é {media: .2f}')