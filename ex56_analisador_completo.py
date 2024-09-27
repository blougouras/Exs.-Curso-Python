soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
idade_menor_20 = 0

for c in range(1, 5):
    print(f"-------- {c}° Pessoa --------")
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    
    if c == 1 and sexo == "M":
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo == "F" and idade < 20:
        idade_menor_20 += 1

    soma_idade += idade

media_idade = (soma_idade / 4)

print(f"\nA média de idade das 4 pessoas é de {media_idade} anos")
print(f"O homem mais velho tem {maior_idade_homem} anos e tem o nome de {nome_mais_velho}")
print(f"Ao todo são {idade_menor_20} mulheres com menos de 20 anos")