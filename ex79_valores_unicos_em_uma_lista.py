lista = []

while True:
    num = int(input("Digite um valor numérico para adicionar na lista: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso!")
    else:
        print("Valor duplicado, não adicionado na lista")
    
    opcao = str(input("Deseja continuar?: ")).strip().upper()
    if opcao == "N":
        break

print(f"\nVocê digitou os valores: {sorted(lista)}")
