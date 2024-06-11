# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário, 
# se por acaso a Carteira de trabalho for diferente de zero. O Dicionário receberá também o ano de contratação e o saláro. 
# Calcule e apresente, além da idade, com quantos anos a pessoa vai se aposentar
from datetime import datetime

def calcular_idade(anoNascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - anoNascimento
    return idade

def calcular_anos_aposentadoria(idade, anosContratados):
    anosContribuidos = 35  
    aposentadoria = 65  
    aposentar = aposentadoria - idade
    anosContribuicao = anosContratados + anosContribuidos - datetime.now().year
    if anosContribuicao < 0:
        return "Já pode se aposentar!"
    elif aposentar <= 0:
        return "Já pode se aposentar!"
    elif aposentar <= anosContribuicao:
        return "Já pode se aposentar!"
    else:
        return aposentar

pessoas = []

while True:
    pessoa = {}
    pessoa['nome'] = input("Digite o nome da pessoa (ou digite 'sair' para encerrar): ")
    if pessoa['nome'].lower() == 'sair':
        break
    anoNascimento = int(input("Digite o ano de nascimento da pessoa: "))
    pessoa['idade'] = calcular_idade(anoNascimento)
    pessoa['carteira_trabalho'] = int(input("Digite o número da carteira de trabalho (0 se não tiver): "))
    if pessoa['carteira_trabalho'] != 0:
        pessoa['anosContratados'] = int(input("Digite o ano de contratação: "))
        pessoa['salario'] = float(input("Digite o salário: "))
        pessoa['anos_aposentadoria'] = calcular_anos_aposentadoria(pessoa['idade'], pessoa['anosContratados'])
    pessoas.append(pessoa)

print("\nCadastro de Pessoas:")
for pessoa in pessoas:
    print("\nNome:", pessoa['nome'])
    print("Idade:", pessoa['idade'])
    if pessoa['carteira_trabalho'] != 0:
        print("Ano de contratação:", pessoa['anosContratados'])
        print("Salário:", pessoa['salario'])
        print("Anos para aposentadoria:", pessoa['anos_aposentadoria'])