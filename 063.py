#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('Digite a expressão: '))

pilha = []

for caractere in expressao:
  if caractere == '(':
    pilha.append(caractere)
  elif caractere == ')':
    try:
      if pilha[-1] == '(':
        pilha.pop()
      else:
        print('Expressão incorreta')
        break

    except IndexError:
      print('Expressão incorretaa')
      break

else:
  if len(pilha) == 0:
    print('Expressão correta')
  else:
    print('Expressão incorreta')