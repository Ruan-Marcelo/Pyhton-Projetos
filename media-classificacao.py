notas = []
while len(notas) < 6:
    try:       
        for r in range(6):
            nota = float(input(f"Digite sua nota: "))
            notas.append(nota)
            soma = sum(notas)
            media = soma/len(notas)

            acima = 0
            abaixo = 0

            for n in notas:
                if n > media:
                    acima += 1
                else:
                    abaixo += 1

        print(f"Média: {media:.2f}");
        print(f"Acima da média: {acima}");
        print(f"Abaixo da média: {media:.2f}");   
   
    except ValueError:
            print("Por favor, digite um número válido ou apenas numeros");
           