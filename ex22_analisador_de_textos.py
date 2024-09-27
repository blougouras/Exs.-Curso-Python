nome = str(input("Insira seu nome e sobrenome: ")).strip()


print(f"Nome e Sobrenome em MAIÚSCULO: {nome.upper()}")
print(f"Nome e Sobrenome em minúsculo: {nome.lower()}")
print(f"Seu nome tem ao todo: {len(nome)-nome.count(" ")} letras")
print(f"Seu primero nome tem ao todo: {nome.find(" ")} letras")