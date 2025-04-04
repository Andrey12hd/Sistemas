import random

print("1 - nivel facil")
print("2 - nivel medio")
print("3 - nivel dificio")
nivel = int(input("Digite o nivel desejado:"))
if (nivel == 1):
    numero_max = 10
    limite_tentativas = 3
elif (nivel == 2):
    numero_max = 50
    limite_tentativas = 5
elif (nivel == 3):
    numero_max = 100
    limite_tentativas = 8
else:
    print("Opção inválida. selecionado o nivel 1")
    numero_max = 10
    limite_tentativas = 3


sorteio = random.randint(1, numero_max)
#print(sorteio)
print("### JOGO DA ADIVINHAÇÃO ###")
print("Adivinhe o número que estou pensando, de 1 a ",numero_max)
tentativa = 1
while (limite_tentativas >= tentativa):
    print("Tentativa", tentativa)
    chute = int(input("Digite o seu chute:"))
    if (chute == sorteio):
        print("Parabéns, você acertou!")
        break
    elif (chute > sorteio):
        print("Chute um número menor!")
    elif (chute < sorteio):
        print("Chute um número maior!")
    tentativa = tentativa + 1
    # FINAL DO LAÇO WHILE
print("O número sorteado era: ##", sorteio, "##")
print("### FIM DO JOGO ###")