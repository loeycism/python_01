import random

def jogar():
    print("*********************************")
    print("Bem-vindo no jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101) #gera um número entr 0.0 e 1.0
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade você deseja?")
    print("(1) Fácil    (2) Médio    (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

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
            print("Você acertou! Sua pontuação foi: {}".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute) #40-20 = 20 pontos perdidos
                pontos = pontos - pontos_perdidos

    print("O número secreto era: ", numero_secreto)
    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()