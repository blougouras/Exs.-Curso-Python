from datetime import date
atual = date.today().year
cont_maioridade = 0
cont_menoridade = 0

for c in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da {c}° pessoa: "))
    idade = (atual - nasc)

    if idade >= 21:
        cont_maioridade += 1
    else:
        cont_menoridade += 1

print(f"Ao todo temos {cont_maioridade} pessoas maiores de idade")
print(f"E também tivemos {cont_menoridade} pessoas menores de idade")