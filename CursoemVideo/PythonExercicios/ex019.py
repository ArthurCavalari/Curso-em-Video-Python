from random import choice
print('Sorteio de quem vai apagar o quadro!')
n1 = str (input('Digite o nome do primeiro dos alunos: '))
n2 = str (input('Digite o nome do segundo aluno: '))
n3 = str (input('Digite o nome do terceiro aluno: '))
n4 = str (input('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
esc = choice(lista)
print(f'O aluno sorteado(a) é: {esc}')
