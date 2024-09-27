times = ("Corinthians", "Bahia", "São Paulo", "Palmeiras", "Chapecoense", 
         "Botafogo", "Flamengo", "Vasco", "Criciúma", "Atlético-PR", 
         "Atlético-GO", "Fluminense", "Bragantino", "Sport", "Avaí", 
         "Ponte Preta", "Coritiba", "Santos", "Inter", "Grêmio")

print(f"Times do Campeonato Brasileiro: {times}\n")
print(f"Os 5 primeiros: {times[0:5]}\n")

print(f"Os 4 ultimos colocados: {times[16:]}\n")
#print(f"Os 4 ultimos colocados: {times[-4:]}")

print(f"Os times em ordem alfabética: {sorted(times)}\n")
print(f"Posição Chapecoense: {times.index("Chapecoense")}°")
