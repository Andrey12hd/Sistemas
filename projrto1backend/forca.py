palavra ="escola"
limite_tentativas = len(palavra) + 5

letras_acertadas = []
for letra in palavra:
    letras_acertadas.append("_")

contador = 1
while(contador <= limite_tentativas):
    print(letras_acertadas)
    print("Tentativa: ",contador,"/",limite_tentativas)
    chute = input("Digite a letra: ")

    indice = 0
    for letra in palavra:
        if chute.lower() ==  letra:
            letras_acertadas[indice] = chute.lower()
        indice = indice +1

    contador = contador + 1
