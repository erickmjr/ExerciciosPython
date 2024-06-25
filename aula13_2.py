#PEDINDO A CONTAGEM PARA O USUÁRIO:
n = int(input('DIGITE UM NÚMERO DE 1 ATÉ 10: '))
for n in range(0, n+1):
    print(n)
print('FIM')

#PEDINDO AO USUÁRIO TODAS AS VARIÁVEIS DA ESTRUTURA:
i = int(input('DIGITE O VALOR DE INÍCIO: '))
f = int(input('DIGITE O VALOR FINAL: '))
p = int(input('DIGITE O PASSO A PASSO: '))

for c in range(i, f+1, p):
    print(c)
print('FIM')

#PEDINDO VALORES DENTRO DA ESTRUTURA:  
for t in range(0, 3):
    w = int(input('ESCREVA UM VALOR: '))
print('FIM')

#PEDINDO VALORES E SOMANDO:
s = 0 
for d in range(0,3):
    a = int(input('DIGITE UM VALOR: '))
    s += a
print(f'SOMA DOS VALORES: {s}')
print('FIM')