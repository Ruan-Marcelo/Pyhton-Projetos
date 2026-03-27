try:
    while True:
        try:
            qtdAlunos = int(input("Informe a quantidade de alunos: "))
            if qtdAlunos <= 0:
                print("A quantidade de alunos deve ser maior que zero.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

    notas = []
    for i in range(qtdAlunos):
        while True:
            try:
                nota = float(input(f"Digite a nota do aluno {len(notas) + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    media = sum(notas) / qtdAlunos
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    aprovados = 0
    reprovados = 0
    
    for nota in notas:
        if nota >= 6:
            aprovados += 1
        else:
            reprovados += 1

    print(f"Quantidade de alunos: {qtdAlunos}")
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Alunos aprovados: {aprovados}")
    print(f"Alunos reprovados: {reprovados}")

except ValueError:
    print("Digite um valor valido")
except ZeroDivisionError:
    print("Erro: Não é possível calcular a média de zero alunos.")