import random
numero_secreto = random.randrange(1,10)

print("Jogo: Adivinhe o número!")
while True:
  try:
    chute = int(input("Digite um número entre 1 e 10: "))
    if chute == numero_secreto:
        print("Parabens! você acertou o número secreto !!")
        break
    else:
        print("Número errado, Tente novamente!")
  except ValueError:
        print("Por favor, digite um número válido ou apenas texto")

        saldo = 1000

print("Sistema báncario")

while True:
  try:
    print("1- Ver saldo")
    print("2- Depositar")
    print("3- Sacar")
    print("4- Sair")
    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        print(f"Seu saldo atual: R$ {saldo}")
    elif opcao == 2:
        print("Quanto deseja depositar?")
        despositar = int(input("Digite o valor: "))
        saldo += despositar
    elif opcao == 3:
        print("Quanto deseja sacar? ")
        sacar = int(input("Digite o valor: "))
        saldo -= sacar
        if sacar > saldo:
            print("Saldo insuficiente")
    elif opcao == 4:
        print("Você saiu do programa")
        break
    else:
        print("Número inválido, Tente novamente!")

  except ValueError:
        print("Por favor, digite um número válido ou apenas texto")
