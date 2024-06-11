#Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista, que mantenha separado as consoantes das vogais

lista = []
consoante = []
vogal = []


for ele in range(7):
    letra = input('Digite uma letra: ').strip().lower()

    if letra in 'aeiou':
        vogal.append(letra)

    elif letra in '1234567890':
        print('Só aceitamos letras!')

    else:
        consoante.append(letra)

lista.append(vogal[:])
lista.append(consoante[:])

print(lista)

