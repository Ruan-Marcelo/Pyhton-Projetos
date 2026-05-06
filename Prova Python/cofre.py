def cofre():
    senha = 123
    
    print("Cofre digital")
    
    try:
        while True:
            print("Bem vindo ao Cofre, escolha uma opção")
            print("1 - Digitar Senha")
            print("2 - Sair")
            
            opcao = input("Digite uma opção (EX: 1): ")
            
            if opcao == "1": 
                tentaiva_senha = int(input("Digite a senha do cofre: "))
                
                if tentaiva_senha == senha:
                    print("Senha correta! O cofre abriu.")
                    break
                else:
                    print("Senha inválida!")
            
            elif opcao == "2":
                print(f"Acesso negado!")
                break
            else:
                print("Opção inválida, digite novamente")
                
    except ValueError:
        print("Erro: Digite apenas números para a senha.")

cofre()