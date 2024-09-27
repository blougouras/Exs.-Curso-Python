nome = str(input("Insira seu nome completo: ")).strip()
n = nome.split()

print(f"Muito prazer em te conhecer {nome}!!")
print(f"Seu primeiro nome é: {n[0]}")

# 2 jeitos de achar o ultimo nome:
#print(f"Seu ultimo nome é: {n[len(nome)]-1}")
print(f"Seu ultimo nome é: {n[-1]}")