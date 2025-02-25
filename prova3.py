
numero_secreto = 7
palpite = None
tentativas = 3

while tentativas > 0:
    palpite = int(input("Informe um palpite para o número secreto: "))
    tentativas=tentativas-1 
    if palpite == numero_secreto:
        print ("Parabens acertou o numero secreto")
        break
    else:
        print("Voce errou.Escolha novamente, você vai conseguir!!  :")
if tentativas == 0:
    print(f"Suas tentativas acabaram.  O número secreto era {numero_secreto}!!")



    