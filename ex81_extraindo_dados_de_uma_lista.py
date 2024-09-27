lista = []
cont = 0

while True:
    lista.append(int(input("Digite um valor: ")))
    cont += 1

    opcao = str(input("Deseja continuar? ")).strip().upper()
    if opcao == "N":
        break

print(f"\nForam digitados {cont} números na lista")

lista.sort(reverse=True)
print(f"Os valores em ordem decrescente são {lista}")

if 5 in lista:
    print("O número 5 foi digitado na lista")
else:
    print("O número 5 não foi encontrado")
