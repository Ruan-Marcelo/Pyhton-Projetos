def cofre():
    senha = 6969
    tentativas = 0
    programa = True
    
    print("\nCofre digital extremamente seguro")
    
    try:
        while programa:
            print("\nBem vindo ao Cofre, escolha uma opção")
            print("1 - Digitar Senha")
            print("2 - Sair")
            
            opcao = input("\nDigite uma opção (EX: 1): ")
            
            if opcao == "1": 
                tentaiva_senha = int(input("Digite a senha do cofre: "))
                tentativas += 1
                
                if tentaiva_senha == senha:
                    print("\nSenha correta! O cofre abriu. Você agora tem acesso aos arquivos da empresa AngolaTech")
                    programa = False 
                else:
                    print("\nSenha inválida!")
            
            elif opcao == "2":
                print(f"\nAcesso negado! Número de tentativas: {tentativas}")
                programa = False
            else:
                print("\nOpção inválida, digite novamente")
                
    except ValueError:
        print("\nErro: Digite apenas números para a senha.")

cofre()