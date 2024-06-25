value = float(input('Digite o valor do produto: '))
payment = int(input('Escolha uma das seguintes formas de pagamento:\n1)DINHEIRO/CHEQUE\n2)À VISTA NO CARTÃO DE CRÉDITO\n3)EM ATÉ 2X NO CARTÃO DE CRÉDITO\n4)EM 3X OU MAIS NO CARTÃO DE CRÉDITO\nR: '))
P1 = value * 0.9
P2 = value * 0.95
P3 = value
P4 = value * 1.2
if payment == 1:
    print(f'VALOR TOTAL DO PRODUTO COM 10% DE DESCONTO: {P1}')
elif payment == 2:
    print(f'VALOR TOTAL DO PRODUTO COM 5% DE DESCONTO: {P2}')
elif payment == 3:
    print(f'VALOR TOTAL DO PRODUTO: {P3}')
elif payment == 4:
    print(f'VALOR TOTAL DO PRODUTO COM 20% DE JUROS: {P4}')
else: 
    print('INVÁLIDO.')