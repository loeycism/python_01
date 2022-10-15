
print("*********************************")
print("Bem-vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #relacionados ao chute
    chute = int(input("Digite um número de 1 a 100: "))

    if(chute < 1 and chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    #condições
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    #lógica
    if (acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo!")
