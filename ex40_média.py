nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))

media = (nota_1 + nota_2) / 2
print(f"O aluno com as notas {nota_1:.1f} e {nota_2:.1f}, tem a média de {media:.2f}")

if media < 5:
    print("O aluno foi Reprovado")
elif media >= 5 and media < 7:
    print("Aluno em Recuperação")
else:
    print("Aluno Aprovado")