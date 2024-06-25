from datetime import date
actual = date.today().year
grupoM = 0
grupoN = 0
for pessoas in range(1,8):
    aux = 0
    nascimento = int(input(f'Digite o ano de nascimento da {pessoas}a pessoa: '))
    if (actual - nascimento) >= 18:
        aux = aux + 1
    if aux == 1:
        grupoM = grupoM + 1
    else:
        grupoN = grupoN + 1
print(f'Total de pessoas com idade maior ou igual a 18 anos: {grupoM}')
print(f'Total de pessoas com idade menor que 18 anos: {grupoN}')
