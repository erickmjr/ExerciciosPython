import math
angulo = float(input("Digite o valor de um ângulo qualquer:"))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(f'Valor do ângulo: {angulo}')
print('-'*35)
print(f'Seno: {seno:.2f}')
print(f'Cosseno: {cosseno:.2f}')
print(f'Tangente: {tangente:.2f}')
print('-'*35)