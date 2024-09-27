matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = maior = scol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}], [{c}]: "))

print("=" * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]}]", end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print("=" * 15)

print(f"A soma de todos os valores pares da matriz é {soma}")

for l in range(0, 3):
    scol += matriz[l][2]
print(f"A soma dos valores na 3° coluna é {scol}")

for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior elemento da 2° linha é {maior}")
