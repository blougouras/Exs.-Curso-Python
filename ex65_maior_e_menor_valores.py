quant = media = soma = maior = menor = 0
continuar = "S"

while continuar in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input("Quer continuar [S/N]: ")).strip().upper()[0]

media = soma / quant

print(f"Você digitou {quant} números e a média foi {media}")
print(f"O maior número digitado foi {maior} e o menor foi {menor}")
