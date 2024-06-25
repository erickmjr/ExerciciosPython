from random import choice
from time import sleep
print('- '*30)
player = int(input('ESCOLHA:\n1)PEDRA\n2)PAPEL\n3)TESOURA\nR: '))
print('- '*30)
options = ('pedra', 'papel', 'tesoura')
pc_choice = choice(options)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(0.6)
print('- '*30)
print('RESULTADOS:')
if player == 1 and pc_choice == 'papel':
    print(f'PC: {pc_choice}\nJOGADOR: PEDRA\nVITÓRIA DO PC!')

elif player == 1 and pc_choice == 'tesoura':
    print(f'PC: {pc_choice}\nJOGADOR: PEDRA\nVITÓRIA DO JOGADOR!')

elif player == 1 and pc_choice == 'pedra':
    print(f'PC: {pc_choice}\nJOGADOR: PEDRA\nEMPATE!')

elif player == 2 and pc_choice == 'pedra':
    print(f'PC: {pc_choice}\nJOGADOR: PAPEL\nVITÓRIA DO JOGADOR!')

elif player == 2 and pc_choice == 'tesoura':
    print(f'PC: {pc_choice}\nJOGADOR: PAPEL\nVITÓRIA DO PC!')

elif player == 2 and pc_choice == 'papel':
    print(f'PC: {pc_choice}\nJOGADOR: PAPEL\nEMPATE!')

elif player == 3 and pc_choice == 'pedra':
    print(f'PC: {pc_choice}\nJOGADOR: TESOURA\nVITÓRIA DO PC!')

elif player == 3 and pc_choice == 'papel':
    print(f'PC: {pc_choice}\nJOGADOR: TESOURA\nVITÓRIA DO JOGADOR!')

elif player == 3 and pc_choice == 'tesoura':
    print(f'PC: {pc_choice}\nJOGADOR: TESOURA\nEMPATE!')

elif player != 1 and player != 2 and player != 3:
    print('INVÁLIDO!')