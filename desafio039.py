from datetime import date
atual = date.today().year
birth = int(input('Digite o ano de nascimento: '))
age = atual - birth
time = (18 - age) + atual
saldo = age - 18
if age == 18:
    print('Já está na idade de se alistar.')
elif age > 18:
    print(f'Já passou em {saldo} ano(s) do tempo para alistamento.')
    
else:
    print(f'Irá se alistar em {time}.')