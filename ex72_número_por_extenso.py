num_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez"
               , "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito"
               , "dezenove", "vinte")

while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    
    if numero >= 0 and numero <= 20:
        break
    print("Tente novamente. ", end='')

print(f"Você digitou o numero {num_extenso[numero]}")
