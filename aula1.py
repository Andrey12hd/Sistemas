import random
sorteio = random.randint(1, 10)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando")
limite_tentativas = 3
tentativa = 1
while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(imput("Digite seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
        break
    elif (chute > sorteio):
        print("Chute um numero menor!")
    elif (chute < sorteio):
        print("Chute um numero maior!")
    tentativa = tentativa + 1