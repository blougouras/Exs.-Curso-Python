sexo = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]

while sexo not in "MmFf":
    sexo = str(input("Dados inválidos, insira seu sexo: ")).strip().upper()[0]

print(f"Sexo {sexo} informado com sucesso")
