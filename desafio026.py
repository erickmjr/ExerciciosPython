frase = str(input('Digite uma frase: '))
minuscula = frase.lower()
contagema = minuscula.count('a') 
primeiravez = minuscula.find('a') + 1
ultimavez = minuscula.rfind('a') + 1
print(f'Na frase, a letra "a" (maiúscula ou minúscula) aparece {contagema} vezes')
print(f'Na frase, a letra "a" (maiúscula ou minúscula) aparece pela primeira vez na posição {primeiravez}')
print(f'Na frase, a letra "a" (maiúscula ou minúscula) aparece pela última vez na posição {ultimavez}')
