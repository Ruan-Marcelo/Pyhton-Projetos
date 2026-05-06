try:
    nome = input("Nome do Motoboy: ")
    ganhos = []
    for i in range(7):
        valor = float(input(f"Valor dia {i+1}: "))
        ganhos.append(valor)

    total_dias = len(ganhos)
    media = sum(ganhos) / total_dias
    
    dias_acima_media = 0
    dias_acima_100 = 0
    dias_abaixo_70 = 0

    for r in ganhos:
        if r > media:
            dias_acima_media += 1
        if r > 100:
            dias_acima_100 += 1
        if r < 70:
            dias_abaixo_70 += 1

    percentual_100 = (dias_acima_100 / total_dias) * 100
    top_3 = sorted(ganhos, reverse=True)[:3]

    print(nome)
    print(f"Media semananl de ganhos: R$ {media:.2f}")
    print(f"Maior ganho: R$ {max(ganhos):.2f}")
    print(f"Menor ganho: R$ {min(ganhos):.2f}")
    print(f"Dias acima da média: {dias_acima_media}")
    print(f"Dias abaixo de 70: {dias_abaixo_70}")
    print(f"Percentual acima de 100: {percentual_100:.1f}%")
    print(f"Top 3 valores: {top_3}")

    print("--- CLASSIFICAÇÃO DE DESEMPENHO---")
    for r in ganhos:
        if r < 70:
            status = "Ruim"
        elif r <= 120:
            status = "Bom"
        else:
            status = "Excelente"
        print(f"R$ {r:.2f} - {status}")

except ValueError:
    print("Erro: Digite apenas números.")
finally:
    print("\nOperação finalizada.")