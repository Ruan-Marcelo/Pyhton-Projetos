# -------------------------------
# login
# -------------------------------

usuario_correto = "admin"
senha_correta = "1234"

tentativas = 0
acesso_liberado = False

while tentativas < 3:
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo ao sistema!")
        acesso_liberado = True
        break
    else:
        print("Usuário ou senha inválidos")
        tentativas += 1

if not acesso_liberado:
    print("Número máximo de tentativas excedido.")
    exit()

# -------------------------------
# usu
# -------------------------------

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
saldo = float(input("Digite seu saldo bancário: "))

# -------------------------------
# validar idade
# -------------------------------

if idade >= 18:
    print("Acesso permitido ao sistema de compras")
else:
    print("Acesso negado. Menor de idade")
    exit()

# -------------------------------
# ver produtos
# -------------------------------

produtos = ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"]

print("\nProdutos disponíveis:")

for produto in produtos:
    print("-", produto)

# -------------------------------
# produto
# -------------------------------

escolha = input("\nDigite o nome do produto que deseja comprar: ")

# Simulação de preço
if escolha.lower() == "notebook":
    valor = 3000
elif escolha.lower() == "mouse":
    valor = 100
elif escolha.lower() == "teclado":
    valor = 150
elif escolha.lower() == "monitor":
    valor = 1200
elif escolha.lower() == "headset":
    valor = 200
else:
    print("Produto inválido")
    exit()

print(f"Valor do produto: R$ {valor}")

# -------------------------------
# ver saldo 
# -------------------------------

saldo_usuario = float(input("Digite o saldo do cartão: "))

if saldo_usuario >= valor:
    print("Compra aprovada com sucesso!")
else:
    print("Saldo insuficiente para esta compra")