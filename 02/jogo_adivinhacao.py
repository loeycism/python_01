
print("*********************************")
print("Bem-vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 43

chute = int(input("Digite o seu número: "))

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

print("Você digitou ", chute)

if (acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo!")
