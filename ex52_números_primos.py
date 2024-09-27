numero = int(input("Digite um número: "))
total = 0

for c in range(1, numero+1):
    if numero % c == 0:
        total += 1
        print('\033[33m', end= '')
    else:
        print('\033[31m', end= '')
    print(f'{c}', end=' ')

print(f"\n\033[mO número {numero} foi divisível {total} vezes")

if total == 2:
    print("O número ele é PRIMO")
else:
    print("o número NÃO É PRIMO")