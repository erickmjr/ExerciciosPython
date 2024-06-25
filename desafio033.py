n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input("Digite o terceiro número: "))

if(n1 > n2 and n1 > n3):
    print(f'O número {n1} é o maior entre {n1}, {n2} e {n3}.')
if(n2 > n1 and n2 > n3):
    print(f'O número {n2} é o maior entre {n1}, {n2} e {n3}.')
if(n3 > n1 and n3 > n2):
    print(f'O número {n3} é o maior entre {n1}, {n2} e {n3}.')
if(n1 < n2 and n1 < n3):
    print(f'O número {n1} é o menor entre {n1}, {n2} e {n3}.')
if(n2 < n1 and n2 < n3):
    print(f'O número {n2} é o menor entre {n1}, {n2} e {n3}.')
if(n3 < n1 and n3 < n2):
    print(f'O número {n3} é o menor entre {n1}, {n2} e {n3}.')
if n1 == n2 == n3:
    print('Todos os números são iguais, portanto não há um maior entre eles.')

