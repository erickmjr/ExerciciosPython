nome = str(input('Digite seu nome:')).strip()
minusc = nome.lower()
verificacao = ('silva' in minusc)
print(f'O nome contém "Silva"? \nResposta: {verificacao}')