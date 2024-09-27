from datetime import datetime

dados = dict()

dados["Nome"] = str(input("Nome: ")).capitalize()
nasc = int(input("Ano de nascimento: "))
dados["Idade"] = datetime.now().year - nasc
dados["CTPS"] = int(input("Carteira de Trabalho ( Digite 0 caso não tenha ): "))

if dados["CTPS"] != 0:
    dados["Contratação"] = int(input("Ano de contratação: "))
    dados["Salário"] = float(input("Salário: R$ "))
    dados["Aposentadoria"] = dados["Idade"] + ((dados["Contratação"] + 35) - datetime.now().year)

print("-=" * 30)

for k, v in dados.items():
    print(f"- {k} tem o valor de {v}")
