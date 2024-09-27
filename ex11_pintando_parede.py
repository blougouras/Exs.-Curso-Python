largura = float(input("Insira a largura da sua parede em metros: "))
altura = float(input("Insira a altura da sua parede em metros: "))

area = (altura * largura)

litro_tinta = (area/2)

print(f"Para uma parede de {area} m², serão necessários {litro_tinta} Litros.")