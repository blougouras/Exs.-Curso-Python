valor_1 = int(input("Primeiro valor: "))
valor_2 = int(input("Segundo valor: "))

programa = True

while programa == True:
    print("""[1.] somar
[2.] multiplicar
[3.] maior
[4.] novos números
[5.] sair do programa
""")
    opcao = int(input(">>>>> Qual é a sua opção: "))
    if opcao == 1:
        soma = (valor_1 + valor_2)
        print(f"A soma entre os 2 valores é de {soma}")
    elif opcao == 2:
        mult = (valor_1 * valor_2)
        print(f"A multiplicação entre os 2 valores é de {mult}")
    elif opcao == 3:
        maior = 0
        if valor_1 > valor_2:
            maior = valor_1
            print(f"O maior valor entre eles é {valor_1}")
        else:
            maior = valor_2
            print(f"O maior valor entre eles é {valor_2}")
    elif opcao == 4:
        valor_1 = int(input("Primeiro valor: "))
        valor_2 = int(input("Segundo valor: "))
    elif opcao == 5:
        programa = False
    else:
        print("Opção Inválida. Tente novamente")

print("Acabou")