from random import randint
itens = ("Pedra", "Papel", "Tesoura")   
computador = randint(0,2)

print('''SUAS OPÇÕES:
0. Pedra
1. Papel
2. Tesoura''')
opcao = int(input("Qual a sua jogada? "))

print("-=" * 11)
print(f"O computador escolheu: {itens[computador]}")
print(f"O jogador escolheu: {itens[opcao]}")
print("-=" * 11)

if computador == 0: # pedra
    if opcao == 0:
        print("EMPATE")
    elif opcao == 1:
        print("Jogador GANHOU")
    elif opcao == 2:
        print("Computador GANHOU")
elif computador == 1: # papel
    if opcao == 0:
        print("Computador GANHOU")
    elif opcao == 1:
        print("EMPATE")
    elif opcao == 2:
        print("Jogador GANHOU")
elif computador == 2: # tesoura
    if opcao == 0:
        print("Jogador GANHOU")
    elif opcao == 1:
        print("Computador GANHOU")
    elif opcao == 2:
        print("EMPATE")
