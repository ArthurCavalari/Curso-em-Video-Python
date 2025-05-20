from random import shuffle
'''Método com list()
nomes = list()
print('Ordem de apresentação de trabalho: ')

n1 = str(input('Digite um nome >> '))
nomes.append(n1)
n2 = str(input('Digite um nome >> '))
nomes.append(n2)
n3 = str(input('Digite um nome >> '))
nomes.append(n3)
n4 = str(input('Digite um nome >> '))
nomes.append(n4)

shuffle(nomes)

print(f'O ordem é:  \n{nomes}')'''

#Método que o Guanabara ensinou

print('Hoje iremos sortear a ordem de apresentação de um trabalho!!')

n1 = str (input('Digite um nome >> '))
n2 = str (input('Digite um nome >> '))
n3 = str (input('Digite um nome >> '))
n4 = str (input('Digite um nome >> '))

lista = [n1, n2, n3, n4]

shuffle(lista)

print(f'A ordem de apresentação é: {lista}')