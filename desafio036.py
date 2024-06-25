housev = float(input('Digite o valor da casa em reais:'))
costsalary = float(input('Digite o valor do salário do comprador: '))
parcel = int(input('Digite a quantidade de anos para compra parcelada:'))
parcel = (parcel*12)
prestmonth = (housev/parcel)
limpayment = (costsalary * 1.3)
if prestmonth > limpayment:
    print(f'Empréstimo recusado! \nValor das parcelas: ({prestmonth}) \nStatus: Excede em mais de 30% o valor salarial.  ')
else:
    print(f'Empréstimo aprovado! \nValor das parcelas: {prestmonth} \nStatus: Não excede em 30% o valor salarial.')