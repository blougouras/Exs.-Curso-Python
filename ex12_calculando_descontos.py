valor_produto = float(input("Insira o valor do produto desejado: "))

desconto = (valor_produto * (5/100))
novo_valor_produto = (valor_produto - desconto)

print(f"O produto que tinha o valor de R$ {valor_produto}, com o desconto de 5% ficará com o novo valor de R$ {novo_valor_produto}.")