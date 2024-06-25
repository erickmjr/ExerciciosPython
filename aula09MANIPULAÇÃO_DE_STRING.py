frase = str(input('digite uma frase:'))
print(frase.isalpha())
print(frase[9::3])
print(frase[0:5])
print(frase[9:21:3])
print(len(frase)) #mostra a quantidade de caracteres da string
print(frase.count('o')) 
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('curso' in frase)
print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) #vai deixar todos os caracteres, menos o primeiro, em minúsculo
print(frase.title()) #deixa cada palavra com seu caractere inicial maiúsculo
print(frase.strip()) #remove todos os espaços inúteis no inicio e final da string
print(frase.rstrip()) #remove somente os espaços a direita
print(frase.lstrip()) #remove somente os espaços a esquerda
print(frase.split()) #cada palavra é colocada dentro de um elemento de uma lista 
print(frase.split()[0][3]) #escolhe a palavra guardada dentro da lista no split e seleciona a letra 
print('-'.join(frase))
print(frase.rfind('a')) #procura a localizacao do ultimo ponto em que a foi escrito
