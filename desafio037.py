num = int(input('Digite um número: '))
conv = int(input('Deseja converter para qual base?\n1)Binario\n2)Octal\n3)Hexadecimal\nR:'))
bin = str(bin(num))
oct = str(oct(num))
hex = str(hex(num))
if conv == 1:
    print(f'{num} em binário: {bin.replace("0b", "")}')
elif conv == 2:
    print(f'{num} em octal: {oct.replace("0o", "")}')
elif conv == 3:
    print(f'{num} em hexadecimal: {hex.replace("0x", "")}')
else:
    print('Opção inválida!')