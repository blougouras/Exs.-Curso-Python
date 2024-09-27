from time import sleep
boletim = []

while True:
    nome = str(input("Nome: ")).capitalize()
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2) / 2
    boletim.append([nome, [nota_1, nota_2], media])

    opcao = str(input("Quer continuar? [S/N] ")).strip().upper()
    if opcao == "N":
        break

print("-=" * 13)
print(f"{"No.":<4}{"NOME":<10}{"MÉDIA":>8}")
print("-" * 26)

for i, a in enumerate(boletim):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")

while True:
    sleep(1)
    opc = int(input("\nMostrar notas de qual aluno? (999 para finalizar programa): "))
    sleep(1)
    if opc == 999:
        print("FINALIZANDO")
        break
    if opc <= len(boletim) - 1:
        print(f"\nNotas de {boletim[opc][0]} são {boletim[opc][1]}")
print("\n<<< VOLTE SEMPRE >>>")
