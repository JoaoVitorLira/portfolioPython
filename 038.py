#Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

#1.	Somar
#2.	Multiplicar
#3.	Maior
#4.	Novos números
#5.	Sair do programa

print('--- Bem vindo a minha calculadora ---')

n1 = int(input('Insira um número: '))
n2 = int(input('Insira um segundo número: '))
n3 = int(input('Insira um terceiro número: '))
escolha = 0

while escolha != 5:
      escolha = int(input('\nCálculos'
      '\n1 - Somar'
      '\n2 - Multiplicar' 
      '\n3 - Maior' 
      '\n4 - Novos números' 
      '\n5 - Sair do programa\n'
      '\nEscolha uma das opções:'))


      if escolha == 1:
            resultado = n1 + n2 + n3
            print(f'\nO resultado é {resultado}')

      elif escolha == 2:
            resultado = n1 * n2 * n3
            print(f'\nO resultado é {resultado}')

      elif escolha == 3:
            if n1 > n2 and n1 > n3:
                  resultado = n1
                  print(f'\nO resultado é {resultado}')

            elif n2 > n1 and n2 > n3:
                  resultado = n2
                  print(f'\nO resultado é {resultado}')

            elif n3 > n1 and n3 > n2:
                  resultado = n3
                  print(f'\nO resultado é {resultado}')

      elif escolha == 4:
            n1 = int(input('Insira um número: '))
            n2 = int(input('Insira um segundo número: '))
            n3 = int(input('Insira um terceiro número: '))

      else:
            print('Opção inválida')




