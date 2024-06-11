print('\n---Bem vindo ao meu jogo da forca!---\n')

palavraSecreta = ["C", "A", "R", "R", "O"]
letrasCertas = ["-"] * len(palavraSecreta)

acertou = False

while not acertou:
    letra = str(input("Digite a letra: "))

    acertou_letra = False

    for i in range(0, len(palavraSecreta)):
        if letra.upper() == palavraSecreta[i]:
            letrasCertas[i] = letra.upper()
            acertou_letra = True

    if acertou_letra:
        print("Você acertou uma letra!")
    else:
        print("Você errou uma letra!")

    print("Palavra secreta: ", " ".join(letrasCertas))

    acertou = "-" not in letrasCertas  
