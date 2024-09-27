salario = float(input("Insira o valor do seu salário atual: "))

aumento = (salario * (15/100))
reajuste_salario = (salario + aumento)

print(f"O seu salário teve um reajuste de 15%, agora o novo valor é de R$ {reajuste_salario:.2f}")