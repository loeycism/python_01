"""
open abre ou cria um novo arquivo
w = write
a = atualizar
r = read
\n = pula linha
"""

from pip import main



def escrever_arquivo(texto):
    diretorio = 'C:\\Users\\Eu\\Documents\\profissional\\estudo\\python_all\\course_DIO\\aula_11\\novo_arquivo.txt'
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('teste2.txt', 'a' )
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    # atualizar_arquivo('Segunda linha.\n')
    # atualizar_arquivo('Quarta linha.\n')
    # ler_arquivo('teste2.txt')