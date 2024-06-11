#Crie um arquivo .py com todas as operações matemáticas, que receba valores, desempacote e return

def somador(*numeros):
    '''
    :param numeros: Vários números a serem desempacotados
    :return: Soma dos números desempacotados
     '''
    return sum(numeros)



def subtrador(*numeros):
    '''
    :param numeros: numeros: Vários números a serem desempacotados
    :return:
    '''
    s = 0
    for valor in numeros:
        s -= valor

    return s

def multiplicador(*numeros):
    '''
    :param numeros:
    :return:
    '''
    s = 1
    for valor in numeros:
        s *= valor


    return s

print(multiplicador(1, 3, 4))



