conjunto = {1, 2, 3, 4, 5}
conjunto_2 = {4, 5, 6, 7, 8, 9}

######################
conjunto_uniao = conjunto.union(conjunto_2)
print(conjunto_uniao)
#.union une os conjuntos

######################
conjunto_interseccao = conjunto.intersection(conjunto_2)
print(conjunto_interseccao)

#.intersection vai pegar o único elemento que se repete

######################
conjunto_diferenca = conjunto.difference(conjunto_2)
print(conjunto_diferenca)


conjunto_diferenca2 = conjunto_2.difference(conjunto)
print(conjunto_diferenca2)
 
print('Diferença entre 1 e 2: {}' .format(conjunto_diferenca))
print('Diferença entre 2 e 1: {}' .format(conjunto_diferenca2))

#.difference vai mostrar os que não tem no conjunto dois, só os que tem no conjunto; literalmente a diferença entre um conjunto com o outro mas levando apenas ele

######################
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto_2)
print('Diferença simétrica: {}' .format(conjunto_diff_simetrica))

#.symmetric_difference vai mostrar os que não tem no conjunto comparando os dois. é uma mistura de .union com .difference

######################
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)

conjunto_subset = conjunto_b.issubset(conjunto_a)
print(conjunto_subset)

#no caso, vai ser falso pq no conjunto A, falta elementos que tem no conjunto B

######################
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)
