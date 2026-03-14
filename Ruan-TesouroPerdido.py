import random
import webbrowser

numero_secreto = random.randint(1, 5)
tentativas = 5

print("Bem-vindo à Ilha Python!")
print("Tente descobrir o número secreto entre 1 e 50.")

try:
    while tentativas > 0:
        try:
            palpite = int(input("Digite seu palpite: "))

            if palpite == numero_secreto:
                print("Parabéns! Você encontrou o tesouro!")
                webbrowser.open("https://www.youtube.com/shorts/OKRh56WxzQw?feature=share")
                break
            elif palpite > numero_secreto:
                print("O número secreto é menor.")
            else:
                print("O número secreto é maior.")

            tentativas -= 1
            print("Tentativas restantes:", tentativas)

        except:
            print("Digite um valor númerico válido!")

    if tentativas == 0:
        print("seus tentativas acabaram pai")
        print("O número secreto era:", numero_secreto)
except ValueError:
    print("Digite um valor válido e tente novamente")