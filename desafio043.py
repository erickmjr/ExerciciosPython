weight = float(input('PESO CORPÓREO (em Kg): '))
height = float(input('ALTURA (em metros): '))
IMC = (weight)/(height*height)
if IMC < 18.5:
    print('O indivíduo está abaixo do pesoa ideal.')
elif IMC >= 18.5 and IMC < 25:
    print('O indivíduo está no peso ideal.')
elif IMC >= 25 and IMC < 30: 
    print('O indivíduo está com sobrepeso.')
elif IMC >=30 and IMC < 40:
    print('O indivíduo está com obesidade.')
else:
    print('O indivíduo está com obesidade mórbida.')   