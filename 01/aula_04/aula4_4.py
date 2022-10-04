a = int(input('primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Digite o valor correto: ')) 
b = int(input('segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Digite o valor correto: '))
c = int(input('terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Digite o valor correto: '))
d = int(input('quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Digite o valor correto: '))
media = (a + b + c + d) / 4

print('media: {}' .format(media))
