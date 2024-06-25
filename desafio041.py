from datetime import date
actual = date.today().year
atl_age = int(input('ANO DE NASCIMENTO DO ATLETA: '))
age = actual - atl_age
print(f'IDADE DO ATLETA: {age}')
if age <= 9:
    print(' CATEGORIA: MIRIM')
elif age > 9 and age <= 14:
    print('CATEGORIA: INFANTIL')
elif age > 14 and age <=19:
    print('CATEGORIA: JÚNIOR')
elif age >19 and age <25:
    print('CATEGORIA: SÊNIOR')
elif age >= 25:
    print('CATEGORIA: MASTER')