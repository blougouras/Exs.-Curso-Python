valor_casa = float(input("Insira o valor da casa: R$"))
salario = float(input("Insira o seu salário: R$"))
anos = float(input("Em quanto tempo (anos) você deseja pagar a casa: "))

prest_mensal = valor_casa / (anos * 12)
minimo = salario * (30/100)

if prest_mensal >= minimo:
    print(f"Empréstimo NEGADO.")
elif prest_mensal <= minimo:
    print(f"Empréstimo APROVADO!!!!")