frase = str(input('Digite uma frase qualquer: '))
minusculo = frase.lower()
palavras = minusculo.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print(f'A frase/palavra: "{frase}". É um palíndromo.')
else:
    print(f'A frase/palavra: "{frase}". Não é um palíndromo')