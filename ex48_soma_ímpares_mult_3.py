s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c
print(f"A soma dos {cont} valores múltiplos de 3 entre 1 e 500 é: {s}")