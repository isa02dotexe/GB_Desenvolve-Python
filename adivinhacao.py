import random

def jogar():
    print("++++++++++++++++++++++++++++++++")
    print("Bem vindo ao jogo de adivinhação!")
    print("++++++++++++++++++++++++++++++++")

    numero_secreto = random.randrange(1,101)    #de 1 a 100
    total_de_tentativa = 0
    pontos = 1000

    print("Qual o nível de dificuldade?", numero_secreto)

    print("(1)Fácil | (2)Médio | (3)Difícil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_de_tentativa = 20
    elif (nivel == 2):
        total_de_tentativa = 10
    else:
        total_de_tentativa = 5

    for rodada in (1, total_de_tentativa +1) :
        print("Tentativa {} de {}" .format(rodada, total_de_tentativa))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou ", chute)

        if (chute < 1 or chute >= 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos !".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto) - chute
            pontos = pontos - pontos_perdidos
        print("Fim do jogo :)")


if (__name__ == "__main__"):
    jogar()