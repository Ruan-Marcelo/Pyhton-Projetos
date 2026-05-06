try:
    numeros = []
    while True:
        print("1 - Cadastrar número")
        print("2 - Listar números")
        print("3 - Mostrar soma")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            num = int(input("Digite um número: "))
            numeros.append(num)

        elif opcao == "2":
            print(numeros)

        elif opcao == "3":
            print("Soma:", sum(numeros))

        elif opcao == "4":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida")
except ValueError:
    print("Entrada inválida. Por favor, digite um número.")
finally:
    print("O programa foi finalizado com sucesso")