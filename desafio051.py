a1 = int(input('Digite o primeiro termo da Progressão Aritmética (PA): '))
r = int(input('Digite a razão: '))
n = 0
for c in range(1, 11):
    n +=1
    pa = a1 + (n - 1) * r
    print(f'{pa}',end = '-> ')
print('FIM')