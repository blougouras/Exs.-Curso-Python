from random import randint

v = 0
while True:
    valor = int(input("Diga um valor: "))
    computador = randint(0, 11)
    total = (computador + valor)
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input("Par ou Impar? ")).strip().upper()[0]

    if tipo == "P":
        if total % 2 == 0:
            print("Você GANHOU")
            v += 1
        else:
            print("Você PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print ("Você GANHOU")
            v += 1
        else:
            print("Você PERDEU")
            break 
    print(f"Você jogou {valor} e o computador jogou {computador}. Total de {total}")

print(f"Seu total de vitórias foi {v}")
