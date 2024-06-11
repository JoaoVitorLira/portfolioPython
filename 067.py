#Escreva um programa que crie um dicionário com as informações de 5 países, como nome, capital, população e idioma oficial. Em seguida, permita que o usuário digite o nome de um país e exiba suas informações.
paises = {
    "Brasil": ["Brasília", 211049527, "Português"],
    "Estados Unidos": ["Washington, D.C.",331002651, "Inglês" ],
    "França": ["Paris", 65273511, "Francês"],
    "Japão": ["Tóquio", 126476461, "Japonês" ],
    "Austrália": ["Canberra", 25499884, "Inglês"]
}
while True:
    try:
        pais = input('Digite o pais [sair para acabar]: ')
        if pais == 'sair':
            break
        print(paises[pais])
    except KeyError:
        print('Pais n"ao cadastrado')


