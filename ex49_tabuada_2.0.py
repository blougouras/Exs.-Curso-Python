numero = int(input('Digite um número para ver sua tabuada: '))

print('-='*7)
print(f'Tabuada do {numero}')
print('-='*7)

for c in range(1, 11):
    print(f"{numero} x {c} = {numero * c}")
