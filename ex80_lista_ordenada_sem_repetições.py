lista = []

for c in range(0,5):
    n = int(input("Digite um valor: "))
    if n not in lista:
        lista.append(n)

print(f"A lista ordenada e sem repetições: {sorted(lista)}")