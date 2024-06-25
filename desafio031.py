distancia = float(input('Digite a distância (km) da viagem: '))
passagem1 = distancia*0.5
passagem2 = distancia*0.45
if distancia <= 200:
    print(f'Valor da passagem para uma viagem de {distancia}km: R${passagem1:.2f}')
if distancia > 200:
    print(f'Valor da passagem para uma viagem de {distancia}km: R${passagem2:.2f}')