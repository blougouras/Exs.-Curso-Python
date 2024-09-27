from random import shuffle

a1 = str(input("Digite o nome de 1 aluno: "))
a2 = str(input("Digite o nome de 1 aluno: "))
a3 = str(input("Digite o nome de 1 aluno: "))
a4 = str(input("Digite o nome de 1 aluno: "))

alunos = [a1, a2, a3, a4]

shuffle(alunos)

print("A ordem de apresentação será:")
print(alunos)