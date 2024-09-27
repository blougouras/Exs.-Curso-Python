velocidade = float(input("Insira a sua velocidade em Km/h: "))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f"Sua velocidade foi de {velocidade}Km/h, você deve pagar uma multa de: R${multa:.2f}")
else:
    print("Velocidade Permitida")