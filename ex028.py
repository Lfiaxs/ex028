from random import randint
from time import sleep
computador = randint (0,5) #Faz o computador "PENSAR"
print('-=-' * 20)
print ('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Qual foi o número que pensei? ')) #Jogador tenta advinhar
print ('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print('Que pena, você errou. ')
print( 'O número que pensei foi o {}'.format(computador))