"""
open abre ou cria um novo arquivo
w = write
a = atualizar
r = read
\n = pula linha
"""

from msilib.schema import Directory
from pip import main



def escrever_arquivo(texto):
    diretorio = 'C:\\Users\\Eu\\Documents\\profissional\\estudo\\python_all\\course_DIO\\aula_11\\notas.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    diretorio = 'C:\\Users\\Eu\\Documents\\profissional\\estudo\\python_all\\course_DIO\\aula_11\\notas.txt'
    arquivo = open(diretorio, 'a' )
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    # escrever_arquivo('Notas:\n')
    aluno = '\nFelipe, 9, 10, 8, 6'
    atualizar_arquivo('notas.txt', aluno)
    # atualizar_arquivo('Quarta linha.\n')
    # ler_arquivo('teste2.txt')