#Crie um arquivo .py com todas as formatações de texto, como título, frase, quebra de linha

def titulo(msg):
    print('---' * len(msg))
    print(msg.title().center(2 * len(msg)))
    print('---' * len(msg))

def frase(fr):
    print(fr.upper())

def quebraLinha():
    print('---' * 30)