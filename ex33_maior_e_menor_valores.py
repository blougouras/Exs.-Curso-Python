valor_1 = int(input("Digite o valor 1: "))
valor_2 = int(input("Digite o valor 2: "))
valor_3 = int(input("Digite o valor 3: "))

menor_valor = valor_1

if valor_2 < valor_1 and valor_2 < valor_3:
    menor_valor = valor_2
if valor_3 < valor_2 and valor_3 < valor_1:
    menor_valor = valor_3

maior_valor = valor_1

if valor_2 > valor_1 and valor_2 > valor_3:
    maior_valor = valor_2
if valor_3 > valor_1 and valor_3 > valor_2:
    maior_valor = valor_3

print(f"O menor valor digitado foi: {menor_valor}")
print(F"O maior valor digitado foi: {maior_valor}")
