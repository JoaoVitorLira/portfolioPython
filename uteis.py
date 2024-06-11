
def linha():
    print('\n')

def area(a,b):
    '''
    :param a: Representa um dos lados da gigura a ser calculado
    :param b: Representa um dos lados da gigura a ser calculado
    :return: Cálculo da Área a * b
    '''

    resultado = a * b
    return resultado

def somador(*numeros):
    '''
    :param numeros: Vários números a serem desempacotados
    :return: Soma dos números desempacotados
    '''
    return sum(numeros)