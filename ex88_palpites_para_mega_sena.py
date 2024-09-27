from random import randint
from time import sleep

print("-" * 40)
print(f"{"JOGA NA MEGA SENA":^40}")
print("-" * 40)

lista = []
jogos = []
total = 1
quant = int(input("Quantos jogos você quer fazer: "))

while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print("\n", "-=" * 3, f"SORTEANDO {quant} JOGOS", "-=" * 3)
sleep(1)

for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
