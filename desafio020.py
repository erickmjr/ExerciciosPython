from random import sample
import emoji
aluno1 = str(input('Digite o nome do primeiro aluno:'))
aluno2 = str(input('Digite o nome do segundo aluno:'))
aluno3 = str(input('Digite o nome do terceiro aluno:'))
aluno4 = str(input("Digite o nome do quarto aluno:"))
sorteado = [aluno1, aluno2, aluno3, aluno4]
sorteio = sample(sorteado,4)
print('-'*40)
print(emoji.emojize(f'Lista dos alunos sorteados :red_heart:'))
print(f'1°Aluno sorteado: {sorteio[0]}')
print(f'2°Aluno sorteado: {sorteio[1]}')
print(f'3°Aluno sorteado: {sorteio[2]}')
print(f'4°Aluno sorteado: {sorteio[3]}')
