salario = float(input('Digite o salário do funcionário: '))
aumento1 = salario * 1.1
aumento2 = salario * 1.15
if salario > 1250:
    print(f'Salário base: R${salario:.2f}\nSalário com aumento de 10%: R${aumento1:.2f}')
else:
    print(f"Salário base: R${salario:.2f}\nSalário com aumento de 15%: R${aumento2:.2f}")