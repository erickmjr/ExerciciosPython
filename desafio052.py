num = int(input('Digite um número inteiro qualquer: '))
totalDiv = 0
for c in range(num, 0, -1):
    if num%c == 0:
      totalDiv += 1
if totalDiv == 2 or totalDiv == 1:
   print(f'O número foi divido {totalDiv} vez(es), portanto ele é primo.')
else:
   print(f'O número foi divido {totalDiv} vezes, portanto ele NÃO é primo.')