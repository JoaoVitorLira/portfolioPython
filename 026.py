#Crie um programa para analisar o IMC de uma pessoa, e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

print('--- Bem vindo ao meu calculador de IMC! ---')

altura = float(input('Digite sua altura: ').strip())
peso = float(input('Digite seu peso: ').strip())

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você possui magreza!')

elif imc >= 18.5 and imc <= 24.9:
    print('Você possui uma quantidade ideal de massa!')

elif imc >= 25 and imc <= 29.9:
    print('Você possui sobrepeso!')

elif imc >= 30 and imc <= 34.9:
    print('Você possui Obesidade grau I!')

elif imc >= 35 and imc <= 39.9:
    print('Você possui obesidade grau II!')

else:
    print('Você possui Obesidade grau III!')