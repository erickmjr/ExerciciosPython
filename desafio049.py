num1 = int(input('Digite um número inteiro qualquer:'))
print(f'TABUADA DO {num1}:')
for c in range(1, 11):
    mult = c * num1
    print(f'{c} X {num1} = {mult}')
