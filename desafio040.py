grade1 = float(input('Digite a primeira nota do aluno: '))
grade2 = float(input('Digite a segunda nota do aluno: '))
media = (grade1 + grade2)/2
if media >= 7:
    print(f'ALUNO APROVADO!\nMÉDIA: {media}')
elif media >=5 and media < 7:
    print(f'ALUNO EM RECUPERAÇÃO!\nMÉDIA: {media}')
else:
    print(f'ALUNO REPROVADO!\nMÉDIA: {media}')