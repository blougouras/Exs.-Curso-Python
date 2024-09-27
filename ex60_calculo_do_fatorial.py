from math import factorial

num = int(input("Digite um valor para ser calculado seu fatorial: "))
cont = num

print(f"Calculando {num}! = ", end='')
while cont > 0:
    print(f"{cont}", end='')
    print(" x " if cont > 1 else " = ", end='')
    cont -= 1

print(factorial(num), end='')