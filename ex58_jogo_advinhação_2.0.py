from random import randint
num = randint(0, 10)

print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10
Consegue pensar qual foi?    
    """)

guess = -1
attempts = 0

while guess != num:
    guess = int(input("Qual é o seu palpite: "))
    if guess > num:
        print("Menos... Tente mais uma vez")
    if guess < num:
        print("Mais... Tente mais um vez")
    attempts += 1

print(f"Acertou com {attempts} tentativas. Parabéns!")