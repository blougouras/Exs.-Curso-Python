print("-="*10)
print("Gerador de PA")
print("-="*10)

primeiro = int(input("\nPrimeiro Termo: "))
razao = int(input("Razão da PA: "))
termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end='')
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais: "))

print(f"Progressão finalizada com {total} termos mostrados")
