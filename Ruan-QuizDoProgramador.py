print("\n Quiz do Progamador")
print("\n Regras do jogo")
print("\n Você tera 5 perguntas com 3 alternativas cada e ao final vou revalar sua classificação como Desenvolvedor")
print("\n ------------------------")
print("\n 5/5 Mestre Python")
print("\n 3-4/5 Programador Intermediário")
print("\n 0-2/5 Aprendiz")

def quiz_Programador():
    pontos = 0
    participando = True

    try:
        while participando:
            print("\n 1. Qual das alternativas abaixo representa uma linguagem de marcação e NÃO uma linguagem de programação?")
            print("\na) Python")
            print("\nb) JavaScript")
            print("\nc) HTML")
            resposta = input("\nSua resposta aqui (Exemplo de resposta: a) Python: ")
            if resposta == "c) HTML":
                pontos += 1
            else:
                pontos += 0

            print("\n2. O que significa depurar (debugar) um programa?")
            print("\na) Torná-lo mais rápido")
            print("\nb) Corrigir erros no código")
            print("\nc) Apagar o programa")
            resposta = input("\nSua resposta aqui (Exemplo de resposta: a) Torná-lo mais rápido: ")
            if resposta == "b) Corrigir erros no código":
                pontos += 1
            else:
                pontos += 0

            print("\n3. Qual é o operador utilizado para comparação estrita (verifica valor e tipo) em JavaScript?")
            print("\na) =")
            print("\nb) ==")
            print("\nc) ===")
            resposta = input("\nSua resposta aqui (Exemplo de resposta: a) =: ")
            if resposta == "c) ===":
                pontos += 1
            else:
                pontos += 0

            print("\n4. Em lógica de programação, qual operador é usado para verificar se duas condições são verdadeiras simultaneamente?")
            print("\na) OR (||)")
            print("\nb) NOT (!)")
            print("\nc) AND (&&)")
            resposta = input("\nSua resposta aqui (Exemplo de resposta: a) OR (||): ")
            if resposta == "c) AND (&&)":
                pontos += 1
            else:
                pontos += 0

            print("\n5. Qual é a principal vantagem de usar Git?")
            print("\na) Aumentar a velocidade da internet")
            print("\nb) Controlar versões do código-fonte")
            print("\nc) Criar gráficos 3D")
            resposta = input("\nSua resposta aqui (Exemplo de resposta: a) Aumentar a velocidade da internet: ")
            if resposta == "b) Controlar versões do código-fonte":
                pontos += 1
            else:
                pontos += 0

            participando = False

        print(f"\n--- Pontuação Final: {pontos}/5 ---")
        if pontos == 5: 
            print("Mestre Python! Prabéns")
        elif pontos >= 3: 
            print("Programador Intermediário! Continue assim")
        else: 
            print("Aprendiz! estude mais  ")


    except ValueError:
        print("Ecolha uma opção válida")

quiz_Programador()