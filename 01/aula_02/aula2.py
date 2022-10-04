#aula 2
# comandos básicos e interação com o usuário
#O que são variáveis e como manipulá-las através de operadores aritméticos e interação com usuário

#a = 10
#b = 7
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
sub = a - b
multi = a * b
div = a / b
resto = a % b

# print('sua soma é: ' + str(soma))
# conversão
# soma = str(soma)
# print(type(soma))

# print('sua subtração é: ' + str(sub))
# print('sua multiplicação é: ' + str(multi))
# print('sua divisão é: ' + str(div))
# print('seu resto é: ' + str(resto))

# \n é o enter
print ('Soma: {soma}. \nSubtração: {sub}. \nMultiplicação: {multi}. \nDivisão: {div}. \nResto: {resto}' .format(soma=soma,
                sub=sub,
                multi=multi,
                div=div,
                resto=resto))
