preco = float(input("Preço das compras: R$"))

print("FORMAS DE PAGAMENTO")
print("1. à vista dinheiro/cheque")
print("2. à vista cartão")
print("3. 2x no cartão de crédito")
print("4. 3x ou mais no cartão de crédito")
opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    desconto = preco - (preco * (10/100))
    print(f"O valor da compra com o desconto de pagar a vista no dinehro/cheque ficou de R${desconto:.2f}")
elif opcao == 2:
    desconto = preco - (preco * (5/100))
    print(f"O valor da compra com o desconto de pagar a vista no cartão ficou de R${desconto:.2f}")
elif opcao == 3:
    total = preco
    parcelas = preco / 2
    print(f"O total das parcelas ficou 2x de R${parcelas}")
    print(f"O valor total da compra ficou R${total:.2f}")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    juros = preco + (preco * (20/100))
    parcelas_juros = juros / parcelas
    print(f"O valor da compra parcelado em {parcelas}x de R${parcelas_juros:.2f} ficou de R${juros:.2f}")