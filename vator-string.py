continuar = True
while continuar:

    try:
        vetor = []
        for r in range(5):
            nome = input(f"Digite o {len(vetor) + 1}° nome: ")
            vetor.append(nome)

        mais = []
        for nome in vetor:
            if len(nome) > 5:
                mais.append(nome)

        if len(mais) > 0:
            print(f"Os nomes com mais de 5 letras são: {mais}")
        else:
            print("Não tem nomes com mais de 5 letras.")

        novamente = input("Deseja testar novamente? (SIM/NÃO)").lower()
        if novamente not in ["s","sim",""]:
            print("Fim do programa")
            continuar = False;


    except ValueError:
        print("Digite um nome valido ")
