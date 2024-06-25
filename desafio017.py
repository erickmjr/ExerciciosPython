from math import hypot
catetoop = float(input("Digite o comprimento do cateto oposto do triângulo retângulo:"))
catetoad = float(input("Digite o comprimento do cateto adjacente do triangulo retângulo:"))
hipotenusa = hypot(catetoop,catetoad)
print(f'Valor do cateto oposto: {catetoop}\nValor do cateto adjacente: {catetoad}\nValor da hipotenusa: {hipotenusa:.2f}')
