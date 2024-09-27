time = list()
jogador = dict()
gols = []
soma = 0

while True:
    jogador.clear()
    jogador["Nome"] = str(input("Nome do Jogador: ")).capitalize()
    quant = int(input("Quantas partidas ele jogou: "))
    gols.clear()

    for c in range(0, quant):
        gols.append(int(input(f"Quantos gols ele fez na partida {c+1}? ")))

    jogador["Gols"] = gols[:]
    jogador["Total de Gols"] = sum(gols)
    time.append(jogador.copy())
    
    while True:
        opcao = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if opcao in "SN":
            break
        print("ERRO! Escreva seu sexo novamente.")
    if opcao == "N":
        break

print("-=" * 40)
print("Cod. ", end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()

print("-=" * 40)
for k, v in enumerate(time):
    print(f"{k:>3} ", end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-=" * 40)

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para finalizar programa) "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f"ERRO! Não existe um jogador com esse código {busca}")
    else:
        print(f" --- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: --- ")
        for i, g in enumerate(time[busca]["Gols"]):
            print(f"No jogo {i+1} ele fez {g} gols.")
    print("-=" * 40)
print("<<< Volte Sempre!!! >>>")