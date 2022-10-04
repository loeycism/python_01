#sem instanciar o valor, tendo que dizer o valor de cada operação
from unicodedata import name


class Calculadora:
    # def __init__(self):
    #     pass #init não pode ficar vazio, o pass vai literalmente pular
    # como não vai instanciar nada, não precisa do init

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def sub(self, valor_a, valor_b):
        return valor_a - valor_b

    def div(self, valor_a, valor_b):
        return valor_a / valor_b

    def multi(self, valor_a, valor_b):
        return valor_a * valor_b

if __name__ == '__main__':
    calculadora = Calculadora()

    print(calculadora.soma(5, 6))
    print(calculadora.sub(10, 5))
    print(calculadora.div(20, 10))
    print(calculadora.multi(2, 3))
