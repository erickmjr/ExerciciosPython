ano = int(input('Digite o ano: '))
bissexto = (ano % 4)
naobissexto = (ano // 1 % 10)
naobissexto2 = (ano//10 % 10)
if bissexto == 0 and (naobissexto != 0 or naobissexto2 != 0) :
    print(f"O ano de {ano} é bissexto.")
if (bissexto != 0 or (ano % 100) == 0) or (naobissexto == 0 and naobissexto2 == 0):
    print(f'O ano de {ano} não é bissexto.')