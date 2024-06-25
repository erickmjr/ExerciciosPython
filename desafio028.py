from random import randint
from time import sleep
sorteio = randint(0,5) #sorteia um numero entre 0 e 5
tentativa = int(input('Tente descobrir qual o número sorteado no intervalo de 0 a 5: ')) #pergunta ao jogador qual numero ele vai tentar
print("PROCESSANDO...")
sleep(1.5)
if tentativa == sorteio:
    print('Parabéns, você acertou!')
    print(f'O número sorteado foi {sorteio}')
else:
    print('Você errou!')
    print(f"O número sorteado foi: {sorteio}")
print('-'*40)

