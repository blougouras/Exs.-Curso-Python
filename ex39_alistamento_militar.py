from datetime import date
ano_atual = date.today().year

ano_nasc = int(input("Insira o ano do seu nascimento: "))

idade = ano_atual - ano_nasc
print(f"Quem nasceu em {ano_nasc} tem {idade} anos no ano de {ano_atual}")

if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!!")
elif idade < 18:
    saldo = ( 18 - idade)
    print(f"Você ainda NÃO tem 18 anos. Ainda faltam {saldo} anos para o alistamento.")
    ano_alist = ( ano_atual + saldo )
    print(f"O ano do seu alistamento será: {ano_alist}")
elif idade > 18:
    saldo = ( idade - 18)
    print(f"Você já passou dos 18 anos! Você deveria ter se alistado há {saldo} ANOS!")
    ano_alist = ( ano_atual - saldo)
    print(f"Você deveria ter se alistado em: {ano_alist}")