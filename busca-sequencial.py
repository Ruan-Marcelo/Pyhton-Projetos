vetor = [];
try:
    for r in range(5):
        numero = int(input(f"Digite o {len(vetor) + 1}° numero: "))
        vetor.append(numero)

except ValueError:
    print("Digite um valor valido");

try:
    alvo = int(input("Digite o valor para buscar no vetor: "))

    if alvo in vetor:
        posicao = vetor.index(alvo)
        print(f"O valor {alvo} existe na posição {posicao}.")
    else:
        print(f"O valor {alvo} não foi encontrado no vetor.")

except ValueError:
    print("Digite um valor valido");

