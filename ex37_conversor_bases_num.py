numero = int(input("Digite um valor a ser convertido: "))

print("1. Converter para a Base BINÁRIA")
print("2. Converter para a Base OCTAL")
print("3. Converter para a Base HEXADECIMAL")
opcao = int(input("Insira a opção de conversão numérica desejada: "))

if opcao == 1:
    print(f"O número {numero} convertido para binário fica: {bin(numero)[2:]}")
elif opcao == 2:
    print(f"O número {numero} convertido para binário fica: {oct(numero)[2:]}")
elif opcao == 3:
    print(f"O número {numero} convertido para binário fica: {hex(numero)[2:]}")
else:
    print(f"Opção Inválida, Tente Novamente")