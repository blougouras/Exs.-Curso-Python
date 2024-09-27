from math import sqrt, hypot
cateto_op = float(input("Insira o valor do cateto oposto: "))
cateto_adj = float(input("Insira o valor do cateto adjascente: "))

# hipotenusa = hypot(cateto_op, cateto_adj)
hipotenusa = sqrt((cateto_op ** 2)+(cateto_adj ** 2))

print(f"O triângulo com os valores dos catetos de {cateto_op} e {cateto_adj} tem o valor da hipotenusa de {hipotenusa:.2f}")