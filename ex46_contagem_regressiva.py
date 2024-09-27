from time import sleep
print("Contagem regressiva para os fogos!!")
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print("BOOM!!!")