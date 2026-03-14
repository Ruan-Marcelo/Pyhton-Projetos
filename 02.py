nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))


media = (nota1 + nota2 + nota3) / 3

print(f"\nA média do aluno é: {media:.2f}")

if media > 6.0:
    print("Status: Aprovado")
elif 4.0 <= media <= 6.0:
    print("Status: Recuperação")
else:
    print("Status: Reprovado")

salario_atual = float(input("Digite o salário atual do colaborador: R$"))
percentual_aumento = float(input("Digite o percentual de aumento (ex: 10 para 10%): "))

valor_aumento = salario_atual * (percentual_aumento / 100)

novo_salario = salario_atual + valor_aumento

print(f"\nSalário atual: R${salario_atual:.2f}")
print(f"Percentual de aumento: {percentual_aumento:.2f}%")
print(f"Valor do aumento: R${valor_aumento:.2f}")
print(f"Novo salário: R${novo_salario:.2f}")

if valor_aumento <= 350.00:
    print("Mensagem: Parabéns pelo seu aumento!")
elif valor_aumento <= 500.00:
    print("Mensagem: Você teve um excelente aumento!")
elif valor_aumento <= 720.00:
    print("Mensagem: Parabéns, você teve um grande aumento!")
else:
    print("Mensagem: Seu aumento foi significativo!")