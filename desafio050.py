s = 0
for c in range(0, 6):
    n = int(input('DIGITE UM NÚMERO INTEIRO QUALQUER: '))
    if n%2 == 0:
        s += n
print(f'SOMA DOS VALORES PARES: {s}')