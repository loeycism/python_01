print("*********************************")
print("Bem-vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 43

chute = int(input("Digite o seu número: "))

print("Você digitou ", chute)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")
