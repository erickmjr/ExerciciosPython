s = 0
cont = 0
for c in range (1, 500):
   if c%2 != 0 and c%3 == 0:
      s = s+c
      cont = cont +1
      print(f'{c}')
print(f"A soma dos {cont} valores ímpares e múltiplos de 3 é = {s}")

    
