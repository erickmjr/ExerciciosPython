reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))
ver1 = abs(reta2 - reta3) < reta1 < reta2 + reta3
ver2 = abs(reta1 - reta3) < reta2 < reta1 + reta3
ver3 = abs(reta1 - reta2) < reta3 < reta1 + reta2
if ver1 == True and ver2 == True and ver3 == True:
    print(f'Um triângulo pode ser formado com retas tendo os valores: {reta1}, {reta2} e {reta3}')
else:
    print(f'Um triângulo não pode ser formado com as retas tendo os valores: {reta1}, {reta2} e {reta3}')

