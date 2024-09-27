import random

numero = int(input("Digite um número entre 0 e 5: "))

num = random.randint(0,5)

if numero == num:
    print("--- !!!PARABÉNS, Você Venceu!!! ---")
else:
    print("--- O computador ganhou e Você PERDEU!!! ---")