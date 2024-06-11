#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois, deve mostrar para cada palavra, suas vogais

palavras = ('Carro', 'Cachorro', 'Porta', 'Tapete', 'Uva')
vogais = ('a', 'e', 'i', 'o', 'u')


for ele in palavras:
    vogalPalavra = ""


    for letra in ele.lower():
        if letra in vogais and letra not in vogalPalavra:
            vogalPalavra += letra


    if vogalPalavra:
        print(f"A palavra {ele}, as vogais são: {vogalPalavra}")
    else:
        print(f"Na palavra '{ele}', não há vogais")
