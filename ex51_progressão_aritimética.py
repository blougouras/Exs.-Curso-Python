termo = int(input("Digite o Primeiro Termo: "))
razao = int(input("Digite a razão da PA: "))
decimo = termo + (10 - 1) * razao

for c in range(termo, decimo + razao, razao):
    print(c, end= ' -> ')

print("ACABOU")