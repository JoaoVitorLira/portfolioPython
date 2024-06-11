'''Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

1 - Apenas os 3 primeiros mais assistidos
2 - Os últimos 2 mais assistidos
3 - A lista em ordem alfabética
4 -     Em que posição está “O rei leão”
'''

filmes = ('Avatar','Vingadores: Ultimato','Avatar: O caminho da água','Titanic','Star Wars: O despertar da força','Vingadores: Guerra infinita',
          'Homem-Aranha: Sem volta pra casa','Jurassic World: O mundo dos dinossauros', 'O rei leão', 'Vingadores')


print(filmes[0:2])
print(filmes[8:10])
print(sorted(filmes))
print(filmes.index('O rei leão')+1)