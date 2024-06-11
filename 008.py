#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

try:
    salario = float(input('Digite o salário: '))

    reajuste = (salario * 0.6) + salario

    print(f'O salário de {salario} com o reajuste de 60% será de: {reajuste}')

except ValueError:
    print('[ERRO] Não digite letras!')