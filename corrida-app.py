ganhos = []
try:
    for i in range(7):
        valor = float(input(f"Digite o valor ddos ganhos do dia {i+1}: "))
        ganhos.append(valor)

    total = sum(ganhos)
    qtd_dias = len(ganhos)
    media_semanal = total / qtd_dias

    melhor_dia = max(ganhos)
    pior_dia = min(ganhos)

    dias_acima_media = 0
    for g in ganhos:
        if g > media_semanal:
            dias_acima_media += 1

    dias_abaixo_70 = 0
    for g in ganhos:
        if g < 70:
            dias_abaixo_70 += 1

    dias_lucrativos = 0
    for g in ganhos:
        if g > media_semanal:
            dias_lucrativos += 1

    percentual_lucrativos = (dias_lucrativos / qtd_dias) * 100

    ranking = sorted(ganhos, reverse=True)[:5]

    print(f"--- RELATÓRIO DE GANHOS ---")
    print(f"Média Semanal: R$ {media_semanal:.2f}")
    print(f"Melhor Dia: R$ {melhor_dia:.2f} | Pior Dia: R$ {pior_dia:.2f}")
    print(f"Dias acima da média: {dias_acima_media}")   
    print(f"Percentual de dias lucrativos: {percentual_lucrativos:.1f}%")
    print(f"Top 5 Ganhos: {ranking}")

    print("--- Classificação Diária ---")
    for i, valor in enumerate(ganhos, 1):
        if valor < 70:
            status = "Ruim"
        elif valor <= 120:
            status = "Bom"
        else:
            status = "Excelente"
        print(f"Dia {i}: R$ {valor:.2f} [{status}]")

except ValueError:
    print("Valores invalidos")
except Exception as e:
    print(f"Erro : {e}")
finally:
    print("Finalizando operação.")