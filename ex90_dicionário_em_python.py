aluno = dict()

aluno["Nome"] = str(input("Nome: ")).capitalize()
media = float(input(f"Média de {aluno["Nome"]}: "))
aluno["Média"] = media

if media >= 7:
    aluno["Situação"] = "Aprovado"
elif media >= 5 and media < 7:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"

for k, v in aluno.items():
    print(f"{k} é igual a {v}")
