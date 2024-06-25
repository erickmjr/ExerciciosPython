velocidade = float(input('Digite a velocidade do veículo (km/h): '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade.')
    print(f'Valor da multa: R${multa:.2f} ')

else:
    print('Você não ultrapassou o limite de velocidade.')