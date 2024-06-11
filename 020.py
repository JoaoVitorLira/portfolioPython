#Crie um programa que verifica se uma pessoa pode ser doadora de sangue, considerando a idade e os critérios de saúde.

peso = int(input('Digite o seu peso: ').strip())
horasSono = int(input('Digite quantas horas de sono você teve: ').strip())
idade = int(input('Digite sua idade: ').strip())
saude = input('Você está em uma boa condição de saúde? (S/N) ').strip().lower()
infeccao = input('Você possuí alguma infecção?(S/N) ').strip().lower()

if peso < 50:
    print('Você não pode ser um doador')

elif horasSono < 6:
    print('Você não pode ser um doador')

elif idade < 16 and idade > 70:
   print('Você não pode ser um doador')

elif idade > 15 and idade < 18:
    print('Venha com a presença de um responsável legal')

elif saude == 'n':
    print('Você não pode ser um doador')

elif infeccao == 's':
    print('Você não pode ser um doador')

else:
    print('Você pode doar sangue')