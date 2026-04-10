defeitos = []

continuar = True
try:
    while continuar:
        for i in range(15):
            qtd = int(input(f"Digite a quantidade de peças com defeito no dia {i+1}: "))
            defeitos.append(qtd)

        media = sum(defeitos) / len(defeitos)

        maior = max(defeitos)
        menor = min(defeitos)

        acima_da_media = 0
        for v in defeitos:
            if v > media:
                acima_da_media += 1

        qtd_acima = acima_da_media
        
        aceitavel = 0
        for v in defeitos:
            if v < 10:
                aceitavel += 1
                
        porcentagem_aceitavel = (aceitavel / 15) * 100

        abaixo_3 = 0
        for v in defeitos:
            if v < 3:
                abaixo_3 += 1

        print("===========================================================")
        print(f"Média de defeitos do período: {media:.2f}")
        print(f"Maior número de falhas: {maior} | Menor número: {menor}")
        print(f"Dias acima da média de defeitos: {qtd_acima}")
        print(f"Dias com qualidade aceitável (menos de 10 defeitos): {aceitavel} ({porcentagem_aceitavel:.1f}%)")
        print(f"Dias com menos de 3 defeitos: {abaixo_3}")
         
        print("============================================================")
        print("==========================Ranked============================")
        
        ranking = sorted(defeitos, reverse=True)[:5]
        print(f"Top 5 dias com mais falhas: {ranking}")

        print("--- Classificação do Período ---")
        if media > 15:
            status = "Crítica"
        elif media >= 5: 
            status = "Atenção"
        else:
            status = "Controlada"
        print(f"Qualidade da Produção: [{status}]")

        rodar = input("Deseja continuar no programa? ").lower()
        if rodar in ["não", "n", "nao"]:
           continuar = False
        

except ValueError:
    print("Numero invalido")