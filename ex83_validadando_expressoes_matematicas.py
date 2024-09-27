expressao = str(input("Digite a sua expressão: "))
expressões = []

for valor in expressao:
    if valor == '(':
        expressões.append('(')
    elif valor == ')':
        if len(expressões) > 0:    
            expressões.pop()
        else: 
            expressões.append(')')
            break

if len(expressões) == 0:
    print("Sua expressão está válida")
else:
    print("Sua expressão está inválida")
