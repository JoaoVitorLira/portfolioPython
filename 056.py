# Usando tuplas, leia um número de 0 a 15, e retorne esse número escrito por extenso

numeros= (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "catorze", "quinze"
)

try:
    numeroUser = int(input("Digite um número entre 0 e 15: "))


    if numeroUser <= 15 and numeroUser >= 0:
            print(f"O número {numeroUser} em extenso é {numeros[numeroUser]}")
    else:
            print("Por favor, insira um número entre 0 e 15.")
except ValueError:
    print('[ERRO] Não digite letras!')