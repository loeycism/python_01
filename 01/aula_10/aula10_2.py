soma = lambda a, b: a + b
sub = lambda a, b: a - b
multi = lambda a, b: a * b
div = lambda a, b: a / b

print(soma(5,10))
print(sub(10, 5))
print(multi(10, 5))
print(div(10, 5))

#calculadora total
calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'multi': lambda a, b: a * b,
    'div': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
multi = calculadora['multi']

print('A soma é: {}' .format(soma(10, 5)))
print('A multiplicação é: {}' .format(multi(10, 5)))

"""
Fazer:
soma = calculadores['soma']

é a mesma coisa de fazer:
soma = lambda a, b: a + b
"""