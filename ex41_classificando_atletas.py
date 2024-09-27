from datetime import date

ano_nasc = int(input("Insira o ano de nascimento: "))

ano_atual = date.today().year
idade = (ano_atual - ano_nasc)

if idade <= 9:
    print(f"O nadador tem {idade} anos e está na classificação MIRIM")
elif idade <= 14:
    print(f"O nadador tem {idade} anos e está na classificação INFANTIL")
elif idade <= 19:
    print(f"O nadador tem {idade} anos e está na classificação JUNIOR")
elif idade <= 25:
    print(f"O nadador tem {idade} anos e está na classificação SÊNIOR")
else:
    print(f"O nadador tem {idade} anos e está na classificação MASTER")