from random import choice
import emoji
aluno1 = str(input('Digite o nome do primeiro aluno:'))
aluno2 = str(input('Digite o nome do segundo aluno:'))
aluno3 = str(input('Digite o nome do terceiro aluno:'))
aluno4 = str(input("Digite o nome do quarto aluno:"))
alunos = (aluno1, aluno2, aluno3, aluno4)
sorteado = choice(alunos)
print('-'*40)
print(emoji.emojize(f'O aluno sorteado foi {sorteado} :polegar_para_cima: ', language = 'pt'))