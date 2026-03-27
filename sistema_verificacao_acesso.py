# Sistema de Verificação de Acesso
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    resultado = "Acesso permitido"
else:
    resultado = "Acesso negado"

print("\n--- Resultado da Verificação ---")
print("Nome:", nome)
print("Idade:", idade)
print("Status:", resultado)
