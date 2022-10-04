#módulos são os arquivos .py

"""
no console:
import aula9_01

pelo módulo dá pra conectar em qualquer coisa

from aula9_01 import Televisão
importando apenas a classe
"""
from aula9_01 import Televisão
from aula9_02 import Calculadora
from aula9_2 import contador_letras

televisao = Televisão()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
lista = ['elefante', 'cachorro']
total_letras = contador_letras(lista)
print('total de letras: {}' .format(total_letras))
