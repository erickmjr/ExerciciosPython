listaHomensNome = []
listaHomensIdade = []
listaMulheresIdade = []
listaIdade = []
somaidadeF = 0
somaidadeT = 0
for c in range(0,4):
    print('-'*20)
    print('Insira as informações nos campos a seguir:')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F):'))
    somaidadeT += idade
    if sexo.lower() == 'm':
            listaHomensNome.insert(c, nome)
            listaHomensIdade.insert(c, idade)
    if sexo.lower() == 'f':
        if (idade < 20) and (sexo.lower() == 'f'):
            somaidadeF += 1

print('-'*35)
if listaHomensIdade.index(max(listaHomensIdade)) == 0:
    print(f'O homem mais velho se chama {listaHomensNome[0]} e tem {listaHomensIdade[0]} anos.')

elif listaHomensIdade.index(max(listaHomensIdade)) == 1:
    print(f'O homem mais velho se chama {listaHomensNome[1]} e tem {listaHomensIdade[1]} anos.')

elif listaHomensIdade.index(max(listaHomensIdade)) == 2:
    print(f'O homem mais velho se chama {listaHomensNome[2]} e tem {listaHomensIdade[2]} anos.') 

elif listaHomensIdade.index(max(listaHomensIdade)) == 3:
    print(f'O homem mais velho se chama {listaHomensNome[3]} e tem {listaHomensIdade[3]} anos.') 

listaIdade = (sum(listaHomensIdade) + sum(listaMulheresIdade))
mediaidade = (somaidadeT)/4
print(f'A média de idade do grupo é {mediaidade} anos.')

if somaidadeF >= 1:
    print(f'Existem {somaidadeF} mulheres com menos de 20 anos no grupo')
else:
    print('O grupo não contém uma mulher com menos de 20 anos.')