distancia = float(input("Qual é a distânia da viagem em KM: "))

if distancia <= 200:
    valor_passagem = (distancia * 0.5)
else:
    valor_passagem = (distancia * 0.45)

print(f"Para uma viagem de {distancia} KM, o valor da passagem fica de R${valor_passagem:.2f}")
