from math import cos, sin, tan, radians

angulo = float(input("Insira um ângulo para saber seu seno, cosseno e tangente: "))

conversao_angulo_radiano = radians(angulo)
seno = sin(conversao_angulo_radiano)
cosseno = cos(conversao_angulo_radiano)
tangente = tan(conversao_angulo_radiano)

print(f"O ângulo escolhido de valor {angulo}°, tem como seu seno {seno:.2f}, cosseno {cosseno:.2f} e tangente {tangente:.2f}")