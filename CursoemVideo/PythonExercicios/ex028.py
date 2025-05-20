from random import randint
from time import sleep

think = int(randint(0,5))
print('-=-' * 30)
jg= int(input('Estou pensando em um número de 0 a 5... Tente adivinhar > '))
print('-=-' * 30)
acerto = (jg == think)
po = str('=')
print('Pensando...')
sleep(3)

if acerto:
    print('Você é a porra de um telepata!! Acertou fdp!')
else:
    print('Você não é pareo para mim arrombado!')
    print(f'Eu pensei na porra do {think} e você na merda do {jg}')
print('Fim dessa porra!!')