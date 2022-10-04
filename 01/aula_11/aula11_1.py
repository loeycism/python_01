"""
open abre ou cria um novo arquivo
w = write
\n = pula linha
"""

arquivo = open('teste.txt', 'w')
arquivo.write('meu primeiro teste\nmeu segundo teste de escrita')
arquivo.close()