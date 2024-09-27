medida = float(input("Insira a medida em metros: "))

cm = (medida * 100)
mm = (medida * 1000)

print(f"O valor escolhido foi {medida} metros, foi convertido para {cm:.0f} centímetros e {mm:.0f} milímetros")