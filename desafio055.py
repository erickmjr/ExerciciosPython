lista = [0, 1, 2, 3, 4]
for c in range(0,5):
    peso = float(input('Digite seu peso (Kg):'))
    lista[c] = peso
print(f'Maior peso dentre os 5 inseridos: {(max(lista))}')
print(f'Menor peso dentre os 5 inseridos: {(min(lista))}')