lista = ("Lápis", 1,
         "Caderno", 15.9,
         "Compasso", 20,
         "Mochila", 123.8,
         "Régua", 8.9)

print("-" * 40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-" * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end='')
    else:
        print(f"R${lista[pos]:>7.2f}")
print("-" * 40)
