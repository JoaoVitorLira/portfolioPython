#Escreva um programa que crie um dicionário com os nomes e preços de 5 produtos. Em seguida, exiba o produto mais barato e o mais caro.

produtos = {'nomes': ['arroz', 'feijão', 'macarrão', 'carvão', 'carne'],
           'preços': [10, 15, 17, 25, 32]
           }

print(f'O produto mais barato é {produtos["nomes"][produtos["preços"].index(min(produtos["preços"]))]} e custa R${min(produtos["preços"])}. O produto mais caro é {produtos["nomes"][produtos["preços"].index(max(produtos["preços"]))]} e custa R${max(produtos["preços"])}')
