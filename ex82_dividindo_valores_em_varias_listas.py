numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input("Digite um valor: ")))
    opcao = str(input("Deseja continuar [S/N]: ")).strip().upper()
    if opcao == "N":
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

numeros.sort()
pares.sort()
impares.sort()

print(f"\nLista completa : {numeros}")
print(f"Lista de pares: {pares}")
print(f"Lista de Ímpares: {impares}")
