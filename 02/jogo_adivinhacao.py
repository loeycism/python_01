
print("*********************************")
print("Bem-vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 43
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #relacionados ao chute
    chute = int(input("Digite o seu número: "))

    #condições
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    print("Você digitou ", chute)

    #lógica
    if (acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo!")
