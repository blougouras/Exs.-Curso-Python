frase = str(input("Digite uma frase: ")).strip().upper()

print(f"A letra A aparece {frase.count("A")} vezes na frase")
print(f"A primeira letra A aparece na {frase.find("A")+1}° posição")
print(f"A ultima letra A aparece na {frase.rfind("A")+1}° posição")