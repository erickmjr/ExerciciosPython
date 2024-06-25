nome = str(input('Digite o seu nome:'))
if nome == 'Erick':
    print('Que nome lindo!')
else:
    print('Ô nome feio!')
print(f'Bom dia {nome}!')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = (n1+n2)/2
if media >= 6 :
    print(f'Parabéns, você passou!\nMédia: {media}')
else:
    print(f'Tu é burro hein cavalo!\nMédia: {media}')