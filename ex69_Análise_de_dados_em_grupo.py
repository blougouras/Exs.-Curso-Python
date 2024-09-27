quant_homem = quant_maior_18 = quant_fem_menor_20 = 0 

while True:
    print("="*20)
    print("CADASTRE UMA PESSOA")
    print("="*20) 
    
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    opcao = str(input("Quer continuar [S/N]: ")).strip().upper()[0]

    if idade >= 18:
        quant_maior_18 += 1
    if sexo == "M":
        quant_homem += 1
    if sexo == "F" and idade < 20:
        quant_fem_menor_20 += 1

    if opcao == "N":
        print(f"Total de pessoas com mais de 18 anos: {quant_maior_18}")
        print(f"Ao todo temos {quant_homem} homens cadastrados")
        print(f"E temos {quant_fem_menor_20} mulheres menores de 20 anos")
        break
