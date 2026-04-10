minutos = []
continuar = True
try:
    while continuar:
        for i in range(7):
            tempo = float(input(f"Digite em minutos seu tempo de tela na Netflix no dia {i+1}: "))
            minutos.append(tempo)

        media = sum(minutos) / len(minutos)

        maior = max(minutos)
        menor = min(minutos)

        acima_da_media = 0
        for v in minutos:
            if v > media:
                acima_da_media += 1

        qtd_acima = acima_da_media
        porcentagem_acima = (qtd_acima / 7) * 100

        abaixo_30  = 0
        for v in minutos:
            if v < 30 :
                abaixo_30  += 1

        print("===========================================================")
        print(f"Média Semanal de minutos assistidos:{media:.2f}")
        print(f"Maior tempo de tela: {maior:.2f} | Menor tempo:  {menor:.2f}")
        print(f"Dias acima da média: {qtd_acima} ({porcentagem_acima:.1f}%)")
        print(f"Dias com minutos abaixo de 30: {abaixo_30}")
         
        print("============================================================")
        print("==========================Ranked============================")
        ranking = sorted(minutos, reverse=True)[:5]
        print(ranking)

        print("--- Classificação Diária ---")
        for i, tempoDeTela in enumerate(minutos, 1):
            if tempoDeTela < 60:
                status = "Baixo"
            elif tempoDeTela <= 120:
                status = "Regular  "
            else:
                status = "Intenso"
            print(f"Dia {i}: {tempoDeTela:.2f} [{status}]")

        rodar = input("Deseja continuar no programa? ").lower()
        if rodar in ["não", "n", "nao"]:
           continuar = False
        


except ValueError:
    print("Numero invalido")