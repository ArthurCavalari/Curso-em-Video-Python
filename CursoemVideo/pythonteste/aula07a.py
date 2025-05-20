n1 = int (input('Um valor: '))
n2 = int (input ('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
resto = n1 % n2
su = n1 - n2
print('A soma é {} \nO produto é {} \nA divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira é {} \nPotência é {}'.format(di, e))
print('O resto da divisão é {} \nA subtração é {}'.format(resto, su))