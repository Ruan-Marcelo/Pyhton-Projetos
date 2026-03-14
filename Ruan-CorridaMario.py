import random

def jogo_mario():
    pontos = 0
    moedas = 0
    vidas = 3
    derrotados = 0
    jogando = True
    
    print("Corrida do Mario em Python ")
    
    try:
        while jogando:
            print(f"\n--- status de jogo: {moedas} Moedas ||||  {vidas} Vidas --- {pontos} Pontos")
            print("Opções de jogo?")
            print("1. Pular")
            print("2. Pegar Moeda")
            print("3. Atacar Inimigo")
            print("4. Sair do Jogo")
            
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                while True:
                    tipoPulo = random.choice(["Pulo Triplo", "Pulo Duplo","Pulo Simples"])
                    print(f"\n Você deu um {tipoPulo}")

                    if tipoPulo == "Pulo Triplo":
                        pontos += 3
                        break
                    elif tipoPulo == "Pulo Duplo":
                        pontos += 2
                        break
                    else:
                        pontos += 0
                        break

            elif escolha == "2":
                ganho = random.randint(1, 50)
                moedas += ganho
                print(f"\n Você pegou {moedas}")
                
            elif escolha == "3":
                inimigo = random.choice(["Goomba", "Wart", "Bowser"])
                sucesso = random.choice([True, False])
                
                print(f"\n O {inimigo} apareceu!")
                while True:
                    if sucesso:
                        derrotados += 1
                        print(f"Você conseguiu derrotar {inimigo}, Parabéns!")
                        break
                    else:
                        vidas -= 1
                        print(f"O {inimigo} te acertou -1 vida")
                        break
                
            elif escolha == "4":
                print(f"\nPontuação final: {moedas} moedas, inimigos derrotados {derrotados} e {pontos} Pontos")
                jogando = False 
                
            else:
                print("\n Opção inválida! Tente de novo.")


            if vidas == 0:
                print("\n Game over ")
                jogando = False

    except ValueError:
        print("Opção inválida, insira uma opção válida")

jogo_mario()
