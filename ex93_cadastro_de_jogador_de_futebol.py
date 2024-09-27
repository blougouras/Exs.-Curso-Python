jogador = dict()
gols = []
soma = 0
jogador["Nome"] = str(input("Nome do Jogador: ")).capitalize()
quant = int(input("Quantas partidas ele jogou: "))

for c in range(0, quant):
    gols.append(int(input(f"Quantos gols ele fez na partida {c}? ")))

jogador["Gols"] = gols[:]
jogador["Total de Gols"] = sum(gols)


print("-=" * 40)
print(jogador)
print("-=" * 40)

for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print("-=" * 40)

print(f"O jogador {jogador['Nome']} jogou {quant} partidas")

for i, v in enumerate(jogador["Gols"]):
    print(f"Na partida {i}, ele fez {v} gols")
print(f"Seu total de gols foi {jogador['Total de Gols']}")
print("-=" * 40)
