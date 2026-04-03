vendas = []
continuar = True
try:
    while continuar:
        for i in range(7):
            valor = float(input(f"Digite o valor da venda do dia {i+1}: "))
            vendas.append(valor)

        media = sum(vendas) / len(vendas)

        maior = max(vendas)
        menor = min(vendas)

        acima_da_media = 0
        for v in vendas:
            if v > media:
                acima_da_media += 1

        qtd_acima = acima_da_media
        porcentagem_acima = (qtd_acima / 7) * 100

        abaixo_100 = 0
        for v in vendas:
            if v < 100:
                abaixo_100 += 1

        print("===========================================================")
        print(f"Média Semanal: R$ {media:.2f}")
        print(f"Maior valor: R$ {maior:.2f} | Menor valor: R$ {menor:.2f}")
        print(f"Dias acima da média: {qtd_acima} ({porcentagem_acima:.1f}%)")
        print(f"Dias com vendas abaixo de R$ 100: {abaixo_100}")
         
        print("============================================================")
        print("==========================Ranked============================")
        ranking = sorted(vendas, reverse=True)[:5]
        print(ranking)

        print("--- Classificação Diária ---")
        for i, valor in enumerate(vendas, 1):
            if valor < 100:
                status = "Baixo"
            elif valor <= 300:
                status = "entre"
            else:
                status = "acima"
            print(f"Dia {i}: R$ {valor:.2f} [{status}]")

        rodar = input("Deseja continuar no programa? ").lower()
        if rodar in ["não", "n", "nao"]:
           continuar = False
        


except ValueError:
    print("Numero invalido")