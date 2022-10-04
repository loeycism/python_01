lista = [12, 10, 5, 7]
lista_animais = ['gato', 'cachorro', 'papagaio']

if 'lobo' in lista_animais:
    print('existe um lobo na lista')
else:
    print('não existe lobo na lista. Será incluído!')
    lista_animais.append('lobo')
