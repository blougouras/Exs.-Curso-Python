print("="*20)
print("LOJAS SUPER BARATÃO")
print("="*20)

total_compra = total_1000 = menor = cont = 0
barato = ' '

while True:
    nome = str(input("Nome do Produto: ")).capitalize()
    preco = float(input("Preço: R$ "))
    cont += 1
    total_compra += preco
    opcao = ' '
    
    while opcao not in "SN":
        opcao = str(input("Quer continuar [S/N]: ")).strip().upper()[0]

    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            barato = nome

    if preco > 1000:
        total_1000 += 1
        
    if opcao == "N":
        break

print(f"-"* 40, "FIM DO PROGRAMA", "-"*40)
print(f"O total da compra foi de R$ {total_compra:.2f}")
print(f"Teve um total de {total_1000} produtos que custaram mais de R$ 1000,00")
print(f"O produto mais barato foi a {barato} e seu preço foi de R$ {menor:.2f}")
