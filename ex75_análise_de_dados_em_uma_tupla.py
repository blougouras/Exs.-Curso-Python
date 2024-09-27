num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
num_3 = int(input("Digite mais um número: "))
num_4 = int(input("Digite um último número: "))

numeros = (num_1, num_2, num_3, num_4)

print(f"Você digitou os valores: {numeros}")

print(f"O valor 9 apareceu {numeros.count(9)} vezes")
if 3 in numeros:
    print(f"O valor 3 apareceu na {numeros.index(3)+1}° posição")
else:
    print("O número 3 não foi digitado")

print("Os valores pares digitados foram ", end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
