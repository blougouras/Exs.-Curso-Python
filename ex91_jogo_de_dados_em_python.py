from random import randint
from time import sleep
from operator import itemgetter

ranking = list()
jogo = {"Jogador 1": randint(1,6),
        "Jogador 2": randint(1,6),
        "Jogador 3": randint(1,6),
        "Jogador 4": randint(1,6)}

sleep(1)
print("Valores Sorteados: ")
sleep(1)

for k, v in jogo.items():
    print(f"{k} tirou o valor {v} no dado")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("\n")

print("=" * 20)
print(f"{"RANKING GERAL":^20}")
print("=" * 20)
sleep(1)

print("\n")

for i, v in enumerate(ranking):
    print(f"{i+1}° Lugar: {v[0]} que tirou no dado o valor {v[1]}")
    sleep(1)
