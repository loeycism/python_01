#aula 3 parte 4
#IF como repetição

a = int(input('primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Digite o valor correto: ')) 
b = int(input('segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Digite o valor correto: '))
c = int(input('terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Digite o valor correto: '))
d = int(input('quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Digite o valor correto: '))
media = (a + b + c + d) / 4

print('media: {}' .ifmat(media))


# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}' .ifmat(media))
# else:
#     print('Foi inifmado um número errado')
