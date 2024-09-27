dias = int(input("Por quantos dias você alugou o carro: "))
km = float(input("Quantos Km você rodou com o carro: "))

diaria = (60 * dias)
km_rodado = (km * 0.15)

preco_pagar = (diaria + km_rodado)

print(f"O alguel do carro ficou no total de R$ {preco_pagar:.2f}")