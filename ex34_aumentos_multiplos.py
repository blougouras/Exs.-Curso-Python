salario = float(input("Qual é o salário do funcionário: R$ "))

if salario > 1250.00:
    aumento = salario + ( salario * 0.10 )
    print(f"Quem ganhava R${salario:.2f}, deve receber R${aumento:.2f}")
else:
    aumento = salario + ( salario * 0.15 )
    print(f"Quem ganhava R${salario:.2f}, deve receber R${aumento:.2f}")