numero = int(input("Insira um número entre 0 à 9999: "))

u = (numero // 1) % 10
d = (numero // 10) % 10
c = (numero // 100) % 10
m = (numero // 1000) % 10

print(f"Analisando o número {numero}...")

print(f"Milhar: {m}")
print(f"Centena: {c}")
print(f"Dezena: {d}")
print(f"Unidade: {u}")