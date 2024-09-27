pessoa = dict()
galera = []
soma = media = 9
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: ")).capitalize()

    while True:
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).strip().upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("ERRO! Escreva seu sexo novamente.")

    pessoa["Idade"] = int(input("Idade: "))
    soma += pessoa["Idade"]
    galera.append(pessoa.copy())


    while True:
        opcao = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
        if opcao in "SN":
            break
        print("ERRO! Escolha entre S ou N")
    if opcao == "N":
        break
print("-=" * 30)

print(f"Ao todo temos {len(galera)} pessoas cadastradas")

media = soma / len(galera)
print(f"A média de idade é de {media:.1f} anos")

print("As mulheres cadastradas foram ", end='')

for p in galera:
    if p["Sexo"] == "F":
        print(f"{p["Nome"]}... ", end='')
print()

print("Lista de pessoas acima da média foram ", end='')
for p in galera:
    if p["Idade"] >= media:
        print(f"{p["Nome"]} com {p["Idade"]} anos de idade... ", end='')
print()
